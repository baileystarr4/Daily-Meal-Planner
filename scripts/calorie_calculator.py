class CalorieCalculator:
    """
    A class used to calculate how many calories a user should eat per 
    day to achieve their weight goals.

    """
    
    def __init__(self,sex, age, feet, inches, weight, activity_level, goal):
        """
        Constructs all necessary attributes for the CalorieCalculator 
        object and starts the calculation.

        Parameters
        ----------
        sex : str
            the user's sex
        age : int
            the user's age
        height : int
            the user's height in cm
        weight : int
            the user's weight in kg
        activity_level : str
            the user's activity level
        goal : str
            the user's weight goal
        """

        self.sex = sex
        self.age = age
        #convert to cm
        self.height = (feet * 30.48) + (inches * 2.54)
        #convert to kg
        self.weight = weight * 0.45359237
        self.activity_level = activity_level
        self.goal = goal

        self.calories = None

        self._calculate_calories()

    def _calculate_BMR(self):
        # calculates BMR using Harris-Benedict formula
        if self.sex == 'male':
            BMR = (66.5 + (13.75 * self.weight) + (5.003 * self.height) 
                   - (6.75 * self.age))
        else:
            BMR = (655.1 + (9.563 * self.weight) + (1.850 * self.height) 
                   - (4.676 * self.age))
        return BMR

    def _calculate_TDEE(self):
        BMR = self._calculate_BMR()
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

    def _calculate_calories(self):
        TDEE = self._calculate_TDEE()
        match self.goal:
            case "gain":
                self.calories = round(TDEE + 500)
            case "lose":
                self.calories = round(TDEE - 500)
                # Daily calorie intake should never fall under 1200
                if self.calories < 1200:
                    self.calories = 1200
            case "maintain":
                self.calories = round(TDEE)