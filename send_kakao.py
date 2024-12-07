import requests
import json

# 토큰 로드 함수
def load_tokens():
    """
    JSON 파일에서 Access Token 및 Refresh Token을 로드합니다.
    """
    try:
        with open("kakao_tokens.json", "r") as token_file:
            return json.load(token_file)
    except FileNotFoundError:
        print("Error: kakao_tokens.json 파일이 없습니다. 새로 발급받으세요.")
        return None

# Access Token 갱신 함수
def refresh_access_token(refresh_token):
    """
    Refresh Token을 사용해 새로운 Access Token을 갱신합니다.
    """
    url = "https://kauth.kakao.com/oauth/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": "2c4b22a97f375523908cdf4d57fe147e",  # REST API 키
        "refresh_token": refresh_token
    }

    response = requests.post(url, data=data)
    tokens = response.json()

    if "access_token" in tokens:
        print("Access Token 갱신 완료:", tokens["access_token"])

        # 갱신된 토큰 저장
        with open("kakao_tokens.json", "w") as token_file:
            json.dump(tokens, token_file, indent=4, ensure_ascii=False)
            print("Tokens saved to kakao_tokens.json")

        return tokens["access_token"]
    else:
        print("Failed to refresh Access Token:", tokens)
        return None

# 메시지 전송 함수
def send_kakao_message(access_token, message):
    """
    Access Token을 사용해 카카오톡 '나와의 채팅'으로 메시지를 전송합니다.
    """
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": message,
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            }
        })
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 401:  # Unauthorized
        print("Access Token 만료. 갱신 중...")
        tokens = load_tokens()
        if tokens and "refresh_token" in tokens:
            new_access_token = refresh_access_token(tokens["refresh_token"])
            if new_access_token:
                send_kakao_message(new_access_token, message)  # 갱신된 토큰으로 재전송
    elif response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message:", response.json())

# 실행
if __name__ == "__main__":
    # 메시지 내용
    message = "출석 현황\nBABY KANGHYERIM: 02:59:36\nKANGHYERIM: 02:59:37\nELON MUSK: 03:03:39"

    # 토큰 로드
    tokens = load_tokens()
    if tokens:
        access_token = tokens["access_token"]
        send_kakao_message(access_token, message)
