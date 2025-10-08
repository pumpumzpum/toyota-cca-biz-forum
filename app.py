import streamlit as st
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, List, Tuple

import altair as alt
import pandas as pd
from streamlit_image_select import image_select

# --------------- Page Config / Header --------------- #
st.set_page_config(page_title="Pick Your Ride!", layout="wide", page_icon="🏎️")
st.title("Pick Your Style → Find Your Ride เลือกสิ่งที่ชอบ…แล้วมาดูรถที่ใช่")
st.write("""🚗 ไม่ต้องรู้เรื่องเครื่องยนต์ ไม่ต้องคิดเยอะ เลือกตามใจ แล้วปล่อยให้ความชอบ พาคุณไปหารถที่พร้อมจะไปกับคุณ""")



# --------------- Data Preparation --------------- #
# questions data structure --> Object = [{key: object(anything --> str, int, float, list, etc.)}]
QUESTIONS: List[Dict[str, object]] = [
    {
        "key": "ของที่ใช้ประจำ",
        "title": "เครื่องมือเครื่องใช้ที่คุ้นเคยกับคุณมากที่สุด?",
        "description": "ลองเลือกดูกันเลยยย",
        "options": [
            {
                "label": "City-smart EV commuter",
                "image": "images\q1_choice1.png",
                "weights": {
                    "Tesla Model Y": 6,
                    "Toyota RAV4 Hybrid": 2,
                    "Mercedes-Benz EQS Sedan": 3,
                },
            },
            {
                "label": "Family-first comfort cruiser",
                "image": "images\q1_choice2.png",
                "weights": {
                    "Toyota RAV4 Hybrid": 6,
                    "Mercedes-Benz EQS Sedan": 3,
                    "BMW 3 Series": 2,
                },
            },
            {
                "label": "Off-road adventure seeker",
                "image": "images\q1_choice3.png",
                "weights": {
                    "Ford Bronco": 7,
                    "Toyota RAV4 Hybrid": 3,
                },
            },
            {
                "label": "Track day thrill lover",
                "image": "images\q1_choice4.png",
                "weights": {
                    "Porsche 911 Carrera": 7,
                    "BMW 3 Series": 4,
                    "Tesla Model Y": 1,
                },
            },
        ],
    },
    {
        "key": "interior_vibe",
        "title": "Which interior vibe feels right to you?",
        "description": "Think about the cabin you want to slip into every day.",
        "options": [
            {
                "label": "Minimalist tech lounge",
                "image": "https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Tesla Model Y": 6,
                    "Mercedes-Benz EQS Sedan": 4,
                    "BMW 3 Series": 2,
                },
            },
            {
                "label": "Executive leather suite",
                "image": "images/Innovazenix_hev_premium.jpg",
                "weights": {
                    "Mercedes-Benz EQS Sedan": 7,
                    "BMW 3 Series": 4,
                    "Porsche 911 Carrera": 2,
                },
            },
            {
                "label": "Flexible family-ready space",
                "image": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Toyota RAV4 Hybrid": 6,
                    "Tesla Model Y": 3,
                    "Ford Bronco": 2,
                },
            },
            {
                "label": "Durable adventure cabin",
                "image": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Ford Bronco": 6,
                    "Toyota RAV4 Hybrid": 3,
                    "Tesla Model Y": 1,
                },
            },
        ],
    },
    {
        "key": "weekend_plan",
        "title": "What does your ideal weekend with the car look like?",
        "description": "Choose the vibe that sounds most fun.",
        "options": [
            {
                "label": "Tackling mountain trails",
                "image": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Ford Bronco": 7,
                    "Toyota RAV4 Hybrid": 3,
                },
            },
            {
                "label": "City nightlife hopping",
                "image": "https://images.unsplash.com/photo-1493238792000-8113da705763?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Porsche 911 Carrera": 6,
                    "BMW 3 Series": 4,
                    "Tesla Model Y": 2,
                },
            },
            {
                "label": "Cross-country road trip",
                "image": "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Toyota RAV4 Hybrid": 7,
                    "Mercedes-Benz EQS Sedan": 3,
                    "Tesla Model Y": 2,
                },
            },
            {
                "label": "Future-tech showcase",
                "image": "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Tesla Model Y": 6,
                    "Mercedes-Benz EQS Sedan": 4,
                    "BMW 3 Series": 2,
                },
            },
        ],
    },
    {
        "key": "must_have",
        "title": "Which must-have feature matters most?",
        "description": "Pick the one you refuse to compromise on.",
        "options": [
            {
                "label": "Autopilot and constant updates",
                "image": "https://images.unsplash.com/photo-1549924231-f129b911e442?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Tesla Model Y": 7,
                    "Mercedes-Benz EQS Sedan": 3,
                    "Toyota RAV4 Hybrid": 2,
                },
            },
            {
                "label": "High-end comfort and audio",
                "image": "https://images.unsplash.com/photo-1517940018979-1a96d1bf9e3e?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Mercedes-Benz EQS Sedan": 7,
                    "BMW 3 Series": 3,
                    "Tesla Model Y": 2,
                },
            },
            {
                "label": "Removable roof and traction",
                "image": "https://images.unsplash.com/photo-1523987355523-c7b5b74a6111?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Ford Bronco": 7,
                    "Toyota RAV4 Hybrid": 3,
                    "Porsche 911 Carrera": 1,
                },
            },
            {
                "label": "Precision handling and power",
                "image": "https://images.unsplash.com/photo-1503736334956-4c8f8e92946d?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Porsche 911 Carrera": 7,
                    "BMW 3 Series": 4,
                    "Tesla Model Y": 2,
                },
            },
        ],
    },
    {
        "key": "personality",
        "title": "Which statement best matches your car personality?",
        "description": "Pick the sentence that sounds like you.",
        "options": [
            {
                "label": "I'm a tech-forward pioneer",
                "image": "https://images.unsplash.com/photo-1462396881884-de2c07cb95ed?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Tesla Model Y": 10,
                    "Mercedes-Benz EQS Sedan": 10,
                    "BMW 3 Series": 2,
                },
            },
            {
                "label": "I'm a sophisticated executive",
                "image": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Mercedes-Benz EQS Sedan": 7,
                    "BMW 3 Series": 4,
                    "Tesla Model Y": 1,
                },
            },
            {
                "label": "I'm an adventurous trailblazer",
                "image": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Ford Bronco": 7,
                    "Toyota RAV4 Hybrid": 4,
                    "Porsche 911 Carrera": 1,
                },
            },
            {
                "label": "I'm a precision performance fan",
                "image": "https://images.unsplash.com/photo-1515777315835-281b94c9589a?auto=format&fit=crop&w=400&q=80",
                "weights": {
                    "Porsche 911 Carrera": 7,
                    "BMW 3 Series": 4,
                    "Tesla Model Y": 2,
                },
            },
        ],
    },
]

