from TemplateRenderer import TemplateRenderer

template1 = "Hello {{name}}. How are you."
template2 = "<html><head><title>{{title}}</title></head><body>{{content}}</body></html>";

renderer1 = TemplateRenderer(template1)
renderer2 = TemplateRenderer(template2)

def test_pick_variables():
  assert renderer1.pick_variables() == ['name']
  assert renderer2.pick_variables() == ['title', 'content']

def test_render():
  assert renderer1.render(name = 'Gaggu') == "Hello Gaggu. How are you."
  assert renderer1.render(name = 'Maninder') == "Hello Maninder. How are you."

  assert renderer2.render(title = "Hello world", content = "<h1>How are you</h1>") == "<html><head><title>Hello world</title></head><body><h1>How are you</h1></body></html>";
  assert renderer2.render(title = "Hello world") == "<html><head><title>Hello world</title></head><body></body></html>";
