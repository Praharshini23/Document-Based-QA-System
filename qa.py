history = []
while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        break

    query_vec = vectorizer.transform([query])
    cosine_sim = np.dot(query_vec, X.T).toarray()[0]

    top_indices = cosine_sim.argsort()[-3:][::-1]

    print("\nTop Answers:")
    for idx in top_indices:
        score = cosine_sim[idx] * 100
        print(f"- {sentences[idx]}  (confidence: {score:.2f}%)")

    history.append((query, [sentences[idx] for idx in top_indices]))

with open("qa_history.txt", "w", encoding="utf-8") as f:
    for q, ans_list in history:
        f.write(f"Q: {q}\n")
        for ans in ans_list:
            f.write(f"A: {ans}\n")
        f.write("\n")
