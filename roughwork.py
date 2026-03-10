from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import json

load_dotenv()

# class Movie(BaseModel):
#     hero: str
#     director: str
#     actress: str
#     release_date: str
#     gross_collections: str  # keep as string

# groq_api_key = os.getenv("GROQ_API_KEY")

# llm = ChatGroq(
#     groq_api_key=groq_api_key,
#     model_name="meta-llama/llama-4-scout-17b-16e-instruct"
# )

# parser = JsonOutputParser(pydantic_object=Movie)

# prompt = PromptTemplate(
#     template="""
#     Give the details of the movie Bahubali.

#     {format_instructions}
#     """,
#     input_variables=[],
#     partial_variables={"format_instructions": parser.get_format_instructions()}
# )

# chain = prompt | llm | parser



# response = chain.invoke({})

# print(parser.get_format_instructions())

# print(type(response))

# # JSON output
# print(json.dumps(response, indent=2))

# # Optional: convert to Pydantic object
# movie_obj = Movie.model_validate(response)
# print(movie_obj.hero)
# print(type(movie_obj))
# print(type(movie_obj.hero))



