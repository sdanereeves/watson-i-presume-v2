# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# URL of the hosted LLMs is hardcoded because at this time all LLMs share the same endpoint
url = "https://us-south.ml.cloud.ibm.com"


import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def main():
    st.set_page_config(
        layout="wide",
        page_title="Dr. Watson Web",
        page_icon="👋",
    )
    # sdr additional code
    jpeg_image_path = "watsonx.jpg"
    image_width = 250
    st.image(jpeg_image_path, width=image_width)
    # Streamlit app title
    # This is the original code
    st.title("Dr. Watson RAG with a Web page")

    #st.markdown('<font color="blue"><b><i>Enter your prompt!</i></b></font>', unsafe_allow_html=True)
    watsonx_project_id=st.text_input("Enter a Project ID:", type="password")
    api_key = st.text_input("Enter your API Key:", type="password")

    user_url = st.text_input('Provide a URL')
    collection_name = st.text_input('Provide a lower case collection name.')

    # UI component to enter the question
    question = st.text_area('Question',height=100)
    button_clicked = st.button("Answer the question")
    st.subheader("Response")

  # Invoke the LLM when the button is clicked
    if button_clicked:
        #response = use_case_RAG_Web.answer_questions_from_web(api_key,watsonx_project_id,user_url,question,collection_name)
        #print("Response from the LLM:" + response)
        #st.write(response)
        st.write( watsonx_project_id, api_key, user_url, collection_name)



if __name__ == "__main__":
    main()
