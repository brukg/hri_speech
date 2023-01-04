

def text2task(text):
    """
    Convert text to task
    """

    if "go to bedroom"  in text or "go to the bedroom" in text  or text == "go to bed room" or text == "go to the bed room":
        return "bedroom"
    elif text == "go to bathroom" or text == "go to the bathroom" or text == "go to bath room" or text == "go to the bath room":
        return "bathroom"

    elif text == "go to living room" or text == "go to the living room" or text == "go to livingroom" or text == "go to the livingroom":
        return "living room"
    elif "go to kitchen" in text or "go to the kitchen" in text or "go to the kitchen" in  text  or "go to the kitchen" in text:
        return "kitchen"