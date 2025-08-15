import reflex as rx
from datetime import datetime
from typing import List, Dict, TypedDict, Union

import aiohttp

# --- Define TypedDicts for better type hinting ---
class Product(TypedDict):
    """Represents a product with its details."""
    title: str
    image_url: str
    affiliate_link: str
    motivation: str
    category: str # Added for robotics products, optional for others

class Guide(TypedDict):
    """Represents a guide with its associated products."""
    id: str
    title: str
    description: str
    icon: str
    products: List[Product]


# -----------------------------------------------------------------------------
# App State
# -----------------------------------------------------------------------------
class State(rx.State):
    """The application state."""

    # Combined and simplified data structure for all guides and their products
    guides_data: List[Guide] = [
        {
            "id": "home_main", # Special ID for the main home page "hero" section if needed
            "title": "Welcome to Pilot My Home!",
            "description": "Guiding Christian families to live more peacefully and intentionally with today's technology.",
            "icon": "home", # Placeholder icon for home post
            "products": [], # No products directly associated with this "post"
        },
        {
            "id": "peaceful_home",
            "title": "A Guide to a Peaceful Home",
            "description": "Create a sanctuary of calm and security. These tools help protect your home and automate daily tasks, giving you priceless peace of mind.",
            "icon": "home", # Reusing icon, adjust if a more specific one is desired
            "products": [
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
        },
        {
            "id": "connected_family",
            "title": "A Guide to a Connected Family",
            "description": "In a world of digital distraction, use technology to bring your family closer together. These picks are designed for shared experiences.",
            "icon": "users",
            "products": [
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
        },
        {
            "id": "abundant_kitchen",
            "title": "A Guide to an Abundant Kitchen",
            "description": "The kitchen is the heart of the home. Steward your resources well and simplify mealtime with technology that serves your family.",
            "icon": "utensils",
            "products": [
                {
                    "title": "Instant Pot Duo Crisp 11‑in‑1 Air Fryer & Pressure Cooker, 6 Qt",
                    "image_url": "https://m.media-amazon.com/images/I/81vc3qXKPpL._AC_SL1500_.jpg",
                    "affiliate_link": "https://www.amazon.com/Instant-Pot-Multi-Use-Pressure-Cooker/dp/B08WCLJ7JG?tag=pilotmyhome-20",
                    "motivation": "Breaking bread together is a sacred act. By simplifying the preparation of meals, we reduce stress and create more opportunity for meaningful conversation and connection around the dinner table, the heart of the home."
                },
                {
                    "title": "Echo Show 8 (2nd Gen, 2021 release) – 8″ HD Smart Display with 13 MP Camera",
                    "image_url": "https://m.media-amazon.com/images/I/71ldF3vJclL._AC_SL1500_.jpg",
                    "affiliate_link": "https://www.amazon.com/All-New-Echo-Show-8/dp/B0BLS3Y632?tag=pilotmyhome-20",
                    "motivation": "Hospitality is a gift. This kitchen companion helps you manage recipes, video call loved ones, and organize your home with ease, empowering you to serve your family and guests with a joyful and ordered spirit."
                },
            ],
        },
        {
            "id": "spirit_ambiance",
            "title": "A Guide to a Spirit-Led Ambiance",
            "description": "Invite the purity of God’s presence into your home with these scriptures, scents, and sacred décor items.",
            "icon": "lightbulb",
            "products": [
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
            ],
        },
        {
            "id": "security",
            "title": "A Christian Family's Guide to Home Security & Peace of Mind",
            "description": "Our homes are our sanctuaries—a gift we are called to steward wisely. In today's world, that stewardship includes being thoughtful about security. When you Ask God to save you,  don't ignore His gift of Wisdom. This isn't about living in fear, but about creating an environment of peace and safety where your family can flourish. Modern technology, when chosen and used intentionally, can be a powerful tool in piloting a secure and peaceful home.",
            "icon": "shield-check",
            "products": [
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
        },
        {
            "id": "stewardship",
            "title": "Good Stewardship of Time: A Guide",
            "description": "Time is one of the most precious resources God has given us. As families striving to live intentionally, being good stewards of our time allows us to focus on what truly matters: our faith, our relationships, and our purpose. While technology can often feel like a distraction, it can also be a powerful ally in automating the mundane tasks of daily life, freeing up hours each week for more meaningful pursuits.",
            "icon": "clock",
            "products": [
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
        },
        {
            "id": "robotics",
            "title": "The Kingdom is Here: A Guide to Advanced Home Robotics",
            "description": "From autonomous housekeepers to companion bots and automated landscapers, discover how robotics can serve your home.",
            "icon": "robot",
            "products": [
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
                    "affiliate_link": "https://www.amazon.com/eufy-Emptying-hands-free-3-35-Inch-Ultra-Slim/dp/B0DCFNZF32?tag=pilotmyhome-20",
                    "motivation": "'Whatever you do, work at it with all your heart, as working for the Lord' (Colossians 3:23). Using intelligent tools to maintain our homes with excellence is a modern way to honor this principle, serving our family with diligence.",
                    "category": "housekeeper"
                },
                {
                    "title": "Amazon Astro",
                    "image_url": "https://m.media-amazon.com/images/I/61fPLtmoSNL._AC_SL1500_.jpg",
                    "affiliate_link": "https://www.amazon.com/introducing-amazon-astro-household-robot-with-intelligent-motion/dp/B078NS8H82?tag=pilotmyhome-20",
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
                    "title": "Loona: The Smart Robot Pet",
                    "image_url": "https://m.media-amazon.com/images/I/71D9dLT8xfL._AC_SL1500_.jpg",
                    "affiliate_link": "https://www.amazon.com/Loona-ChatGPT-4o-AI-Powered-Interaction-Monitoring/dp/B0DCF53PCH?tag=pilotmyhome-20",
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
                    "affiliate_link": "https://www.amazon.com/i105N-Perimeter-AI-Assisted-Multi-Zone-Management/dp/B0CX8LL2PC?tag=pilotmyhome-20",
                    "motivation": "'Let all things be done decently and in order' (1 Corinthians 14:40). Applying this principle to our homes creates an external environment that reflects inner peace. Precise, automated tools help achieve this order, freeing our time for higher callings.",
                    "category": "landscaper"
                },
            ],
        },
        {
            "id": "digital_media",
            "title": "Faith in Focus: A Guide to Digital Media for Spiritual Growth",
            "description": "Utilize digital resources to deepen your understanding of scripture, enrich your prayer life, and cultivate spiritual discipline.",
            "icon": "book-open",
            "products": [
                {
                    "title": "NIV Study Bible, Fully Revised Edition",
                    "image_url": "https://m.media-amazon.com/images/I/61X-21r-RzL._SY450_.jpg",
                    "affiliate_link": "https://www.amazon.com/NIV-Study-Bible-Fully-Revised/dp/0310450378?tag=pilotmyhome-20",
                    "motivation": "The Word of God is a lamp to our feet and a light to our path. A study Bible provides invaluable insights, commentaries, and resources to deepen your understanding and application of Scripture in daily life."
                },
                {
                    "title": "My Prayer Journal: A Guided Christian Journal",
                    "image_url": "https://m.media-amazon.com/images/I/71u9+54m0PL._SY450_.jpg",
                    "affiliate_link": "https://www.amazon.com/My-Prayer-Journal-Guided-Christian/dp/1523507548?tag=pilotmyhome-20",
                    "motivation": "Journaling your prayers and reflections can transform your spiritual walk. It allows you to track God's faithfulness, express your heart, and grow in gratitude as you witness His answers and guidance over time."
                },
                {
                    "title": "Mere Christianity by C.S. Lewis",
                    "image_url": "https://m.media-amazon.com/images/I/8106xK01u7L._SY450_.jpg",
                    "affiliate_link": "https://www.amazon.com/Mere-Christianity-C-S-Lewis/dp/0060652926?tag=pilotmyhome-20",
                    "motivation": "Good books can sharpen our minds and deepen our faith. This classic work offers a clear and compelling defense of Christian belief, encouraging thoughtful engagement with foundational truths."
                },
                {
                    "title": "Emotionally Healthy Spirituality by Peter Scazzero",
                    "image_url": "https://m.media-amazon.com/images/I/718yG7y-0YL._SY450_.jpg",
                    "affiliate_link": "https://www.amazon.com/Emotionally-Healthy-Spirituality-Ignored-Transform/dp/0310342223?tag=pilotmyhome-20",
                    "motivation": "True spiritual growth encompasses our whole being. This guide offers practical steps to integrate emotional health with spiritual maturity, fostering deeper relationships with God and others."
                },
                {
                    "title": "Coffee and Bible Time Prayer Journal: 3 Sticky Note Pads Included",
                    "image_url": "https://m.media-amazon.com/images/I/71X+U-4aFQL._AC_SL1500_.jpg",
                    "affiliate_link": "https://www.amazon.com/Coffee-Bible-Time-Prayer-Journal/dp/B09NK2789L?tag=pilotmyhome-20",
                    "motivation": "Deepen your prayer life with this guided journal, fostering a closer relationship with God through daily reflection and gratitude in a Christian home setting."
                },
                {
                    "title": "2025 Christian Homemakers' Quarterly Planner, Bullet Journal, and Habit Tracker",
                    "image_url": "https://m.media-amazon.com/images/I/61f0j-3vJPL._AC_SL1500_.jpg",
                    "affiliate_link": "https://www.amazon.com/Quarterly-Planner-Journal-Christian-Homemakers/dp/B0CT2MTX1J?tag=pilotmyhome-20",
                    "motivation": "Steward your home with grace using this planner, integrating household tasks with spiritual habits to create a harmonious, faith-filled living space."
                },
                {
                    "title": "Walk With Me Jesus: Daily Words of Hope and Encouragement",
                    "image_url": "https://m.media-amazon.com/images/I/81z4y8m2KPL._AC_SL1500_.jpg",
                    "affiliate_link": "https://www.amazon.com/Walk-Me-Jesus-Daily-Encouragement/dp/1424550483?tag=pilotmyhome-20",
                    "motivation": "Receive daily encouragement from Scripture, reminding you of God's promises of abundance and hope in every aspect of life as a Christian family."
                },
                {
                    "title": "God's Plan for Living: A Simple Roadmap to Your IDEAL Kingdom Life",
                    "image_url": "https://m.media-amazon.com/images/I/61K8G8y-3JL._AC_SL1500_.jpg",
                    "affiliate_link": "https://www.amazon.com/Gods-Plan-Living-Roadmap-Kingdom/dp/B0BZ34CNFY?tag=pilotmyhome-20",
                    "motivation": "Design your life according to God's blueprint, creating a spiritual 'floor plan' that aligns your daily living with Kingdom principles for fulfillment and purpose in your home."
                },
            ],
        },
        {
            "id": "tucson_arizona_in_person_service",
            "title": "Tucson Arizona In Person Service",
            "description": "Join fellow believers in Tucson for uplifting in-person services, fostering community and spiritual growth in Christ's love.",
            "icon": "map-pin",
            "products": [],
        },
        {
            "id": "things_for_sell",
            "title": "Things for Sell",
            "description": "Discover items that support your faith journey, where every purchase sows seeds of abundance in God's kingdom.",
            "icon": "shopping-cart",
            "products": [],
        },
    ]

    verse: str = "Loading daily verse..."
    email: str = ""
    subscribed: bool = False
    sidebar_expanded: bool = False

    async def fetch_verse(self):
        """Fetch the Verse of the Day from API.Bible."""
        api_key = "your_api_key_here"  # Replace with your actual API key from https://scripture.api.bible/
        bible_id = "61fd76eafa1577c2-02"  # Example Bible ID (e.g., NIV)
        verses = [
            "JER.29.11", "PSA.23", "1COR.4.4-8", "PHP.4.13", "JHN.3.16",
            "ROM.8.28", "ISA.41.10", "PSA.46.1", "GAL.5.22-23", "HEB.11.1",
            "2TI.1.7", "1COR.10.13", "PRO.22.6", "ISA.40.31", "JOS.1.9",
            "HEB.12.2", "MAT.11.28", "ROM.10.9-10", "PHP.2.3-4", "MAT.5.43-44",
            "PSA.119.105", "EPH.2.8-9", "JAS.1.5", "COL.3.23", "1PE.5.7",
            "MAT.6.33", "ROM.12.2", "PSA.37.4", "PRO.3.5-6", "1TH.5.16-18",
            "MIC.6.8",
        ]
        day_index = datetime.now().day - 1
        verse_id = verses[day_index % len(verses)]  # Cycle through list if <31 days

        url = f"https://api.scripture.api.bible/v1/bibles/{bible_id}/search?query={verse_id}"
        headers = {"api-key": api_key}

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        passage = data["data"]["passages"][0]
                        self.verse = f"{passage['content']} - {passage['reference']}"
                    else:
                        self.verse = "For God so loved the world... - John 3:16 (Fallback)"
        except Exception:
            self.verse = "For God so loved the world... - John 3:16 (Fallback)"

    def handle_subscribe(self, form_data: dict):
        """Handle newsletter subscription."""
        self.email = form_data["email"]
        self.subscribed = True

    def toggle_sidebar(self):
        self.sidebar_expanded = not self.sidebar_expanded

    @rx.var
    def all_posts(self) -> List[Guide]:
        """A computed var that combines all guides and special posts."""
        return self.guides_data + [
            Guide(
                id="daily_verse_post",
                title="Daily Scripture for Your Home",
                description=self.verse,
                icon="book-open",
                products=[],
            ),
            Guide(
                id="flr_callout_post",
                title="Partnering with Family Life Radio",
                description="We endorse Family Life Radio as a God-provided source to honor Jesus together in worship tuning sessions anytime. Join us in this active prayer by tuning in or supporting their ministry.",
                icon="heart",
                products=[],
            ),
        ]

    @rx.var
    def guide_id_from_route(self) -> str:
        """Get the guide ID from the router, converting hyphens to underscores for lookup."""
        return self.router.url.params.get("guide_id", "").replace("-", "_")

    @rx.var
    def current_guide(self) -> Guide:
        """Get the current guide based on the route ID."""
        for guide in self.guides_data:
            if guide["id"] == self.guide_id_from_route:
                return guide
        # Return a default "Not Found" guide
        return Guide(
            id="404",
            title="Guide Not Found",
            description="The requested guide could not be found.",
            icon="x-circle",
            products=[]
        )
    
    @rx.var
    def housekeeper_products(self) -> List[Product]:
        if self.current_guide["id"] == "robotics":
            return [p for p in self.current_guide["products"] if p.get("category") == "housekeeper"]
        return []

    @rx.var
    def companion_products(self) -> List[Product]:
        if self.current_guide["id"] == "robotics":
            return [p for p in self.current_guide["products"] if p.get("category") == "companion"]
        return []

    @rx.var
    def landscaper_products(self) -> List[Product]:
        if self.current_guide["id"] == "robotics":
            return [p for p in self.current_guide["products"] if p.get("category") == "landscaper"]
        return []

    @rx.var
    def page_title(self) -> str:
        """Computes the page title based on the current route."""
        route = self.router.url.path
        guide_id = self.guide_id_from_route

        if guide_id and guide_id != "404":
            return f"{self.current_guide['title']} | Pilot My Home"
        
        if route == "/":
            return "Pilot My Home | Abundant Living with Technology"
        if route == "/guides":
            return "Guides | Pilot My Home"
        if route == "/about":
            return "About | Pilot My Home"
        return "Pilot My Home"

    @rx.var
    def page_description(self) -> str:
        """Computes the page description based on the current route."""
        route = self.router.url.path
        guide_id = self.guide_id_from_route
        
        if guide_id and guide_id != "404":
            return self.current_guide['description']

        if route == "/":
            return "Christian guide to smart homes for abundant living in Jesus' truth."
        if route == "/guides":
            return "In-depth Christian guides to thoughtful smart home technology."
        if route == "/about":
            return "About Pilot My Home - Faith, family, and thoughtful tech."
        return "A Christian guide to smart homes."

    @rx.var
    def sidebar_guides(self) -> List[Guide]:
        return [g for g in self.guides_data if g["id"] != "home_main"]

# -----------------------------------------------------------------------------
# Reusable Components
# -----------------------------------------------------------------------------
def product_card(product: Product) -> rx.Component:
    """Render a product card with image, title, and motivation."""
    return rx.vstack(
        rx.link(
            rx.image(
                src=product["image_url"],
                alt=f"{product['title']} - Inspired by {product['motivation'][:50]}...",
                height="150px",
                width="auto",
                object_fit="contain",
                loading="lazy",
            ),
            rx.text(product["title"], height="5em", text_align="center", font_weight="500", size="3"),
            href=product["affiliate_link"],
            is_external=True,
            width="100%",
        ),
        rx.vstack(
            rx.text("Point of Usage Wisdom", font_weight="bold", size="2"),
            rx.text(product["motivation"], size="2", trim="both"),
            spacing="1",
            padding="0.5em",
            margin_top="0.5em",
            border_top="1px solid #EAEAEA",
            width="100%",
            align_items="flex-start",
        ),
        spacing="3",
        align="center",
        justify_content="space-between",
        style={
            "text_decoration": "none",
            "color": "var(--gray-11)",
            "border": "1px solid #EAEAEA",
            "border_radius": "10px",
            "padding": "1em",
            "width": "280px",
            "height": "100%",
            "_hover": {
                "box_shadow": "0px 4px 20px rgba(0,0,0,0.1)",
                "transition": "box-shadow 0.3s ease",
            },
        }
    )

def flr_callout() -> rx.Component:
    """Creative callout for Family Life Radio endorsement."""
    return rx.callout(
        rx.vstack(
            rx.text(
                "As we pray 'Thy Kingdom come, Thy will be done on Earth as in Heaven,' my wife and I endorse Family Life Radio as a God-provided source to honor Jesus together in worship tuning sessions anytime. Join us in this active prayer by tuning in or supporting their ministry.",
                text_align="center", size="3", color="var(--gray-11)",
            ),
            rx.hstack(
                rx.link(rx.button("Tune In Now", variant="outline"), href="https://www.myflr.org/", is_external=True),
                rx.link(rx.button("Donate", variant="outline"), href="https://www.myflr.org/membership/", is_external=True),
                spacing="3",
            ),
            spacing="3",
            align="center",
        ),
        icon="heart",
        color_scheme="amber",
        variant="surface",
        high_contrast=True,
        padding="1em",
        border_radius="md",
        max_width="600px",
    )

def footer() -> rx.Component:
    """Render the footer with links, disclosure, and newsletter signup."""
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
        rx.cond(
            ~State.subscribed,
            rx.form(
                rx.hstack(
                    rx.input(placeholder="Enter your email", name="email"),
                    rx.button("Subscribe"),
                    spacing="2",
                ),
                on_submit=State.handle_subscribe,
            ),
            rx.text("Thank you for subscribing!"),
        ),
        rx.text("Join our family in following Christ through intentional living."),
        align="center", spacing="2",
        padding="2em", width="100%",
        background_color="var(--gray-2)"
    )

def guide_post_card(guide_dict: Guide) -> rx.Component:
    """Render a full guide as a "post" on the main feed."""
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
                    rx.text(guide_dict["title"], size="4", font_weight="medium"),
                    rx.text(guide_dict["description"], size="3", color="var(--gray-11)"),
                    rx.cond(
                        guide_dict["products"],
                        rx.flex(
                            rx.foreach(guide_dict["products"], product_card),
                            spacing="5", padding_y="1em",
                            wrap="wrap", justify="center",
                            align_items="stretch",
                        ),
                        rx.box(),
                    ),
                    rx.hstack(
                        rx.icon(tag="message-circle", size=16, color="gray"),
                        rx.text("0", color="gray", size="2"),
                        rx.icon(tag="repeat", size=16, color="gray"),
                        rx.text("0", color="gray", size="2"),
                        rx.icon(tag="heart", size=16, color="gray"),
                        rx.text("0", color="gray", size="2"),
                        rx.icon(tag="share", size=16, color="gray"),
                        spacing="4",
                        padding_top="0.5em",
                    ),
                    spacing="1",
                    width="100%",
                ),
                spacing="3",
                align="start",
            ),
        ),
        border_bottom="1px solid var(--gray-4)",
        padding="1em",
        width="100%",
        max_width="700px",
        background="white",
    )

