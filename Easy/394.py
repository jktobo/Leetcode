class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        curr_str = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((curr_str, num))
                curr_str = ""
                num = 0
            elif char == ']':
                prev_str, repeat_times = stack.pop()
                curr_str = prev_str + curr_str * repeat_times
            else:
                curr_str += char
        
        return curr_str
