import streamlit as st
import random

def show():
    st.header("Login / Sign Up")

    phone = st.text_input("Enter phone number", placeholder="+91XXXXXXXXXX")

    if st.button("Send OTP"):
        if phone.strip() == "":
            st.warning("Please enter a phone number.")
            return

        otp = str(random.randint(1000, 9999))
        st.session_state["mock_otp"] = otp

        st.success("OTP sent! (Mock for Phase 1)")
        st.info(f"Mock OTP for testing: {otp}")

    entered = st.text_input("Enter OTP")

    if st.button("Verify OTP"):
        if "mock_otp" in st.session_state and entered == st.session_state["mock_otp"]:
            st.session_state["user_phone"] = phone
            st.success("OTP Verified! Logged in.")
        else:
            st.error("Incorrect OTP")

    if st.session_state.get("user_phone"):
        st.write(f"📱 Logged in as: **{st.session_state['user_phone']}**")
