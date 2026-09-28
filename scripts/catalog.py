"""Validate Markdown cards and generate their deterministic public catalogs.

The Turkish cards at the root are the original collection. An optional English
edition under en/ translates the same cards and must keep their identifiers,
relations and structure. Only the Python standard library is used. Markdown is
read as text, never executed.
"""

import argparse
import json
from pathlib import Path
import re
import sys


FIELDS = (
    "id",
    "slug",
    "title",
    "section",
    "tags",
    "aliases",
    "mark",
    "file",
    "related_ids",
)
# Everything except the reader-facing title and aliases is shared across languages.
TRANSLATED_FIELDS = ("title", "aliases")
HEADER = {
    "schema": "prompt-atlas.catalog",
    "version": 1,
    "language": "tr",
    "content_license": "CC-BY-4.0",
}
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LANGUAGES = {
    "tr": {
        "folder": "",
        "headings": (
            "## Nedir?",
            "## Ne zaman işe yarar?",
            "## Örnekler",
            "### Basit (Simple)",
            "### Orta (Medium)",
            "### İleri (Hard)",
            "## Nerede durmalı?",
            "## Kaynaklar",
        ),
        "situation": "**Durum**",
        "prompt": "**Prompt**",
        "outputs": ("**Örnek çıktı**", "**Örnek diyalog**"),
        "result": "**Ne elde ettik?**",
    },
    "en": {
        "folder": "en",
        "headings": (
            "## What is it?",
            "## When does it help?",
            "## Examples",
            "### Simple",
            "### Medium",
            "### Hard",
            "## Where should you stop?",
            "## Sources",
        ),
        "situation": "**Situation**",
        "prompt": "**Prompt**",
        "outputs": ("**Sample output**", "**Sample dialogue**"),
        "result": "**What did we get?**",
    },
}
# Backwards-compatible names for the original Turkish template.
HEADINGS = LANGUAGES["tr"]["headings"]
SCENARIO_FIELDS = {
    "**Durum**",
    "**Prompt**",
    "**Örnek çıktı**",
    "**Örnek diyalog**",
    "**Ne elde ettik?**",
}
LINK = re.compile(r"\[[^\]\n]+\]\((https?://[^\s)]+)\)")


class ValidationError(ValueError):
    """Invalid public input or an out-of-date generated catalog."""


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def safe_path(path):
    require(not path.is_symlink(), f"{path.name}: symlink is not allowed")
    return path


def read_text(path):
    safe_path(path)
    require(path.is_file(), f"{path.name}: missing regular file")
    try:
        text = path.read_bytes().decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValidationError(f"{path.name}: invalid UTF-8") from error
    require(not text.startswith("﻿"), f"{path.name}: UTF-8 BOM is not allowed")
    require("\r" not in text, f"{path.name}: use LF line endings")
    require("\0" not in text, f"{path.name}: NUL is not allowed")
    require(text.endswith("\n"), f"{path.name}: final newline is required")
    return text


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"JSON duplicate key: {key}")
        result[key] = value
    return result


def invalid_constant(value):
    raise ValidationError(f"JSON non-finite number: {value}")


def read_json(path):
    try:
        return json.loads(
            read_text(path),
            object_pairs_hook=unique_object,
            parse_constant=invalid_constant,
        )
    except json.JSONDecodeError as error:
        raise ValidationError(f"{path.name}: invalid JSON: {error.msg}") from error


def nonempty_string(value):
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        value.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return "\0" not in value and "\r" not in value and "\n" not in value


