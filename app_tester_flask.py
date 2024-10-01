from flask import Flask, request,render_template, Response
from flask_cors import CORS
from workout_tracker_helper import WorkTracker
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "null"}})

@app.route('/')
def index():
    return render_template('app.html')

TOTAL_NUMBER_OF_WORKOUT = None
TOTAL_NUMBER_OF_SET = None
SET_DURATION = None
SET_REST_DURATION = None
WORKOUT_REST_DURATION = None


@app.route('/submit', methods=['POST'])
def submit():
    category_list = ["STRENGTH WORKOUT", "CARDIO WORKOUT", "FLEXIBILITY WORKOUT",
         "MOBILITY WORKOUT", "BODYWEIGHT WORKOUT", "YOGA WORKOUT",
         "POWER LIFTING", "HIIT", "CORE WORKOUT", "LOW IMPACT WORKOUT"]

    level_list = ["BEGINNER", "INTERMEDIATE", "ADVANCED"]

    name = request.form.get('name')
    age = int(request.form.get('age'))
    category = int(request.form.get('category'))
    level = int(request.form.get('level'))
    frequency = int(request.form.get('frequency'))

    category_str = category_list[category-1]
    level_str = level_list[level-1]

    tracker = WorkTracker(name,age, category, level, frequency)

    tracker.AlreadyDefSetRepSorted()
    outcome = tracker.AlreadyDefSetRepSorted()
    return render_template('result.html',
                           userdata=outcome["userdata"],
                           plan=outcome["plan"],
                           category_str = category_str,
                           level_str = level_str)

@app.route('/custom_workout', methods=['GET', 'POST'])
def custom_workout():
    if request.method == 'POST':
        workout_name = request.form.get('workout_name')
        workout_sets = int(request.form.get('workout_sets'))
        workout_reps = int(request.form.get('workout_reps'))
        workout_duration = int(request.form.get('workout_duration'))
        rest_time = int(request.form.get('rest_time'))
        return render_template('custom_workout_result.html',
                               workout_name=workout_name,
                               workout_sets=workout_sets,
                               workout_reps=workout_reps,
                               workout_duration=workout_duration,
                               rest_time=rest_time)

    return render_template('custom_workout.html')


@app.route('/send_confirm_predefine', methods=['POST'])
def custom_def_mode():
    workout_limit = int(request.form.get('workout_limit'))
    workout_sets = int(request.form.get('workout_sets'))
    workout_duration = int(request.form.get('workout_duration'))
    rest_time_set = int(request.form.get('rest_time_set'))
    rest_time_workout = int(request.form.get('rest_time_workout'))
    mode = 0

    outcome = WorkTracker.CustomWorkoutTracker(mode, workout_limit, workout_sets, workout_duration, rest_time_set, rest_time_workout)

    minutesToComplete, remsecondsToComplete, total_number_of_workout, no_of_set, time_of_set, rest_of_set, rest_of_workout = outcome

    return render_template('custom_workout.html',
                           minutesToComplete=minutesToComplete,
                           remsecondsToComplete=remsecondsToComplete,
                           total_number_of_workout=total_number_of_workout,
                           no_of_set=no_of_set,
                           time_of_set=time_of_set,
                           rest_of_set=rest_of_set,
                           rest_of_workout=rest_of_workout,
                           mode=mode)


@app.route('/custom_time_mode', methods=['POST'])
def custom_time_mode():
    workout_limit = int(request.form.get('workout_limit'))
    workout_sets = int(request.form.get('workout_sets'))
    workout_duration = int(request.form.get('workout_duration'))
    rest_time_set = int(request.form.get('rest_time_set'))
    rest_time_workout = int(request.form.get('rest_time_workout'))
    mode = 1

    outcome = WorkTracker.CustomWorkoutTracker(mode, workout_limit, workout_sets, workout_duration, rest_time_set, rest_time_workout)

    totalNumberOfWorkout, no_of_set, time_of_set, rest_of_set, rest_of_workout = outcome

    return render_template('custom_workout.html',
                           total_number_of_workout=totalNumberOfWorkout,
                           no_of_set=no_of_set,
                           time_of_set=time_of_set,
                           rest_of_set=rest_of_set,
                           rest_of_workout=rest_of_workout,
                           mode=mode)


