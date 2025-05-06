import requests

def test_ollama():
    try:
        response = requests.post('http://localhost:11434/api/generate',
                               json={
                                   "model": "llama2",
                                   "prompt": "Say hello",
                                   "stream": False
                               })
        print("Status Code:", response.status_code)
        print("Response:", response.json())
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    test_ollama() 