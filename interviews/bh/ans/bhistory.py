# ===================================================
# PART 1:
class BrowserHistory:
    def __init__(self, url: str):
        self.current = [url]
        self.future = []

    def status(self) -> str:
        return self.current[-1]

    def visit(self, url: str) -> None:
        self.current.append(url)
        self.future = []  # reset the forward stack

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


# ===================================================
# PART 2:
class Tab:
    # BrowserHistory is now Tab
    pass


class BrowserHistory2:
    def __init__(self):
        self.tabs = []

    def run_tab(self, tab: int) -> Tab:
        pass

# ===================================================
# PART 3:
# OPT1, DB:
# CREATE TABLE Table1(
#    session_id  INT PRIMARY KEY NOT NULL,
#    history     VARCHAR(100)  NOT NULL,    JSON: {"current": ["url1", "url2], "history": ["url3"]}
# );

# many rows representing the history, with order column
# CREATE TABLE Table2(
#    session_id  INT PRIMARY KEY NOT NULL,
#    history     VARCHAR(100)  NOT NULL,    "url1" (1x instance)
#    order       INT  NOT NULL;             # idx=0
# );

# OPT2, DISK:
# One file, each line represents a session, separated by ',' for current/history
#   ["url1", "url2"], ["url3"]
# File-per-session/tab, each file represents session/tab
# ...
