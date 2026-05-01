import shutil
import os


def on_post_build(config):
    site_dir = config["site_dir"]
    docs_dir = config["docs_dir"]
    generated = os.path.join(site_dir, "sitemap.xml")
    renamed = os.path.join(site_dir, "sitemap-root.xml")
    sitemap_index = os.path.join(docs_dir, "sitemap.xml")

    if os.path.exists(generated):
        shutil.copy2(generated, renamed)

    if os.path.exists(sitemap_index):
        shutil.copy2(sitemap_index, generated)