from __future__ import annotations

import random
import string
from functools import wraps
from typing import Callable

import reflex as rx
from reflex.components.datadisplay.code import Theme
from reflex.experimental import ClientStateVar

from SapphireUI.wrappers.base.main import Chart_Theme

# Common styles extracted as constants
BUTTON_STYLE = {
    "align_items": "center",
    "justify_content": "center",
    "white_space": "nowrap",
    "padding_top": "0.5rem",
    "padding_bottom": "0.5rem",
    "vertical_align": "middle",
    "font_weight": "600",
    "min_width": "32px",
    "gap": "0.375rem",
    "font_size": "0.75rem",
    "height": "1.5rem",
    "padding_left": "0.75rem",
    "padding_right": "0.75rem",
    "cursor": "pointer",
    "border_radius": "0.5rem",
}

TAB_CONTAINER_STYLE = {
    "display": "inline-flex",
    "height": "2.125rem",
    "align_items": "baseline",
    "justify_content": "flex-start",
    "border_radius": "0.5rem",
    "padding": "0.25rem",
    "border": f"1.25px dashed {rx.color('gray', 4)}",
}

CODE_BLOCK_PROPS = {
    "language": "python",
    "theme": rx.color_mode_cond(Theme.light, Theme.darcula),
    "background": "transparent !important",
    "text_align": "left",
    "width": "100%",
    "font_size": "12px",
    "scrollbar_width": "none",
    "code_tag_props": {"pre": "transparent"},
    "custom_style": {
        "background": "transparent !important",
        "pre": {"background": "transparent !important"},
        "code": {"background": "transparent !important"},
    },
    "border_radius": "10px",
}


