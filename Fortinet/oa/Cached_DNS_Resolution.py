'''

'''

def getMinTime(cache_size, cache_time, server_time, urls):
    # This will store the URLs in the cache
    cache = []
    # This will store the times taken for each URL resolution
    times = []
    
    for url in urls:
        if url in cache:
            # If the URL is in the cache, it takes cache_time to resolve
            times.append(cache_time)
            # Move the URL to the end to represent recent usage
            cache.remove(url)
            cache.append(url)
        else:
            # If the URL is not in the cache, it takes server_time to resolve
            times.append(server_time)
            # If the cache is full, remove the oldest element
            if len(cache) >= cache_size:
                cache.pop(0)
            # Add the new URL to the cache
            cache.append(url)
    
    return times

# Example usage
cache_size = 3
cache_time = 2
server_time = 5
urls = ["http://www.hackerrank.com", "http://www.google.com", "http://www.yahoo.com", "http://www.hackerrank.com", "http://www.google.com", "http://www.yahoo.com"]
result = getMinTime(cache_size, cache_time, server_time, urls)
print(result)

