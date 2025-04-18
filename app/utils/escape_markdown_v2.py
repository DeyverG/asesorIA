import re

def escape_markdown_v2(text: str) -> str:
    # Patrón para detectar enlaces Markdown: [texto](url)
    pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    escaped_parts = []
    last_end = 0

    for match in pattern.finditer(text):
        start, end = match.span()

        # Escapamos texto fuera del enlace
        escaped_parts.append(escape_markdown_v2_chars(text[last_end:start]))

        # Escapamos solo el texto visible del enlace, NO la URL
        escaped_text = escape_markdown_v2_chars(match.group(1))
        url = match.group(2)
        escaped_parts.append(f'[{escaped_text}]({url})')

        last_end = end

    # Escapamos el resto del texto después del último enlace
    escaped_parts.append(escape_markdown_v2_chars(text[last_end:]))

    return ''.join(escaped_parts)

def escape_markdown_v2_chars(text: str) -> str:
    # Todos los caracteres que deben escaparse en Markdown V2
    escape_chars = r"[]()>#+-={}.!\\"
    return ''.join(f'\\{c}' if c in escape_chars else c for c in text)