ALL_CARS: List[str] = [
    "Tesla Model Y",
    "BMW 3 Series",
    "Ford Bronco",
    "Porsche 911 Carrera",
    "Toyota RAV4 Hybrid",
    "Mercedes-Benz EQS Sedan",
]

CAR_IMAGE_LOOKUP: Dict[str, str] = {
    "Tesla Model Y": "images/Innovazenix_hev_premium.jpg",
    "BMW 3 Series": "images/Innovazenix_hev_premium.jpg",
    "Ford Bronco": "images/Innovazenix_hev_premium.jpg",
    "Porsche 911 Carrera": "images/Innovazenix_hev_premium.jpg",
    "Toyota RAV4 Hybrid": "images/Innovazenix_hev_premium.jpg",
    "Mercedes-Benz EQS Sedan": "images/Innovazenix_hev_premium.jpg",
}

IMAGE_BOX_HEIGHT = 190
SUMMARY_IMAGE_HEIGHT = 240


# --------------- Utilize function --------------- #


def render_choice_image(
    image_url: str,
    alt_text: str,
    box_height: int = IMAGE_BOX_HEIGHT,
    selected: bool = False,
) -> None:
    """Render a fixed-height image box so all options share the same footprint."""
    border_color = "#3b82f6" if selected else "rgba(0, 0, 0, 0.08)"
    border_width = "3px" if selected else "1px"
    card_html = f"""
        <div
            title="{alt_text}"
            style="
                background-image: url('{image_url}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                border-radius: 12px;
                height: {box_height}px;
                width: 100%;
                background-color: #f5f5f5;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
                border: {border_width} solid {border_color};
            "
        ></div>
    """
    st.markdown(card_html.strip(), unsafe_allow_html=True)


FALLBACK_PERCENTAGES: List[Tuple[str, float]] = [
    ("Toyota RAV4 Hybrid", 40.0),
    ("Tesla Model Y", 30.0),
    ("Ford Bronco", 20.0),
    ("BMW 3 Series", 10.0),
]


def allocate_percentages(weights: List[float], precision: str = "0.1") -> List[float]:
    """Convert raw weights into percentages that add up to exactly 100.0."""
    if not weights:
        return []
    
    # precision = Decimal(precision)
    # total = sum(weights)

    quantize_to = Decimal(precision)
    hundred = Decimal("100")
    decimal_weights = [Decimal(str(value)) for value in weights]
    total = sum(decimal_weights)

    if total == 0:
        equal_share = hundred / Decimal(len(weights)) # -> 100/number of weights ----> 100/4 = 0.25
        decimals = [equal_share for _ in weights] # ??? for what?
    else:
        decimals = [(value / total) * hundred for value in decimal_weights] # --> list of weight (float)

    decimals = [number.quantize(quantize_to, rounding=ROUND_HALF_UP) for number in decimals]
    difference = hundred - sum(decimals)
    if decimals:
        decimals[-1] = (decimals[-1] + difference).quantize(quantize_to, rounding=ROUND_HALF_UP)

    return [float(number) for number in decimals]


