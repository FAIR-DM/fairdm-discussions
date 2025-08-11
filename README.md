# FairDM Discussions

FairDM Discussions is a plugin for [FairDM](https://www.fairdm.org/en/latest) that allows users to engage in discussions around various database entries (e.g. projects, datasets, etc.). This plugin aims to enhance collaboration, communication and community-engagement within your FairDM-powered portal.

This plugin utilizes the popular [django-comments-xtd](https://github.com/danirus/django-comments-xtd) package to provide a well-tested and feature-rich commenting system. 

NOTE: For simplicity, this plugin uses the javascript frontend provided by django-comments-xtd, which means UI customization is limited.

## Installation

```bash
poetry add git+https://github.com/FAIR-DM/fairdm-discussions
```

Note: Installation is direct from the GitHub repository. We will publish this package to PyPI in the future when the FairDM API is more stable.

Then, in your `config/settings.py` module, make sure to add `fairdm_discussions` to your `fairdm.setup` call:

```python
import fairdm

fairdm.setup(addons=["fairdm_discussions"])
```

That's it! The FairDM Discussions plugin is now installed and ready to use.


## Configuration

The following settings are provided by default when you install this plugin as above. You can override these settings in your `config/settings.py` file as needed.

```python
COMMENTS_XTD_MAX_THREAD_LEVEL = 8  # Maximum depth for comment threads
COMMENTS_XTD_LIST_ORDER = ("-thread_id", "order")  # Default comment ordering
COMMENTS_XTD_APP_MODEL_OPTIONS = {
    "default": {
        "allow_flagging": True,
        "allow_feedback": True,
        "show_feedback": True,
        "who_can_post": "users",  # NOTE: this plugin is untested for anonymous comments. Changes to this value may have unintended consequences.
    }
}
```




