import os
import django
import sys
import json

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from web_app.services.analysis_service import analyze_text

def run_tests():
    test_cases = [
        {
            "name": "Banking Scam (Financial Fraud)",
            "text": "We have leaked bank credentials and verified balance available for transfer partner.",
            "expected_category": "Financial Fraud"
        },
        {
            "name": "Login Credential Theft (Phishing)",
            "text": "Your account suspended. Visit the fake login portal to verify account and reset password.",
            "expected_category": "Phishing"
        },
        {
            "name": "Hidden Encrypted Coordination (Suspicious Comm)",
            "text": "Trusted buyer, we need a silent delivery through the encrypted channel tonight.",
            "expected_category": "Suspicious Communication"
        },
        {
            "name": "Anonymous Selling (Dark Web Marketplace)",
            "text": "Verified seller has a product listing on the darknet market with anonymous payment via escrow.",
            "expected_category": "Dark Web Marketplace"
        },
        {
            "name": "Mixed-Language Suspicious Text (Multilingual Threat)",
            "text": "We need a secure paquete delivery. Transferencia tonight via the encrypted canal for the comprador.",
            "expected_category": "Suspicious Communication"
        },
        {
            "name": "Encoded Slang Communication (Hidden Slang)",
            "text": "Need fresh onions and keys tonight. The tickets are ready.",
            "expected_category": "Illegal Trade" # or Financial Fraud for tickets
        }
    ]

    print("=== RUNNING THREAT DETECTION TESTS ===\n")
    for idx, tc in enumerate(test_cases, 1):
        print(f"Test {idx}: {tc['name']}")
        print(f"Input: {tc['text']}")
        
        result = analyze_text(tc["text"])
        
        print(f"Detected Category : {result['intent']}")
        print(f"Threat Level      : {result['threat_level']} (Score: {result['confidence_score']})")
        if result.get('slang_matches'):
            print(f"Slang Matches     : {result['slang_matches']}")
        if result.get('multilingual_flags'):
            print(f"Multilingual Flags: {result['multilingual_flags']}")
        print(f"AI Summary        : {result['summary']}")
        print("-" * 50)

if __name__ == "__main__":
    run_tests()
