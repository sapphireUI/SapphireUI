import os

VERSION = "v0.1.0"
NAME = "SapphireUI"

SAPPHIREUI_URL = "https://sapphire-ui.reflex.run/"
SAPPHIREUI_SLOGAN = (
    "Beautifully designed Reflex components to build your web apps faster. Open source."
)
SAPPHIREUI_KEY_WORDS = (
    "SapphireUI, ui, web apps, framework, open source, frontend, backend, full stack"
)


BASE_GITHUB_URL = "https://github.com/sapphireUI/SapphireUI/blob/main/SapphireUI"
SITE_LOGO_URL = "https://raw.githubusercontent.com/sapphireUI/SapphireUI/refs/heads/main/assets/new_logo.PNG"

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

LOCAL_BASE_CHART_PATH = os.path.join(project_root, NAME, NAME, "charts")
LOCAL_BASE_PANTRY_PATH = os.path.join(project_root, NAME, NAME, "pantry")

BASE_PANTRY_PATH = BASE_GITHUB_URL + "pantry/"
BASE_CHART_PATH = BASE_GITHUB_URL + "charts/"


SITE_THEME = "system"
FONT_FAMILY = "JetBrains Mono,ui-monospace,monospace"

SITE_META_TAGS = [
    {"name": "application-name", "content": "SapphireUI"},
    {"name": "keywords", "content": SAPPHIREUI_KEY_WORDS},
    {"name": "description", "content": SAPPHIREUI_SLOGAN},
    {"property": "og:url", "content": SAPPHIREUI_URL},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "SapphireUI"},
    {"property": "og:description", "content": SAPPHIREUI_SLOGAN},
    {"property": "og:image", "content": SITE_LOGO_URL},
    {"property": "og:image:width", "content": "1200"},
    {"property": "og:image:height", "content": "630"},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:domain", "content": SAPPHIREUI_URL},
    {"property": "twitter:url", "content": SAPPHIREUI_URL},
    {"name": "twitter:title", "content": "SapphireUI"},
    {"name": "twitter:description", "content": SAPPHIREUI_SLOGAN},
    {"name": "twitter:image", "content": SITE_LOGO_URL},
]
