from docutils import nodes
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator
from sphinx.environment import BuildEnvironment
from sphinx.util.docutils import SphinxRole

iconify_script_url = "https://code.iconify.design/iconify-icon/3.0.1/iconify-icon.min.js"


class iconify_icon(nodes.General, nodes.Element):
    tagname = "iconify-icon"
    local_attributes = ("icon", "width", "height")
    list_attributes = nodes.Element.basic_attributes + local_attributes
    known_attributes = list_attributes + ("source",)


def visit_iconify_icon_html(self: HTML5Translator, node: iconify_icon):
    self.body.append(node.starttag())


def depart_iconify_icon_html(self: HTML5Translator, node: iconify_icon):
    self.body.append(node.endtag())


class IconifyRole(SphinxRole):
    """Role to embed an icon with ``<iconify-icon>`` web component.

    .. code-block:: reST

        :iconify:`simple-icons:github`

        :iconify:`simple-icons:github width=24px height=24px`
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """Run the role."""
        values = self.text.split()
        attrs = {
            "icon": values[0],
        }

        if len(values) > 1:
            # parse extra attributes
            for value in values[1:]:
                try:
                    k, v = value.split("=")
                    attrs[k] = v
                except ValueError:
                    pass

        node = iconify_icon(self.rawtext, **attrs)
        self.set_source_info(node)
        return [node], []


def setup_iconify(app: Sphinx) -> None:
    app.add_node(
        iconify_icon,
        html=(visit_iconify_icon_html, depart_iconify_icon_html),
    )
    app.add_config_value("iconify_script_url", iconify_script_url, "env")
    app.add_role("iconify", IconifyRole())


def insert_iconify_script(app: Sphinx, env: BuildEnvironment) -> None:
    url: str = env.config.iconify_script_url
    if url:
        app.add_js_file(url)
