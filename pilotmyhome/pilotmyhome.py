import reflex as rx
from datetime import datetime
from typing import List, Dict

# -----------------------------------------------------------------------------
# App State
# -----------------------------------------------------------------------------
class State(rx.State):
    """The application state."""

    product_hubs: Dict[str, List[Dict[str, str]]] = {
        "peaceful_home": [
            {
                "title": "Ring Battery Doorbell with Head‑to‑Toe Video – Satin Nickel",
                "image_url": "https://m.media-amazon.com/images/I/519N1IBi3iL._SY450_.jpg",
                "affiliate_link": "https://www.amazon.com/Ring-Battery-Doorbell-Head-to-Toe-Video-Satin-Nickel/dp/B0BZWRSRWV?tag=pilotmyhome-20"
            },
            {
                "title": "Philips Hue Smart 60W A19 LED Bulb – White Ambiance (Bluetooth)",
                "image_url": "https://m.media-amazon.com/images/I/611-Y8IALHL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Philips-Hue-Bluetooth-compatible-Assistant/dp/B07QV9XLSD?tag=pilotmyhome-20"
            },
            {
                "title": "roborock Q7 M5 Robot Vacuum and Mop Combo, 10 000 Pa HyperForce",
                "image_url": "https://m.media-amazon.com/images/I/7162dbcZW3L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/roborock-Q7-M5-Anti-Tangle-APP-Controlled/dp/B0DSJ93KPD?tag=pilotmyhome-20"
            },
        ],
        "connected_family": [
            {
                "title": "Aura Digital Picture Frame – 10.1″ HD Mat Display, Unlimited Storage",
                "image_url": "https://m.media-amazon.com/images/I/71WSCdw8rJL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Digital-Picture-Unlimited-Storage-Anywhere/dp/B09X2CL5HG?tag=pilotmyhome-20"
            },
            {
                "title": "Anker NEBULA Capsule Smart Wi‑Fi Mini Projector (100 ANSI lumen)",
                "image_url": "https://m.media-amazon.com/images/I/610dDc+YfDL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Projector-Anker-Portable-High-Contrast-Playtime/dp/B076Q3GBJK?tag=pilotmyhome-20"
            },
            {
                "title": "Amazon Echo Dot (5th Gen, 2022 Release) Glacier White",
                "image_url": "https://m.media-amazon.com/images/I/7116ea3BmTL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Amazon-release-vibrant-helpful-routines/dp/B09B94RL1R?tag=pilotmyhome-20"
            },
        ],
        "abundant_kitchen": [
            {
                "title": "Instant Pot Duo Crisp 11‑in‑1 Air Fryer & Pressure Cooker, 6 Qt",
                "image_url": "https://m.media-amazon.com/images/I/81vc3qXKPpL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Instant-Pot-Multi-Use-Pressure-Cooker/dp/B08WCLJ7JG?tag=pilotmyhome-20"
            },
            {
                "title": "Echo Show 8 (2nd Gen, 2021 release) – 8″ HD Smart Display with 13 MP Camera",
                "image_url": "https://m.media-amazon.com/images/I/71ldF3vJclL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/All-New-Echo-Show-8/dp/B0BLS3Y632?tag=pilotmyhome-20"
            },
        ],
        "spirit_ambiance": [
            {
                "title": "The Battle Is Not Yours - Warrior Christian Wall Art Print, Angel Inspirational Bible Verse Art",
                "image_url": "https://m.media-amazon.com/images/I/71qQE25MhBL._SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Battle-Not-Yours-Inspirational-Motivational/dp/B0F2VSXLXV?tag=pilotmyhome-20"
            },
            {
                "title": "Wooden Scripture Prayer Bowl for Home Decor – Christian Tabletop Centerpiece",
                "image_url": "https://m.media-amazon.com/images/I/81iWvF9qS3L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/P-Graham-Dunn-Acacia-Wood-Scripture/dp/B0B6W5M2G4?tag=pilotmyhome-20"
            },
            {
                "title": "Bible‑Verse Scented Candle Set (36 Tins) – Scripture Aroma Candles",
                "image_url": "https://m.media-amazon.com/images/I/81urHfEWxVL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Threlaco-Christian-Scripture-Birthday-Graduation/dp/B0CRKTPTWY?tag=pilotmyhome-20"
            },
        ]
    }
    
    guide_products: Dict[str, List[Dict[str, str]]] = {
        "security": [
            {
                "title": "Ring Battery Doorbell with Head‑to‑Toe Video – Satin Nickel",
                "image_url": "https://m.media-amazon.com/images/I/519N1IBi3iL._SY450_.jpg",
                "affiliate_link": "https://www.amazon.com/Ring-Battery-Doorbell-Head-to-Toe-Video-Satin-Nickel/dp/B0BZWRSRWV?tag=pilotmyhome-20"
            },
            {
                "title": "Blink Outdoor 4 (4th Gen) – Wire-free smart security camera",
                "image_url": "https://m.media-amazon.com/images/I/61s4s6sXyIL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Blink-Outdoor-4th-Gen-Wire-free/dp/B0B12C2N2X?tag=pilotmyhome-20"
            },
            {
                "title": "eufy Security S220 SoloCam, Wireless Outdoor Security Camera",
                "image_url": "https://m.media-amazon.com/images/I/61Vd6v-0gmL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/eufy-Security-S220-SoloCam-Spotlight/dp/B09T92N52N?tag=pilotmyhome-20"
            },
        ],
        "stewardship": [
            {
                "title": "roborock Q7 M5 Robot Vacuum and Mop Combo, 10 000 Pa HyperForce",
                "image_url": "https://m.media-amazon.com/images/I/7162dbcZW3L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/roborock-Q7-M5-Anti-Tangle-APP-Controlled/dp/B0DSJ93KPD?tag=pilotmyhome-20"
            },
            {
                "title": "Instant Pot Duo Crisp 11‑in‑1 Air Fryer & Pressure Cooker, 6 Qt",
                "image_url": "https://m.media-amazon.com/images/I/81vc3qXKPpL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Instant-Pot-Multi-Use-Pressure-Cooker/dp/B08WCLJ7JG?tag=pilotmyhome-20"
            },
            {
                "title": "Amazon Echo Dot (5th Gen, 2022 Release) Glacier White",
                "image_url": "https://m.media-amazon.com/images/I/7116ea3BmTL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Amazon-release-vibrant-helpful-routines/dp/B09B94RL1R?tag=pilotmyhome-20"
            },
        ]
    }

# -----------------------------------------------------------------------------
# Reusable Components
# -----------------------------------------------------------------------------
def product_card(product: dict):
    return rx.link(
        rx.vstack(
            rx.image(src=product["image_url"], alt=product["title"],
                     height="150px", width="auto", object_fit="contain"),
            rx.text(product["title"], height="5em",
                    text_align="center", font_weight="500", size="3"),
            rx.button("View on Amazon", width="100%"),
            spacing="4", align="center"),
        href=product["affiliate_link"], is_external=True,
        style=rx.Style({
            "text_decoration": "none",
            "color": "var(--gray-11)",
            "border": "1px solid #EAEAEA",
            "border_radius": "10px",
            "padding": "1em",
            "width": "280px",
            "_hover": {"box_shadow": "0px 4px 20px rgba(0,0,0,0.1)"}
        })
    )

def hub_section(title: str, text_content: str, products: list[dict]):