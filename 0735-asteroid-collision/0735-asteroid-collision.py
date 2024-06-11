class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            stack.append(i)

            while len(stack) > 1 and stack[-1] < 0 < stack[-2]:
                right = stack.pop()
                left = stack.pop()

                if -right == left:
                    break
                elif -right > left:
                    stack.append(right)
                else:
                    stack.append(left)
        
        return stack