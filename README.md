# WebAlly: GPT-4 Web Accessibility Project

## Overview
WebAlly is an advanced web accessibility evaluation tool designed to enhance digital inclusivity. It leverages the power of GPT-4 AI to provide detailed insights into website accessibility, aiming to make the digital world more accommodating for users with disabilities.

## Key Functionalities

### Website Scraping
Upon receiving a URL input from the user, WebAlly extracts HTML and CSS content from the specified website. This initial step is crucial for a comprehensive accessibility evaluation.

### Accessibility Report Generation
WebAlly analyzes the site for potential accessibility issues using the scraped content. It utilizes GPT-4's advanced capabilities to interpret the site's elements, identifying areas that may impede accessibility.

### ARIA Compliance Scoring
The application calculates an ARIA (Accessible Rich Internet Applications) compliance score on a scale of 0 to 10. This metric provides a quantitative assessment of the website's adherence to key accessibility standards.

### Recommendations for Improvement
WebAlly identifies accessibility issues and offers specific, actionable recommendations for improvement. These suggestions aim to enhance various aspects of web accessibility, such as navigational ease, readability, and overall compliance.

### Updated Code Generation
In addition to providing recommendations, WebAlly generates updated code that implements these suggestions. This feature aids developers in quickly making their websites more accessible.

## TruLens Integration
WebAlly integrates TruLens' text-to-text application for logging and feedback purposes. This integration allows us to continuously improve our LLM-based application by analyzing the feedback and refining our algorithms.

## Getting Started

streamlit run app.py 
truelens-eval

---

For more information, please reach out to me at sohamppatil7@gmail.com

