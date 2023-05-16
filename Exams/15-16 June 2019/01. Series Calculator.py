series_name = input()
seasons = int(input())
episodes = int(input())
episode_time = float(input())

episode_length = (0.2 * episode_time) + episode_time
special_episodes = seasons * 10

total_time = (episode_length * episodes * seasons) + special_episodes

print(f"Total time needed to watch the {series_name} series is {int(total_time)} minutes.")
