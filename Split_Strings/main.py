def solution(s):
    res = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(s) % 2 != 0: res[-1] += "_"
    return res