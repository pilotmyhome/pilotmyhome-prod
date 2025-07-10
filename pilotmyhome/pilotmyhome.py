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
                "affiliate_link": "https://www.amazon.com/Ring-Battery-Doorbell-Head-to-Toe-Video-Satin-Nickel/dp/B0BZWRSRWV?tag=pilotmyhome-20",
                "motivation": "The Bible calls us to be wise and vigilant. Guarding the threshold of your home is an act of stewardship, creating a sanctuary of peace where your family can flourish without fear, welcoming guests with confidence."
            },
            {
                "title": "Philips Hue Smart 60W A19 LED Bulb – White Ambiance (Bluetooth)",
                "image_url": "https://m.media-amazon.com/images/I/611-Y8IALHL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Philips-Hue-Bluetooth-compatible-Assistant/dp/B07QV9XLSD?tag=pilotmyhome-20",
                "motivation": "As we are called to be a light in the world, let us first cultivate light within our homes. Use your home's atmosphere to set aside moments for peace, prayer, and warm fellowship, letting your light shine for others to see."
            },
            {
                "title": "roborock Q7 M5 Robot Vacuum and Mop Combo, 10 000 Pa HyperForce",
                "image_url": "https://m.media-amazon.com/images/I/7162dbcZW3L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/roborock-Q7-M5-Anti-Tangle-APP-Controlled/dp/B0DSJ93KPD?tag=pilotmyhome-20",
                "motivation": "Our time is a precious gift from God. By being good stewards of our minutes and automating the mundane, we reclaim time not for idleness, but for purpose: for family, for prayer, and for serving others with renewed energy."
            },
        ],
        "connected_family": [
            {
                "title": "Aura Digital Picture Frame – 10.1″ HD Mat Display, Unlimited Storage",
                "image_url": "https://m.media-amazon.com/images/I/71WSCdw8rJL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Digital-Picture-Unlimited-Storage-Anywhere/dp/B09X2CL5HG?tag=pilotmyhome-20",
                "motivation": "Let your home tell a story of gratitude. A digital frame becomes a living testament to God's blessings, displaying a rotating gallery of cherished moments and loved ones, reminding us daily of the joy He has given."
            },
            {
                "title": "Anker NEBULA Capsule Smart Wi‑Fi Mini Projector (100 ANSI lumen)",
                "image_url": "https://m.media-amazon.com/images/I/610dDc+YfDL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Projector-Anker-Portable-High-Contrast-Playtime/dp/B076Q3GBJK?tag=pilotmyhome-20",
                "motivation": "Fellowship is a cornerstone of a faith-filled life. This tool helps transform any room into a place for shared, wholesome experiences, strengthening family bonds one movie night or shared presentation at a time."
            },
            {
                "title": "Amazon Echo Dot (5th Gen, 2022 Release) Glacier White",
                "image_url": "https://m.media-amazon.com/images/I/7116ea3BmTL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Amazon-release-vibrant-helpful-routines/dp/B09B94RL1R?tag=pilotmyhome-20",
                "motivation": "The book of Proverbs speaks of the power of a timely word. Use this helper to fill your home with worship music, listen to the Word of God, or set reminders for prayer, intentionally inviting His presence into your daily rhythm."
            },
        ],
        "abundant_kitchen": [
            {
                "title": "Instant Pot Duo Crisp 11‑in‑1 Air Fryer & Pressure Cooker, 6 Qt",
                "image_url": "https://m.media-amazon.com/images/I/81vc3qXKPpL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Instant-Pot-Multi-Use-Pressure-Cooker/dp/B08WCLJ7JG?tag=pilotmyhome-20",
                "motivation": "Breaking bread together is a sacred act. By simplifying the preparation of meals, we reduce stress and create more opportunity for meaningful conversation and connection around the dinner table, the heart of the home."
            },
            {
                "title": "Echo Show 8 (2nd Gen, 2021 release) – 8″ HD Smart Display with 13 MP Camera",
                "image_url": "https://m.media-amazon.com/images/I/71ldF3vJclL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/All-New-Echo-Show-8/dp/B0BLS3Y632?tag=pilotmyhome-20",
                "motivation": "Hospitality is a gift. This kitchen companion helps you manage recipes, video call loved ones, and organize your home with ease, empowering you to serve your family and guests with a joyful and ordered spirit."
            },
        ],
        "spirit_ambiance": [
            {
                "title": "The Battle Is Not Yours - Warrior Christian Wall Art Print, Angel Inspirational Bible Verse Art",
                "image_url": "https://m.media-amazon.com/images/I/71qQE25MhBL._SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Battle-Not-Yours-Inspirational-Motivational/dp/B0F2VSXLXV?tag=pilotmyhome-20",
                "motivation": "Surround your family with visual reminders of God's promises. This artwork serves as a daily declaration of faith, reinforcing the truth that our strength comes from Him, and our battles are ultimately in His hands."
            },
            {
                "title": "Wooden Scripture Prayer Bowl for Home Decor – Christian Tabletop Centerpiece",
                "image_url": "https://m.media-amazon.com/images/I/81iWvF9qS3L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/P-Graham-Dunn-Acacia-Wood-Scripture/dp/B0B6W5M2G4?tag=pilotmyhome-20",
                "motivation": "Prayer is our direct line to the Father. A prayer bowl creates a physical space for the spiritual discipline of intercession, encouraging family members to write down and lift up their praises and petitions together."
            },
            {
                "title": "Bible‑Verse Scented Candle Set (36 Tins) – Scripture Aroma Candles",
                "image_url": "https://m.media-amazon.com/images/I/81urHfEWxVL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Threlaco-Christian-Scripture-Birthday-Graduation/dp/B0CRKTPTWY?tag=pilotmyhome-20",
                "motivation": "Engage all senses in worship. The gentle light and pleasant aroma of a candle can transform a space, quieting the mind and preparing the heart for devotion, scripture reading, or a moment of peaceful reflection."
            },
        ]
    }
    
    guide_products: Dict[str, List[Dict[str, str]]] = {
        "security": [
            {
                "title": "Ring Battery Doorbell with Head‑to‑Toe Video – Satin Nickel",
                "image_url": "https://m.media-amazon.com/images/I/519N1IBi3iL._SY450_.jpg",
                "affiliate_link": "https://www.amazon.com/Ring-Battery-Doorbell-Head-to-Toe-Video-Satin-Nickel/dp/B0BZWRSRWV?tag=pilotmyhome-20",
                "motivation": "The Bible calls us to be wise as serpents and innocent as doves. Guarding the threshold of your home is an act of wisdom, creating a sanctuary of peace where your family can flourish without fear.",
                "category": "security"
            },
            {
                "title": "Blink Outdoor 4 (4th Gen) – Wire-free smart security camera",
                "image_url": "https://m.media-amazon.com/images/I/61s4s6sXyIL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Blink-Outdoor-4th-Gen-Wire-free/dp/B0B12C2N2X?tag=pilotmyhome-20",
                "motivation": "Good stewardship extends to the property God has blessed us with. A watchful eye over your home provides not just security, but also the peace of mind that allows you to rest, knowing you've taken practical steps to protect your family.",
                "category": "security"
            },
            {
                "title": "eufy Security S220 SoloCam, Wireless Outdoor Security Camera",
                "image_url": "https://m.media-amazon.com/images/I/61Vd6v-0gmL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/eufy-Security-S220-SoloCam-Spotlight/dp/B09T92N52N?tag=pilotmyhome-20",
                "motivation": "Let your peace not be disturbed by worry. Tools that provide awareness of your surroundings free your mind from 'what-ifs', allowing you to be more present and focused on your family and your walk with God.",
                "category": "security"
            },
        ],
        "stewardship": [
            {
                "title": "roborock Q7 M5 Robot Vacuum and Mop Combo, 10 000 Pa HyperForce",
                "image_url": "https://m.media-amazon.com/images/I/7162dbcZW3L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/roborock-Q7-M5-Anti-Tangle-APP-Controlled/dp/B0DSJ93KPD?tag=pilotmyhome-20",
                "motivation": "Our time is a precious gift from God. By being good stewards of our minutes and automating the mundane, we reclaim time not for idleness, but for purpose: for family, for prayer, and for serving others with renewed energy.",
                "category": "stewardship"
            },
            {
                "title": "Instant Pot Duo Crisp 11‑in‑1 Air Fryer & Pressure Cooker, 6 Qt",
                "image_url": "https://m.media-amazon.com/images/I/81vc3qXKPpL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Instant-Pot-Multi-Use-Pressure-Cooker/dp/B08WCLJ7JG?tag=pilotmyhome-20",
                "motivation": "Breaking bread together is a sacred act. By simplifying the preparation of meals, we reduce stress and create more opportunity for meaningful conversation and connection around the dinner table, the heart of the home.",
                "category": "stewardship"
            },
            {
                "title": "Amazon Echo Dot (5th Gen, 2022 Release) Glacier White",
                "image_url": "https://m.media-amazon.com/images/I/7116ea3BmTL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Amazon-release-vibrant-helpful-routines/dp/B09B94RL1R?tag=pilotmyhome-20",
                "motivation": "The book of Proverbs speaks of the power of a timely word. Use this helper to fill your home with worship music, listen to the Word of God, or set reminders for prayer, intentionally inviting His presence into your daily rhythm.",
                "category": "stewardship"
            },
        ],
        "robotics": [
            {
                "title": "Roborock S8 MaxV Ultra",
                "image_url": "https://m.media-amazon.com/images/I/712iLYEEb3L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/roborock-S8-MaxV-Ultra-Self-Drying/dp/B0CQLPNB2X?tag=pilotmyhome-20",
                "motivation": "The Kingdom of God is one of peace and order. By delegating the constant task of maintaining a clean foundation for our home, we act as wise stewards of our God-given energy, focusing less on the dust of the world and more on cultivating a sanctuary of peace.",
                "category": "housekeeper"
            },
            {
                "title": "ECOVACS DEEBOT T50 PRO Omni Robot Vacuum and Mop, 3.19",
                "image_url": "https://m.media-amazon.com/images/I/610I+9D8U6L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/ECOVACS-T50-PRO-Ultra-Slim-Self-Emptying/dp/B0DSB92P1N?tag=pilotmyhome-20",
                "motivation": "A well-ordered home that is ready to welcome others is an act of hospitality and love. Automating the core of our home's cleanliness prepares our hearts and our space to be present for fellowship, unburdened by the stress of pending chores.",
                "category": "housekeeper"
            },
            {
                "title": "eufy Robot Vacuum Omni C20",
                "image_url": "https://m.media-amazon.com/images/I/7162dbcZW3L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/roborock-Q7-M5-Anti-Tangle-APP-Controlled/dp/B0DSJ93KPD?tag=pilotmyhome-20", # Placeholder link
                "motivation": "'Whatever you do, work at it with all your heart, as working for the Lord' (Colossians 3:23). Using intelligent tools to maintain our homes with excellence is a modern way to honor this principle, serving our family with diligence.",
                "category": "housekeeper"
            },
            {
                "title": "Amazon Astro",
                "image_url": "https://m.media-amazon.com/images/I/61fPLtmoSNL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/eufy-Emptying-hands-free-3-35-Inch-Ultra-Slim/dp/B0DCFNZF32?tag=pilotmyhome-20",
                "motivation": "A 'helper' is a deeply biblical concept. This automaton can act as a central hub, a tireless helper that assists in managing daily tasks, connecting with loved ones, and guarding the home—a modern tool for a well-managed household.",
                "category": "companion"
            },
            {
                "title": "Enabot Home Security Camera",
                "image_url": "https://m.media-amazon.com/images/I/619BkgEoP1L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Enabot-Security-Wireless-Self-Charging-Detection/dp/B09R6V3CJM?tag=pilotmyhome-20",
                "motivation": "The fifth commandment instructs us to honor our parents. Technology can be a bridge for compassionate care, allowing us to lovingly watch over elderly family members and fulfill our duty of care with peace of mind.",
                "category": "companion"
            },
            {
                "title": "Youtooz Helluva Loona 5",
                "image_url": "https://m.media-amazon.com/images/I/61DtyARb76L._AC_SL1200_.jpg",
                "affiliate_link": "utooz-Helluva-Loona-Collectible-Boss/dp/B0D7CJD2YC?tag=pilotmyhome-20",
                "motivation": "God's creation is filled with joy and personality. A robotic pet can be a source of innocent joy and laughter, reminding us of the importance of play and lighthearted connection in a loving home.",
                "category": "companion"
            },
            {
                "title": "Husqvarna Automower 415X Robotic Lawn Mower",
                "image_url": "https://m.media-amazon.com/images/I/61YL4bgni8L._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/Husqvarna-Navigation-Installation-Ultra-Quiet-Technology/dp/B09WNDLXJL?tag=pilotmyhome-20",
                "motivation": "From Eden, humanity was tasked with tending creation. Automating the care of our property is an act of modern stewardship, creating a well-ordered space for our families to enjoy and for offering hospitality to others.",
                "category": "landscaper"
            },
            {
                "title": "Segway Navimow H-Series",
                "image_url": "https://m.media-amazon.com/images/I/61EDud-50eL._AC_SL1500_.jpg",
                "affiliate_link": "https://www.amazon.com/i105N-Perimeter-AI-Assisted-Multi-Zone-Management/dp/B0CX8LL2PC?pilotmyhome-20",
                "motivation": "'Let all things be done decently and in order' (1 Corinthians 14:40). Applying this principle to our homes creates an external environment that reflects inner peace. Precise, automated tools help achieve this order, freeing our time for higher callings.",
                "category": "landscaper"
            },
        ]
    }

    # --- NEW COMPUTED VARS START HERE ---
    @rx.var
    def housekeeper_products(self) -> list[dict]:
        return [p for p in self.guide_products["robotics"] if p["category"] == "housekeeper"]

    @rx.var
    def companion_products(self) -> list[dict]:
        return [p for p in self.guide_products["robotics"] if p["category"] == "companion"]

    @rx.var
    def landscaper_products(self) -> list[dict]:
        return [p for p in self.guide_products["robotics"] if p["category"] == "landscaper"]
    # --- NEW COMPUTED VARS END HERE ---

