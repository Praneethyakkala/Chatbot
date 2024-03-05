# import google.generativeai as palm
# palm.configure(api_key="AIzaSyA3f186uIsh6AaIFU8jfA_LHHbH44U5Pig")

# defaults = {
#   'model': 'models/text-bison-001',
#   'temperature': 0.7,
#   'candidate_count': 1,
#   'top_k': 40,
#   'top_p': 0.95,
#   'max_output_tokens': 1024,
#   'stop_sequences': [],
# }
# while True:
#   prompt = input("Question: ")
#   response = palm.generate_text(
#     **defaults,
#     prompt=prompt
#   )
#   print("Answer:", response.result)


import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("PALM_API_KEY")
palm.configure(api_key=API_KEY)

def main():
    # st.image("./Google_PaLM_Logo.svg.webp", use_column_width=False, width=100)
    st.header("Chat with PaLM")
    st.write("")

    prompt = st.text_input("Prompt please...", placeholder="Prompt", label_visibility="visible")

    if st.button("SEND", use_container_width=True):
        model = "models/text-bison-001"    # This is the only model currently available

        response = palm.generate_text(
            model=model,
            prompt=prompt,
            max_output_tokens=1024
        )

        st.write("")
        st.header(":blue[Response]")
        st.write("")

        st.markdown(response.result, unsafe_allow_html=False, help=None)

if __name__ == "__main__":
    main()

