import requests
import json
import time

def test_ollama():
    print("Testing Ollama connection...")
    try:
        # First, test if the server is running
        response = requests.get('http://localhost:11434/api/tags')
        print(f"Server status: {response.status_code}")
        
        # Now test the generate endpoint
        print("\nTesting story generation...")
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                "model": "llama2",
                "prompt": "Write a very short story about a cat.",
                "stream": False
            },
            timeout=30  # 30 second timeout
        )
        
        print(f"Response status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print("\nGenerated story:")
            print(result['response'])
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama. Make sure it's running.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out. The model might be taking too long to respond.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_ollama() 