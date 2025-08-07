import reflex as rx

from SapphireUI.static.routes import ChartRoutes, GettingStartedRoutes, PantryRoutes

from .style import FooterStyle


def create_footer_item(title: str, routes: list[dict[str, str]]):
    def item(data):
        return rx.el.div(
            rx.link(
                rx.el.label(
                    (
                        data["name"]
                        if data["name"] != "Frequently Asked Questions"
                        else "FAQ"
                    ),
                    _hover={"color": rx.color("slate", 12)},
                    class_name="text-sm font-regular cursor-pointer "
                    + rx.color_mode_cond("text-slate-700", "text-slate-200"),
                ),
                href=data["path"],
                text_decoration="none",
            ),
            class_name="w-full",
        )

    return rx.vstack(
        rx.text(title, weight="bold", size="1", color=rx.color("slate", 12)),
        rx.hstack(*[item(data) for data in routes], **FooterStyle.footer_item),
        width="100%",
        padding="0.5em 0em",
        spacing="2",
    )


def footer():
    return rx.vstack(
        create_footer_item("Home", GettingStartedRoutes),
        create_footer_item("Charts UI", ChartRoutes),
        create_footer_item("Pantry UI", PantryRoutes),
        rx.vstack(
            rx.el.label(
                "SapphireUI",
                class_name="text-sm font-bold",
            ),
            rx.el.label(
                "© 2024 - 2025 Sumangal Karan. All rights reserved.",
                class_name="text-sm font-light",
            ),
            width="100%",
            spacing="2",
        ),
        class_name="p-4",
    )


def desktop_footer():
    return rx.vstack(
        rx.vstack(
            rx.el.label(
                "SapphireUI",
                class_name="text-sm font-bold",
            ),
            rx.el.label(
                "© 2024 - 2025 Sumangal Karan. All rights reserved.",
                class_name="text-sm font-light",
            ),
            spacing="2",
            width="100%",
        ),
        class_name="py-5",
    )
