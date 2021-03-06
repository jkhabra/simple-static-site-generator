class MarkdownParser:
    def __init__(self, md_str):
        self.md_str = md_str

    def to_html(self):
        lines = self.md_str.split('\n')
        html_lines = []

        for item in lines:
            identifying_char = item.strip().split(' ')[0] + ' '
            item = item.strip().replace(identifying_char, '')

            if identifying_char == '# ':
                item = "<h1>" + item + "</h1>"
            if identifying_char == '## ':
                item = "<h2>" + item + "</h2>"
            if identifying_char == '### ':
                item = "<h3>" + item + "</h3>"
            if identifying_char == '- ':
                item = '<li>' + item + '</li>'

            html_lines.append(item)

        return '\n'.join(html_lines)
