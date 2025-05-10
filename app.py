import streamlit as st
import cohere

# 💥 Put your actual Cohere API key here (keep it safe in prod)
COHERE_API_KEY = "vzSUUNFPnI6IBHil4qwn0rQxVDegkZaHL9cZNNiR"
# Initialize Cohere Client
co = cohere.Client(COHERE_API_KEY)

# Streamlit UI Setup
st.set_page_config(page_title="Generate Blogs 🤖",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input('No of Words', value="150")
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'),
                              index=0)

submit = st.button("Generate")

# Cohere prompt function
def generate_blog_with_cohere(topic, word_limit, style):
    prompt = f"""
    You are a professional blog writer. Write a blog for the job profile of a {style}.
    The topic is: "{topic}"
    The blog should be engaging, informative, and within {word_limit} words.
    """
    
    # Make sure prompt is long enough for Cohere
    if len(prompt) < 250:
        prompt += " Add more details, context, and background to ensure full understanding."

    response = co.generate(
        model='command',  # or 'command-nightly' if you're spicy 🌶️
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )
    return response.generations[0].text.strip()

# Final Output
if submit:
    blog_response = generate_blog_with_cohere(input_text, no_words, blog_style)
    st.subheader("📝 Generated Blog:")
    st.write(blog_response)