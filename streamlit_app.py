import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(page_title="PromoPlay Lab – Chickasaw Nation", page_icon="🎰")

# Define sample patron segments
segments = {
    "High Value Frequent": {"trips": 14, "coin_in": 38000},
    "High Value Infrequent": {"trips": 3, "coin_in": 17800},
    "Mid Value": {"trips": 2.3, "coin_in": 2270},
    "Low Value": {"trips": 1.4, "coin_in": 275},
}

# Define promotion impact multipliers
promotions = {
    "$50 Free Play": {"trips_mult": 1.3, "coin_in_mult": 1.2, "cost": 50},
    "$100 Free Play": {"trips_mult": 1.6, "coin_in_mult": 1.5, "cost": 100},
    "Hotel Comp": {"trips_mult": 1.2, "coin_in_mult": 1.1, "cost": 75},
    "SMS Campaign": {"trips_mult": 1.1, "coin_in_mult": 1.05, "cost": 5},
    "VIP Event Invite": {"trips_mult": 1.4, "coin_in_mult": 1.3, "cost": 120},
}

# Sidebar
st.sidebar.title("PromoPlay Lab 🎯")
st.sidebar.markdown("A drag-and-drop simulator for strategic promotions.")
segment_choice = st.sidebar.selectbox("Select Patron Segment", list(segments.keys()))
promo_choices = st.sidebar.multiselect("Choose Promotions", list(promotions.keys()))

# Base metrics
base = segments[segment_choice]
total_trips = base["trips"]
total_coin_in = base["coin_in"]
total_cost = 0

# Apply promotions
for promo in promo_choices:
    promo_data = promotions[promo]
    total_trips *= promo_data["trips_mult"]
    total_coin_in *= promo_data["coin_in_mult"]
    total_cost += promo_data["cost"]

# Estimate ROI
roi = (total_coin_in * 0.05 - total_cost) / total_cost if total_cost > 0 else 0

# Display
st.title("🎰 Casino Promo Strategy Simulator")
st.subheader(f"📊 Segment: `{segment_choice}`")

col1, col2 = st.columns(2)
col1.metric("Projected Trips", f"{total_trips:.1f}")
col2.metric("Projected Coin-In", f"${total_coin_in:,.2f}")

col3, col4 = st.columns(2)
col3.metric("Promotion Cost", f"${total_cost:,.2f}")
col4.metric("Estimated ROI", f"{roi:.2f}x")

st.divider()
st.markdown("#### 🎯 Promotion Details")
if promo_choices:
    for promo in promo_choices:
        st.write(
            f"- **{promo}**: +{int((promotions[promo]['coin_in_mult'] - 1)*100)}% coin-in, "
            f"Cost = ${promotions[promo]['cost']}"
        )
else:
    st.info("Choose one or more promotions from the sidebar to simulate results.")

st.caption("Built by MIS 3213 Group 8 for the Chickasaw Nation Casino Strategy Competition 🧠")