@app.route('/custom_work_mode', methods=['POST'])
def custom_work_mode():
    workout_limit = int(request.form.get('workout_number'))
    workout_sets = int(request.form.get('workout_sets'))
    workout_duration = int(request.form.get('workout_duration'))
    rest_time_set = int(request.form.get('rest_time_set'))
    rest_time_workout = int(request.form.get('rest_time_workout'))
    mode = 2

    outcome = WorkTracker.CustomWorkoutTracker(mode, workout_limit, workout_sets, workout_duration, rest_time_set,
                                   rest_time_workout)

    minutesToComplete, remsecondsToComplete, no_of_workout, no_of_set, time_of_set, rest_of_set, rest_of_workout = outcome

    return render_template('custom_workout.html',
                           minutesToComplete=minutesToComplete,
                           remsecondsToComplete=remsecondsToComplete,
                           total_number_of_workout=no_of_workout,
                           no_of_set=no_of_set,
                           time_of_set=time_of_set,
                           rest_of_set=rest_of_set,
                           rest_of_workout=rest_of_workout,
                           mode=mode)


@app.route('/send_confirm_workout', methods=['POST'])
def startall_work_mode():

    global TOTAL_NUMBER_OF_WORKOUT, TOTAL_NUMBER_OF_SET, SET_DURATION, SET_REST_DURATION, WORKOUT_REST_DURATION

    TOTAL_NUMBER_OF_WORKOUT = int(request.form.get('total_no_of_workout'))
    TOTAL_NUMBER_OF_SET = int(request.form.get('total_no_of_set'))
    SET_DURATION = int(request.form.get('set_duration'))
    SET_REST_DURATION = int(request.form.get('set_rest_duration'))
    WORKOUT_REST_DURATION = int(request.form.get('workout_rest_duration'))

    return render_template('start_workout.html')


def starTrackAlong(no_of_workout, no_of_set, time_of_set, rest_of_set, rest_of_workout):
    def generate():
        c = 1
        while c <= no_of_workout:
            yield f"data: WORKOUT {c} WILL START NOW\n\n"
            time.sleep(5)  # Wait before starting the workout

            for i in range(1, no_of_set + 1):
                yield f"data: START SET {i}\n\n"
                time.sleep(time_of_set)  # Simulate set duration
                yield f"data: STOP SET {i}, TAKE REST\n\n"
                if i < no_of_set:
                    time.sleep(rest_of_set)  # Simulate rest duration between sets

            if c < no_of_workout:
                yield f"data: WORKOUT {c} COMPLETED, TAKE REST BEFORE NEXT WORKOUT.\n\n"
            else:
                yield f"data: WORKOUT {c} COMPLETED, WORKOUT SESSION FINISHED!\n\n"

            time.sleep(rest_of_workout)  # Simulate rest duration between workouts
            c += 1

        yield "data: ALL WORKOUTS COMPLETED. GREAT JOB!\n\n"

    return Response(generate(), mimetype='text/event-stream')


# SSE endpoint (Server-Sent Events)
# https://chatgpt.com/share/66fad613-8b98-8002-8bbe-365ebbfcf6ad ( EXPLANATION Y CHATGPT )
@app.route('/stream_workout', methods=['GET'])
def stream_workout():
    no_of_workout = TOTAL_NUMBER_OF_WORKOUT
    no_of_set = TOTAL_NUMBER_OF_SET
    time_of_set = SET_DURATION
    rest_of_set = SET_REST_DURATION
    rest_of_workout = WORKOUT_REST_DURATION

    return starTrackAlong(no_of_workout, no_of_set, time_of_set, rest_of_set, rest_of_workout)


if __name__ == '__main__':
    print("Starting python flask server for workout tracker..")
    app.run(debug=True)

