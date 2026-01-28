from turtle import Turtle, Vec2D


class TurtleApp:
    def __init__(self) -> None:
        self._turtle = Turtle()
        self.stylo_actif=True

    def set_up(self):
        # Initial position: pointing upward
        self._turtle.setheading(90)

        # Bind screen events
        self.bind_screen_events()

        # Set up callbacks in the screen object
        self._turtle.screen.listen()

    def activation_stylo(self):
        if self.stylo_actif:
            self._turtle.penup()
            self.stylo_actif=False
        else: 
            self._turtle.pendown()
            self.stylo_actif=True

    def run_app(self):
        # Set up the app
        self.set_up()

        # Infinite main loop
        self._turtle.screen.mainloop()

    def bind_screen_events(self):
        self._turtle.screen.onkey(self.on_up_key_event, "Up")
        self._turtle.screen.onkey(self.on_down_key_event, "Down")
        self._turtle.screen.onkey(self.on_left_key_event, "Left")
        self._turtle.screen.onkey(self.on_right_key_event, "Right")
        self._turtle.screen.onkey(self.reset_turtle, "space")
        self._turtle.screen.onkey(self.activation_stylo,"p")
        self._turtle.screen.onscreenclick(self.rosace)

    def on_up_key_event(self):
        self._turtle.forward(10)

    def on_down_key_event(self):
        self._turtle.back(10)

    def on_left_key_event(self):
        self._turtle.left(20)

    def on_right_key_event(self):
        self._turtle.right(20)

    def rosace(self, x_mouse, y_mouse):
        # Drawing sequence
        self._turtle.teleport(x_mouse, y_mouse)
        self._turtle.begin_fill() 
        while True: 
            self._turtle.forward(150) 
            self._turtle.left(140) 
            if abs(self._turtle.pos() - Vec2D(x_mouse, y_mouse)) < 1: 
                break 
        self._turtle.end_fill()



    def reset_turtle(self):
        self._turtle.clear()
        self._turtle.teleport(0, 0)
        self._turtle.setheading(90)
        self._turtle.color("black")
        self._turtle.fillcolor("black")
