# Import required libraries
import requests  # For making HTTP requests
import time     # For measuring execution time
import threading  # For threading support
from concurrent.futures import ThreadPoolExecutor  # For managing thread pools

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
    Main function demonstrating threading approach
    - Creates 10 identical URLs
    - Uses ThreadPoolExecutor to manage multiple threads
    - Each thread executes do_request function
    """
    # Create list of 10 identical URLs
    urls = ["https://example.com"] * 10
    
    # Start timing
    start_time = time.time()
    
    # Create a thread pool with maximum 10 workers
    # ThreadPoolExecutor automatically manages thread creation and cleanup
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Map the do_request function to each URL
        # This creates a thread for each URL
        executor.map(do_request, urls)
    
    # End timing
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nTotal execution time with threading: {total_time:.2f} seconds")

if __name__ == '__main__':
    main() 