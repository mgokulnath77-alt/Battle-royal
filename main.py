import streamlit as st
import random
import math
import time

st.set_page_config(page_title="Battle Royale", layout="wide")

# --- GAME STATE ---
if "players" not in st.session_state:
    st.session_state.players = 20
    st.session_state.zone_radius = 100
    st.session_state.health = 100
    st.session_state.bots = [
        {"x": random.randint(-50, 50), "y": random.randint(-50, 50), "alive": True}
        for _ in range(19)
    ]

st.title("🪖 Web Battle Royale (Prototype)")
st.write("Drop → Loot → Fight → Survive → Win")

# --- ZONE LOGIC ---
def in_zone(x, y, r):
    return math.sqrt(x*x + y*y) < r

st.session_state.zone_radius -= 0.2

if st.session_state.zone_radius < 20:
    st.session_state.zone_radius = 20

# --- PLAYER ---
player_x, player_y = 0, 0

if not in_zone(player_x, player_y, st.session_state.zone_radius):
    st.session_state.health -= 0.5

# --- BOTS ---
for bot in st.session_state.bots:
    if not bot["alive"]:
        continue

    bot["x"] += (player_x - bot["x"]) * 0.01
    bot["y"] += (player_y - bot["y"]) * 0.01

    if not in_zone(bot["x"], bot["y"], st.session_state.zone_radius):
        if random.random() < 0.05:
            bot["alive"] = False

alive_bots = sum(bot["alive"] for bot in st.session_state.bots)

# --- UI ---
col1, col2, col3 = st.columns(3)

col1.metric("❤️ Health", int(st.session_state.health))
col2.metric("🧍 Players Left", alive_bots + 1)
col3.metric("🟦 Zone Radius", int(st.session_state.zone_radius))

# --- END GAME ---
if st.session_state.health <= 0:
    st.error("💀 You Died!")
    st.stop()

if alive_bots == 0:
    st.success("🏆 Winner Winner Chicken Dinner!")
    st.stop()

time.sleep(0.3)
st.rerun()


