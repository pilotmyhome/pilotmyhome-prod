import reflex as rx
from datetime import datetime
from typing import List, Dict, TypedDict, Union
import aiohttp
import random

# --- Define TypedDicts for better type hinting ---
class Product(TypedDict):
    """Represents a product with its details."""
    title: str
    image_url: str
    affiliate_link: str
    motivation: str
    category: str # Added for robotics products, optional for others
    guide_id: str # Added to link back to the parent guide

class Guide(TypedDict):
    """Represents a guide with its associated products."""
    id: str
    title: str
    description: str
    icon: str
    products: List[Product]
# -----------------------------------------------------------------------------# App State# -----------------------------------------------------------------------------
class State(rx.State):
    """The application state."""
    guides_data: List[Guide] = [
        {
            "id": "peaceful_home",
            "title": "A Guide to a Peaceful Home",
            "description": "Create a sanctuary of calm and security. These tools help protect your home and automate daily tasks, giving you priceless peace of mind.",
            "icon": "home",
            "products": [
                { "title": "Ring Battery Doorbell with Head‑to‑Toe Video – Satin Nickel", "image_url": "https://m.media-amazon.com/images/I/519N1IBi3iL._SY450_.jpg", "affiliate_link": "https://www.amazon.com/Ring-Battery-Doorbell-Head-to-Toe-Video-Satin-Nickel/dp/B0BZWRSRWV?tag=pilotmyhome-20", "motivation": "The Bible calls us to be wise and vigilant. Guarding the threshold of your home is an act of stewardship, creating a sanctuary of peace where your family can flourish without fear, welcoming guests with confidence." },
                { "title": "Philips Hue Smart 60W A19 LED Bulb – White Ambiance (Bluetooth)", "image_url": "https://m.media-amazon.com/images/I/611-Y8IALHL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Philips-Hue-Bluetooth-compatible-Assistant/dp/B07QV9XLSD?tag=pilotmyhome-20", "motivation": "As we are called to be a light in the world, let us first cultivate light within our homes. Use your home's atmosphere to set aside moments for peace, prayer, and warm fellowship, letting your light shine for others to see." },
                { "title": "roborock Q7 M5 Robot Vacuum and Mop Combo, 10 000 Pa HyperForce", "image_url": "https://m.media-amazon.com/images/I/7162dbcZW3L._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/roborock-Q7-M5-Anti-Tangle-APP-Controlled/dp/B0DSJ93KPD?tag=pilotmyhome-20", "motivation": "Our time is a precious gift from God. By being good stewards of our minutes and automating the mundane, we reclaim time not for idleness, but for purpose: for family, for prayer, and for serving others with renewed energy." },
            ],
        },
        {
            "id": "connected_family",
            "title": "A Guide to a Connected Family",
            "description": "In a world of digital distraction, use technology to bring your family closer together. These picks are designed for shared experiences.",
            "icon": "users",
            "products": [
                { "title": "Aura Digital Picture Frame – 10.1″ HD Mat Display, Unlimited Storage", "image_url": "https://m.media-amazon.com/images/I/71WSCdw8rJL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Digital-Picture-Unlimited-Storage-Anywhere/dp/B09X2CL5HG?tag=pilotmyhome-20", "motivation": "Let your home tell a story of gratitude. A digital frame becomes a living testament to God's blessings, displaying a rotating gallery of cherished moments and loved ones, reminding us daily of the joy He has given." },
                { "title": "Anker NEBULA Capsule Smart Wi‑Fi Mini Projector (100 ANSI lumen)", "image_url": "https://m.media-amazon.com/images/I/610dDc+YfDL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Projector-Anker-Portable-High-Contrast-Playtime/dp/B076Q3GBJK?tag=pilotmyhome-20", "motivation": "Fellowship is a cornerstone of a faith-filled life. This tool helps transform any room into a place for shared, wholesome experiences, strengthening family bonds one movie night or shared presentation at a time." },
                { "title": "Amazon Echo Dot (5th Gen, 2022 Release) Glacier White", "image_url": "https://m.media-amazon.com/images/I/7116ea3BmTL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Amazon-release-vibrant-helpful-routines/dp/B09B94RL1R?tag=pilotmyhome-20", "motivation": "The book of Proverbs speaks of the power of a timely word. Use this helper to fill your home with worship music, listen to the Word of God, or set reminders for prayer, intentionally inviting His presence into your daily rhythm." },
            ],
        },
        {
            "id": "abundant_kitchen",
            "title": "A Guide to an Abundant Kitchen",
            "description": "The kitchen is the heart of the home. Steward your resources well and simplify mealtime with technology that serves your family.",
            "icon": "utensils",
            "products": [
                { "title": "Instant Pot Duo Crisp 11‑in‑1 Air Fryer & Pressure Cooker, 6 Qt", "image_url": "https://m.media-amazon.com/images/I/81vc3qXKPpL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Instant-Pot-Multi-Use-Pressure-Cooker/dp/B08WCLJ7JG?tag=pilotmyhome-20", "motivation": "Breaking bread together is a sacred act. By simplifying the preparation of meals, we reduce stress and create more opportunity for meaningful conversation and connection around the dinner table, the heart of the home." },
                { "title": "Echo Show 8 (2nd Gen, 2021 release) – 8″ HD Smart Display with 13 MP Camera", "image_url": "https://m.media-amazon.com/images/I/71ldF3vJclL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/All-New-Echo-Show-8/dp/B0BLS3Y632?tag=pilotmyhome-20", "motivation": "Hospitality is a gift. This kitchen companion helps you manage recipes, video call loved ones, and organize your home with ease, empowering you to serve your family and guests with a joyful and ordered spirit." },
            ],
        },
        {
            "id": "spirit_ambiance",
            "title": "A Guide to a Spirit-Led Ambiance",
            "description": "Invite the purity of God’s presence into your home with these scriptures, scents, and sacred décor items.",
            "icon": "lightbulb",
            "products": [
                { "title": "The Battle Is Not Yours - Warrior Christian Wall Art Print, Angel Inspirational Bible Verse Art", "image_url": "https://m.media-amazon.com/images/I/71qQE25MhBL._SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Battle-Not-Yours-Inspirational-Motivational/dp/B0F2VSXLXV?tag=pilotmyhome-20", "motivation": "Surround your family with visual reminders of God's promises. This artwork serves as a daily declaration of faith, reinforcing the truth that our strength comes from Him, and our battles are ultimately in His hands." },
                { "title": "Wooden Scripture Prayer Bowl for Home Decor – Christian Tabletop Centerpiece", "image_url": "https://m.media-amazon.com/images/I/81iWvF9qS3L._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/P-Graham-Dunn-Acacia-Wood-Scripture/dp/B0B6W5M2G4?tag=pilotmyhome-20", "motivation": "Prayer is our direct line to the Father. A prayer bowl creates a physical space for the spiritual discipline of intercession, encouraging family members to write down and lift up their praises and petitions together." },
                { "title": "Bible‑Verse Scented Candle Set (36 Tins) – Scripture Aroma Candles", "image_url": "https://m.media-amazon.com/images/I/81urHfEWxVL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Threlaco-Christian-Scripture-Birthday-Graduation/dp/B0CRKTPTWY?tag=pilotmyhome-20", "motivation": "Engage all senses in worship. The gentle light and pleasant aroma of a candle can transform a space, quieting the mind and preparing the heart for devotion, scripture reading, or a moment of peaceful reflection." },
            ],
        },
        {
            "id": "security",
            "title": "A Christian Family's Guide to Home Security & Peace of Mind",
            "description": "Our homes are our sanctuaries—a gift we are called to steward wisely. In today's world, that stewardship includes being thoughtful about security. This isn't about living in fear, but about creating an environment of peace and safety where your family can flourish.",
            "icon": "shield-check",
            "products": [
                { "title": "Ring Battery Doorbell with Head‑to‑Toe Video – Satin Nickel", "image_url": "https://m.media-amazon.com/images/I/519N1IBi3iL._SY450_.jpg", "affiliate_link": "https://www.amazon.com/Ring-Battery-Doorbell-Head-to-Toe-Video-Satin-Nickel/dp/B0BZWRSRWV?tag=pilotmyhome-20", "motivation": "The Bible calls us to be wise as serpents and innocent as doves. Guarding the threshold of your home is an act of wisdom, creating a sanctuary of peace where your family can flourish without fear.", "category": "security" },
                { "title": "Blink Outdoor 4 (4th Gen) – Wire-free smart security camera", "image_url": "https://m.media-amazon.com/images/I/61s4s6sXyIL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Blink-Outdoor-4th-Gen-Wire-free/dp/B0B12C2N2X?tag=pilotmyhome-20", "motivation": "Good stewardship extends to the property God has blessed us with. A watchful eye over your home provides not just security, but also the peace of mind that allows you to rest, knowing you've taken practical steps to protect your family.", "category": "security" },
                { "title": "eufy Security S220 SoloCam, Wireless Outdoor Security Camera", "image_url": "https://m.media-amazon.com/images/I/61Vd6v-0gmL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/eufy-Security-S220-SoloCam-Spotlight/dp/B09T92N52N?tag=pilotmyhome-20", "motivation": "Let your peace not be disturbed by worry. Tools that provide awareness of your surroundings free your mind from 'what-ifs', allowing you to be more present and focused on your family and your walk with God.", "category": "security" },
            ],
        },
        {
            "id": "stewardship",
            "title": "Good Stewardship of Time: A Guide",
            "description": "Time is one of the most precious resources God has given us. Being good stewards of our time allows us to focus on what truly matters: our faith, our relationships, and our purpose.",
            "icon": "clock",
            "products": [
                { "title": "roborock Q7 M5 Robot Vacuum and Mop Combo, 10 000 Pa HyperForce", "image_url": "https://m.media-amazon.com/images/I/7162dbcZW3L._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/roborock-Q7-M5-Anti-Tangle-APP-Controlled/dp/B0DSJ93KPD?tag=pilotmyhome-20", "motivation": "Our time is a precious gift from God. By being good stewards of our minutes and automating the mundane, we reclaim time not for idleness, but for purpose: for family, for prayer, and for serving others with renewed energy.", "category": "stewardship" },
                { "title": "Instant Pot Duo Crisp 11‑in‑1 Air Fryer & Pressure Cooker, 6 Qt", "image_url": "https://m.media-amazon.com/images/I/81vc3qXKPpL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Instant-Pot-Multi-Use-Pressure-Cooker/dp/B08WCLJ7JG?tag=pilotmyhome-20", "motivation": "Breaking bread together is a sacred act. By simplifying the preparation of meals, we reduce stress and create more opportunity for meaningful conversation and connection around the dinner table, the heart of the home.", "category": "stewardship" },
                { "title": "Amazon Echo Dot (5th Gen, 2022 Release) Glacier White", "image_url": "https://m.media-amazon.com/images/I/7116ea3BmTL._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/Amazon-release-vibrant-helpful-routines/dp/B09B94RL1R?tag=pilotmyhome-20", "motivation": "The book of Proverbs speaks of the power of a timely word. Use this helper to fill your home with worship music, listen to the Word of God, or set reminders for prayer, intentionally inviting His presence into your daily rhythm.", "category": "stewardship" },
            ],
        },
        {
            "id": "robotics",
            "title": "The Kingdom is Here: A Guide to Advanced Home Robotics",
            "description": "From autonomous housekeepers to companion bots and automated landscapers, discover how robotics can serve your home.",
            "icon": "robot",
            "products": [
                { "title": "Roborock S8 MaxV Ultra", "image_url": "https://m.media-amazon.com/images/I/712iLYEEb3L._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/roborock-S8-MaxV-Ultra-Self-Drying/dp/B0CQLPNB2X?tag=pilotmyhome-20", "motivation": "The Kingdom of God is one of peace and order. By delegating the constant task of maintaining a clean foundation for our home, we act as wise stewards of our God-given energy, focusing less on the dust of the world and more on cultivating a sanctuary of peace.", "category": "housekeeper" },
                { "title": "ECOVACS DEEBOT T50 PRO Omni Robot Vacuum and Mop, 3.19", "image_url": "https://m.media-amazon.com/images/I/610I+9D8U6L._AC_SL1500_.jpg", "affiliate_link": "https://www.amazon.com/ECOVACS-T50-PRO-Ultra-Slim-Self-Emptying/dp/B0DSB92P1N?tag=pilotmyhome-20", "motivation": "A well-ordered home that is ready to welcome others is an act of hospitality and love. Automating the core of our home's cleanliness prepares our hearts and our space to be present for fellowship, unburdened by the stress of pending chores.", "category": "housekeeper" },
            ],
        },
        {
            "id": "digital_media",
            "title": "Faith in Focus: A Guide to Digital Media for Spiritual Growth",
            "description": "Utilize digital resources to deepen your understanding of scripture, enrich your prayer life, and cultivate spiritual discipline.",
            "icon": "book-open",
            "products": [
                { "title": "NIV Study Bible, Fully Revised Edition", "image_url": "https://m.media-amazon.com/images/I/61X-21r-RzL._SY450_.jpg", "affiliate_link": "https://www.amazon.com/NIV-Study-Bible-Fully-Revised/dp/0310450378?tag=pilotmyhome-20", "motivation": "The Word of God is a lamp to our feet and a light to our path. A study Bible provides invaluable insights, commentaries, and resources to deepen your understanding and application of Scripture in daily life." },
                { "title": "My Prayer Journal: A Guided Christian Journal", "image_url": "https://m.media-amazon.com/images/I/71u9+54m0PL._SY450_.jpg", "affiliate_link": "https://www.amazon.com/My-Prayer-Journal-Guided-Christian/dp/1523507548?tag=pilotmyhome-20", "motivation": "Journaling your prayers and reflections can transform your spiritual walk. It allows you to track God's faithfulness, express your heart, and grow in gratitude as you witness His answers and guidance over time." },
            ],
        },
    ]

    non_product_guides: List[Guide] = [
        {
            "id": "tucson-arizona-in-person-service",
            "title": "Tucson Arizona In Person Service",
            "description": "Join fellow believers in Tucson for uplifting in-person services, fostering community and spiritual growth in Christ's love.",
            "icon": "church",
            "products": [],
        },
        {
            "id": "things-for-sell",
            "title": "Things for Sell",
            "description": "Discover items that support your faith journey, where every purchase sows seeds of abundance in God's kingdom.",
            "icon": "gift",
            "products": [],
        },
    ]

    all_products: List[Product] = []
    product_deck: List[Product] = []
    feed_products: List[Product] = []
    hovered_sidebar_item: str = ""

    def _initialize_products(self):
        """Build the master list of all products."""
        if not self.all_products:
            temp_products = []
            for guide in self.guides_data:
                for product in guide["products"]:
                    product["guide_id"] = guide["id"]
                    temp_products.append(product)
            self.all_products = temp_products

    def _create_new_deck(self) -> List[Product]:
        """Create a new shuffled deck of all products."""
        self._initialize_products()
        new_deck = self.all_products[:]
        random.shuffle(new_deck)
        return new_deck

    def shuffle_feed(self):
        """Create a new deck and deal the first few products to the feed."""
        self.product_deck = self._create_new_deck()
        self.feed_products = [self.product_deck.pop(0) for _ in range(5) if self.product_deck]

    def load_more_products(self):
        """Deal another product from the deck, reshuffling if empty."""
        if not self.product_deck:
            self.product_deck = self._create_new_deck()
        
        if self.product_deck:
            self.feed_products.append(self.product_deck.pop(0))

    def set_hovered_sidebar_item(self, item: str):
        """Set the currently hovered sidebar item to display its label."""
        self.hovered_sidebar_item = item

    def clear_hovered_sidebar_item(self):
        """Clear the hovered sidebar item."""
        self.hovered_sidebar_item = ""

    @rx.var
    def get_guide_by_id(self) -> Guide:
        """Get a guide (product or non-product) by its route ID."""
        guide_id = self.router.page.params.get("guide_id", "")
        all_guides = self.guides_data + self.non_product_guides
        for guide in all_guides:
            if guide["id"] == guide_id:
                return guide
        return Guide(id="404", title="Guide Not Found", description="The requested guide could not be found.", icon="x-circle", products=[])

    @rx.var
    def page_title(self) -> str:
        """Computes the page title based on the current route."""
        route = self.router.page.path
        if route == "/":
            return "Pilot My Home | Abundant Living with Technology"
        
        guide_id = self.router.page.params.get("guide_id", "")
        if guide_id:
            guide = self.get_guide_by_id
            if guide and guide["id"] != "404":
                return f"{guide.get('title', 'Guide')} | Pilot My Home"
        return "Pilot My Home"

