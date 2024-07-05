from openai import OpenAI, RateLimitError

# pip install openai
# client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="sk-proj-dFzF1iVQagIsPs7kxko0T3BlbkFJFH8bs3nbqq1sWKs8PPJh",
#   api_key="sk-proj-ueXigqrXp8cZhAodCKbBT3BlbkFJ4T49fSBtZUbTHiCNULIK", #ik
#   api_key="sk-proj-3ktlWQbkG5og9syjYHRAT3BlbkFJfacjQ5OA74xeaQPqrMpe", nl
) 

try:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis, skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is programming"}
    ]
    )

    # print(completion.choices[0].message.content)
    if completion.choices:
        print(completion.choices[0].message["content"])
    else:
        print("No response from the model.")

except RateLimitError as e:
    print(f"Rate limit exceeded: {e}")
    # Handle rate limit error, e.g., wait and retry after some time

except Exception as e:
    print(f"An error occurred: {e}")
    # Handle other exceptions here
