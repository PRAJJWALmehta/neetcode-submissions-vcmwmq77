class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        operators = set(['+', '-', '*', '/'])

        for val in tokens:
            if val in operators:
                b = st.pop()
                a = st.pop()
                res = 0

                match val:
                    case "+":
                        res = a + b
                    case "-":
                        res = a - b
                    case "*":
                        res = a*b
                    case "/":
                        res = a/b
                
                st.append(int(res))
            else:
                st.append(int(val))
        
        return st.pop()
    
            
                

