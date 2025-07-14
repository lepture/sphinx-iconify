:description: Sphinx Iconify allowing you to embed icons from over 200,000 open-source vector icons for your documentation.

Sphinx Iconify
==============

.. rst-class:: lead

   Embedding icons from over 200,000 open-source vector icons.

----------

``sphinx-iconify`` provides the ``:iconify:`` role, which allows you to
use the ``<iconify-icon>`` web component powered by Iconify_.

.. _Iconify: https://iconify.design/

Install
-------

``sphinx-iconify`` is conveniently available as a Python package on PyPI
and can be easily installed using pip and uv.

.. tab-set::
    :class: outline

    .. tab-item:: :iconify:`devicon:pypi` pip

        .. code-block:: shell

            pip install sphinx-iconify

    .. tab-item:: :iconify:`material-icon-theme:uv` uv

        .. code-block:: shell

            uv add --dev sphinx-iconify


Add ``sphinx_iconify`` to your ``docs/conf.py``:

.. code-block:: python
    :caption: docs/conf.py

    extensions = [
        'sphinx_iconify',
    ]

Usage
-----

Using the role ``iconify`` to embed an icon:

.. tab-set::

    .. tab-item:: Markdown

        .. code-block:: markdown

            {iconify}`devicon:pypi`

    .. tab-item:: RST

        .. code-block:: none

            :iconify:`devicon:pypi`

:iconify:`devicon:pypi`


It is also possible to add extra attributes to the icon:

.. tab-set::

    .. tab-item:: Markdown

        .. code-block:: markdown

            {iconify}`devicon:pypi width=48px height=48px`

    .. tab-item:: RST

        .. code-block:: none

            :iconify:`devicon:pypi width=48px height=48px`

:iconify:`devicon:pypi width=48px height=48px`

Icon sets
---------

You can find all the available icons on https://icon-sets.iconify.design/.


Configuration
-------------

Besides adding ``sphinx_iconify`` to your ``docs/conf.py``, there is also
a ``iconify_script_url`` setting. The default value is:

.. code-block:: none

    https://code.iconify.design/iconify-icon/3.0.0/iconify-icon.min.js


When using shibuya_ theme, you can set the value to empty, because shibuya_
theme has built-in ``<iconify-icon>`` web component.

.. code-block:: python
    :caption: docs/conf.py

    extensions = [
        "sphinx_iconify",
    ]
    iconify_script_url = ""
    html_theme = "shibuya"

.. _shibuya: https://shibuya.lepture.com/

License
-------

BSD
