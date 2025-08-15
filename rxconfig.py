import reflex as rx

config = rx.Config(
    app_name="pilotmyhome",
    db_url="sqlite:///reflex.db",
    plugins=["reflex.plugins.sitemap.SitemapPlugin"],
)