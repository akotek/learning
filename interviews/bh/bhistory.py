class BrowserHistory:
    def __init__(self, url: str):
        self.current = [url]
        self.future = []

    def status(self) -> str:
        return self.current[-1]

    def visit(self, url: str) -> None:
        self.current.append(url)

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.current) > 1:
            self.future.append(self.current.pop())
            steps -= 1
        return self.current[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.future) > 0:
            self.current.append(self.future.pop())
            steps -= 1
        return self.current[-1]
