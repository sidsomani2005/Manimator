import streamlit as st
from streamlit_theme import st_theme
from PIL import Image
import base64


# Load and display background or illustrative image
def set_background(image_path):
    image = Image.open(image_path)
    st.image(image, use_column_width=True)


LOGO = (
    "./frontend/assets/logo.png"
    if st_theme()["base"] != "dark"
    else "./frontend/assets/inverted-logo.png"
)

with open("./frontend/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

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
        font-size: 60px;
        font-weight: bold;
        margin-right: 40px;
    }
    .logo-img {
        float:right;
        width: 72px;
        height: 72px;
        margin-bottom: 26px;
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
    <img class="nav logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO, "rb").read()).decode()}">
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='navcontainer'></div>", unsafe_allow_html=True)


st.markdown(
    """
<style>.element-container:has(#button-after) + div a {
    position: fixed;
    top: 35px;
    left: 150px;
    outline: none !important;
    border: none !important;
    background: none !important;
    cursor: pointer;
    z-index: 2;
 }</style>""",
    unsafe_allow_html=True,
)
st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
st.link_button(
    "Home",
    "/",
)
st.markdown(
    """
<style>.element-container:has(#button-after2) + div a {
    position: fixed;
    top: 35px;
    left: 250px;
    outline: none !important;
    border: none !important;
    background: none !important;
    cursor: pointer;
    z-index: 2;
 }</style>""",
    unsafe_allow_html=True,
)
st.markdown('<span id="button-after2"></span>', unsafe_allow_html=True)
st.link_button(
    "Animate",
    "/Animate",
)


def Landing():
    # Set up background image or gradient
    # set_background("./frontend/assets/bg-cropped.png")  # Use your uploaded image here

    # Title and Welcome Section
    # st.markdown(
    #     "<h1 style='text-align: center; font-size: 64px; font-weight: bold;'>manimator</h1>",
    #     unsafe_allow_html=True,
    # )

    st.markdown(
        f"""
    <div class="header-container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO, "rb").read()).decode()}">
        <p class="logo-text">manimator</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h2 style='text-align: center; color: #aaa; margin-bottom: 10px'>automated animations for every idea.</h2>",
        unsafe_allow_html=True,
    )

    # Call-to-action Button
    st.markdown(
        "<div style='text-align: center; margin-top 20px;'>", unsafe_allow_html=True
    )

    st.link_button("Get Started", "/Animate")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        "<hr style='border: none; border-top: 1px solid #333; margin-bottom: 40px'/>",
        unsafe_allow_html=True,
    )

    # Features Section with Icons
    st.markdown(
        "<h2 style='font-weight: bold; margin-bottom: 10px' class='section-title'>Features</h2>",
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-box">
                <div class="feature-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-monitor"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></div>
                <div class="feature-title">User-Friendly Interface</div>
                <div class="feature-description">Instantly create animations with ease.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="feature-box">
                <div class="feature-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-film"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"></rect><line x1="7" y1="2" x2="7" y2="22"></line><line x1="17" y1="2" x2="17" y2="22"></line><line x1="2" y1="12" x2="22" y2="12"></line><line x1="2" y1="7" x2="7" y2="7"></line><line x1="2" y1="17" x2="7" y2="17"></line><line x1="17" y1="17" x2="22" y2="17"></line><line x1="17" y1="7" x2="22" y2="7"></line></svg></div>
                <div class="feature-title">High-Quality Output</div>
                <div class="feature-description">Professionally made animations.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="feature-box">
                <div class="feature-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-mic"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg></div>
                <div class="feature-title">Voiceover Integration</div>
                <div class="feature-description">Automatic voiceovers for your animations.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div class='vertical-spacer'></div>", unsafe_allow_html=True)

    # How It Works Section with Steps
    st.markdown(
        "<h2 style='font-weight: bold; margin-bottom: 10px' class='section-title'>How It Works</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <ol>
            <li><b>Enter Your Prompt:</b> Describe the concept you want to animate.</li>
            <li><b>Generate Animation:</b> Let Manimator create the animation for you.</li>
            <li><b>Download & Share:</b> Use your animation anywhere you like.</li>
        </ol>
        """,
        unsafe_allow_html=True,
    )

    # Testimonials or Social Proof Section

    # Footer
    st.markdown(
        "<hr style='border: none; border-top: 1px solid #333;'/>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center;'>2024 Manimator | AI ATL</p>",
        unsafe_allow_html=True,
    )


Landing()
