# Import required libraries
import requests  # For making HTTP requests
import time     # For measuring execution time
from multiprocessing import Pool  # For managing process pools

def do_request(url):
    """
    Function to make a single HTTP request
    Args:
        url (str): The URL to request
    """
    req = requests.get(url)
    print(f"{url} => {req.status_code}")

def main():
    """
    Main function demonstrating multiprocessing approach
    - Creates 10 identical URLs
    - Uses Process Pool to manage multiple processes
    - Each process executes do_request function independently
    - Processes run in parallel on different CPU cores
    """
    # Create list of 10 identical URLs
    urls = ["https://example.com"] * 10
    
    # Start timing
    start_time = time.time()
    
    # Create a process pool with 10 worker processes
    # Each process has its own Python interpreter and memory space
    with Pool(processes=10) as pool:
        # Map the do_request function to each URL
        # This creates a process for each URL
        pool.map(do_request, urls)
    
    # End timing
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal execution time with multiprocessing: {total_time:.2f} seconds")

if __name__ == '__main__':
    main() 