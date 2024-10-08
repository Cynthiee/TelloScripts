import time
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

sim_key = '79f839c4-48c5-4d6e-9f03-f761e3c63606'

def perform_takeoff(drone):
    """Handles the drone takeoff."""
    drone.takeoff()

def hover_for_duration(hover_time):
    """Handles the drone hover and calculates elapsed time."""
    start_time = time.time()
    time.sleep(hover_time)
    elapsed_time = time.time() - start_time
    print(f"Time elapsed: {elapsed_time:.2f} seconds")

def perform_landing(drone):
    """Handles the drone landing."""
    drone.land()

def main(sim_key):
    """Main function to control the drone."""
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        perform_takeoff(drone)
        hover_for_duration(15)
        perform_landing(drone)

if __name__ == '__main__':
    main(sim_key)
