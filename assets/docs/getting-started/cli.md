

# Command Line Interface (CLI)

The Sapphire UI CLI is a powerful tool designed to streamline the process of adding components, wrapped React components, and themes to your Reflex project. It ensures that all necessary files are placed in the correct locations, making integration seamless.

## Installation

If you haven't already, install the Sapphire UI CLI using pip:

```bash
pip install sapphireui
```

## Usage Context

All `sapphireui` CLI commands must be run from the root directory of your Reflex project. This is typically the directory where your `rxconfig.py` file is located. The CLI uses this file to identify your project and its structure.

# Commands

# list

This command displays all available components, wrapped React components, and themes from the Sapphire UI library. It's useful for discovering what's available before adding it to your project.

```bash
sapphireui  list
```

**Example Output:**

```
Listing available items from repository...

--- Standard Components ---
- avatar
- badge
- button
... (more standard components) ...

--- Wrapped React Components ---
- react_countup
- simple_icon
... (more wrapped React components) ...

--- Themes ---
- amber
- blue
- gray
... (more themes) ...
```

# add

The `sapphireui add` command is used to bring specific items from the Sapphire UI library into your project. It has several subcommands for different types of items.

## sapphireui add component <name>

Adds a standard sapphire UI component and its Python utility dependencies to your project.

```bash
sapphireui add component button
```

**Example:** To add the `button` component:

```bash
sapphireui add component button
```

This command will:
*   Ensure your local component library cache is up-to-date.
*   Validate that you are in a Reflex project.
*   Add the `button.py` component and its necessary utility dependencies (like `twmerge.py`) to your `your_app_name/components/ui/` directory.

## sapphireui add wrapped-react <name>

Adds a wrapped React component (a Python wrapper around a React component) and its Python utility dependencies to your project.

```bash
sapphireui add wrapped-react simple_icon
```

**Example:** To add the `simple_icon` wrapped React component:

```bash
sapphireui add wrapped-react simple_icon
```

This command will:
*   Ensure your local component library cache is up-to-date.
*   Validate that you are in a Reflex project.
*   Add the `simple_icon.py` component and its necessary utility dependencies to your `your_app_name/components/ui/` directory.

## sapphireui add theme <name>

Adds a CSS theme (including both light and dark variants) to your project's `assets/css/` directory.

```bash
sapphireui add theme blue
```

**Example:** To add the `blue` theme:

```bash
sapphireui add theme blue
```

This command will:
*   Ensure your local component library cache is up-to-date.
*   Validate that you are in a Reflex project.
*   Extract the `.theme-blue` and `.theme-blue-dark` CSS rules from the Sapphire UI library.
*   Create an `assets/css/` directory in your project root (if it doesn't exist).
*   Save the extracted CSS into a new file named `blue.css` within `assets/css/`.

# Next Steps

After adding components or themes, you can import and use them in your Reflex application files. Refer to the specific component or theming documentation for usage examples.
