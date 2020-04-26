def merge_intervals(ranges):
    start_time = -1
    end_time = -1
    ranges.append([25, 25])
    merged_ranges = []
    
    for range in ranges:
        if start_time == -1:
            start_time = range[0]
            end_time = range[1]
            continue
        if range[0] > end_time: 
            merged_ranges.append([start_time, end_time])
            start_time, end_time = (range[0], range[1])
            continue
        if range[0] < start_time:
            start_time = range[0]
        if range[1] > end_time:
            end_time = range[1]
        
    
    return merged_ranges

ranges = [[1,4], [2,5], [7,10], [12, 16]]
print(merge_intervals(ranges))

