class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i == ']':
                string = ''

                while True:
                    x = stack.pop()

                    if x == '[':
                        cnt = ''
                        while stack and stack[-1].isnumeric():
                            cnt = stack.pop() + cnt
                        string = string * int(cnt)
                        stack.append(string)
                        break
                    else:
                        string = x + string

            else:
                stack.append(i)
        
        return "".join(stack)