def score_answers(responses: Dict[str, str]) -> Dict[str, float]:
    """Aggregate weights for each car based on the selected options."""
    scores = {car: 0.0 for car in ALL_CARS} # --> {'camry':0.0, 'ativ':0.0, ...}
    for question in QUESTIONS:
        choice = responses.get(question["key"]) # --> "index: 0,1,2,3" 4 choices
        if choice:
            option = next((opt for opt in question["options"] if opt["label"] == question["options"][choice]["label"]), None)
            if option:
                for car, weight in option["weights"].items():
                    scores[car] = scores.get(car, 0.0) + float(weight)

    return scores


def summarize_preferences(responses: Dict[str, str]):
    """Build the guessed car summary and provide metadata about answer completeness."""
    scores = score_answers(responses)
    # st.write(f"score {scores}")
    candidates = [(car, score) for car, score in scores.items() if score > 0]
    candidates.sort(key=lambda item: item[1], reverse=True)
    names = [car for car, _ in candidates]
    weights = [score for _, score in candidates]
    percentages = allocate_percentages(weights)
    summary = [
        {"car_name": car, "percentage": percentage}
        for car, percentage in zip(names, percentages)
    ]
    return summary


def describe_user_choices(responses: Dict[str, str]) -> List[str]: # OK CAN EDIT
    """Create human-friendly summaries of the user's selections."""
    descriptions: List[str] = []
    for question in QUESTIONS:
        selection = responses.get(question["key"])
        if not selection:
            continue
        descriptions.append(f"สำหรับคำถาม: '{question['title']}', คุณได้เลือก: '{question['options'][selection]['label']}'.")
    return descriptions


# --------------- UI Development --------------- #

for question in QUESTIONS:
    st.subheader(question["title"])
    st.caption(question["description"])

    option_labels = [option["label"] for option in question["options"]]
    option_images = [option["image"] for option in question["options"]]

    selected_caption = image_select(
        label=f"เลือกรูปภาพที่ใกล้เคียงมากที่สุด {question['title']}",
        images=option_images,
        captions=option_labels,
        use_container_width=True,
        return_value="original",
        key=f"answer_{question['key']}",
    )

    # st.markdown(f"Current pick: **{selected_caption}**")
    st.divider()

submitted = st.button("ลองทายดู", type="primary")

if submitted:
    answers = {
        question["key"]: st.session_state.get(f"answer_{question['key']}")
        for question in QUESTIONS
    }
    summary = summarize_preferences(answers)
    choice_descriptions = describe_user_choices(answers)

    st.markdown("### รถที่ใช่สำหรับคุณคืออ")
    # st.json({"guessed_cars": summary})

    chart_df = pd.DataFrame(summary).sort_values('percentage', ascending=False).reset_index(drop=True)
    st.markdown("#### มาดูสัดส่วนรถที่คุณชอบกัน!!! ")
    bar_height = 60
    chart_height = max(bar_height * len(chart_df), bar_height * 3)
    base_chart = alt.Chart(chart_df).encode(
        x=alt.X('percentage:Q', title='Match likelihood (%)', scale=alt.Scale(domain=(0, 100))),
        y=alt.Y('car_name:N', sort='-x', title=None),
        color=alt.Color('car_name:N', legend=None),
        tooltip=[
            alt.Tooltip('car_name:N', title='Car'),
            alt.Tooltip('percentage:Q', title='Likelihood', format='.1f'),
        ],
    )
    bar_layer = base_chart.mark_bar(size=45, cornerRadiusTopRight=6, cornerRadiusBottomRight=6)
    label_layer = base_chart.mark_text(dx=6, dy=0, align='left', baseline='middle', fontWeight='bold').encode(
        text=alt.Text('percentage:Q', format='.1f'),
    )
    combined_chart = (
        alt.layer(bar_layer, label_layer)
        .properties(height=chart_height)
        .configure_view(stroke=None)
    )
    st.altair_chart(combined_chart, use_container_width=True)

    st.markdown("#### ความชอบของคุณ... พาคุณมาหารถที่ใช่ได้อย่างไร ")
    if choice_descriptions:
        st.write("จากที่คุณบอกเรามา")
        for detail in choice_descriptions:
            st.write(f"- {detail}")
    st.write("มาดูว่าคุณน่าจะชอบรถอะไรบ้างกันดู!")
    for entry in summary:
        st.write(f"- {entry['car_name']} - {entry['percentage']}% fit")

    showcase_entries = summary[: min(3, len(summary))]
    if showcase_entries:
        st.markdown("#### ตัวอย่างของรถที่คุณชอบ 3 อันดับแรก")
        columns = st.columns(len(showcase_entries))
        for column, entry in zip(columns, showcase_entries):
            with column:
                image_url = CAR_IMAGE_LOOKUP.get(entry["car_name"])
                if image_url:
                    st.image(image_url)
                    # render_choice_image(image_url, entry['car_name'], box_height=SUMMARY_IMAGE_HEIGHT)
                st.caption(f"{entry['car_name']} - {entry['percentage']}% match")

    st.success("ขอบคุณที่ร่วมเล่นสนุกกับเรา รอรับของรางวัลต่อได้เลย!")
