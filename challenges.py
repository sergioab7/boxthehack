from htbapi.core import getRequest, rawPostSSL

class challenges:
    def ownChallenge(challengeid: int, apitoken: str, flag: str, difficulty: int) -> str:
        response =  rawPostSSL("/challenges/own/", f'challenge_id={challengeid}&flag={flag}&difficulty={difficulty * 10}', apitoken, "x-www-form-urlencoded", "")
        if '"success":"1"'.encode() in response:
            return "success"
        elif "Incorrect flag".encode() in response:
            return "flag_invalid"
        else:
            return "failed"

    # def getAllChallenges(apitoken):
    # cant seem to find challenge listing... web scraping?