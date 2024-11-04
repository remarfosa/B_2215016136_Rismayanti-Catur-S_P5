from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Tunggu antara 1 hingga 5 detik sebelum request

    @task
    def get_users(self):
        self.client.get("/users")  # Mendapatkan daftar semua user

    @task
    def create_users(self):
        # Daftar user yang akan ditambahkan
        users = [
            {"name": "Alice Smith", "username": "alicesmith", "email": "alice@example.com"},
            {"name": "Bob Johnson", "username": "bobjohnson", "email": "bob@example.com"},
            {"name": "Charlie Brown", "username": "charliebrown", "email": "charlie@example.com"}
        ]
        
        # Mengirimkan request POST untuk setiap user
        for user in users:
            self.client.post("/users", json=user)

    @task
    def get_user(self):
        # Mendapatkan user dengan ID tertentu
        self.client.get("/users/1")

    @task
    def update_user(self):
        # Memperbarui user dengan ID tertentu
        self.client.put("/users/1", json={
            "name": "Alice Smith Updated",
            "username": "aliceupdated",
            "email": "aliceupdated@example.com"
        })

    @task
    def delete_user(self):
        # Menghapus user dengan ID tertentu
        self.client.delete("/users/3")