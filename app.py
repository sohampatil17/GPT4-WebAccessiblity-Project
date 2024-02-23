import streamlit as st
from main import scrape_website, generate_accessibility_report, generate_aria_score, implement_recommendations

def process_url():
    url = st.session_state['url']
    if url:
        with st.spinner("Scraping the website..."):
            html_content, css_files, js_files = scrape_website(url)
        
        with st.spinner("Generating Accessibility Report..."):
            accessibility_issues = generate_accessibility_report(html_content, css_files)
            
        with st.spinner("Calculating ARIA Compliance Score..."):
            aria_compliance_score = generate_aria_score(accessibility_issues)
            
        # Create two columns: One for Accessibility Report and one for Updated Code
        col1, col2 = st.columns(2)

        # Column 1: Accessibility Issues and Recommendations
        with col1:
            st.subheader("Accessibility Issues and Recommendations")
            st.write(accessibility_issues)
            st.subheader("ARIA Compliance Score")
            st.markdown(f"<h1 style='text-align: center; color: red;'>{aria_compliance_score}</h1>", unsafe_allow_html=True)

        # If the user clicks the button, update the code with recommendations
        if st.button("Implement Recommendations in Code"):
            with st.spinner("Updating code with recommendations..."):
                updated_code = implement_recommendations(html_content, css_files, accessibility_issues)

            # Column 2: Updated Code with Implemented Recommendations
            with col2:
                st.subheader("Updated Code")
                st.write(updated_code)


def main():
    
    
    st.set_page_config(layout="wide")
    
    st.markdown("<h1 style='text-align: center; font-size:50px;'> Web Accessibility Evaluator 💻🌐</h1>", unsafe_allow_html=True)
    
    # URL input with a key to reference in session_state
    url_input = st.text_input("Enter the URL of the website to scrape:", key='url')

    # Check if there's a URL and if so, process it
    if url_input:
        process_url()

if __name__ == "__main__":
    main()