import openai
import motionGPTv0_2
import api_key

# Set up your OpenAI API credentials
# This key will be deactivated on Github push, don't even try it
openai.api_key = api_key.api_key

v0_2prompt = motionGPTv0_2.create_prompt()

# Define your prompt
prompt = v0_2prompt
initial_message = [{"role": "user", "content": prompt}]

# Send the message to the API
def send_message(messages)
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
      #max_tokens=100,
      temperature=0.6,
    )

def print_response(response)
    print(response)

    # Extract the AI's response from the API response
    ai_response = response.choices[0].message.content

    print(ai_response)
    


