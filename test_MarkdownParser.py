from MarkdownParser import MarkdownParser

parser = MarkdownParser("""# hello world
- how you doing
- how are you
- I am good""")

def test_to_html():
    assert parser.to_html() == """<h1>hello world</h1>
<li>how you doing</li>
<li>how are you</li>
<li>I am good</li>"""