def x_sidebar() -> rx.Component:
    """X.com style left sidebar."""
    link_style = {
        "padding_x": "1em",
        "padding_y": "0.7em",
        "border_radius": "full",
        "_hover": {"background_color": "var(--gray-3)"},
        "width": "100%",
        "display": "flex",
        "align_items": "center",
        "gap": "1em",
    }
    
    return rx.vstack(
        rx.tooltip(
            rx.link(
                rx.hstack(
                    rx.icon(tag="home", size=32),
                    rx.cond(State.sidebar_expanded, rx.text("P.I.L.O.T.M.Y.H.O.M.E.", size="4")),
                    align_items="center",
                    width="100%",
                ),
                href="/",
                style=link_style,
            ),
            label="P.I.L.O.T.M.Y.H.O.M.E.",
        ),
        rx.tooltip(
            rx.link(
                rx.hstack(
                    rx.icon(tag="book-open", size=32),
                    rx.cond(State.sidebar_expanded, rx.text("Guides", size="4")),
                    align_items="center",
                    width="100%",
                ),
                href="/guides",
                style=link_style,
            ),
            label="Guides",
        ),
        rx.tooltip(
            rx.link(
                rx.hstack(
                    rx.icon(tag="info", size=32),
                    rx.cond(State.sidebar_expanded, rx.text("About Us", size="4")),
                    align_items="center",
                    width="100%",
                ),
                href="/about",
                style=link_style,
            ),
            label="About Us",
        ),
        rx.spacer(),
        rx.tooltip(
            rx.link(
                rx.button(
                    rx.cond(State.sidebar_expanded, "Subscribe", rx.icon(tag="mail", size=32)),
                    size="3",
                    width="100%",
                    variant="solid",
                    color_scheme="blue",
                ),
                href="#footer_subscribe",
                is_external=False,
            ),
            label="Subscribe",
        ),
        width=rx.cond(State.sidebar_expanded, "250px", "60px"),
        min_height="100vh",
        padding="1em",
        border_right="1px solid var(--gray-4)",
        align_items="flex-start",
        position="sticky",
        top="0",
        on_mouse_enter=State.toggle_sidebar,
        on_mouse_leave=State.toggle_sidebar,
        transition="width 0.3s ease-in-out",
        z_index="100",
        background="white",
    )

