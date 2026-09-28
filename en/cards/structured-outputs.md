# Structured Outputs

Give the output schema to an API that supports it; check the meaning of the returned data separately.

## What is it?

Structured Outputs constrains output generation with a JSON Schema on a model/API path that supports it. The schema defines the types of the fields and the allowed values. A “write JSON” prompt, and a JSON mode that only produces valid JSON, do not provide the same schema contract.

The application builds the API request, separates a refusal or an incomplete response, and then processes the result. A number that fits the schema can still be wrong. The pieces below are not real calls; they are concrete request and check outlines to be placed into an application.

## When does it help?

Use it when a program will read the model's answer. First check the supported schema subset, model compatibility and the refusal/error path; a chat interface does not always offer this setting.

## Examples

The situations and responses below are fictional teaching examples; they are not results from a model, tool or benchmark that was actually run.

### Simple

**Situation**

You are preparing an API application that will sort a support message into a single label.

**Prompt**

```text
The application sends the input and text.format fields in a Responses API request to a model that supports Structured Outputs:
input: “Message: I can't log in to my account. Label the topic.”
text.format:
{"type":"json_schema","name":"ticket","strict":true,"schema":{"type":"object","properties":{"label":{"type":"string","enum":["access","billing","unclear"]}},"required":["label"],"additionalProperties":false}}
The client takes the model ID from its own verified configuration. It makes one call; first it checks for an API error, a refusal and an incomplete status. It parses only completed schema output. If there is a refusal, it does not invent a label.
```

**Sample output**

Representative acceptable body: `{"label":"access"}`. `{"label":"other"}` does not fit this schema.

**What did we get?**

The values the program expects are clear. Without making a real API call, you cannot claim that schema enforcement works.

### Medium

**Situation**

In an opening-hours text, the closing time is unknown; you do not want the field to disappear.

**Prompt**

```text
Input: “Note: The hall opens at 10:00. The closing time is not stated. Write the unknown closing time as null.”
The supported API's text.format setting:
{"type":"json_schema","name":"hours","strict":true,"schema":{"type":"object","properties":{"opening":{"type":"string"},"closing":{"type":["string","null"]}},"required":["opening","closing"],"additionalProperties":false}}
The application makes one call; on a refusal/truncation it does not save the record. After reading the schema, it checks with its own code that the time string is in a valid HH:MM format. It does not accept a time that is not in the source.
```

**Sample output**

Representative body: `{"opening":"10:00","closing":null}`.

**What did we get?**

Missing information and a missing field were separated. Even though the schema constrains the string type, whether the time is correct in meaning is the application's check.

### Hard

**Situation**

A number that fits the schema can contradict the source.

**Prompt**

```text
Input: “Source K1: Capacity 16 people. Extract only the source code and the capacity.”
text.format:
{"type":"json_schema","name":"capacity","strict":true,"schema":{"type":"object","properties":{"source":{"type":"string","enum":["K1"]},"capacity":{"type":"integer"}},"required":["source","capacity"],"additionalProperties":false}}
The coordinator makes at most two attempts. It compares the capacity in the first completed response with K1. If they do not match, it makes one correction call with the same source and the concrete difference; on a second mismatch, it sets the case aside for human review. It does not turn an error/refusal or truncation into a success object.
```

**Sample output**

The representative first response `{"source":"K1","capacity":60}` is valid in form but wrong in meaning. Representative correction `{"source":"K1","capacity":16}`; acceptance requires a match with K1.

**What did we get?**

Schema checking and source checking became two separate gates. There is also a concrete budget for automatic retries.

## Where should you stop?

Writing the strict setting inside the prompt text does not enable it in the API. The schema features a provider supports and its response error formats can change. Tool calling is used for choosing actions, structured text for data answers; neither grants permission to act by itself.

## Sources

- [Structured model outputs | OpenAI API](https://developers.openai.com/api/docs/guides/structured-outputs) — OpenAI. Publication date not verified. Explains the distinctions between Structured Outputs with a supported JSON Schema, JSON mode, refusals and incomplete responses; does not guarantee content accuracy. Evidence level: page body.
