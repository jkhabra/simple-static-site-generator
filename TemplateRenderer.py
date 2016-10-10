class TemplateRenderer:
  def __init__(self, template):
    self.template = template

  def pick_variables(self):
    template_fragments = self.template.split("{{")
    variables = []

    for i in template_fragments:
      close_location = i.find("}}")

      if close_location >= 0:
        variable = i[:close_location]
        variables.append(variable)

    return variables

  def render(self, **data):
    variables = self.pick_variables()
    template = self.template

    for v in variables:
      value = data.get(v, '')
      template = template.replace("{{" + v + "}}", value)

    return template
