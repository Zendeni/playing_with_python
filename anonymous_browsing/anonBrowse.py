import mechanize
import http.cookiejar as cookielib
import random
import time

class AnonBrowser(mechanize.Browser):
    def __init__(self, proxies=None, user_agents=None):
        super(AnonBrowser, self).__init__()
        self.set_handle_robots(False)
        self.proxies = proxies or []
        self.user_agents = user_agents or []
        self.user_agents += [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
        ]
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)
        self.anonymize()

    def clear_cookies(self):
        self.cookie_jar = cookielib.LWPCookieJar()
        self.set_cookiejar(self.cookie_jar)

    def change_user_agent(self):
        user_agent = random.choice(self.user_agents)
        self.addheaders = [('User-agent', user_agent)]

    def change_proxy(self):
        if self.proxies:
            proxy = random.choice(self.proxies)
            self.set_proxies({'http': proxy})

    def anonymize(self, sleep=False):
        self.clear_cookies()
        self.change_user_agent()
        self.change_proxy()
        if sleep:
            time.sleep(60)
