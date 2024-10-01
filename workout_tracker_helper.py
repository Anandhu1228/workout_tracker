import time

class WorkTracker:

    def __init__(self,name,age,category,level,frequency):
        self.name = name
        self.age = age
        self.category = category
        self.level = level
        self.frequency = frequency

    def AlreadyDefSetRepSorted(self):
        workouts = {
            1: {  #STRENGTH WORKOUT
                1: {"workout_count": 4, "sets": 3, "reps_per_set": 12, "set_time": 40,
                    "rest_between_sets": 60, "rest_between_workouts": 120},
                2: {"workout_count": 5, "sets": 4, "reps_per_set": 10, "set_time": 45,
                    "rest_between_sets": 90, "rest_between_workouts": 150},
                3: {"workout_count": 6, "sets": 5, "reps_per_set": 8, "set_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 180}
            },
            2: {  #CARDIO WORKOUT
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 30, "set_time": 60,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 20, "set_time": 75,
                    "rest_between_sets": 120, "rest_between_workouts": 150},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 15, "set_time": 90,
                    "rest_between_sets": 150, "rest_between_workouts": 180}
            },
            3: {  #FLEXIBILITY WORKOUT
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 10, "set_time": 30,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 8, "set_time": 40,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 6, "set_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            4: {  #MOBILITY WORKOUT
                1: {"workout_count": 4, "sets": 3, "reps_per_set": 10, "set_time": 30,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 5, "sets": 4, "reps_per_set": 8, "set_time": 40,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 6, "sets": 5, "reps_per_set": 6, "set_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            5: {  #BODYWEIGHT WORKOUT
                1: {"workout_count": 4, "sets": 3, "reps_per_set": 12, "set_time": 35,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 5, "sets": 4, "reps_per_set": 10, "set_time": 40,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 6, "sets": 5, "reps_per_set": 8, "set_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            6: {  #YOGA WORKOUT
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 5, "set_time": 60,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 5, "set_time": 75,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 5, "set_time": 90,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            7: {  #POWER LIFTING
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 5, "set_time": 45,
                    "rest_between_sets": 120, "rest_between_workouts": 180},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 5, "set_time": 60,
                    "rest_between_sets": 150, "rest_between_workouts": 180},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 3, "set_time": 75,
                    "rest_between_sets": 180, "rest_between_workouts": 240}
            },
            8: {  #HIIT
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 15, "set_time": 45,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 12, "set_time": 60,
                    "rest_between_sets": 120, "rest_between_workouts": 150},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 10, "set_time": 75,
                    "rest_between_sets": 150, "rest_between_workouts": 180}
            },
            9: {  #CORE WORKOUT
                1: {"workout_count": 4, "sets": 3, "reps_per_set": 15, "set_time": 40,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 5, "sets": 4, "reps_per_set": 12, "set_time": 45,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 6, "sets": 5, "reps_per_set": 10, "set_time": 50,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            },
            10: {  #LOW IMPACT WORKOUT
                1: {"workout_count": 3, "sets": 3, "reps_per_set": 12, "set_time": 30,
                    "rest_between_sets": 60, "rest_between_workouts": 90},
                2: {"workout_count": 4, "sets": 4, "reps_per_set": 10, "set_time": 35,
                    "rest_between_sets": 90, "rest_between_workouts": 120},
                3: {"workout_count": 5, "sets": 5, "reps_per_set": 8, "set_time": 40,
                    "rest_between_sets": 120, "rest_between_workouts": 150}
            }
        }

        userdata = {
            "name": self.name,
            "age": self.age,
            "frequency": self.frequency
        }
        plan = workouts[self.category][self.level]

        return {"userdata": userdata, "plan": plan}

    @staticmethod
    def CustomWorkoutTracker(mode, constraint, noOfSet, timeOfSet, restOfSet, restOfWorkout):
        if mode == 1:
            time_limit = constraint
            no_of_set = noOfSet
            time_of_set = timeOfSet
            rest_of_set = restOfSet
            rest_of_workout = restOfWorkout

            timeOfEachSet = time_of_set + rest_of_set
            timeOfEachWorkout = (timeOfEachSet * no_of_set) + rest_of_workout

            totalNumberOfWorkout = (time_limit * 60) // timeOfEachWorkout
            return (totalNumberOfWorkout,no_of_set,time_of_set,rest_of_set,rest_of_workout)
        elif mode == 2 or mode == 0:
            no_of_workout = constraint
            no_of_set = noOfSet
            time_of_set = timeOfSet
            rest_of_set = restOfSet
            rest_of_workout = restOfWorkout

            timeOfEachSet = time_of_set + rest_of_set
            timeOfEachWorkout = (timeOfEachSet * no_of_set) + rest_of_workout

            totalTimeNeeded = timeOfEachWorkout * no_of_workout
            minutesToComplete = totalTimeNeeded // 60
            remsecondsToComplete = totalTimeNeeded % 60

            return (minutesToComplete,remsecondsToComplete,no_of_workout,no_of_set,time_of_set,rest_of_set,rest_of_workout)
