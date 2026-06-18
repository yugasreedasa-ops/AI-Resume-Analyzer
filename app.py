import streamlit as st
import pdfplumber
st.set_page_config(page_title="AI Resume Analyzer")
st.title("📄 AI Resume Analyzer")
uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)
if uploaded_file:
    text = ""
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    st.subheader("Resume Preview")
    st.write(text[:1000])
    skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "html",
        "css",
        "javascript"
    ]
    found = []
    for skill in skills:
        if skill.lower() in text.lower():
            found.append(skill)
    st.subheader("Skills Found")
    if found:
        st.success(", ".join(found))
    else:
        st.error("No skills detected")
    st.metric(
        "Total Skills Found",
        len(found)
    )
    score = (len(found) / len(skills)) * 100
    st.subheader("Resume Score")
    st.progress(int(score))
    st.write(f"Score: {score:.0f}%")
    if score >= 70:
        st.success("✅ Strong Resume")
    elif score >= 40:
        st.warning("⚠️ Average Resume")
    else:
        st.error("❌ Needs Improvement")