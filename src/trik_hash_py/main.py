"""
Hash Calculator — tool-mode trik.

Compute and compare cryptographic hashes.
Uses wrap_tool_handlers() for native tool export.
"""

import hashlib
from typing import Any

from trikhub.sdk import wrap_tool_handlers, TrikContext


async def compute_hash(input: dict[str, Any], context: TrikContext) -> dict[str, Any]:
    text = input["text"]
    algorithm = input["algorithm"]
    h = hashlib.new(algorithm)
    h.update(text.encode("utf-8"))
    return {"algorithm": algorithm, "hash": h.hexdigest()}


async def compare_hash(input: dict[str, Any], context: TrikContext) -> dict[str, Any]:
    text = input["text"]
    expected = input["hash"]
    algorithm = input["algorithm"]
    h = hashlib.new(algorithm)
    h.update(text.encode("utf-8"))
    return {"match": h.hexdigest() == expected.lower(), "algorithm": algorithm}


default = wrap_tool_handlers({
    "computeHash": compute_hash,
    "compareHash": compare_hash,
})
