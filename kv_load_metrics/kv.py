"""
Pad for Kunal Gupta - Evergreen - BLR SWE - L5 to L6 Infra

Suppose you are thinking of putting a key value store in your application. Before doing so, you want to measure the average load your system will take. Thus, you decide to create a “Mock” in-memory key value store (i.e. a hashmap) that can be queried for its load over time.

"""

import time

class InMemoryKV:
    """
    metrics = [a, b, c, d, e, ]
    get_arr = [(100, ts), (450, ts+x), (850, ts+2x)...]
    curr_ts = tx+2x+y (y < x)
    t = get_arr[-1][1]
    delta = (get_arr[-1][0]/x) * (curr_ts - t)
    self.get_counts + get_arr[-1]

    n = number of requests
    t = load time
    
    TC: get O(1), put O(1)
    get_load_for_gets = O(1) 
    get_

    window_max = 1hr - 3600 seconds
    window_size = k
    get_load_for_gets - O(k)
    get_load_for_puts - O(k)
    """
    def __init__(self, window = 5):
        self.store = {}
        self.window = window
        self.get_counts = 0
        self.put_counts = 0
        ## We will use a simple library that will perform the following every x seconds (default = 1)
        ## 1. extract get_counts and put_counts
        self.get_metrics = []
        self.put_metrics = []

    
    def get(self, key):
        self.get_counts += 1
        if key not in self.store:
            raise ValueError("Key not found")
        return self.store[key]
    
    def put(self, key, value):
        self.put_counts += 1
        self.store[key] = value
    
    def get_load_for_gets(self):
        lookback = time.time() - self.window
        total_load = 0
        for idx in range(len(self.get_metrics)-1, -1, -1):
            count, ts = self.get_metrics[idx]
            if ts < lookback:
                break
            total_load += count
        return total_load
    
    def get_load_for_puts(self):
        lookback = time.time() - self.window
        total_load = 0
        for idx in range(len(self.put_metrics)-1, -1, -1):
            count, ts = self.put_metrics[idx]
            if ts < lookback:
                break
            total_load += count
        return total_load


    def perform(self):
        self.get_metrics.append((self.get_counts, time.time()))
        self.put_metrics.append((self.put_counts, time.time()))
        self.get_counts = 0
        self.put_counts = 0
        lookback_ts = time.time() - self.window
        start_idx = 0
        for idx, (ct, ts) in enumerate(self.get_metrics):
            if ts >= lookback_ts:
                start_idx = idx
                break 
        self.get_metrics = self.get_metrics[start_idx:]
        for idx, (ct, ts) in enumerate(self.put_metrics):
            if ts >= lookback_ts:
                start_idx = idx
                break 
        self.put_metrics = self.put_metrics[start_idx:]

if __name__ == "__main__":
    start_ts = time.time()
    window_ts = start_ts
    update_ts = start_ts
    kv = InMemoryKV()
    k, v = 0, 0
    while True:
        if time.time() - start_ts >= 100:
            break
        if time.time() - window_ts >= 3:
            kv.perform()
            window_ts = time.time()
        if time.time() - update_ts >= 1:
            kv.put(k, v)
            k+=1
            v+=1
            kv.put(k, v)
            kv.get(k)
            update_ts = time.time()
        if (time.time() - start_ts) % 7 == 0:
            print(kv.get_load_for_gets())
            print(kv.get_load_for_puts())

        