# -----------------------------------------------------------------------------
# Reusable Components
# -----------------------------------------------------------------------------
def product_card(product: dict):
    return rx.dialog.root(
        rx.vstack(
            rx.link(
                rx.vstack(
                    rx.image(src=product["image_url"], alt=product["title"],
                             height="150px", width="auto", object_fit="contain"),
                    rx.text(product["title"], height="5em",
                            text_align="center", font_weight="500", size="3"),
                ),
                href=product["affiliate_link"],
                is_external=True,
            ),
            rx.spacer(min_y="0.5em"),
            rx.dialog.trigger(
                rx.badge(
                    "Motivation",
                    cursor="pointer",
                    color_scheme="grass",
                    variant="soft",
                )
            ),
            rx.link(
                rx.button("View on Amazon", width="100%", margin_top="0.5em"),
                href=product["affiliate_link"],
                is_external=True,
                width="100%",
            ),
            spacing="2",
            align="center",
            style={
                "text_decoration": "none",
                "color": "var(--gray-11)",
                "border": "1px solid #EAEAEA",
                "border_radius": "10px",
                "padding": "1em",
                "width": "280px",
                "height": "100%",
                "_hover": {"box_shadow": "0px 4px 20px rgba(0,0,0,0.1)"},
            }
        ),
        rx.dialog.content(
            rx.dialog.title("A Point of Motivation"),
            rx.dialog.description(product["motivation"]),
            rx.flex(
                rx.dialog.close(
                    rx.button("Close", variant="soft", color_scheme="gray"),
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            style={"max_width": "450px"},
        ),
    )


def hub_section(title: str, text_content: str, products: list[dict]):
    return rx.vstack(
        rx.heading(title, size="7"),
        rx.text(text_content, max_width="600px",
                text_align="center", color="var(--gray-11)"),
        rx.flex(
            rx.foreach(products, product_card),
            spacing="5", padding_y="2em",
            wrap="wrap", justify="center",
            align_items="stretch", 
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

def base_layout(child: rx.Component):
    return rx.vstack(child, footer(), spacing="0", align="center")


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
                    align="center", 
                    justify="center", 
                    text_align="center",
                    spacing="5", 
                    padding="2em", 
                    height="100%",
                ),
                background_image="linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), "
                                 "url('https://images.unsplash.com/photo-1558002038-1055907df827?q=80&w=2940&auto=format&fit=crop')",
                background_size="cover", 
                background_position="center",
                width="100%", 
                height="50vh",
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
            rx.link("The Kingdom is Here: A Guide to Advanced Home Robotics", href="/guides/robotics"),
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
                wrap="wrap", justify="center",
                align_items="stretch",
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
                wrap="wrap", justify="center",
                align_items="stretch",
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

@rx.page(route="/guides/robotics", title="The Kingdom is Here: Advanced Robotics | Pilot My Home")
def guide_robotics() -> rx.Component:
    return base_layout(
        rx.vstack(
            rx.heading("The Kingdom is Here: A Guide to Advanced Home Robotics", size="8", text_align="center"),
            rx.text(f"Published {datetime.now().strftime('%B %d, %Y')}", color="var(--gray-10)", text_align="center"),

            rx.vstack(
                # Housekeeper Section
                rx.heading("The Autonomous Housekeeper", size="7", padding_top="1.5em"),
                rx.text(
                    "The latest robotic floor cleaners have evolved into truly hands-off cleaning systems, capable of not just vacuuming and mopping, but also of maintaining themselves.",
                    max_width="800px",
                ),
                rx.flex(
                    rx.foreach(
                        State.housekeeper_products,
                        product_card
                    ),
                    spacing="5", padding_y="2em",
                    wrap="wrap", justify="center",
                    align_items="stretch",
                ),

                # Companion Section
                rx.heading("The Social Companion & Home Guardian", size="7", padding_top="1.5em"),
                rx.text(
                    "Moving beyond cleaning, a new category of companion robots aims to integrate more deeply into the fabric of daily life, offering a blend of security, communication, and companionship.",
                    max_width="800px",
                ),
                rx.flex(
                    rx.foreach(
                        State.companion_products,
                        product_card
                    ),
                    spacing="5", padding_y="2em",
                    wrap="wrap", justify="center",
                    align_items="stretch",
                ),

                # Landscaper Section
                rx.heading("The Automated Landscaper", size="7", padding_top="1.5em"),
                rx.text(
                    "For those with a yard to maintain, robotic lawnmowers offer a set-it-and-forget-it solution to landscaping, now with more advanced navigation and control than ever before.",
                    max_width="800px",
                ),
                rx.flex(
                    rx.foreach(
                        State.landscaper_products, 
                        product_card
                    ),
                    spacing="5", padding_y="2em",
                    wrap="wrap", justify="center",
                    align_items="stretch",
                ),

                spacing="4",
                max_width="90%",
                align="center",
                text_align="center",
            ),
            padding="2em", spacing="4", align="center"
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