def validate_record(record, seen):
    require(isinstance(record, dict), "index record must be an object")
    require(
        set(record) == set(FIELDS), "index record fields must match the public schema"
    )
    for key in ("id", "slug", "title", "section", "mark", "file"):
        require(
            nonempty_string(record[key]), f"{key}: expected a nonempty UTF-8 string"
        )
    require(re.fullmatch(r"[A-Z][A-Z0-9]*", record["id"]), "id: invalid identifier")
    for key in ("slug", "section"):
        require(SLUG.fullmatch(record[key]), f"{key}: expected lowercase ASCII slug")
    require(
        record["file"] == record["slug"] + ".md",
        "file must equal slug + .md (no paths)",
    )
    for key in ("tags", "aliases", "related_ids"):
        values = record[key]
        require(
            isinstance(values, list) and all(nonempty_string(v) for v in values),
            f"{key}: expected an array of nonempty strings",
        )
        require(len(values) == len(set(values)), f"{key}: duplicate values")
        if key != "aliases":
            require(all(SLUG.fullmatch(v) for v in values), f"{key}: invalid slug")
    require(bool(record["tags"]), "tags: at least one tag is required")
    for key in ("id", "slug", "file"):
        require(record[key] not in seen[key], f"duplicate {key}: {record[key]}")
        seen[key].add(record[key])


def visible_lines(text):
    """Keep line positions while hiding fenced code from structural checks."""
    result = []
    fence = None
    for line in text.splitlines():
        if fence:
            if re.fullmatch(
                r" {0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*", line
            ):
                fence = None
            result.append("")
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if opening:
            fence = opening.group(1)
            result.append("")
        else:
            result.append(line)
    require(fence is None, "Markdown: unclosed fence")
    return result


def validate_markdown(text, filename, language="tr"):
    spec = LANGUAGES[language]
    expected_headings = spec["headings"]
    scenario_fields = {spec["situation"], spec["prompt"], spec["result"]} | set(
        spec["outputs"]
    )
    raw = text.splitlines()
    visible = visible_lines(text)
    headings = [
        (i, line) for i, line in enumerate(visible) if re.match(r"^#{1,6} ", line)
    ]
    require(
        len(headings) == 1 + len(expected_headings)
        and headings[0][1].startswith("# ")
        and headings[0][1][2:].strip()
        and tuple(line for _, line in headings[1:]) == expected_headings,
        f"{filename}: headings must follow the template, with all three levels",
    )
    for level in range(4, 7):
        start, end = headings[level][0] + 1, headings[level + 1][0]
        fields = [
            (i, visible[i]) for i in range(start, end) if visible[i] in scenario_fields
        ]
        labels = [label for _, label in fields]
        require(
            len(labels) == 4
            and labels[:2] == [spec["situation"], spec["prompt"]]
            and labels[2] in spec["outputs"]
            and labels[3] == spec["result"],
            f"{filename}: scenario fields must follow the template",
        )
        boundaries = [position for position, _ in fields] + [end]
        for left, right in zip(boundaries, boundaries[1:]):
            require(
                any(line.strip() for line in raw[left + 1 : right]),
                f"{filename}: empty scenario field",
            )
    sources = "\n".join(visible[headings[-1][0] + 1 :])
    require(
        LINK.search(sources),
        f"{filename}: {expected_headings[-1][3:]} needs a public source link "
        "outside code fences",
    )


def structure(text, language):
    """Language-neutral shape of a card, used to prove translation parity."""
    spec = LANGUAGES[language]
    visible = visible_lines(text)
    fences = [
        match.group(2).strip()
        for match in (
            re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line) for line in text.splitlines()
        )
        if match
    ]
    return {
        # Opening and closing lines are both counted; info strings must match.
        "fences": fences,
        "links": LINK.findall("\n".join(visible)),
        "list_items": sum(
            bool(re.match(r"^\s*(?:[-*+]|\d+[.)])\s", line)) for line in visible
        ),
        "outputs": [
            spec["outputs"].index(line) for line in visible if line in spec["outputs"]
        ],
    }


