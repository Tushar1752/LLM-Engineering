"""
04 - Output parsers: turn a reply into typed DATA, not prose.

A model returns text. But often you want a Python object you can use directly:
a rating you can compare, a list you can loop, fields you can store. Parsers do
that final "text -> data" step.

Two levels:
  * StrOutputParser  -> plain string 
  * with_structured_output(PydanticModel) -> a validated object with real fields.
    This is the modern, reliable way to get JSON out of a model.

Offline, we show a JSON parser working on a fixed string. The live part uses a
key to make the model actually fill the structure.
"""

from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
load_dotenv()
MODEL = "llama-3.1-8b-instant"
class MovieReview(BaseModel):
    title: str = Field(description="The movie title")
    sentiment: str = Field(description="One of: positive, negative, mixed")
    rating: int = Field(description="A score from 1 to 10")
    reasons: list[str] = Field(description="Short bullet reasons for the rating")
fake_model_output = (
    '{"title":"Inception",'
    '"sentiment":"positive",'
    '"rating":9,'
    '"reasons":["clever plot","great score"]}'
)
parser = JsonOutputParser()
parsed = parser.invoke(fake_model_output)
print("JsonOutputParser turned text into a real dict:")
print("Type:", type(parsed).__name__)
print("Rating + 1:", parsed["rating"] + 1, "(it is a real int we can do maths)")
print()
review_text = (
    "I finally watched Interstellar. "
    "The visuals and the score blew me away, "
    "though the middle dragged a bit. "
    "Still, easily one of the best sci-fi films I've seen."
)
if not os.getenv("GROQ_API_KEY"):
    print("No GROQ_API_KEY set - skipping the live structured call (this is fine).")
    print("With a key, this is the whole trick:")
    print("structured = ChatGroq(...).with_structured_output(MovieReview)")
    print("result = structured.invoke(review_text)  # -> a MovieReview object")
else:
    model = ChatGroq(
        model=MODEL,
        temperature=0
    )
    structured = model.with_structured_output(MovieReview)
    result = structured.invoke(
        f"Extract a structured review from:\n{review_text}"
    )
    print("Got back a", type(result).__name__, "object with real fields:")
    print("Title      :", result.title)
    print("Sentiment  :", result.sentiment)
    print("Rating     :", result.rating, "/10")
    print("Reasons:")
    for r in result.reasons:
        print("-", r)
print()
print("StrOutputParser -> a string for humans.")
print("with_structured_output(Model) -> a typed object for your code. Prefer it")
print('Whatever the next step is, "do something with the data", not "show text".')