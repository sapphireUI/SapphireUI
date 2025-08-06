import reflex as rx

from SapphireUI.start.style import markdown_component_map
from SapphireUI.wrappers.base.main import base

md_content = """

# Who is SapphireUI?

**SapphireUI** is more than just a UI component library—it's a design philosophy built on clarity, creativity, and effortless execution.

In a world full of endless design choices, developers and designers often feel overwhelmed by decisions. **SapphireUI** removes the friction by offering you a curated set of reusable, beautifully designed components that are ready to integrate into any project.

---

# Why *Sapphire*?

The name **Sapphire** is inspired by the gemstone—renowned for its **clarity**, **depth**, and **timeless beauty**. It also draws influence from the [song “Sapphire”](https://en.wikipedia.org/wiki/Sapphire_%28song%29), reflecting a sense of calm rhythm and polished elegance.

**SapphireUI** represents:

* ✨ **Elegance** – Sleek, modern components that fit any aesthetic.
* ⚙️ **Simplicity** – Pre-built elements that save time and reduce complexity.
* 📘 **Clarity** – Easy-to-follow documentation and intuitive APIs.

---

# Why SapphireUI?

With SapphireUI, you no longer have to choose between complexity and creativity. We provide a growing library of high-quality components that make building stunning interfaces faster and easier.

Whether you’re starting a new project or refining an existing one, **SapphireUI** empowers you to focus on what matters—**creating great user experiences** without hesitation.

---

# Explore and Create

Dive into our collection and see how SapphireUI can transform your development workflow. From buttons and modals to advanced layout systems, everything is crafted with precision and care.

🎨 **SapphireUI – Build beautifully.**

"""


@base("/getting-started/who-is-SapphireUI", "Who Is SapphireUI?")
def SapphireUI():
    return [
        rx.box(
            rx.markdown(md_content, component_map=markdown_component_map),
            class_name="p-4",
        )
    ]
