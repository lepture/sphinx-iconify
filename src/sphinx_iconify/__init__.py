"""A sphinx extension for designing beautiful, view size responsive web components."""

from typing import TYPE_CHECKING

__version__ = "0.1.0"

if TYPE_CHECKING:
    from typing import TypedDict
    from sphinx.application import Sphinx

    class SetupReturns(TypedDict):
        version: str
        parallel_read_safe: bool
        parallel_write_safe: bool


def setup(app: "Sphinx") -> "SetupReturns":
    from .roles import setup_iconify, insert_iconify_script

    setup_iconify(app)
    app.connect("env-updated", insert_iconify_script)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
