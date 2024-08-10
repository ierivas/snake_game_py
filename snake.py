from turtle import Turtle

#STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20

class Snake:
    """Snake mode"""

    def __init__(self):

        self.snake = []
        for position in STARTING_POSITIONS:
            self.add_snake_seg(position)
        self.head =self.snake[len(self.snake)-1]
        print(f"init head {self.head.position()}")
        self.tail =self.snake[0]

    def add_snake_seg(self,position):
        snake_piece = Turtle("square")
        snake_piece.penup()
        snake_piece.goto(position)
        snake_piece.color("white")
        self.snake.append(snake_piece)

    def add_snake_eat(self, position):
        snake_piece = Turtle("square")
        snake_piece.penup()
        snake_piece.goto(position)
        snake_piece.color("white")
        self.snake.insert(0,snake_piece)
        self.head = self.snake[len(self.snake) - 1]
        self.tail = self.snake[0]
    def move(self):
        print(f"head move -> {self.head.position()}")
        for pos in range(-len(self.snake), -1, 1):
            position = (self.snake[pos + 1].xcor(), self.snake[pos + 1].ycor())
            self.snake[pos].goto(position)
        self.snake[-1].forward(MOVE_DISTANCE)


    def move_up(self):
        head_angle = self.head.heading()
        print(f"head angle MU->{head_angle}")
        if head_angle in (0, 180):
            self.head.setheading(90)

    def move_down(self):
        head_angle = self.head.heading()
        print(f"head angle MD->{head_angle}")
        if head_angle in (0, 180):
            self.head.setheading(270)

    def move_left(self):
        head_angle = self.head.heading()
        print(f"head angle ML->{head_angle}")
        if head_angle in (90, 270):
            self.head.setheading(180)

    def move_right(self):
        head_angle = self.head.heading()
        print(f"head angle MR->{head_angle}")
        if head_angle in (270, 90):
            self.head.setheading(0)

    def extend_snake(self):
        x_seg = self.tail.xcor()
        y_seg = self.tail.ycor()
        if self.head.heading() == 90:
            self.add_snake_eat((x_seg, y_seg-20))
        if self.head.heading() == 270:
            self.add_snake_eat((x_seg, y_seg+20))
        if self.head.heading() == 0:
            print(f"right eat -> {self.head.heading()}")
            self.add_snake_eat((x_seg-20, y_seg))
        if self.head.heading() == 180:
            print(f"left eat -> {self.head.heading()}")
            self.add_snake_eat((x_seg+20, y_seg))

    def screem_limit(self):
        print(f"Head -> {self.head.xcor()}")
        if self.head.xcor() >= 300:
            return False
        elif self.head.xcor()<= -300:
            return False
        elif self.head.ycor()>= 300:
            return False
        elif self.head.ycor() <= -300:
            return False
        else:
            return True

    def detect_coalition(self):
        coalition = False
        print (f"coalition head ->{self.head.position()} len -> {len(self.snake)-1}")
        for seg in range(0, len(self.snake)-1, 1):
            print(f"seg-> {seg} --- t{self.snake[seg].position()} d {self.head.distance(self.snake[seg])}")

            if self.head.distance(self.snake[seg]) <5:
                 print(f"colition->h{self.head.position()} - t{self.snake[seg].position()}")
                 coalition = True
                 break
            else:
                 coalition = False

        return coalition

    def detect_coalition2(self):
        coalition = False
        # print(f"coalition head ->{self.head.position()} len -> {len(self.snake) - 1}")
        print(f"snake -> {self.head in self.snake[:len(self.snake)-1]}")
        for seg in self.snake:

            if seg == self.head:
                pass
            # print(f"seg-> {seg.position()} --- t{seg.position()} d {self.head.distance(seg.position())}")

            elif self.head.distance(seg) < 5:
                print(f"colition->h{self.head.position()} - t{seg.position()}")
                coalition = True
                break
            else:
                coalition = False

        return coalition
#self.head =self.snake[len(self.snake) - 1]