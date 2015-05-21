from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):
    def on_start(self):
        self.client.get("http://show-me.php.viawolf.com/home", verify=False)

    @task(1)
    def directory1(self):
        self.client.get("http://show-me.php.viawolf.com/about", verify=False)
    @task(2)
    def directory2(self):
        self.client.get("http://show-me.php.viawolf.com/projects/search", verify=False)
    @task(3)
    def directory3(self):
        self.client.get("http://show-me.php.viawolf.com/contact", verify=False)
    @task(4)
    def directory4(self):
        self.client.get("http://show-me.php.viawolf.com/projectsc", verify=False)
    @task(5)
    def directory5(self):
        self.client.get("http://show-me.php.viawolf.com/privacy", verify=False)
    @task(6)
    def directory6(self):
        self.client.get("http://show-me.php.viawolf.com/terms", verify=False)
    @task(7)
    def directory7(self):
        self.client.get("http://show-me.php.viawolf.com/projects/view/114", verify=False)
    



class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
