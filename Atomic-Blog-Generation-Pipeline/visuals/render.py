"""Renders every figure for one blog post into public/blog/<slug>/.

    python visuals/render.py <slug> [figure-name ...]

Each post has a module in visuals/posts/ named after its slug (dashes become underscores)
with a build() function that returns {figure_name: page}.
"""
import importlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import atomic_viz as viz  # noqa: E402


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    slug, only = sys.argv[1], set(sys.argv[2:])
    mod = importlib.import_module("posts." + slug.replace("-", "_"))
    out = os.path.join(viz.PUBLIC, "blog", slug)
    for name, page in mod.build().items():
        if only and name not in only:
            continue
        print("rendered", os.path.relpath(viz.render(name, page, out), viz.COMMUNITY))
    # The HTML sources are for review only. Keep them out of public/.
    shutil.rmtree(os.path.join(out, "_src"), ignore_errors=True)


if __name__ == "__main__":
    main()
