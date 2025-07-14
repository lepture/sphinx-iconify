# sphinx-iconify

A sphinx extension to use ``<iconify-icon>`` web component.

## Install

```
pip install sphinx-iconify
```

## Usage

Add extension into ``docs/conf.py``:

```python
extensions = [
    "sphinx_iconify",
]
```

Use the role in your documentation:

```
This is a GitHub icon :iconify:`simple-icons:github`
```

## License

BSD
