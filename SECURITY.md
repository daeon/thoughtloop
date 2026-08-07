# Security

ThoughtLoop is a skill pack. Its Markdown and metadata can influence how an AI coding agent searches, edits files, uses tools, and evaluates results.

## Reporting a concern

Do not publish secrets, private logs, credentials, or exploitable prompt content in a public issue. Use GitHub's private vulnerability reporting for this repository when it is available. If it is not available, contact the maintainer through the [daeon GitHub profile](https://github.com/daeon) before disclosing the issue publicly.

When reporting, include:

- the affected file and version;
- a minimal reproduction or prompt;
- the expected and observed behavior;
- the possible impact;
- any safe mitigation you have identified.

## Safe contribution rules

- Do not commit credentials, tokens, private data, or real customer logs.
- Treat copied prompts and examples as untrusted input until reviewed.
- Keep delegation bounded and never require hidden chain-of-thought.
- Prefer deterministic tests and observable evidence for security-sensitive behavior.
