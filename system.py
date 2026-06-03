from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

sample_context = """
Artificial Intelligence is a branch of computer science that focuses
on creating intelligent machines capable of performing tasks that
typically require human intelligence. Machine Learning is a subset
of Artificial Intelligence. Deep Learning is a subset of Machine Learning.
"""

while True:

    question = input("\nEnter your question: ")

    result = qa_pipeline(
        question=question,
        context=context
    )

    print("\nAnswer:", result["answer"])
    print("Confidence:", round(result["score"], 4))

    choice = input("\nAsk another question? (y/n): ")

    if choice.lower() != "y":
        break
