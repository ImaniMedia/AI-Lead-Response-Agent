
# intent_detection.py
# This is a placeholder script to simulate AI intent detection.

def detect_intent(inquiry_text):
    if 'book' in inquiry_text.lower():
        return 'Booking Inquiry'
    elif 'price' in inquiry_text.lower():
        return 'Pricing Inquiry'
    else:
        return 'General Inquiry'

if __name__ == "__main__":
    sample_text = "I would like to book an appointment"
    print(detect_intent(sample_text))
