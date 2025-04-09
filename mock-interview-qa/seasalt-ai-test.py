""
### **Asynchronous Programming Task: Restaurant Order Processing System**


# #### **Background**
# You are tasked with simulating a simple restaurant order processing system. The restaurant has two roles:
# 1. **Cashier**: Responsible for adding orders to a queue (simulates customers placing orders).
# 2. **Chef**: Responsible for processing the orders (processing time is random int in [1, 2] seconds,
# use asyncio.sleep to simulate).




# #### **Requirements**
# 1. Implement an asynchronous function `cashier` that simulates adding one new order to a queue every 1 second (n orders in total). 

## Please print the order number when adding an order to the queue.

# e.g.
# Cashier: Added order 1
# 2. Implement an asynchronous function `chef` that fetches and processes orders from the queue. 

## Please print the chef ID and order number when starting and finishing an order. 
# e.g.
# Chef 1: Started processing order 1
# Chef 1: Finished order 1


# 3. The main program should start both the cashier and multiple chefs in the same time,
# and it should ensure that all orders are processed before exiting. # create_task to schedule, async with




# follow-ups:
# 1. The kitchen can only allow **one chef to work at a time**
# 1. The kitchen can only allow **n chef to work at a time**


# Note:
# You can use threading instead of asyncio if you want.
# # ---


# ### **Code Template**
# Complete the following code to fulfill the requirements:




import asyncio

dq = asyncio.Queue()

async def cashier(order_count: int):
    """Simulate the cashier adding new orders."""
    # TODO: Implement the cashier function, the argument can be augmented as needed
    print(f'Start Fetching order...')
    for i in range(1, order_count + 1):
        await asyncio.sleep(1) # simulate IO ops for 1 second
        await dq.put(i)
        print(f'Added order {i}')

    # ⭐️ Signal the chefs to stop by adding sentinel values
    for _ in range(order_count):
        await dq.put(None)

    pass


async def chef(chef_id: int):
    """Simulate a chef processing orders."""
    # TODO: Implement the cashier function, the argument can be augmented as needed
    
    # take peek order from the dq
    # Chef{chef_id}: Start Processing Order {i}
    # Chef{chef_id}: Finish Order {i}

    print('run this line')
    while dq:
        # chef_id(1) - id = 1, id = 2
        order_number = await dq.get()
        
        if order_number is None:
            print('No more Order - End the chef task')
            dq.task_done()
            break

        print(f'Chef{chef_id}: Starting processing Order{order_number}')
        await asyncio.sleep(1.5) # simulat IO ops
        print(f'Chef{chef_id}: Finish Order{order_number}')
        

        dq.task_done() # ⭐️ Mark task as complete for dq.join()
        
        

async def main():
    chef_count = 2 
    order_count = 5
    # Some asyncio primitives may be needed to be passed as arguments
    chef_coroutines = [chef(chef_id=i + 1) for i in range(chef_count)]
    tasks = [cashier(order_count), *chef_coroutines]
    
    # ⭐️ Until all tasks are complete
    await dq.join()
    # Start the cashier and chefs
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
