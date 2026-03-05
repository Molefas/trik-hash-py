# Hash Calculator (Python)

A demo **tool-mode trik** that computes and compares cryptographic hashes. This is the **Python implementation**, functionally identical to the TypeScript version. No LLM, no conversation, no handoff — just pure tools that appear as native capabilities on the consuming agent.

## How It Works

Tool-mode triks are the simplest kind of trik. They export structured tools with strict input/output schemas. The gateway executes them directly and returns the result to the agent via an `outputTemplate`. There is no separate LLM involved.

### Security Model (TDPS)

Every field in the output is **constrained by type**:

- `algorithm`: enum (`sha256`, `md5`, `sha1`) — cannot contain arbitrary text
- `hash`: pattern-restricted string (`^[a-f0-9]+$`) — only hex characters
- `match`: boolean — `true` or `false`, nothing else

Because all output types are agent-safe (enum, pattern, boolean), the result rendered via `outputTemplate` is guaranteed free of prompt injection. The agent sees something like `sha256: e3b0c44...` — never free-form text from the trik.

## Tools

### `computeHash`

Compute a cryptographic hash of the given text.

```
Input:  { text: "hello world", algorithm: "sha256" }
Output: sha256: b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
```

### `compareHash`

Check if text matches a given hash.

```
Input:  { text: "hello world", hash: "b94d27b...", algorithm: "sha256" }
Output: Hash sha256 match: true
```

## Installation

```bash
trik install @molefas/trik-hash-py
```

No configuration needed — this trik has no secrets or API keys.

## Cross-Language Parity

This Python trik is consumed identically to its TypeScript counterpart. A JS gateway can load this Python trik (and vice versa) — the manifest is language-agnostic, and the worker protocol handles cross-runtime execution.

## License

MIT
