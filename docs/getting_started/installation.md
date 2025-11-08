---
title: "Installation"
description: "Steps to install and start using Sapphire in your project."
order: 2
---

# Check your Python version

To use Sapphire UI components, you need to have **Python version 3.11 or above** installed on your system.

```bash
python3 --version
```

# Install Reflex (if you haven't already)

Sapphire UI components are built with Reflex. If you don't have Reflex installed, use the following command:

```bash
pip install reflex
```

Make sure the latest version of Reflex is installed:

```bash
reflex --version
```

# Install the SapphireUI CLI

The Sapphire UI CLI allows you to easily add components to your Reflex project.

```bash
pip install sapphireui
```

# Create or navigate to your Reflex Web Application

The `` CLI commands must be run from the root directory of your Reflex project (where your `rxconfig.py` file is located).

If you need to create a new Reflex app:

```bash
reflex init my_app_name
cd my_app_name
```

# Using the Sapphire UI CLI

For detailed instructions on how to use the Sapphire UI CLI to add components, wrapped React components, and themes to your project, please refer to the [CLI Documentation](/getting-started/cli).
