import streamlit as st
from main import scrape_website, generate_accessibility_report, generate_aria_score, implement_recommendations

def process_url():
    url = st.session_state['url']
    if url:
        with st.spinner("Scraping the website..."):
            html_content, css_files, js_files = scrape_website(url)
        
        with st.spinner("Generating Accessibility Report..."):
            accessibility_issues = generate_accessibility_report(html_content, css_files)
            st.write("Accessibility Issues and Recommendations:", accessibility_issues)

        with st.spinner("Calculating ARIA Compliance Score..."):
            aria_compliance_score = generate_aria_score(accessibility_issues)
            st.write("ARIA Compliance Score (out of 10):", aria_compliance_score)

        # If the user clicks the button, then update the code with recommendations
        if st.button("Implement Recommendations in Code"):
            with st.spinner("Updating code with recommendations..."):
                updated_code = implement_recommendations(html_content, css_files, accessibility_issues)
                st.write("Updated Code with Implemented Recommendations:", updated_code)

def main():
    st.title("Web Accessibility Evaluator")
    
    # URL input with a key to reference in session_state
    url_input = st.text_input("Enter the URL of the website to scrape:", key='url')

    # Check if there's a URL and if so, process it
    if url_input:
        process_url()

if __name__ == "__main__":
    main()