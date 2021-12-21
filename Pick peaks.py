# Pick peaks

def pick_peaks(arr):
    peaks = {"pos": [], "peaks": []}
    for (pos, val) in enumerate(arr[1:-1], 1):
        if arr[pos-1] < val > arr[pos+1]:
            peaks["pos"].append(pos)
            peaks["peaks"].append(val)
        if arr[pos-1] < val and val == arr[pos+1]:
            for i in arr[pos:]:
                if i < val:
                    peaks["pos"].append(pos)
                    peaks["peaks"].append(val)
                    break
                if i > val:
                    break
    return peaks