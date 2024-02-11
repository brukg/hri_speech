import json
import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
# path = rospkg.RosPack().get_path('hri_speech') + "scripts/"
openai.api_key = os.getenv("OPENAI_API_KEY")


def text2task(text):
    """
    Convert text to task
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Convert this text to a programmatic command in JSON format with keys action  and location if the text is a movement action otherwise convert into JSON with the  key answer that contains the proper response to the text if the text is incomplete ask again don't autocomplete prompt sentence only JSON output: "+text,
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0
    )
    print(response.choices[0])
    data = json.loads(response.choices[0].text)
    print(data)
    if data.get("action") is not None and data.get("location") is not None and not "none" in (data["action"]).lower():
        print("action: "+data["action"])
        if "go"  in data["action"]:# if data["action"] else "unknown"):
            if "bed" in data["location"]:
                return "go", "bedroom"
            elif "bath" in data["location"]:
                return "go", "bathroom"
            elif "living" in data["location"]:
                return "go", "living room"
            elif "kitchen" in data["location"]:
                return "go", "kitchen"
            else:
                return "go",  data["location"]
        elif "stop" in data["action"]:
            return "stop", "none"
        else:
            return "unknown", "unknown"
    else:
        print("answer: "+ data["answer"] if data.get("answer") is not None else "unknown")
        return "answer", data["answer"] if data.get("answer") is not None else "unknown"