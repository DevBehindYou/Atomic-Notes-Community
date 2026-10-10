"""Renders a Support Blog's figures and its social images into its Output folder.

    python visuals/render_support.py <module> "<Output/Support Blogs/Uxx ... folder>"

The module lives in visuals/support/<module>.py and defines:
    build()  -> {figure_name: page}      written next to the article (01-banner.png, 02-....png)
    social() -> {"03 Instagram/slide-01": page, "07 Pinterest/pin": page, ...}
                                          written under "Super Support Posts/" in the same folder
"""
import importlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import atomic_viz as viz  # noqa: E402


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    mod = importlib.import_module("support." + sys.argv[1])
    out = os.path.abspath(sys.argv[2])
    if not os.path.isdir(out):
        sys.exit(f"No such folder: {out}")
    for name, page in mod.build().items():
        print("rendered", viz.render(name, page, out))
    shutil.rmtree(os.path.join(out, "_src"), ignore_errors=True)
    if hasattr(mod, "social"):
        for key, page in mod.social().items():
            sub, name = os.path.split(key)
            target = os.path.join(out, "Super Support Posts", sub)
            print("rendered", viz.render(name, page, target))
            shutil.rmtree(os.path.join(target, "_src"), ignore_errors=True)


if __name__ == "__main__":
    main()
