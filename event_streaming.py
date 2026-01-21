"""
Given a stream of message with timestamp,return the valid message in the same order of input 
having conditions that any duplicate messages that are with in 10 sec should be 
discarded (message at t and t+10 both need to be discarded).
Input:
10 a
12 b 
13 a
15 c
15 b
22 a
30 b
35 a
35 c
....

Output:
15c
30b
35a
35c
...
"""

def process_events(events):
    processed_events = []
    event_map = {} ## event : ([timestamps], is_eligible)
    for ts, evt in events:
        if evt not in event_map:
            event_map[evt] = [[ts], True]
        else:
            if event_map[evt][0][-1] < ts - 10:
                if event_map[evt][1]:
                    event_map[evt][0].append(ts)
                else:
                    event_map[evt][0] = [ts]
                    event_map[evt][1] = True
            else:
                event_map[evt] = [[ts], False]
    for evt in event_map.keys():
        if event_map[evt][1]:
            for ts in event_map[evt][0]:
                processed_events.append([ts, evt])
    return list(sorted(processed_events, key = lambda x : x[0]))
    


if __name__ == "__main__":
    events = [[10, 'a'], [12, 'b'], [13, 'a'], [15, 'c'], [15, 'b'], [22, 'a'], [30, 'b'], [35, 'a'], [35, 'c']]
    processed_events = process_events(events)
    for ts, evt in processed_events:
        print(ts, evt)