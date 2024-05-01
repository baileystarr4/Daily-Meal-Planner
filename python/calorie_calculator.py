class Calorie_Calculator:
    def __init__(self,sex, age, feet, inches, weight, activity_level, weight_goal):
        self.sex = sex
        self.age = age
        #convert to cm
        self.height = (feet * 30.48) + (inches * 2.54)
        #convert to kg
        self.weight = weight * 0.45359237
        self.activity_level = activity_level
        self.goal = weight_goal

        self.calculate_calories()

    # calculate BMR using Harris-Benedict formula
    def calculate_BMR(self):
        if self.sex == 'male':
            BMR = 66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.75 * self.age)
        else:
            BMR = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age)
        return BMR

    def calculate_TDEE(self):
        BMR = self.calculate_BMR()
        match self.activity_level:
            case "sedentary":
                TDEE = BMR * 1.2
            case "light":
                TDEE = BMR * 1.375
            case "moderate":
                TDEE = BMR * 1.55
            case "very":
                TDEE = BMR * 1.725
            case "extra":
                TDEE = BMR * 1.9
        return TDEE

    # calculates how many calories you should eat to obtain your goal
    def calculate_calories(self):
        TDEE = self.calculate_TDEE()
        match self.goal:
            case "gain":
                self.calories = round(TDEE + 500)
            case "lose":
                self.calories = round(TDEE - 500)
                if self.calories < 1200:
                    self.calories = 1200
            case "maintain":
                self.calories = round(TDEE)

    def get_calories(self):
        return self.calories
