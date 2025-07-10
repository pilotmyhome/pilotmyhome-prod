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
    return rx.vstack(
        rx.heading(title, size="7"),
        rx.text(text_content, max_width="600px",
                text_align="center", color="var(--gray-11)"),
        rx.flex(
            rx.foreach(products, product_card),
            spacing="5", padding_y="2em",
            wrap="wrap", justify="center"
        ),
        spacing="4", align="center",
        width="100%", padding_y="3em"
    )

def footer():
    return rx.vstack(
        rx.hstack(
            rx.link("Home", href="/"),
            rx.link("Guides", href="/guides"),
            rx.link("About Us", href="/about"),
            spacing="5",
        ),
        rx.text(
            "As an Amazon Associate, we earn from qualifying purchases.",
            font_style="italic", size="2", color="var(--gray-10)", margin_top="1em"
        ),
        rx.text(f"© {datetime.now().year} Pilot My Home", margin_top="1em"),
        align="center", spacing="2",
        padding="2em", width="100%",
        background_color="var(--gray-2)"
    )
    
def persistent_stream_panel():
    """A persistent, rotated panel for the embedded stream."""
    return rx.box(
        rx.vstack(
            rx.text(
                "We support the Kingdom by supporting myflr.org",
                size="1",
                font_weight="bold",
            ),
            rx.link(
                "Give to myflr.org",
                href="https://www.myflr.org/give/",
                is_external=True,
                size="1",
            ),
            # Using rx.html() to render the iframe directly
            rx.html("<iframe src='https://www.myflr.org/stream/' style='border:none; width:280px; height:30px;'></iframe>"),
            spacing="1",
            align="center",
            padding="0.5em",
        ),
        style={
            "position": "fixed",
            "bottom": "170px",
            "right": "-110px", 
            "width": "300px",   
            "height": "90px",   
            "transform": "rotate(-90deg)", 
            "transform_origin": "bottom right",
            "z_index": "9999",
            "border": "1px solid #EAEAEA",
            "border_radius": "8px",
            "background_color": "rgba(255, 255, 255, 0.95)",
            "box_shadow": "0px 4px 20px rgba(0,0,0,0.15)",
        }
    )

def base_layout(child: rx.Component):
    """The base layout for all pages, now including the persistent panel."""
    return rx.box(
        rx.vstack(
            child, 
            footer(), 
            spacing="0", 
            align="center"
        ),
        persistent_stream_panel(),
        position="relative" 
    )


# -----------------------------------------------------------------------------
# Main Pages
# -----------------------------------------------------------------------------
@rx.page(route="/", title="Pilot My Home | Abundant Living with Technology")
def index() -> rx.Component:
    return base_layout(
        rx.vstack(
            # Hero Section
            rx.box(
                rx.vstack(
                    rx.heading("Pilot Your Home Towards Abundance",
                               size="9", color="white"),
                    rx.text(
                        "Guiding Christian families to live more peacefully and intentionally with today's technology.",
                        size="5", color="white"),
                    rx.link(
                        rx.button("Explore Our Guides", size="3", margin_top="1em"),
                        href="/guides",
                    ),
                    align="center", justify="center", text_align="center",
                    padding="2em", height="100%",
                ),
                background_image="linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), "
                                 "url('https://images.unsplash.com/photo-1558002038-1055907df827?q=80&w=2940&auto=format&fit=crop')",
                background_size="cover", background_position="center",
                width="100%", height="50vh",
            ),

            # Mission Section
            rx.vstack(
                rx.heading("Faith, Family, and the Thoughtful Home", size="7"),
                rx.text(
                    "Welcome to Pilot My Home. We believe technology shouldn't complicate life, but enrich it. We're here to help you navigate the world of smart home tech to create more time for what truly matters: your family and your faith. Let's build a home of peace and purpose, together.",
                    max_width="700px", text_align="center"
                ),
                padding_y="3em", align="center", spacing="4",
            ),

            # Product Hubs
            hub_section(
                "The Peaceful Home",
                "Create a sanctuary of calm and security. These tools help protect your home and automate daily tasks, giving you priceless peace of mind.",
                State.product_hubs["peaceful_home"],
            ),
            hub_section(
                "The Connected Family",
                "In a world of digital distraction, use technology to bring your family closer together. These picks are designed for shared experiences.",
                State.product_hubs["connected_family"],
            ),
            hub_section(
                "The Abundant Kitchen",
                "The kitchen is the heart of the home. Steward your resources well and simplify mealtime with technology that serves your family.",
                State.product_hubs["abundant_kitchen"],
            ),
            hub_section(
                "Spirit‑Led Ambiance",
                "Invite the purity of God’s presence into your home with these scriptures, scents, and sacred décor items.",
                State.product_hubs["spirit_ambiance"],
            ),
            spacing="0", width="100%", align="center",
        )
    )


@rx.page(route="/guides", title="Guides | Pilot My Home")
def guides() -> rx.Component:
    return base_layout(
        rx.vstack(
            rx.heading("Our Guides", size="8"),
            rx.text("In-depth resources to help you build a more thoughtful home."),
            rx.link("A Christian Family's Guide to Home Security & Peace of Mind",
                    href="/guides/security"),
            rx.link("Good Stewardship of Time: A Guide", href="/guides/stewardship"),
            spacing="5", padding="4em", align="center"
        )
    )

