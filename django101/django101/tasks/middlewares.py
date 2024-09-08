import time


def measure_time(get_response):
    def middleware(request, *args, **kwargs):

        print("Before view")
        start_time = time.time()
        result = get_response(request, *args, **kwargs)
        end_time = time.time()
        print("After view")
        print(f"Request took: {end_time - start_time} seconds")

        return result
    return middleware
