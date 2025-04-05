import asyncio

async def cancel_me():
    print('--- cancel_me(): sleep ---')

    try:
        # wait for one hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('--- cancel_me(): cancel sleep ---')
        raise
    finally:
        print('--- cancel_me(): after sleep ---')

async def main():
    print('--- main(): running ---')
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me()) # <- schedule cancel_me() to run concurrently as a Task. 
    # But it won't execute immediately
    # the event loop needs control first

    # Wait for 5 seconds
    print('--- main(): sleep ---')
    await asyncio.sleep(10) # <- hits a sleep for 10 seconds
    # While the main coroutine is 'sleeping', the event loop gives control to other schedules tasks - like `cancel_me()`
    # This lets cancel_me() begin execution.

    print('--- main(): call cancel ---')
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print('main(): cancel_me is cancelled now')

asyncio.run(main())

"""
--- main(): running ---
===== schedule cancel_me() to run concurrently as a Task =====

--- main(): sleep ---
===== hit a sleep for 10 seconds, event loop give control to other schedule tasks, begin cancel_me() execution =====

--- cancel_me(): sleep ---
===== hit a sleep for 3600 second, event loop give control back to main task
===== after 10 seconds ======

--- main(): call cancel ---
===== Then it calls task.cancel() - which send a cancellation request to the task.
The next time the task yields (it's at await asyncio.sleep(3600)), it will raise asyncio.CancelledError

===== So the sleep call is interrupted, raising CancelledError.
The "coroutine jumps to the `except` block and prints

--- cancel_me(): cancel sleep ---
===== Then it hits `finally`, which always runs
--- cancel_me(): after sleep ---

===== back in main(), your `await task` now is in a "cancel state". It raises CancelledError here too
which you catch, and then print
--- main(): cancel_mne is cancelled now


"""

"""
Time --->

main() starts
 |
 |--> print 'main(): running'
 |--> create_task(cancel_me)
 |--> print 'main(): sleep'
 |--> await sleep(10) ────┐
                         ↓ (main suspended, other tasks run)
                cancel_me() starts
                |--> print 'cancel_me(): sleep'
                |--> await sleep(3600) [interrupted by cancel]
                         ↑
main() resumes after 10s ──┘
 |
 |--> print 'main(): call cancel'
 |--> task.cancel()
 |--> await task
           |
           |--> cancel_me receives CancelledError
           |--> print 'cancel sleep'
           |--> print 'after sleep'
           |--> re-raise CancelledError
 |
 |--> catches CancelledError
 |--> print 'main(): cancel_me is cancelled now'

"""