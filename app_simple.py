from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import random
import os

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

def mock_detect_language(text):
    """Comprehensive Indian language detection"""
    # Kannada
    if any(char in text for char in ['ಕ', 'ಖ', 'ಗ', 'ಘ', 'ಙ', 'ಚ', 'ಛ', 'ಜ', 'ಝ', 'ಞ', 'ಟ', 'ಠ', 'ಡ', 'ಢ', 'ಣ', 'ತ', 'ಥ', 'ದ', 'ಧ', 'ನ', 'ಪ', 'ಫ', 'ಬ', 'ಭ', 'ಮ', 'ಯ', 'ರ', 'ಲ', 'ವ', 'ಶ', 'ಷ', 'ಸ', 'ಹ', 'ಳ', 'ೞ']):
        return "Kannada", 0.95
    
    # Telugu
    elif any(char in text for char in ['అ', 'ఆ', 'ఇ', 'ఈ', 'ఉ', 'ఊ', 'ఋ', 'ౠ', 'ఎ', 'ఏ', 'ఐ', 'ఒ', 'ఓ', 'ఔ', 'క', 'ఖ', 'గ', 'ఘ', 'ఙ', 'చ', 'ఛ', 'జ', 'ఝ', 'ఞ', 'ట', 'ఠ', 'డ', 'ఢ', 'ణ', 'త', 'థ', 'ద', 'ధ', 'న', 'ప', 'ఫ', 'బ', 'భ', 'మ', 'య', 'ర', 'ల', 'వ', 'శ', 'ష', 'స', 'హ', 'ళ', 'ఱ']):
        return "Telugu", 0.92
    
    # Tamil
    elif any(char in text for char in ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ', 'க', 'ங', 'ச', 'ஜ', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ன', 'ப', 'ம', 'ய', 'ர', 'ற', 'ல', 'ள', 'ழ', 'வ', 'ஷ', 'ஸ', 'ஹ']):
        return "Tamil", 0.89
    
    # Malayalam
    elif any(char in text for char in ['അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'ഋ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ', 'ക', 'ഖ', 'ഗ', 'ഘ', 'ങ', 'ച', 'ഛ', 'ജ', 'ഝ', 'ഞ', 'ട', 'ഠ', 'ഡ', 'ഢ', 'ണ', 'ത', 'ഥ', 'ദ', 'ധ', 'ന', 'പ', 'ഫ', 'ബ', 'ഭ', 'മ', 'യ', 'ര', 'ല', 'വ', 'ശ', 'ഷ', 'സ', 'ഹ', 'ള', 'ഴ', 'റ']):
        return "Malayalam", 0.87
    
    # Hindi/Devanagari
    elif any(char in text for char in ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ओ', 'औ', 'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह', 'ळ', 'क्ष', 'ज्ञ']):
        return "Hindi", 0.94
    
    # Bengali
    elif any(char in text for char in ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ', 'ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', 'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল', 'শ', 'ষ', 'স', 'হ', 'ড়', 'ঢ়', 'য়']):
        return "Bengali", 0.91
    
    # Gujarati
    elif any(char in text for char in ['અ', 'આ', 'ઇ', 'ઈ', 'ઉ', 'ઊ', 'ઋ', 'એ', 'ઐ', 'ઓ', 'ઔ', 'ક', 'ખ', 'ગ', 'ઘ', 'ઙ', 'ચ', 'છ', 'જ', 'ઝ', 'ઞ', 'ટ', 'ઠ', 'ડ', 'ઢ', 'ણ', 'ત', 'થ', 'દ', 'ધ', 'ન', 'પ', 'ફ', 'બ', 'ભ', 'મ', 'ય', 'ર', 'લ', 'વ', 'શ', 'ષ', 'સ', 'હ', 'ળ']):
        return "Gujarati", 0.88
    
    # Punjabi (Gurmukhi)
    elif any(char in text for char in ['ਅ', 'ਆ', 'ਇ', 'ਈ', 'ਉ', 'ਊ', 'ਏ', 'ਐ', 'ਓ', 'ਔ', 'ਕ', 'ਖ', 'ਗ', 'ਘ', 'ਙ', 'ਚ', 'ਛ', 'ਜ', 'ਝ', 'ਞ', 'ਟ', 'ਠ', 'ਡ', 'ਢ', 'ਣ', 'ਤ', 'ਥ', 'ਦ', 'ਧ', 'ਨ', 'ਪ', 'ਫ', 'ਬ', 'ਭ', 'ਮ', 'ਯ', 'ਰ', 'ਲ', 'ਵ', 'ਸ', 'ਹ', 'ੜ']):
        return "Punjabi", 0.86
    
    # Marathi (keywords)
    elif any(word in text for word in ['मराठी', 'महाराष्ट्र', 'पुणे', 'मुंबई']):
        return "Marathi", 0.93
    
    # Urdu
    elif any(char in text for char in ['ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ہ', 'ی', 'ے']):
        return "Urdu", 0.93
    
    # Assamese
    elif any(char in text for char in ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'এ', 'ঐ', 'ও', 'ঔ', 'ৰ', 'ল']):
        return "Assamese", 0.85
    
    # Odia
    elif any(char in text for char in ['ଅ', 'ଆ', 'ଇ', 'ଈ', 'ଉ', 'ଊ', 'ଋ', 'ଏ', 'ଐ', 'ଓ', 'ଔ', 'କ', 'ଖ', 'ଗ', 'ଘ', 'ଙ', 'ଚ', 'ଛ', 'ଜ', 'ଝ', 'ଞ', 'ଟ', 'ଠ', 'ଡ', 'ଢ', 'ଣ', 'ତ', 'ଥ', 'ଦ', 'ଧ', 'ନ', 'ପ', 'ଫ', 'ବ', 'ଭ', 'ମ', 'ଯ', 'ର', 'ଲ', 'ଶ', 'ଷ', 'ସ', 'ହ', 'ଡ଼', 'ଢ଼', 'ୟ', 'ୱ']):
        return "Odia", 0.84
    
    # English (keywords)
    elif text.lower() in ['hello', 'hi', 'goodbye', 'thanks', 'please', 'yes', 'no', 'okay', 'welcome']:
        return "English", 0.98
    
    # Unknown
    else:
        languages = ["English", "Hindi", "Kannada", "Telugu", "Tamil", "Malayalam", "Bengali", "Gujarati", "Punjabi", "Marathi", "Urdu", "Assamese", "Odia"]
        return random.choice(languages), random.uniform(0.7, 0.95)

@app.route("/")
def home():
    with open("index.html", "r") as f:   # make sure index.html is in project root
        return f.read()


@app.route('/api/detect', methods=['POST'])
def detect():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        lang_name, confidence = mock_detect_language(text)
        
        return jsonify({
            'text': text,
            'language': lang_name,
            'confidence': round(confidence, 4),
            'confidence_percentage': round(confidence * 100, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/samples', methods=['GET'])
def get_samples():
    samples = [
        {"text": "ನಮಸ್ಕಾರ", "language": "Kannada", "description": "Hello"},
        {"text": "నమస్కారం", "language": "Telugu", "description": "Hello"},
        {"text": "வணக்கம்", "language": "Tamil", "description": "Hello"},
        {"text": "നമസ്കാരം", "language": "Malayalam", "description": "Hello"},
        {"text": "नमस्ते", "language": "Hindi", "description": "Hello"},
        {"text": "নমস্কার", "language": "Bengali", "description": "Hello"},
        {"text": "નમસ્તે", "language": "Gujarati", "description": "Hello"},
        {"text": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ", "language": "Punjabi", "description": "Greeting"},
        {"text": "नमस्कार", "language": "Marathi", "description": "Hello"},
        {"text": "السلام علیکم", "language": "Urdu", "description": "Peace be upon you"},
        {"text": "নমস্কাৰ", "language": "Assamese", "description": "Hello"},
        {"text": "ନମସ୍କାର", "language": "Odia", "description": "Hello"},
        {"text": "hello", "language": "English", "description": "Greeting"},
        {"text": "धन्यवाद", "language": "Hindi", "description": "Thank you"}
    ]
    return jsonify(samples)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'mode': 'mock'})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Language Detection Tool Starting on port {port}...")
    app.run(host="0.0.0.0", port=port, debug=False)
