from docutils import nodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util.docutils import SphinxRole

iconify_script_url = "https://code.iconify.design/iconify-icon/3.0.0/iconify-icon.min.js"


class IconifyRole(SphinxRole):
    """Role to embed an icon with ``<iconify-icon>`` web component.

    .. code-block:: reST

        :iconify:`simple-icons:github`

        :iconify:`simple-icons:github width=24px height=24px`
    """

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """Run the role."""
        values = self.text.split()
        icon = values[0]
        attrs = [f'icon="{icon}"']
        if len(values) > 1:
            # parse extra attributes
            for value in values[1:]:
                try:
                    k, v = value.split("=")
                    attrs.append(f'{k}="{v}"')
                except ValueError:
                    pass

        text = "<iconify-icon " + " ".join(attrs) + "></iconify-icon>"
        node = nodes.raw(self.rawtext, nodes.Text(text), format="html")
        self.set_source_info(node)
        return [node], []


def setup_iconify(app: Sphinx) -> None:
    app.add_config_value("iconify_script_url", iconify_script_url, "env")
    app.add_role("iconify", IconifyRole())


def insert_iconify_script(app: Sphinx, env: BuildEnvironment) -> None:
    url: str = env.config.iconify_script_url
    if url:
        app.add_js_file(url)
