from tqdm import tqdm
import time

# Number of iterations in your loop
total_iterations = 100

# Use tqdm to create a progress bar
progress_bar = tqdm(total=total_iterations, position=0, leave=True)
progress_counter = 0

for i in range(total_iterations):
    # Your processing logic goes here

    # Simulate some processing time
    time.sleep(0.1)

    # Update the progress bar and counter
    progress_bar.update(1)
    progress_counter += 1


# Close the progress bar
progress_bar.close()

