import time
class Customer:
    def __init__(self, name, mood, personality, initial_patience: float = 100, arrive_time=None):
        self.name = name
        self.mood = mood
        self.personality = personality
        self.arrive_time = arrive_time if arrive_time else int(time.time())
        self.initial_patience = initial_patience
        self.patience = initial_patience

    def get_mood(self):
        return self.mood

    def get_waiting_time(self, current_time=None):
        if current_time is None:
            current_time = int(time.time())
        return float(current_time - self.arrive_time)

    def get_patience(self):
        return round(self.patience, 2)

    def __repr__(self):
        max_line = max(
            len("name: " + (self.name.__repr__())),
            len("mood: " + str(self.mood.__repr__())),
            len("personality: " + str(self.personality.__repr__())),
            len("patience: " + self.patience.__repr__())
        )
        star_line = "*" * (max_line + 4)
        return (
            f"{star_line}\n"
            f"* name: {(self.name.__repr__()).ljust(max_line - len('name: '))} *\n"
            f"* mood: {str(self.mood.__repr__()).ljust(max_line - len('mood: '))} *\n"
            f"* personality: {str(self.personality.__repr__()).ljust(max_line - len('personality: '))} *\n"
            f"* patience: {str(self.get_patience()).ljust(max_line - len('patience: '))} *\n"
            f"{star_line}"
        )

    def update(self, waiting_time=None):
        if waiting_time is None:
            waiting_time = self.get_waiting_time()
        patience_factor = self.mood.get_patience_factor(waiting_time)
        self.patience = round(self.initial_patience - patience_factor, 2)
        self.mood = self.personality.adjust_mood(self.mood, waiting_time)


