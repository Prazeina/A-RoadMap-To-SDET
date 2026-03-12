import json

def analyze_performance(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    memory_samples = []
    for entry in data:
        memory_samples.append(entry['mem_rss_mb'])
    
    max_mem = 0
    for val in memory_samples:
        if val > max_mem:
            max_mem = val

    is_leaking = True 
    for i in range(len(memory_samples) - 1):
        if not (memory_samples[i] < memory_samples[i+1]):
            is_leaking = False
            break

    has_spike = False
    for i in range(len(memory_samples) - 1):
        if memory_samples[i+1] > (memory_samples[i] * 2):
            has_spike = True

    # Return a dictionary instead of a string (Easier for automation to read!)
    return {
        "is_leaking": is_leaking,
        "has_spike": has_spike,
        "max_mem": max_mem
    }