import reflex as rx

tailwind_config = {
    "plugins": ["@tailwindcss/typography"],
    "theme": {
        "extend": {
            "colors": {
                "background": "var(--background)",
                "foreground": "var(--foreground)",
                "border": "var(--border)",
                "pattern-ui": "var(--pattern-ui)",
                "pattern-lab": "var(--pattern-lab)",
            },
        }
    },
}


config = rx.Config(
    app_name="SapphireUI",
    app_version="0.1.0",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    show_built_with_reflex=False,
    telemetry=False,
    tailwind_config=tailwind_config,
)
