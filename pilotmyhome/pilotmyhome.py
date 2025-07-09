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
                "affiliate_link": "