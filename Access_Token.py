import requests
import json

url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "authorization_code",
    "client_id": "1964cb99de158dcb5c6a86775a395cd5",  # REST API 키
    "redirect_uri": "http://localhost",               # Redirect URI
    "code": "44jiTeiw9TOjGoyey4PdfRVGEYqQ4LSG0SLcQTRK231eaJt2SwstuwAAAAQKPXQRAAABk6P9AVH7Ewsnpgvovw"  # 새로운 인가 코드
}

response = requests.post(url, data=data)
tokens = response.json()

if "access_token" in tokens:
    print("Access Token:", tokens["access_token"])
    print("Refresh Token:", tokens["refresh_token"])
    print("Expires In:", tokens["expires_in"], "seconds")

    # Access Token 저장
    with open("kakao_tokens.json", "w") as token_file:
        json.dump(tokens, token_file, indent=4, ensure_ascii=False)
        print("Tokens saved to kakao_tokens.json")
else:
    print("Failed to get Access Token:", tokens)