def generate_component_id():
    """Generate a unique component ID."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=10))


def create_breadcrumb(items):
    """Create a breadcrumb navigation component."""
    breadcrumb_items = []
    for i, item in enumerate(items):
        if i > 0:
            breadcrumb_items.append(
                rx.el.label(
                    "›", class_name="text-sm font-medium", color=rx.color("slate", 11)
                )
            )

        color = rx.color("slate", 12) if i == len(items) - 1 else rx.color("slate", 11)
        weight = "font-medium" if i == len(items) - 1 else "font-regular"

        breadcrumb_items.append(
            rx.el.label(
                item,
                class_name=f"text-sm {weight}",
                color=color,
            )
        )

    return rx.hstack(*breadcrumb_items, spacing="1", id=f"{items[0]}-{items[1]}")


def create_copy_button(source_code):
    """Create a standardized copy button."""
    return rx.button(
        rx.text("Copy", color=rx.color("slate", 9)),
        on_click=[
            rx.set_clipboard(source_code),
            rx.toast.success("Component copied!"),
        ],
        aria_disabled="false",
        background="transparent",
        style=BUTTON_STYLE,
        class_name="hidden sm:inline-flex",
    )


def create_expand_button(is_expanded_var):
    """Create a standardized expand button."""
    return rx.button(
        rx.text(
            rx.cond(is_expanded_var.value, "Collapse", "Expand"),
            color=rx.color("slate", 10),
        ),
        on_click=[rx.call_function(is_expanded_var.set_value(~is_expanded_var.value))],
        aria_disabled="false",
        background=rx.color("gray", 3),
        style={
            **BUTTON_STYLE,
            "display": "inline-flex",
            "border_radius": "0.375rem",
            "box_shadow": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
        },
    )


def create_tab_button(tab, index, active_tab):
    """Create a standardized tab button."""
    return rx.button(
        rx.text(
            tab,
            color=rx.cond(
                active_tab.value == index,
                rx.color("slate", 12),
                rx.color("slate", 10),
            ),
        ),
        on_click=[rx.call_function(active_tab.set_value(index))],
        aria_disabled="false",
        background=rx.cond(
            active_tab.value == index,
            rx.color("gray", 3),
            "transparent",
        ),
        style={
            **BUTTON_STYLE,
            "display": "inline-flex",
            "border_radius": rx.cond(active_tab.value == index, "0.375rem", "0.5rem"),
            "box_shadow": rx.cond(
                active_tab.value == index,
                "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
                "none",
            ),
        },
    )


def create_code_block(code_content):
    """Create a standardized code block component."""
    return rx.code_block(code_content, **CODE_BLOCK_PROPS)


def create_expandable_code_block(code_content, component_id=None):
    """Create an expandable code block with collapse/expand functionality."""
    if not component_id:
        component_id = generate_component_id()

    is_expanded = ClientStateVar.create(f"code_expanded_{component_id}", False)

    return rx.box(
        rx.box(
            create_code_block(code_content),
            style={
                "max_height": rx.cond(is_expanded.value, "none", "400px"),
                "overflow": "hidden",
            },
        ),
        class_name="w-full",
    )


def create_content_wrapper(content, add_px_on_condition=None):
    """Create a standardized content wrapper."""
    base_class = (
        "rounded-xl h-full w-full flex align-center justify-center items-center py-6 "
    )

    if add_px_on_condition is not None:
        class_name = base_class + rx.cond(add_px_on_condition, "px-4", "").to(str)
    else:
        class_name = base_class

    return rx.box(content, class_name=class_name)


def create_section_header(title, subtitle, id=""):
    """Create a standardized section header."""
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                title,
                class_name="text-3xl sm:3xl font-bold py-2",
            ),
            rx.el.label(
                subtitle,
                class_name="text-sm text-slate-11",
            ),
            class_name="w-full justify-start flex flex-col -mb-8",
        ),
        id=id,
        class_name="flex flex-col p-0 gap-y-2 w-full",
    )


def extract_chart_info(path):
    import re

    # Regex pattern to match both 'charts' and 'pantry' base paths
    match = re.search(r"(charts|pantry)/([a-zA-Z]+)/v(\d+)", path)
    if match:
        chart_name = match.group(2)  # 'area', 'animations', etc.
        version = match.group(3)  # Version number

        return create_breadcrumb([chart_name, f"v{version}"])

    raise ValueError(
        f"Error: Path '{path}' is invalid or not in the expected format (charts/pantry/...). Please check your input."
    )


def tab_selector(tabs=["Preview", "Code"], component_id=None, source_code=""):
    # Create a unique ID if none provided
    if not component_id:
        component_id = generate_component_id()

    # Create a unique active tab state variable for this specific tab selector
    active_tab = ClientStateVar.create(f"active_tab_{component_id}", 0)

    return rx.box(
        rx.hstack(
            create_copy_button(source_code),
            rx.foreach(tabs, lambda tab, i: create_tab_button(tab, i, active_tab)),
            style=TAB_CONTAINER_STYLE,
        )
    )


def component_wrapper(path: str):
    # Generate a single random ID for this component
    component_id = generate_component_id()

    # Create a unique client state variable for this component's preview/code toggle
    active_tab = ClientStateVar.create(f"active_tab_{component_id}", 0)

    def decorator(func: Callable[[], list[rx.Component | str | int]]):
        @wraps(func)
        def wrapper():
            component, component_code, flexgen_path = func()

            return rx.box(
                rx.box(
                    rx.el.label(extract_chart_info(path), class_name="text-sm"),
                    rx.box(
                        tab_selector(["Preview", "Code"], component_id, component_code),
                        class_name="flex align-center gap-2",
                    ),
                    class_name="h-14 px-4 py-4 w-full flex align-center justify-between items-center rounded-xl "
                    + rx.cond(active_tab.value == 1, "sticky top-0", "").to(str),
                ),
                create_content_wrapper(
                    rx.cond(
                        active_tab.value == 0,  # 0 = Preview, 1 = Code
                        component,
                        create_code_block(component_code),
                    ),
                    active_tab.value == 0,
                ),
                border=f"1px dashed {rx.color('gray', 5)}",
                class_name="rounded-xl shadow-sm size-full flex flex-col p-1 "
                + Chart_Theme.value.to(str),
            )

        return wrapper

    return decorator