@rx.page(route="/guides/security", title="Home Security Guide | Pilot My Home")
def guide_security() -> rx.Component:
    return base_layout(
        rx.vstack(
            rx.heading("A Christian Family's Guide to Home Security",
                       size="8", text_align="center"),
            rx.text(f"Published {datetime.now().strftime('%B %d, %Y')}", color="var(--gray-10)", text_align="center"),
            
            rx.vstack(
                rx.text(
                    "Our homes are our sanctuaries—a gift we are called to steward wisely. In today's world, that stewardship includes being thoughtful about security. When you Ask God to save you,  don't ignore His gift of Wisdom. This isn't about living in fear, but about creating an environment of peace and safety where your family can flourish. Modern technology, when chosen and used intentionally, can be a powerful tool in piloting a secure and peaceful home."
                ),
                rx.heading("The Digital Welcome Mat: Video Doorbells", size="6", padding_top="1em"),
                rx.text(
                    "The front door is the primary entry point to your home. A video doorbell acts as a digital gatekeeper, allowing you to see and speak with anyone who approaches, whether you're in the kitchen or away from home. This brings incredible peace of mind, from verifying a delivery to politely declining a solicitor without opening the door. It's a simple first step towards a more secure home."
                ),
                rx.heading("Your Watchful Eyes: Outdoor Cameras", size="6", padding_top="1em"),
                rx.text(
                    "For a broader view of your property, outdoor security cameras provide another layer of reassurance. They allow you to check on children playing in the yard, monitor your property at night, and keep a record of any unusual activity. Modern wireless cameras are simple to install and offer features like motion alerts sent directly to your phone, so you are aware of what's happening at home."
                ),
                rx.heading("A Note on Digital Stewardship", size="6", padding_top="1em"),
                rx.text(
                    "As we bring these tools into our homes, it's also our responsibility to be good digital stewards. Always secure your devices with strong, unique passwords and enable two-factor authentication (2FA) whenever possible. This ensures that the technology meant to protect your family is itself protected."
                ),
                spacing="4",
                max_width="800px",
            ),

            rx.heading("Our Top Recommended Security Products",
                       size="6", padding_top="2em"),
            rx.flex(
                rx.foreach(State.guide_products["security"], product_card),
                spacing="5", padding_y="2em",
                wrap="wrap", justify="center"
            ),
            max_width="90%", padding="2em", spacing="4", align="center"
        )
    )

@rx.page(route="/guides/stewardship", title="Stewardship Guide | Pilot My Home")
def guide_stewardship() -> rx.Component:
    return base_layout(
        rx.vstack(
            rx.heading("A Guide to Good Stewardship of Your Time", size="8", text_align="center"),
            rx.text(f"Published {datetime.now().strftime('%B %d, %Y')}", color="var(--gray-10)", text_align="center"),
            
            rx.vstack(
                rx.text(
                    "Time is one of the most precious resources God has given us. As families striving to live intentionally, being good stewards of our time allows us to focus on what truly matters: our faith, our relationships, and our purpose. While technology can often feel like a distraction, it can also be a powerful ally in automating the mundane tasks of daily life, freeing up hours each week for more meaningful pursuits."
                ),
                rx.heading("Automating the Home Base", size="6", padding_top="1em"),
                rx.text(
                    "Think about the recurring chores that consume time every day. A robot vacuum, for example, can take over the daily task of sweeping floors, giving your family back 15-30 minutes each day. That's time that can be spent reading together, in prayer, or simply enjoying a moment of peace. Delegating these simple tasks to automation is a practical form of stewardship."
                ),
                rx.heading("Simplifying Mealtime", size="6", padding_top="1em"),
                rx.text(
                    "The daily question of 'what's for dinner?' can be a significant mental and time-based burden. Smart kitchen gadgets can streamline this entire process. An Instant Pot can turn a meal that takes hours into one that takes minutes. A smart display like an Echo Show can walk you through recipes step-by-step, manage your grocery list, and set timers with just your voice. This leads to less stress in the kitchen and more blessed time together around the dinner table."
                ),
                spacing="4",
                max_width="800px",
            ),

            rx.heading("Recommended Stewardship Tools",
                       size="6", padding_top="2em"),
            rx.flex(
                rx.foreach(State.guide_products["stewardship"], product_card),
                spacing="5", padding_y="2em",
                wrap="wrap", justify="center"
            ),
            max_width="90%", padding="2em", spacing="4", align="center"
        )
    )

@rx.page(route="/about", title="About | Pilot My Home")
def about() -> rx.Component:
    return base_layout(
        rx.vstack(
            rx.heading("About Pilot My Home", size="8", text_align="center"),
            rx.vstack(
                rx.heading("Our Mission", size="6", padding_top="1em"),
                rx.text(
                    "Welcome to Pilot My Home! We are a husband and wife team dedicated to our faith, our family, and the incredible potential of technology to enrich our lives. We started Pilot My Home to share our journey and help other Christian families navigate the world of smart home devices.",
                ),
                rx.text(
                    "Our goal is to provide honest guidance on how these tools can be used not as a distraction, but as a way to create a more peaceful, secure, and intentional home environment. We believe that by thoughtfully automating daily tasks and simplifying our routines, we can be better stewards of our time, freeing us up for what truly matters: fellowship, prayer, and family."
                ),
                rx.heading("What You'll Find Here", size="6", padding_top="1em"),
                rx.text(
                    "Here you'll find practical guides, in-depth reviews, and curated recommendations for products we believe in. We're so glad you're here and pray this resource is a blessing to you and your family."
                ),
                spacing="4",
                max_width="800px",
                text_align="left",
            ),
            max_width="90%", padding="2em", spacing="4", align="center"
        )
    )

# -----------------------------------------------------------------------------
# App Initialization
# -----------------------------------------------------------------------------
app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="sky",
        radius="large",
    ),
)