import requests
from openai import OpenAI
from bs4 import BeautifulSoup

client = OpenAI(api_key='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') 

def scrape_website(url):
    # Fetch the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all linked CSS files
    css_links = soup.find_all("link", {"rel": "stylesheet"})
    js_scripts = soup.find_all("script")

    css_contents = {}
    js_contents = {}

    for link in css_links:
        href = link.get('href')
        if href and href.startswith('http'):
            css_url = href
        elif href:
            css_url = url + href
        else:
            continue

        # Fetch CSS content
        css_response = requests.get(css_url)
        css_contents[css_url] = css_response.text

    for script in js_scripts:
        src = script.get('src')
        if src and src.startswith('http'):
            js_url = src
        elif src:
            js_url = url + src
        else:
            continue

        # Fetch JS content
        js_response = requests.get(js_url)
        js_contents[js_url] = js_response.text

    return html_content, css_contents, js_contents

def generate_accessibility_report(html_content, css_files, js_files):
    # Combine CSS and JS content into single strings
    css_content = '\n\n'.join(css_files.values())
    js_content = '\n\n'.join(js_files.values())

    # Construct the prompt for issues and recommendations
    prompt_issues = f"""
    Analyze the following web page for accessibility issues (visual navigation, ease, readability)
    HTML Code:
    {html_content}

    CSS Code:
    {css_content}

    List any accessibility issues found in the code and provide between 4 to 7 specific recommendations to fix these issues.
    """

    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt_issues}],
        stream=True,
    )

    # Iterate through the stream and print the response
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


def generate_aria_score(issues):
    # Construct the prompt for ARIA compliance score
    prompt_score = f"""
    Given the following identified accessibility issues in the web page, evaluate its ARIA (Accessible Rich Internet Applications) compliance and provide a score on a scale of 0 to 10.

    Identified Accessibility Issues:
    {issues}
    
    Provide an ARIA compliance score for the webpage based on these issues identified (return only the decimal).
    """

    # Sending the prompt to get the ARIA score
    stream_score = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[{"role": "user", "content": prompt_score}],
        stream=True,
    )

    # Iterate through the stream and capture the ARIA score
    aria_score = ""
    for chunk in stream_score:
        if chunk.choices[0].delta.content is not None:
            aria_score += chunk.choices[0].delta.content

    return aria_score



# Let the user input the URL
url = input("Enter the URL of the website to scrape: ")
html_content, css_files, js_files = scrape_website(url)

# Generate the accessibility report
print("Generating Accessibility Report...")
accessibility_issues = generate_accessibility_report(html_content, css_files, js_files)
print("Accessibility Issues and Recommendations:\n", accessibility_issues)

# Generate the ARIA compliance score
print("\nCalculating ARIA Compliance Score...")
aria_compliance_score = generate_aria_score(accessibility_issues)
print("ARIA Compliance Score (out of 10):\n", aria_compliance_score)
