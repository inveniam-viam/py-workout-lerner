def run_timing() -> None:

    total_runs: int = 0
    total_time: float = 0

    while run_time := input("Enter your 10K run time (in minutes): "):

        try:
            total_time += float(run_time)
            total_runs += 1
        except ValueError:
            print("Please enter valid numeric input.")
        
    if total_runs > 0:
        print(f"Average of {(total_time / total_runs):.2f} over {total_runs} runs.")
    else:
        print("Invalid inputs encountered.")

if __name__ == "__main__":

    run_timing()
