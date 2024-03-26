class Calorie_Calculator:
    def _init__(self,sex, age, height, weight, activity_level, goal):
        self.sex = sex
        self.age = age
        #convert to cm
        self.height = (height[0] * 30.48) + (height[1] * 2.54)
        #convert to kg
        self.weight = weight * 0.45359237
        self.activity_level = activity_level
        self.goal = goal

        self.calculate_BMR()
        self.calculate_TDEE()
        self.calculate_calories()

    #calculate BMR using Harris-Benedict formula
    def calculate_BMR(self):
        if self.sex == 'male':
            self.BMR = 66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.75 * self.age)
        else:
            self.BMR = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)
    
    def calculate_TDEE(self):
        match self.activity_level:
            case "sedentary":
                self.TDEE = self.BMR * 1.2
            case "lightly":
                self.TDEE = self.BMR * 1.375
            case "moderately":
                self.TDEE = self.BMR * 1.55
            case "very":
                self.TDEE = self.BMR * 1.725
            case "extra":
                self.TDEE = self.BMR * 1.9

    # calculates how many calories you should eat to obtain your goal
    def calculate_calories(self):
        match self.goal:
            case "gain":
                self.calories = self.TDEE + 500
            case "lose":
                self.calories = self.TDEE - 500
            case "maintain":
                self.calories = self.TDEE

    def get_calories(self):
        return self.calories