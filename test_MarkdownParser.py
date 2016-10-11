from MarkdownParser import MarkdownParser

parser = MarkdownParser("""# hello world
- how you doing
- how are you
- I am good""")

parser2 = MarkdownParser("""# hello world
- how you doing
## How do you do
- how are you
   - I am good
### Foo bar""")

def test_to_html():
    assert parser.to_html() == """<h1>hello world</h1>
<li>how you doing</li>
<li>how are you</li>
<li>I am good</li>"""

    assert parser2.to_html() == """<h1>hello world</h1>
<li>how you doing</li>
<h2>How do you do</h2>
<li>how are you</li>
<li>I am good</li>
<h3>Foo bar</h3>"""
