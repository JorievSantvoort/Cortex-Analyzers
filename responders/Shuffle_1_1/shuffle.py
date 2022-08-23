#!/usr/bin/env python3
from cortexutils.responder import Responder
import requests

class Shuffle(Responder):
    def __init__(self):
        Responder.__init__(self)
        self.api_key = self.get_param("config.api_key", "")
        self.url = self.get_param("config.url", "")
        self.workflow_id = self.get_param("config.workflow_id", "")
        
        self.use_webhook_mode = self.get_param("config.use_webhook_mode", "")
        self.webhook_URI = self.get_param("config.webhook_URI", "")
        self.authentication_headers = self.get_param("config.authentication_headers", "")



    def run(self):
        Responder.run(self)

        if self.use_webhook_mode == False:

            parsed_url = "%s/api/v1/workflows/%s/execute" % (self.url, self.workflow_id)
            headers = {
                "Authorization": "Bearer %s"  % self.api_key
            }
            r = requests.post(parsed_url, headers=headers)
            if r.status_code == 200:
                self.report({"Message": "Executed workflow"})
            else:
                self.error(r.status_code)
        else:
            ## Webhook mode
            ## TheHive input data to post to Shuffle
            inputdata = self.get_param("data", None)

            if not self.authentication_headers:
                headers = {
                    "%s"  % self.authentication_headers
                }
                r = requests.post(self.webhook_URI,data=inputdata,headers=headers)
            else:
                r = requests.post(self.webhook_URI,data=inputdata) 
            
            if r.status_code == 200:
                self.report({"Message": "Executed webhook post"})
            else:
                self.error(r.status_code)
            
            

if __name__ == '__main__':
    Shuffle().run()

