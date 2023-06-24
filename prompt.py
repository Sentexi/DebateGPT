import openai
import motionGPTv0_2
import api_key
import pprint

# Set up your OpenAI API credentials
# This key will be deactivated on Github push, don't even try it
openai.api_key = api_key.api_key

v0_2prompt = motionGPTv0_2.create_prompt()

# Define your prompt
prompt = v0_2prompt
initial_message = [{"role": "user", "content": prompt}]

# Send the message to the API
def send_message(messages):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
      #max_tokens=100,
      temperature=0.6,
    )
    return response

def print_response(response):
    # Extract the AI's response from the API response
    ai_response = response.choices[0].message.content
    return response.choices[0].message
    
def update_conversation(current_message,ai_response,new_prompt):
    # Convert the JSON response to a dictionary
    ai_response_dict = ai_response.to_dict()
    
    current_message.append(ai_response_dict)
    current_message.append({"role": "user", "content": new_prompt})
    
    refined_message = current_message
    return refined_message
    
def create_motion():
    #initial the creation of motions based on the initial prompt    
    initial_response = send_message(initial_message)
    #evaluate the response
    ai_response = print_response(initial_response)

    #a sort of cheapish attempt to choose the best motion available at the time
    new_prompt = 'Now choose the best motion from these five and print it'
    refined_message = update_conversation(initial_message,ai_response,new_prompt)

    current_response = send_message(refined_message)
    ai_response = print_response(current_response)
    
    #At the end we have the newly crafted motion
    motion = ai_response.content
    
    return motion