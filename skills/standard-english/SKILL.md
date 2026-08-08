---
name: standard-english
description: Select and apply an explicit language standard, controlled-language profile, normative keyword system, terminology policy, accessibility writing profile, or formal documentation guide.
---

# Standard English

Use only when an explicit profile materially improves preservation of obligations, safety or legal interpretation, requirements quality, terminology, accessibility, localization, publication consistency, or conformance-oriented review. For ordinary writing, use the requested channel, repository, or house style and return `No external profile required`.

Route in this order:

```text
need for explicit profile -> governing sources -> task classification ->
profile fit -> conflict elimination -> material-risk gates -> evidence strength
-> permitted claim -> output mode
```

Keep roles distinct: governing source, one document/content profile, at most one language constraint, and at most one delivery overlay unless independent risks justify more. Do not silently mix RFC `MUST/SHOULD/MAY` with ISO-style `shall/should/may/can`; flag conflicting normative systems.

Useful profile families include ISO 24495 and CAN-ASC plain language, ASD-STE100 controlled technical English, IEC/IEEE 82079-1 and ISO/IEC/IEEE 26514 product information, ISO/IEC/IEEE 29148 requirements, RFC 2119/8174 normative keywords, ISO 704 and TBX terminology, WCAG and W3C COGA accessibility guidance, and organization or publication guides such as GOV.UK, Microsoft, Google, or Canada.ca. Select by task fit, not because a profile is available.

Preserve facts, conditions, exceptions, thresholds, actors, permissions, prohibitions, sequence, terminology, and normative force. Treat supplied glossaries, schemas, API definitions, and UI catalogs as authoritative unless a higher-order source conflicts.

Separate profile fit, routing confidence, material risk, evidence strength, and claim level. Missing evidence limits the claim; it does not make a poorer profile fit preferable. Use `edited using`, `aligned with`, or `candidate issue` when formal conformance evidence is unavailable. Do not claim compliance, certification, or conformance without the required source, scope, process, and qualified human review. Classify findings as confirmed issue, candidate issue, content ambiguity, domain decision, or preference.

This is not a general grammar checker, a certification engine, or a substitute
for authoritative standards, audience testing, implementation testing, or
subject-matter review. A wording review cannot establish page-level WCAG
conformance, and textual inspection alone cannot establish CAN-ASC or ASD-STE
conformance. Preserve unresolved domain decisions for qualified reviewers.

In a graph, this is an optional policy node between `decide` and `builder` or between `builder` and `verify`. It remains independently callable.
