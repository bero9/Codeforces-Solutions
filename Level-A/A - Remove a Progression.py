"""
Problem Name: A. Remove a Progression
Platform: Codeforces
Approach: Math / Pattern Recognition
Time Complexity: O(1) per testcase

Description:
When repeatedly removing the i-th element from an array [1..n], 
the surviving elements form a sequence of even numbers (2, 4, 6...).
Therefore, the value at the x-th position in the remaining array is simply 2 * x.
The variable 'n' is entirely irrelevant to the final output.
"""

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx]) # قراءة طول المصفوفة (لا نستخدمه فعلياً في الحل)
        idx += 1
        x = int(input_data[idx]) # قراءة الترتيب المطلوب
        idx += 1
        
        # النمط الرياضي المباشر
        out.append(str(2 * x))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()