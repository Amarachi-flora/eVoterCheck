import streamlit as st

# --------------------------
# PAGE CONFIGURATION
# --------------------------
st.set_page_config(
    page_title="eVoterCheck - Nigeria",
    page_icon="nigeria_flag_64.png"
)

# --------------------------
# CUSTOM BACKGROUND: Green-White-Green Stripes
# --------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #008751 33.3%, #ffffff 33.3%, #ffffff 66.6%, #008751 66.6%);
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------
# SIDEBAR INFO
# --------------------------
st.sidebar.title("About eVoterCheck 🇳🇬")
st.sidebar.markdown("""
**Created by:** Amarachi Florence  
**Learner @ 3MTT DeepTech Ready Program**  
**ALC:** Quantum Business School, Port Harcourt  
---  

**eVoterCheck** is a civic-tech web app that helps Nigerians check if they are eligible to vote.  

Built with **Python**, **Object-Oriented Programming**, and **Streamlit**.
""")

# --------------------------
# OOP CLASSES
# --------------------------
class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Name: {self.name} | Age: {self.age}"

class Voter(Person):
    def __init__(self, name, age, lga, nin, has_voter_card, is_citizen, willing_to_vote):
        super().__init__(name, age)
        self.lga = lga
        self.nin = nin
        self.has_voter_card = has_voter_card
        self.is_citizen = is_citizen
        self.willing_to_vote = willing_to_vote

    def introduce(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"LGA: {self.lga}\n"
            f"NIN: {self.nin}"
        )

    def check_eligibility(self):
        if self.age < 18:
            return "Not eligible: You must be at least 18 years old to vote."
        if not self.is_citizen:
            return "Not eligible: Only Nigerian citizens can vote."
        if not self.has_voter_card:
            return "Not eligible: A valid voter's card is required to vote."
        if not self.willing_to_vote:
            return "You're eligible, but you've indicated you're not willing to vote."
        return "You are eligible and ready to vote. Let your voice be heard."

# --------------------------
# MAIN APP UI
# --------------------------

# Welcome Banner
st.title("🇳🇬 Welcome to eVoterCheck")
st.markdown("""
### Powered by the *Independent National Electoral Commission (INEC)* simulation

**Check if you can vote in the upcoming elections.**  
This tool helps you verify your eligibility in less than a minute.  
""")

# Form Section
st.header("Voter Eligibility Check")
st.write("Please fill in your details below:")

with st.form("voter_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    lga = st.text_input("Local Government Area (LGA)")
    nin = st.text_input("National Identification Number (NIN)")

    has_voter_card = st.radio("Do you have a Voter's Card?", ["Yes", "No"]) == "Yes"
    is_citizen = st.radio("Are you a Nigerian Citizen?", ["Yes", "No"]) == "Yes"
    willing_to_vote = st.radio("Are you willing to vote?", ["Yes", "No"]) == "Yes"

    submitted = st.form_submit_button("Check My Eligibility")

# Result Section
if submitted:
    voter = Voter(name, age, lga, nin, has_voter_card, is_citizen, willing_to_vote)

    st.success("Form Submitted Successfully")

    st.subheader("Voter Summary")
    st.markdown(f"```{voter.introduce()}```")

    st.subheader("Eligibility Result")
    result = voter.check_eligibility()
    st.info(result)