def base_layout(child: rx.Component) -> rx.Component:
    """Base layout wrapping content with dynamic metadata, sidebar, and footer."""
    return rx.fragment(
        rx.el.title(State.page_title),
        rx.el.meta(name="description", content=State.page_description),
        rx.vstack(
            rx.hstack(
                x_sidebar(),
                rx.vstack(
                    child,
                    rx.box(id="footer_subscribe"),
                    footer(),
                    spacing="0",
                    width="100%",
                    max_width="700px",
                    border_x="1px solid var(--gray-4)",
                    min_height="100vh",
                ),
                spacing="0",
                align_items="flex-start",
                width="100%",
                justify="center",
            ),
            width="100vw",
            min_height="100vh",
            spacing="0",
        )
    )

# -----------------------------------------------------------------------------
# Main Pages
# -----------------------------------------------------------------------------
# Note: The 'title' and 'meta' arguments have been removed from the decorators.
# They are now handled dynamically in the base_layout function.
@rx.page(
    route="/", 
    on_load=State.fetch_verse,
)
def index() -> rx.Component:
    """Home page with a feed of all guide entities as posts."""
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
            ),
            rx.vstack(
                rx.foreach(
                    State.all_posts,
                    guide_post_card,
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
def guides() -> rx.Component:
    """Guides listing page - now a redirect or a simple overview."""
    return base_layout(
        rx.vstack(
            rx.heading("Explore All Our Guides", size="8"),
            rx.text("All our guides are now featured directly on the home page feed for easy discovery.", text_align="center"),
            rx.link(rx.button("Go to Home Feed", size="3"), href="/"),
            spacing="5", padding="4em", align="center"
        )
    )

@rx.page(route="/guides/[guide_id]")
def guide_detail() -> rx.Component:
    """A dynamic page to display a single guide and its products."""
    return base_layout(
        rx.vstack(
            rx.heading(State.current_guide["title"], size="8", text_align="center"),
            rx.text(
                f"Published {datetime.now().strftime('%B %d, %Y')}", 
                color="var(--gray-10)", 
                text_align="center"
            ),
            
            # Main description from data source
            rx.text(
                State.current_guide["description"], 
                padding_y="1em", 
                max_width="800px"
            ),

            # Default product display for guides without special layouts
            rx.cond(
                (State.guide_id_from_route != "robotics") & (State.guide_id_from_route != "security") & (State.guide_id_from_route != "stewardship"),
                rx.flex(
                    rx.foreach(State.current_guide["products"], product_card),
                    spacing="5", padding_y="2em",
                    wrap="wrap", justify="center",
                    align_items="stretch",
                )
            ),

            # Special section for the Security guide
            rx.cond(
                State.guide_id_from_route == "security",
                rx.vstack(
                    rx.heading("The Digital Welcome Mat: Video Doorbells", size="6", padding_top="1em"),
                    rx.text("The front door is the primary entry point to your home. A video doorbell acts as a digital gatekeeper, allowing you to see and speak with anyone who approaches, whether you're in the kitchen or away from home. This brings incredible peace of mind, from verifying a delivery to politely declining a solicitor without opening the door. It's a simple first step towards a more secure home."),
                    rx.heading("Your Watchful Eyes: Outdoor Cameras", size="6", padding_top="1em"),
                    rx.text("For a broader view of your property, outdoor security cameras provide another layer of reassurance. They allow you to check on children playing in the yard, monitor your property at night, and keep a record of any unusual activity. Modern wireless cameras are simple to install and offer features like motion alerts sent directly to your phone, so you are aware of what's happening at home."),
                    rx.heading("A Note on Digital Stewardship", size="6", padding_top="1em"),
                    rx.text("As we bring these tools into our homes, it's also our responsibility to be good digital stewards. Always secure your devices with strong, unique passwords and enable two-factor authentication (2FA) whenever possible. This ensures that the technology meant to protect your family is itself protected."),
                    rx.heading("Our Top Recommended Security Products", size="6", padding_top="2em"),
                    rx.flex(
                        rx.foreach(State.current_guide["products"], product_card),
                        spacing="5", padding_y="2em",
                        wrap="wrap", justify="center",
                        align_items="stretch",
                    ),
                    spacing="4", max_width="800px",
                )
            ),
            
            # Special section for the Stewardship guide
            rx.cond(
                State.guide_id_from_route == "stewardship",
                rx.vstack(
                    rx.heading("Automating the Home Base", size="6", padding_top="1em"),
                    rx.text("Think about the recurring chores that consume time every day. A robot vacuum, for example, can take over the daily task of sweeping floors, giving your family back 15-30 minutes each day. That's time that can be spent reading together, in prayer, or simply enjoying a moment of peace. Delegating these simple tasks to automation is a practical form of stewardship."),
                    rx.heading("Simplifying Mealtime", size="6", padding_top="1em"),
                    rx.text("The daily question of 'what's for dinner?' can be a significant mental and time-based burden. Smart kitchen gadgets can streamline this entire process. An Instant Pot can turn a meal that takes hours into one that takes minutes. A smart display like an Echo Show can walk you through recipes step-by-step, manage your grocery list, and set timers with just your voice. This leads to less stress in the kitchen and more blessed time together around the dinner table."),
                    rx.heading("Recommended Stewardship Tools", size="6", padding_top="2em"),
                    rx.flex(
                        rx.foreach(State.current_guide["products"], product_card),
                        spacing="5", padding_y="2em",
                        wrap="wrap", justify="center",
                        align_items="stretch",
                    ),
                    spacing="4", max_width="800px",
                )
            ),

            # Special section for the Robotics guide
            rx.cond(
                State.guide_id_from_route == "robotics",
                rx.vstack(
                    rx.heading("The Autonomous Housekeeper", size="7", padding_top="1.5em"),
                    rx.text("The latest robotic floor cleaners have evolved into truly hands-off cleaning systems, capable of not just vacuuming and mopping, but also of maintaining themselves.", max_width="800px"),
                    rx.flex(rx.foreach(State.housekeeper_products, product_card), spacing="5", padding_y="2em", wrap="wrap", justify="center", align_items="stretch"),
                    rx.heading("The Social Companion & Home Guardian", size="7", padding_top="1.5em"),
                    rx.text("Moving beyond cleaning, a new category of companion robots aims to integrate more deeply into the fabric of daily life, offering a blend of security, communication, and companionship.", max_width="800px"),
                    rx.flex(rx.foreach(State.companion_products, product_card), spacing="5", padding_y="2em", wrap="wrap", justify="center", align_items="stretch"),
                    rx.heading("The Automated Landscaper", size="7", padding_top="1.5em"),
                    rx.text("For those with a yard to maintain, robotic lawnmowers offer a set-it-and-forget-it solution to landscaping, now with more advanced navigation and control than ever before.", max_width="800px"),
                    rx.flex(rx.foreach(State.landscaper_products, product_card), spacing="5", padding_y="2em", wrap="wrap", justify="center", align_items="stretch"),
                    spacing="4", max_width="90%", align="center", text_align="center",
                )
            ),
            max_width="90%", padding="2em", spacing="4", align="center"
        )
    )

@rx.page(route="/about")
def about() -> rx.Component:
    """About page with mission and contact form."""
    return base_layout(
        rx.vstack(
            rx.heading("About Pilot My Home", size="8", text_align="center"),
            rx.vstack(
                rx.heading("Our Mission", size="6", padding_top="1em"),
                rx.text("Welcome to Pilot My Home! We are a husband and wife team dedicated to our faith, our family, and the incredible potential of technology to enrich our lives. We started Pilot My Home to share our journey and help other Christian families navigate the world of smart home devices."),
                rx.text("Our goal is to provide honest guidance on how these tools can be used not as a distraction, but as a way to create a more peaceful, secure, and intentional home environment. We believe that by thoughtfully automating daily tasks and simplifying our routines, we can be better stewards of our time, freeing us up for what truly matters: fellowship, prayer, and family."),
                rx.heading("What You'll Find Here", size="6", padding_top="1em"),
                rx.text("Here you'll find practical guides, in-depth reviews, and curated recommendations for products we believe in. We're so glad you're here and pray this resource is a blessing to you and your family."),
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
        accent_color="blue",
        radius="large",
    ),
    style={"body": {"background": "#F0F2F5"}},
)