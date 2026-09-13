"""Synthetic fixtures only; no card prompt or code is ever executed."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "catalog.py"
SPEC = importlib.util.spec_from_file_location("catalog", SCRIPT)
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)


def synthetic_card():
    text = (
        "# Sentetik kart\n\nYalnız doğrulama için hazırlanmış bir test girdisi.\n\n"
        "## Nedir?\n\nSentetik açıklama.\n\n"
        "## Ne zaman işe yarar?\n\nDosya doğrulama testinde.\n\n"
        "## Örnekler\n\nKurgusal örneklerdir; benchmark sonucu değildir.\n\n"
    )
    for level in ("Basit (Simple)", "Orta (Medium)", "İleri (Hard)"):
        text += (
            f"### {level}\n\n**Durum**\n\nSentetik durum.\n\n"
            "**Prompt**\n\n```python\nraise RuntimeError('NEVER EXECUTE')\n```\n\n"
            "**Örnek çıktı**\n\nTemsili çıktı.\n\n"
            "**Ne elde ettik?**\n\nYapı kontrolü.\n\n"
        )
    return text + (
        "## Nerede durmalı?\n\nBu bir yöntem veya başarı iddiası değildir.\n\n"
        "## Kaynaklar\n\n"
        "- [Sentetik kaynak](https://example.org/source) — Test yazarı, 2026. "
        "Yalnız bağlantı biçimi için sentetik kaynak; doğrulanmış araştırma değildir.\n"
    )


def metadata(identifier="X01", slug="sentetik-bir", related=None):
    return {
        "id": identifier,
        "slug": slug,
        "title": "Sentetik kart",
        "section": "temel",
        "tags": ["yazi"],
        "aliases": ["Synthetic fixture"],
        "mark": identifier,
        "file": f"{slug}.md",
        "related_ids": related or [],
    }


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "cards").mkdir()
        self.records = [
            metadata(related=["sentetik-iki"]),
            metadata("X02", "sentetik-iki", ["sentetik-bir"]),
        ]
        for record in self.records:
            (self.root / "cards" / record["file"]).write_text(
                synthetic_card(), encoding="utf-8"
            )
        self.write_index()
        self.card = self.root / "cards" / self.records[0]["file"]

    def write_index(self):
        (self.root / "index.json").write_text(
            json.dumps(self.records, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def rejected(self, fragment):
        with self.assertRaisesRegex(catalog.ValidationError, fragment):
            catalog.build_catalog(self.root)

    def test_complete_markdown_metadata_and_order(self):
        result = catalog.build_catalog(self.root)
        self.assertEqual(
            set(result), {"schema", "version", "language", "content_license", "cards"}
        )
        self.assertEqual(result["schema"], "prompt-atlas.catalog")
        self.assertEqual(result["version"], 1)
        self.assertEqual(result["language"], "tr")
        self.assertEqual(result["content_license"], "CC-BY-4.0")
        self.assertEqual(len(result["cards"]), 2)
        for actual, expected in zip(result["cards"], self.records):
            self.assertEqual(actual, {**expected, "markdown": synthetic_card()})

    def test_future_card_count_is_not_fixed_at_81(self):
        self.records.append(metadata("NEW99", "yeni-kart"))
        (self.root / "cards" / "yeni-kart.md").write_text(
            synthetic_card(), encoding="utf-8"
        )
        self.write_index()
        self.assertEqual(len(catalog.build_catalog(self.root)["cards"]), 3)

    def test_duplicate_ids(self):
        self.records[1]["id"] = "X01"
        self.write_index()
        self.rejected("duplicate id")

    def test_duplicate_slugs(self):
        self.records[1]["slug"] = "sentetik-bir"
        self.records[1]["file"] = "sentetik-bir.md"
        self.write_index()
        self.rejected("duplicate slug")

    def test_missing_card(self):
        self.card.unlink()
        self.rejected("missing cards")

    def test_extra_card(self):
        (self.root / "cards" / "extra.md").write_text(synthetic_card(), encoding="utf-8")
        self.rejected("extra cards")

    def test_unsafe_paths(self):
        for value in ("../outside.md", "/tmp/outside.md", "sub/card.md", "..\\x.md"):
            with self.subTest(value=value):
                self.records[0]["file"] = value
                self.write_index()
                self.rejected("file must equal")

    def test_symlink_card(self):
        self.card.unlink()
        self.card.symlink_to(self.root / "cards" / self.records[1]["file"])
        self.rejected("symlink")

    def test_symlink_cards_directory(self):
        folder = self.root / "cards"
        folder.rename(self.root / "original-cards")
        folder.symlink_to(self.root / "original-cards", target_is_directory=True)
        self.rejected("symlink")

    def test_symlink_index(self):
        index = self.root / "index.json"
        index.rename(self.root / "original-index.json")
        index.symlink_to(self.root / "original-index.json")
        self.rejected("symlink")

    def test_symlink_catalog_is_neither_read_nor_overwritten(self):
        target = self.root / "outside.json"
        target.write_text("untouched\n", encoding="utf-8")
        (self.root / "catalog.json").symlink_to(target)
        for command in ("generate", "check"):
            with self.subTest(command=command):
                result = self.cli(command)
                self.assertEqual(result.returncode, 1)
                self.assertIn("symlink", result.stderr)
                self.assertEqual(target.read_text(), "untouched\n")

    def test_nested_or_non_markdown_entries(self):
        entry = self.root / "cards" / "nested"
        entry.mkdir()
        self.rejected("regular Markdown")
        entry.rmdir()
        entry.write_text("text\n", encoding="utf-8")
        self.rejected("regular Markdown")

    def test_invalid_related_reference(self):
        for refs in (["missing-slug"], ["X02"], ["sentetik-bir"]):
            with self.subTest(refs=refs):
                self.records[0]["related_ids"] = refs
                self.write_index()
                self.rejected("related_ids")

    def test_index_exact_fields(self):
        for field in ("image_id", "source_ids", "motif", "markdown", "local_path"):
            with self.subTest(field=field):
                self.records[0][field] = "forbidden"
                self.write_index()
                self.rejected("fields")
                del self.records[0][field]
        del self.records[0]["title"]
        self.write_index()
        self.rejected("fields")

    def test_invalid_metadata_types_and_values(self):
        cases = (
            ("id", "../x"), ("slug", "Uppercase"), ("title", ""),
            ("section", ""), ("mark", 1), ("tags", "yazi"),
            ("tags", ["yazi", "yazi"]), ("aliases", [None]),
            ("related_ids", ["sentetik-iki", "sentetik-iki"]),
        )
        for field, value in cases:
            with self.subTest(field=field, value=value):
                original = self.records[0][field]
                self.records[0][field] = value
                self.write_index()
                self.rejected(field)
                self.records[0][field] = original

    def test_index_must_be_nonempty_array_of_objects(self):
        for value in ({}, [], [None], [1]):
            with self.subTest(value=value):
                self.records = value
                self.write_index()
                self.rejected("index|record")

    def test_corrupted_and_ambiguous_json(self):
        for raw in ("[\n", '[{"id":"X01","id":"X02"}]\n', "[NaN]\n"):
            with self.subTest(raw=raw):
                (self.root / "index.json").write_text(raw, encoding="utf-8")
                self.rejected("JSON")

    def test_utf8_and_newline_validation(self):
        original = self.card.read_bytes()
        for bad in (original[:-1], original.replace(b"\n", b"\r\n"), b"\xff\n",
                    b"\xef\xbb\xbf" + original, original + b"\x00\n"):
            with self.subTest(bad=bad[:20]):
                self.card.write_bytes(bad)
                self.rejected("UTF-8|newline|LF|BOM|NUL")
        self.card.write_bytes(original)
        index = self.root / "index.json"
        index.write_bytes(index.read_bytes().rstrip(b"\n"))
        self.rejected("newline")

    def test_missing_or_reordered_levels(self):
        for heading in ("### Basit (Simple)", "### Orta (Medium)", "### İleri (Hard)"):
            with self.subTest(heading=heading):
                self.card.write_text(synthetic_card().replace(heading, "### Eksik"), encoding="utf-8")
                self.rejected("headings")
        self.card.write_text(synthetic_card().replace("### Basit (Simple)", "### İleri (Hard)"), encoding="utf-8")
        self.rejected("headings")

    def test_source_and_limits_boundaries(self):
        for heading in ("## Kaynaklar", "## Nerede durmalı?"):
            with self.subTest(heading=heading):
                self.card.write_text(synthetic_card().replace(heading, "**Başlık değil**"), encoding="utf-8")
                self.rejected("headings")
        self.card.write_text(synthetic_card().replace("https://example.org/source", "../private.md"), encoding="utf-8")
        self.rejected("public source")

    def test_sources_inside_fences_do_not_count(self):
        self.card.write_text(synthetic_card().replace(
            "- [Sentetik kaynak]", "```text\n- [Sentetik kaynak]"
        ) + "```\n", encoding="utf-8")
        self.rejected("public source")

    def test_scenario_fields_present_ordered_and_nonempty(self):
        for field in ("**Durum**", "**Prompt**", "**Örnek çıktı**", "**Ne elde ettik?**"):
            with self.subTest(field=field):
                self.card.write_text(synthetic_card().replace(field, "", 1), encoding="utf-8")
                self.rejected("scenario fields")
        self.card.write_text(synthetic_card().replace("Sentetik durum.", "", 1), encoding="utf-8")
        self.rejected("empty scenario field")

    def test_dialogue_is_an_accepted_output_field(self):
        self.card.write_text(synthetic_card().replace("**Örnek çıktı**", "**Örnek diyalog**"), encoding="utf-8")
        self.assertEqual(len(catalog.build_catalog(self.root)["cards"]), 2)

    def test_fenced_headings_are_not_parsed_or_executed(self):
        value = synthetic_card().replace(
            "raise RuntimeError('NEVER EXECUTE')",
            "## Kaynaklar\n### İleri (Hard)\n**Durum**\nraise RuntimeError('NEVER EXECUTE')",
        )
        self.card.write_text(value, encoding="utf-8")
        self.assertEqual(catalog.build_catalog(self.root)["cards"][0]["markdown"], value)

    def test_unclosed_fence_is_rejected(self):
        self.card.write_text(synthetic_card() + "\n```text\nunclosed\n", encoding="utf-8")
        self.rejected("unclosed fence")

    def cli(self, command):
        return subprocess.run(
            [sys.executable, "-B", str(SCRIPT), command, "--root", str(self.root)],
            text=True, capture_output=True, check=False,
        )

    def test_generate_twice_is_deterministic_and_check_is_readonly(self):
        first = self.cli("generate")
        self.assertEqual(first.returncode, 0, first.stderr)
        path = self.root / "catalog.json"
        before = path.read_bytes()
        self.assertEqual(self.cli("generate").returncode, 0)
        self.assertEqual(path.read_bytes(), before)
        modified = path.stat().st_mtime_ns
        self.assertEqual(self.cli("check").returncode, 0)
        self.assertEqual(path.stat().st_mtime_ns, modified)
        self.assertTrue(before.endswith(b"\n"))
        self.assertIn("İleri", before.decode("utf-8"))

    def test_stale_catalog_fails_without_rewriting(self):
        self.assertEqual(self.cli("generate").returncode, 0)
        path = self.root / "catalog.json"
        before = path.read_bytes()
        self.card.write_text(synthetic_card().replace("Sentetik açıklama.", "Yeni sentetik açıklama."), encoding="utf-8")
        result = self.cli("check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("stale", result.stderr)
        self.assertEqual(path.read_bytes(), before)

    def test_corrupted_or_wrong_schema_catalog_rejected(self):
        self.assertEqual(self.cli("generate").returncode, 0)
        path = self.root / "catalog.json"
        expected = json.loads(path.read_text())
        mutations = ["{\n"]
        for key, value in (("version", 2), ("language", "en"), ("content_license", "MIT"),
                           ("extra", True), ("version", True)):
            mutations.append(json.dumps({**expected, key: value}, ensure_ascii=False) + "\n")
        changed = json.loads(json.dumps(expected))
        changed["cards"][0]["image_id"] = "excluded"
        mutations.append(json.dumps(changed) + "\n")
        for raw in mutations:
            with self.subTest(raw=raw[:50]):
                path.write_text(raw, encoding="utf-8")
                result = self.cli("check")
                self.assertEqual(result.returncode, 1)
                self.assertEqual(path.read_text(), raw)

    def test_missing_catalog_check_fails(self):
        result = self.cli("check")
        self.assertEqual(result.returncode, 1)
        self.assertIn("catalog.json", result.stderr)


if __name__ == "__main__":
    unittest.main()
