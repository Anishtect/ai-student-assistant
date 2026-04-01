import streamlit as st
import random
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎓 AI Student Assistant 🤖</h1>", unsafe_allow_html=True)
st.markdown("### 📚 Learn Faster | Smarter | Better")

st.set_page_config(page_title="AI Student Assistant", layout="centered")

st.title("🎓 AI Student Assistant 🤖")
st.write("Smart tool for answers, summaries & MCQs")

context = st.text_area("📘 Enter Study Material:")
question = st.text_input("❓ Ask your question:")

# Answer logic
if st.button("Get Answer"):
    if context and question:
        if "what" in question.lower() or "define" in question.lower():
            answer = context.split('.')[0]
        elif "why" in question.lower():
            answer = "This happens because " + context.split('.')[0]
        else:
            answer = context[:150]
        st.success("Answer: " + answer)

# Summary logic
if st.button("Generate Summary"):
    if context:
        sentences = context.split('.')
        summary = '.'.join(sentences[:2])
        st.info("Summary: " + summary)

# MCQ Generator
if st.button("Generate MCQ"):
    if context:
        sentences = context.split('.')
        st.write("### 📝 MCQs")

        for i in range(1, 4):
            sentence = random.choice(sentences).strip()

            words = sentence.split()
            if len(words) < 5:
                continue

            keyword = random.choice(words)

            # blank question
            question = sentence.replace(keyword, "___")

            st.write(f"Q{i}: {question}?")

            # options
            options = [keyword, "Technology", "Science", "Data"]
            random.shuffle(options)

            for opt in options:
                st.write(f"- {opt}")

            st.success(f"Correct Answer: {keyword}")
            st.write("---")