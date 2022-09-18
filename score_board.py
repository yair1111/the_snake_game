from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"score: {self.current_score}, High score: {self.high_score}", False, "center", ("Courier", 20, "normal"))

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.update_score_board()

    def increase(self):
        self.current_score += 1
        self.update_score_board()








