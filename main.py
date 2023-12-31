import requests
from time import time, sleep

class APIClient:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': 'Bearer ' + self.token,
            'Accept': 'application/json',
        }

    def buy_activation(self, country, operator, product):
        url = f'https://5sim.net/v1/user/buy/activation/{country}/{operator}/{product}'
        response = requests.get(url, headers=self.headers)
        return response.json() if response.status_code == 200 else response.status_code

    def ban_order(self, id):
        url = f'https://5sim.net/v1/user/ban/{id}'
        response = requests.get(url, headers=self.headers)
        return response.status_code == 200

    def cancel_order(self, id):
        url = f'https://5sim.net/v1/user/cancel/{id}'
        response = requests.get(url, headers=self.headers)
        return response.status_code == 200

    def get_sms(self, id):
        url = f'https://5sim.net/v1/user/check/{id}'
        response = requests.get(url, headers=self.headers)
        return response.json() if response.status_code == 200 else response.status_code


class ActivationHandler:
    def __init__(self, api_client):
        self.api_client = api_client
        self.purchased = False
        self.activation_id = 0
        self.start_time = 0 

    def buy_and_check_activation(self, country, operator, product):
        while True:
            if not self.purchased:
                activation_response = self.api_client.buy_activation(country, operator, product)
                print(f'buy_activation: {activation_response}')
                if not isinstance(activation_response, int):
                    self.activation_id = activation_response.get('id', 0)
                    print(f'Activation ID: {self.activation_id}')
                    self.purchased = True
                    self.start_time = time() 
                    print("Starting timer...")

            if self.purchased:
                elapsed_time = time() - self.start_time
                print(f'Seconds elapsed: {elapsed_time}')

                if elapsed_time > 300:
                    if not self.api_client.ban_order(self.activation_id):
                        print("Could not ban the number")
                        print("Attempting to cancel")
                        if not self.api_client.cancel_order(self.activation_id):
                            print("Could not cancel the number")
                            print("Attempting to purchase another")
                            self.purchased = False
                            self.start_time = 0  # Reinicia o cronômetro
                    break

                sms = self.api_client.get_sms(self.activation_id)
                if not isinstance(sms, int):
                    print(sms)
                    if len(sms.get('sms', [])) != 0:
                        print(sms['sms'])
                        break
                print("Waiting for SMS")
                sleep(15)
            sleep(10)



if __name__ == "__main__":
    token = 'your_token_here'
    country = 'butan'
    operator = 'any'
    product = 'telegram'

    api_client = APIClient(token)
    activation_handler = ActivationHandler(api_client)
    activation_handler.buy_and_check_activation(country, operator, product)
