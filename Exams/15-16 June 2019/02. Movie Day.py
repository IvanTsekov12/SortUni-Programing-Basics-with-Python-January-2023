import math

shooting_time = int(input())
scenes = int(input())
scene_length = int(input())

terrain_prep = shooting_time * 0.15
scene_shooting = scenes * scene_length

needed_time = scene_shooting + terrain_prep

if needed_time <= shooting_time:
    print(f"You managed to finish the movie on time! You have {math.ceil((shooting_time - needed_time))} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {math.ceil((needed_time - shooting_time))} minutes.")