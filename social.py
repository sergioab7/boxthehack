from htbapi.core import rawPostSSL, getRequest
import json


class social:
    def getShoutboxLatest(apitoken: str) -> dict:
        response = rawPostSSL(f"/shouts/get/initial/html/1", "", apitoken, "", "}").decode()
        if '"success":"0"' in response:
            return "failed"
        response = response[response.find('{"success":"1"'):]
        jsondata = json.loads(response)
        return jsondata

    def sendShoutbox(msg: str, apitoken: str) -> str:
        response = rawPostSSL("/shouts/new/", f"text={msg}", apitoken, "x-www-form-urlencoded", "")
        if '"success":"1"'.encode() in response:
            return "success"
        else:
            return "failed"

    def startConversation(msg: str, recipient: str, apitoken: str) -> str:
        response =  rawPostSSL("/conversations/new/", f"recipients%5B%5D={recipient}&message={msg}", apitoken, "x-www-form-urlencoded", "")
        if "No valid recipients selected".encode() in response:
            return "invalid_recipient"
        elif '{"id":'.encode() in response:
            return "success"
        else:
            return "failed"

    def sendConversationMessage(msg: str, conversationid: int, apitoken: str) -> str:
        response = rawPostSSL(f"/conversations/send/{conversationid}/", f"id={conversationid}&message={msg}", apitoken, "x-www-form-urlencoded", "")
        # if you type an invalid id you for some reason get the skid message...
        if "You must have Script Kiddie rank or higher to send messages".encode() in response:
            return "no_skid_or_invalid_id"
        # could be a non-success, but we cant confirm so here we go...
        elif "HTTP/1.1 200".encode() in response:
            return "success"
        else:
            return "failed"
        

    def getConversations(apitoken: str) -> list:
        response = rawPostSSL("/conversations/list/", "", apitoken, "", '"}]').decode()
        response = response[response.find('[{"id":'):]
        jsondata = json.loads(response)
        return jsondata


    def getConversation(conversationid: int, apitoken: str) -> list:
        response = rawPostSSL(f"/conversations/load/{conversationid}", "", apitoken, "", "}]\r\n").decode()
        response = response[response.find('[{"id":'):]
        jsondata = json.loads(response)
        return jsondata
    