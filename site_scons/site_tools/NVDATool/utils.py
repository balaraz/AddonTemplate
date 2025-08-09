import gettext
from collections.abc import Callable, Container, Mapping

from .typings import Strable



def format_nested_section(
	section_name: str,
	data: Mapping[str, Mapping[str, Strable]],
	include_only_keys: Container[str]|None = None,
	_: Callable[[str], str] = gettext.gettext,
) -> str:
	lines = [f"\n[{section_name}]"]
	for item_name, inner_dict in data.items():
		lines.append(f"[[{item_name}]]")
		for key, val in inner_dict.items():
			if include_only_keys and key not in include_only_keys:
				continue
			lines.append(f"{key} = {_(str(val))}")
	return "\n".join(lines) + "\n"