# -----------------------------------------------------------------------------# Reusable Components# -----------------------------------------------------------------------------

def product_post_card(product: Product) -> rx.Component:
    """A component to render a single product as a post."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.avatar(fallback="PMH", size="3", variant="soft"),
                rx.vstack(
                    rx.hstack(
                        rx.text("Pilot My Home", font_weight="bold", size="3"),
                        rx.text("@pilotmyhome", color="gray", size="2"),
                        rx.text(f"· {datetime.now().strftime('%b %d')}", color="gray", size="2"),
                        spacing="2",
                    ),
                    rx.text(product["title"], size="4", font_weight="medium", padding_y="0.5em"),
                    align_items="flex-start",
                ),
                spacing="3",
                align="start",
                width="100%",
            ),
            rx.link(
                rx.image(
                    src=product["image_url"],
                    alt=product["title"],
                    width="100%",
                    height="auto",
                    object_fit="contain",
                    border_radius="md",
                    border="1px solid var(--gray-4)",
                ),
                href=product["affiliate_link"],
                is_external=True,
                width="100%",
            ),
            rx.text(product["motivation"], size="3", color="var(--gray-11)", padding_y="0.5em"),
            rx.hstack(
                rx.link(
                    rx.button("View on Amazon", variant="soft"),
                    href=product["affiliate_link"],
                    is_external=True
                ),
                rx.link(
                    rx.button("View in Guide", variant="outline"),
                    href=f"/guides/{product['guide_id']}"
                ),
                spacing="3",
                padding_top="0.5em",
            ),
            spacing="3",
        ),
        border_bottom="1px solid var(--gray-4)",
        padding="1em",
        width="100%",
        max_width="700px",
        background="white",
    )

def sidebar_link(icon: str, href: str, label: str) -> rx.Component:
    """A reusable component for a sidebar link with a hover label."""
    return rx.link(
        rx.button(rx.icon(tag=icon, size=28), variant="ghost", width="100%"),
        href=href,
        width="100%",
        on_mouse_enter=lambda: State.set_hovered_sidebar_item(label),
    )

def x_sidebar() -> rx.Component:
    """X.com style left sidebar."""
    return rx.box(
        rx.vstack(
            sidebar_link("home", "/", "Home"),
            sidebar_link("book-open", "/guides", "All Guides"),
            sidebar_link("church", "/tucson-arizona-in-person-service", "Tucson Service"),
            sidebar_link("gift", "/things-for-sell", "Things For Sale"),
            rx.spacer(),
            width="60px",
            min_height="100vh",
            padding="1em",
            border_right="1px solid var(--gray-4)",
            align_items="center",
            position="sticky",
            top="0",
            z_index="100",
            background="white",
            spacing="2",
        ),
        on_mouse_leave=State.clear_hovered_sidebar_item,
    )

def base_layout(child: rx.Component) -> rx.Component:
    """Base layout wrapping content with dynamic metadata, sidebar, and footer."""
    return rx.fragment(
        rx.el.title(State.page_title),
        rx.hstack(
            rx.box(
                x_sidebar(),
                rx.cond(
                    State.hovered_sidebar_item != "",
                    rx.box(
                        State.hovered_sidebar_item,
                        position="absolute",
                        left="70px",
                        top="2em", # Adjust vertical position as needed
                        bg="var(--gray-2)",
                        color="var(--gray-11)",
                        padding_x="1em",
                        padding_y="0.5em",
                        border_radius="md",
                        font_weight="500",
                        z_index="99",
                        box_shadow="lg",
                    )
                ),
            ),
            rx.vstack(
                child,
                spacing="0",
                width="100%",
                align_items="center",
            ),
            spacing="0",
            align_items="flex-start",
            width="100%",
        )
    )

# -----------------------------------------------------------------------------# Main Pages# -----------------------------------------------------------------------------
@rx.page(
    route="/", 
    on_load=State.shuffle_feed,
)
def index() -> rx.Component:
    """Home page with a feed of all products as posts."""
    return base_layout(
        rx.vstack(
            rx.hstack(
                rx.avatar(fallback="PMH", size="4"),
                rx.heading("Home", size="7", margin_left="1em"),
                width="100%",
                padding="1em",
                border_bottom="1px solid var(--gray-4)",
                position="sticky",
                top="0",
                background="rgba(255, 255, 255, 0.8)",
                backdrop_filter="blur(10px)",
                z_index="10",
                max_width="700px",
            ),
            rx.vstack(
                rx.foreach(
                    State.feed_products,
                    product_post_card,
                ),
                rx.box(
                    on_mount=State.load_more_products,
                    padding="2em",
                ),
                spacing="0",
                width="100%",
                align_items="center",
            ),
            width="100%",
            spacing="0",
        )
    )

@rx.page(route="/guides")
def guides_index() -> rx.Component:
    """A page listing all available guides with products."""
    return base_layout(
        rx.vstack(
            rx.heading("All Product Guides", size="8", padding_bottom="1em"),
            rx.foreach(
                State.guides_data,
                lambda guide: rx.link(
                    rx.card(
                        rx.vstack(
                            rx.hstack(rx.icon(guide["icon"]), rx.heading(guide["title"], size="5")),
                            rx.text(guide["description"], size="2")
                        )
                    ),
                    href=f"/guides/{guide['id']}",
                    width="100%"
                )
            ),
            spacing="5",
            padding="2em",
            max_width="700px",
            width="100%"
        )
    )
    
@rx.page(route="/guides/[guide_id]")
def guide_detail() -> rx.Component:
    """A dynamic page to display a single guide and its products."""
    return base_layout(
        rx.vstack(
            rx.heading(State.get_guide_by_id["title"], size="8", text_align="center"),
            rx.text(State.get_guide_by_id["description"], padding_y="1em", max_width="800px"),
            rx.flex(
                rx.foreach(State.get_guide_by_id["products"], product_post_card),
                spacing="5",
                padding_y="2em",
                wrap="wrap",
                justify="center",
                align_items="stretch",
            ),
            max_width="90%", padding="2em", spacing="4", align="center"
        )
    )

@rx.page(route="/tucson-arizona-in-person-service")
def tucson_service() -> rx.Component:
    """Page for the Tucson, AZ in-person service."""
    guide = State.get_guide_by_id
    return base_layout(
        rx.vstack(
            rx.heading(guide["title"], size="8", text_align="center", padding="2em"),
            rx.text(guide["description"], max_width="800px"),
            align="center"
        )
    )

@rx.page(route="/things-for-sell")
def things_for_sell() -> rx.Component:
    """Page for items for sale."""
    guide = State.get_guide_by_id
    return base_layout(
        rx.vstack(
            rx.heading(guide["title"], size="8", text_align="center", padding="2em"),
            rx.text(guide["description"], max_width="800px"),
            align="center"
        )
    )

# -----------------------------------------------------------------------------# App Initialization# -----------------------------------------------------------------------------
app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="blue",
        radius="large",
    ),
    style={"body": {"background": "#F0F2F5"}},
)