def build_catalog(root, language="tr"):
    spec = LANGUAGES[language]
    root = safe_path(Path(root))
    require(root.is_dir(), "root: missing directory")
    if spec["folder"]:
        root = safe_path(root / spec["folder"])
        require(root.is_dir(), f"{spec['folder']}: missing directory")
    records = read_json(root / "index.json")
    require(
        isinstance(records, list) and bool(records), "index must be a nonempty array"
    )
    seen = {key: set() for key in ("id", "slug", "file")}
    for record in records:
        validate_record(record, seen)
    for record in records:
        for related in record["related_ids"]:
            require(
                related in seen["slug"] and related != record["slug"],
                f"{record['id']}: related_ids must name another card's slug",
            )
    folder = safe_path(root / "cards")
    require(folder.is_dir(), "cards: missing directory")
    entries = list(folder.iterdir())
    for path in entries:
        safe_path(path)
        require(
            path.is_file() and path.suffix == ".md",
            f"cards/{path.name}: expected a regular Markdown file",
        )
    actual = {path.name for path in entries}
    require(
        not seen["file"] - actual, f"missing cards: {sorted(seen['file'] - actual)}"
    )
    require(not actual - seen["file"], f"extra cards: {sorted(actual - seen['file'])}")
    cards = []
    for record in records:
        text = read_text(folder / record["file"])
        validate_markdown(text, record["file"], language)
        cards.append({**{key: record[key] for key in FIELDS}, "markdown": text})
    return {**HEADER, "language": language, "cards": cards}


def check_translation(original, translation):
    """A translation covers every original card with the same shared metadata."""
    language = translation["language"]
    require(
        [card["id"] for card in translation["cards"]]
        == [card["id"] for card in original["cards"]],
        f"{language}: cards must match the Turkish index one-to-one and in order",
    )
    for source, target in zip(original["cards"], translation["cards"]):
        for key in FIELDS:
            if key not in TRANSLATED_FIELDS:
                require(
                    source[key] == target[key],
                    f"{language}/{target['file']}: {key} must match the Turkish card",
                )
        require(
            len(source["aliases"]) == len(target["aliases"]),
            f"{language}/{target['file']}: aliases must translate one-to-one",
        )
        before = structure(source["markdown"], "tr")
        after = structure(target["markdown"], language)
        for key, value in before.items():
            require(
                after[key] == value,
                f"{language}/{target['file']}: {key} differ from the Turkish card",
            )


def serialize_catalog(value):
    return (
        json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    ).encode("utf-8")


def check_catalog(path, expected):
    current = read_json(path)
    require(
        isinstance(current, dict) and set(current) == set(expected),
        "catalog.json: schema fields differ",
    )
    for key, value in {**HEADER, "language": expected["language"]}.items():
        require(
            type(current[key]) is type(value) and current[key] == value,
            f"catalog.json: invalid {key}",
        )
    require(
        isinstance(current["cards"], list)
        and all(
            isinstance(card, dict) and set(card) == set(FIELDS) | {"markdown"}
            for card in current["cards"]
        ),
        "catalog.json: invalid card fields",
    )
    require(
        path.read_bytes() == serialize_catalog(expected),
        "catalog.json: stale or noncanonical; run generate",
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("generate", "check"))
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args(argv)
    try:
        original = build_catalog(args.root)
        results = [("tr", original)]
        # The English edition is optional; when present it is always validated.
        english = LANGUAGES["en"]["folder"]
        if (args.root / english).exists() or (args.root / english).is_symlink():
            translation = build_catalog(args.root, "en")
            check_translation(original, translation)
            results.append(("en", translation))
        for language, result in results:
            folder = LANGUAGES[language]["folder"]
            target = safe_path(
                (args.root / folder if folder else args.root) / "catalog.json"
            )
            if args.command == "generate":
                target.write_bytes(serialize_catalog(result))
            else:
                check_catalog(target, result)
        for language, result in results:
            count = len(result["cards"])
            prefix = "" if language == "tr" else f"{language}: "
            print(
                f"{args.command}: {prefix}{count} cards, "
                f"{count * 3} scenario headings; OK"
            )
        return 0
    except (ValidationError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
