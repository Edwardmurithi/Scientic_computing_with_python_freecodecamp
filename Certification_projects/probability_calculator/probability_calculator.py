import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents = []
        else:
            for _ in range(num_balls):
                chosen_ball = random.choice(self.contents)
                self.contents.remove(chosen_ball)
                drawn_balls.append(chosen_ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Create a copy of the hat's contents to ensure no modification of the original hat
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the balls drawn
        drawn_ball_count = {}
        for ball in drawn_balls:
            if ball in drawn_ball_count:
                drawn_ball_count[ball] += 1
            else:
                drawn_ball_count[ball] = 1
        
        # Check if the drawn balls match the expected balls
        success = True
        for color, count in expected_balls.items():
            if drawn_ball_count.get(color, 0) < count:
                success = False
                break
        
        if success:
            success_count += 1
    
    return success_count / num_experiments

if __name__ == "__main__":
    hat = Hat(blue=5, red=4, green=2)
    probability = experiment(
        hat=hat,
        expected_balls={'red': 1, 'green': 2},
        num_balls_drawn=4,
        num_experiments=2000
    )
    print("Probability:", probability)
