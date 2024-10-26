import streamlit as st
from streamlit_theme import st_theme
import base64, sys, asyncio
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent / "backend"))
generate = __import__("generate")
LOGO = (
    "./frontend/assets/logo.png"
    if st_theme()["base"] != "dark"
    else "./frontend/assets/inverted-logo.png"
)

st.markdown(
    """
    <style>
    .header-container {
        display: flex;
        width: 100%;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }
    .logo-text {
        font-size: 40px;
        font-weight: bold;
    }
    .logo-img {
        float:right;
        width: 50px;
        height: 50px;
        margin-bottom: 22px;
    }
    .empty-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 180px;
    }
    .empty-text {
        font-size: 24px;
        font-weight: bold;
        opacity: 0.2;
    }
    .stForm {
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="header-container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO, "rb").read()).decode()}">
        <p class="logo-text">manimator</p>
    </div>
    """,
    unsafe_allow_html=True,
)


async def call_generate(prompt):
    output = await generate.generate(prompt)
    videoPath = await generate.generate_video()
    code, transcript = output
    return (code, transcript, videoPath)


with st.form("chat_input_form"):
    inputCol, buttonCol = st.columns([6, 1], vertical_alignment="bottom")

    with inputCol:
        prompt = st.text_input(
            "",
            value="",
            placeholder="Visually explain of how matrix transformations work",
            label_visibility="collapsed",
        )
    with buttonCol:
        submitted = st.form_submit_button("Generate")

    if prompt and submitted:

        with st.spinner("Generating animation..."):
            output = asyncio.run(call_generate(prompt))
            code, transcript, videoPath = output

        st.video(
            data=videoPath,
            format="video/mp4",
            autoplay=True,
        )
        (
            transcriptTab,
            codeTab,
        ) = st.tabs(["Transcript", "Source Code"])

        with transcriptTab:
            st.write("### Transcript")
            st.markdown(f"```\n{transcript}\n```")

        with codeTab:
            st.write("### Source Code")
            st.markdown(f"```python\n{code}\n```")

    else:
        emptyContainer = st.container(border=1, height=200)
        emptyContainer.markdown(
            f"""
            <div class="empty-container">
                <p class="empty-text">Enter a prompt to generate an animation!</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
