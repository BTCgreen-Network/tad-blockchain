from __future__ import annotations

from typing import Any

from tad.types.blockchain_format.program import Program


def json_to_tadlisp(json_data: Any) -> Any:
    list_for_tadlisp = []
    if isinstance(json_data, list):
        for value in json_data:
            list_for_tadlisp.append(json_to_tadlisp(value))
    else:
        if isinstance(json_data, dict):
            for key, value in json_data:
                list_for_tadlisp.append((key, json_to_tadlisp(value)))
        else:
            list_for_tadlisp = json_data
    return Program.to(list_for_tadlisp)
