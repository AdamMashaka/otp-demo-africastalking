import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Afri Auth SMS Demo")

tab1, tab2 = st.tabs(
    [
        "Register",
        "Verify OTP"
    ]
)

with tab1:

    phone = st.text_input(
        "Phone Number",
        placeholder="+2557XXXXXXXX"
    )

    if st.button("Send OTP"):

        response = requests.post(
            f"{API_URL}/register",
            json={
                "phone": phone
            }
        )

        st.json(response.json())

with tab2:

    verify_phone = st.text_input(
        "Phone",
        key="verify_phone"
    )

    otp_code = st.text_input(
        "OTP Code"
    )

    if st.button("Verify"):

        response = requests.post(
            f"{API_URL}/verify",
            json={
                "phone": verify_phone,
                "code": otp_code
            }
        )

        st.write("Status Code:", response.status_code)
        st.write("Response Text:")
        st.code(response.text)