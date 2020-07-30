from htbapi.core import getRequest, rawPostSSL



class machines:
    def ownRoot(machineid: int, apitoken: str, flag: str, difficulty: int) -> str:
        response = rawPostSSL(f"/machines/own/root/{machineid}", f'{{"flag":"{flag}","difficulty":{difficulty * 10}}}', apitoken, "json", "")
        if '"success":"1"'.encode() in response:
            return "success"
        elif "Incorrect hash".encode() in response:
            return "flag_invalid"
        else:
            return "failed"

    def ownUser(machineid: int, apitoken: str, flag: str, difficulty: int) -> str:
        response =  rawPostSSL(f"/machines/own/user/{machineid}", f'{{"flag":"{flag}","difficulty":{difficulty * 10}}}', apitoken, "json", "")
        if '"success":"1"'.encode() in response:
            return "success"
        elif "Incorrect hash".encode() in response:
            return "flag_invalid"
        else:
            return "failed"

    def ownMachine(machineid: int, apitoken: str, flag: str, difficulty: int) -> str:
        response =  rawPostSSL(f"/machines/own", f'{{"flag":"{flag}","difficulty":{difficulty * 10},"id":{machineid}}}', apitoken, "json", "")
        if '"success":"1"'.encode() in response:
            return "success"
        elif "Incorrect flag".encode() in response:
            return "flag_invalid"
        else:
            return "failed"

    def getAllMachines(apitoken: str) -> list:
        return getRequest("/machines/get/all/", apitoken).json()
            
    def getAllActiveMachines(apitoken: str) -> list:
        activemachines = []
        allmachines = getAllMachines(apitoken)
        for machine in allmachines:
            if machine["retired"] == False:
                activemachines.append(machine)
        return activemachines

    def getAllRetiredMachines(apitoken: str) -> list:
        retiredmachines = []
        allmachines = getAllMachines(apitoken)
        for machine in allmachines:
            if machine["retired"] == True:
                retiredmachines.append(machine)
        return retiredmachines

    def resetMachine(machineid: int, apitoken: str) -> str:
        response =  rawPostSSL(f"/vm/reset/{machineid}", "", apitoken, "", "")
        if "requested a reset on".encode() in response:
            return "success"
        else:
            return "failed"

    def assignMachine(machineid: int, apitoken: str) -> str:
        response = rawPostSSL(f"/vm/vip/assign/{machineid}", "", apitoken, "", "")
        if "Machine deployed to lab.".encode() in response:
            return "success"
        elif "You already have an active machine.".encode() in response:
            return "already_have_machine"
        elif "Incorrect lab type.".encode() in response:
            return "no_vip"
        else:
            return "failed"

    def stopMachine(machineid: int, apitoken: str) -> str:
        response = rawPostSSL(f"/vm/vip/remove/{machineid}", "", apitoken, "", "")
        if "Machine scheduled for termination.".encode() in response:
            return "success"
        elif "This machine is not active.".encode() in response:
            return "machine_not_active"
        elif "Incorrect lab type.".encode() in response:
            return "no_vip"
        else:
            return "failed"

    def extendMachine(machineid: int, apitoken: str) -> str:
        response = rawPostSSL(f"/vm/vip/extend/{machineid}", "", apitoken, "", "")
        if "Machine not assigned to this lab.".encode() in response:
            return "machine_not_active"
        elif "Machine extended by 24 hours.".encode() in response:
            return "success"
        elif "Incorrect lab type.".encode() in response:
            return "no_vip"
        else: 
            return "failed"

    def getSpawnedMachines(apitoken: str) -> list:
        return getRequest("/machines/spawned/", apitoken).json()

    def getTerminatingMachines(apitoken: str) -> list:
        return getRequest("/machines/terminating/", apitoken).json()

    def getResettingMachines(apitoken: str) -> list:
        return getRequest("/machines/resetting/", apitoken).json()

