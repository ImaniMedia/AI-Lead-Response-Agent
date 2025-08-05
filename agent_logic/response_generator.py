
# response_generator.py
# This generates a personalized response based on detected intent.

def generate_response(name, intent):
    responses = {
        'Booking Inquiry': f"Hi {name}, thank you for reaching out! We can help you schedule a booking immediately.",
        'Pricing Inquiry': f"Hi {name}, we offer competitive prices. Let me send you our price list.",
        'General Inquiry': f"Hi {name}, thank you for your message! How can we assist you today?"
    }
    return responses.get(intent, responses['General Inquiry'])

if __name__ == "__main__":
    name = "Jane"
    intent = "Booking Inquiry"
    print(generate_response(name, intent))
