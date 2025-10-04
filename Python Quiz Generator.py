import random

# Harder world affairs questions
questions = [
    {"question": "Who is the Secretary-General of the United Nations as of 2025?", "answer": "António Guterres"},
    {"question": "Which country left the European Union in 2020?", "answer": "United Kingdom"},
    {"question": "Which country is currently in a conflict over the Donbas region?", "answer": "Ukraine"},
    {"question": "What does NATO stand for?", "answer": "North Atlantic Treaty Organization"},
    {"question": "Which Asian country has ongoing tensions with Taiwan?", "answer": "China"},
    {"question": "Which African country had a military coup in 2023?", "answer": "Niger"},
    {"question": "Who is the President of the United States as of 2025?", "answer": "Joe Biden"},
    {"question": "Which country hosted the G20 summit in 2023?", "answer": "India"},
    {"question": "What is BRICS?", "answer": "An economic alliance"},
    {"question": "Which country has the largest oil reserves?", "answer": "Venezuela"}
]

# Shuffle questions for randomness
random.shuffle(questions)

# Quiz start
print("🌍 Welcome to the World Affairs Quiz!")
print("Answer the following questions about global politics, events, and organizations.")
print("----------------------------------------------------------\n")

score = 0

# Ask 5 questions only (or all if preferred)
for i in range(5):
    q = questions[i]
    print(f"Q{i+1}: {q['question']}")
    user_answer = input("Your answer: ")

    if user_answer.strip().lower() == q["answer"].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer is: {q['answer']}\n")

# Final message
print("🎓 Quiz complete!")
print(f"Your score: {score} out of 5")

# Rank performance
if score == 5:
    print("🏆 You're a global affairs genius!")
elif score >= 3:
    print("👍 Solid knowledge of world events!")
elif score == 2:
    print("🤔 Not bad, but room to improve.")
else:
    print("📘 Time to catch up on international news!")

print("\nThanks for playing!")
