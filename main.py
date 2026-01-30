import streamlit as st
import random
import math
import time

st.set_page_config(
    page_title="Web Battle Royale (Prototype)",
    layout="wide"
)

# ---------------- INITIAL STATE ----------------
if "init" not in st.session_state:
    st.session_state.init = True
    st.session_state.health = 100
    st.session_state.zone_radius = 100
    st.session_state.player_x = 0
    st.session_state.player_y = 0

    # 19 bots + player = 20
    st.session_state.bots = [
        {
            "x": random.randint(-80, 80),
            "y": random.randint(-80, 80),
            "alive": True
        }
        for _ in range(19)
    ]

# ---------------- FUNCTIONS ----------------
def in_zone(x, y, r):
    return math.sqrt(x*x + y*y) <= r

# ---------------- TITLE ----------------
st.title("🪖 Web Battle Royale (Prototype)")
st.caption("Drop → Loot → Fight → Survive → Win")

# ---------------- GAME LOGIC ----------------
# Shrink zone
st.session_state.zone_radius -= 0.5
if st.session_state.zone_radius < 25:
    st.session_state.zone_radius = 25

# Zone damage to player
if not in_zone(
    st.session_state.player_x,
    st.session_state.player_y,
    st.session_state.zone_radius
):
    st.session_state.health -= 2

# Bots update
for bot in st.session_state.bots:
    if not bot["alive"]:
        continue

    # Move bots toward player
    bot["x"] += (st.session_state.player_x - bot["x"]) * 0.05
    bot["y"] += (st.session_state.player_y - bot["y"]) * 0.05

    # Zone damage to bots
    if not in_zone(bot["x"], bot["y"], st.session_state.zone_radius):
        if random.random() < 0.2:
            bot["alive"] = False

alive_bots = sum(bot["alive"] for bot in st.session_state.bots)

# ---------------- HUD ----------------
col1, col2, col3 = st.columns(3)

col1.metric("❤️ Health", max(0, int(st.session_state.health)))
col2.metric("🧍 Players Left", alive_bots + 1)
col3.metric("🟦 Zone Radius", int(st.session_state.zone_radius))

# ---------------- MAP DISPLAY ----------------
st.subheader("🗺️ Map (Text View)")
st.write(f"Player Position: ({st.session_state.player_x}, {st.session_state.player_y})")
st.write("Alive Enemies:")

for i, bot in enumerate(st.session_state.bots):
    if bot["alive"]:
        st.write(f"Enemy {i+1}: ({int(bot['x'])}, {int(bot['y'])})")

# ---------------- CONTROLS ----------------
st.subheader("🎮 Controls")

c1, c2, c3 = st.columns(3)
with c2:
    if st.button("⬆️ Move Forward"):
        st.session_state.player_y += 5

c4, c5, c6 = st.columns(3)
with c4:
    if st.button("⬅️ Left"):
        st.session_state.player_x -= 5
with c6:
    if st.button("➡️ Right"):
        st.session_state.player_x += 5
with c5:
    if st.button("⬇️ Back"):
        st.session_state.player_y -= 5

# ---------------- COMBAT ----------------
st.subheader("⚔️ Combat")

if st.button("🔫 Shoot Nearest Enemy"):
    for bot in st.session_state.bots:
        if bot["alive"]:
            bot["alive"] = False
            st.success("💥 Enemy eliminated!")
            break
    else:
        st.warning("No enemies left!")

# ---------------- END CONDITIONS ----------------
if st.session_state.health <= 0:
    st.error("💀 You Died! Game Over.")
    if st.button("🔁 Restart"):
        st.session_state.clear()
        st.rerun()
    st.stop()

if alive_bots == 0:
    st.success("🏆 Winner Winner Chicken Dinner!")
    if st.button("🔁 Play Again"):
        st.session_state.clear()
        st.rerun()
    st.stop()

# ---------------- LOOP ----------------
time.sleep(0.4)
st.rerun()
