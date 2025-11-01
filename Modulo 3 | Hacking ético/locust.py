from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # evita ráfagas uniformes

    @task(5)
    def home(self):
        self.client.get("/")

    @task(1)
    def search(self):
        self.client.get("/search?q=test", name="/search")
