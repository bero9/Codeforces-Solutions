import sys

def solve():
    # 1. استخدام القراءة السريعة (Fast I/O) لتجنب الـ TLE بسبب كثرة المدخلات
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        segments = []
        # 2. قراءة الفترات وتخزينها مع "رقمها الأصلي" (Index)
        for i in range(n):
            l = int(input_data[idx])
            r = int(input_data[idx+1])
            idx += 2
            segments.append((l, r, i))
            
        # 3. الترتيب مرة واحدة فقط خارج حلقة المقارنات!
        # بايثون سيقوم بترتيبها تصاعدياً بناءً على قيمة l (الطرف الأيسر)
        segments.sort()
        
        # مصفوفة الإجابات لتخزين النتيجة (1 أو 2) بنفس الترتيب الأصلي
        ans = [0] * n
        
        # 4. الفترة الأولى (بعد الترتيب) نضعها دائماً في المجموعة 1
        max_r = segments[0][1]
        ans[segments[0][2]] = 1
        
        possible = False
        
        # 5. المرور على باقي الفترات لمرة واحدة فقط O(N)
        for i in range(1, n):
            l = segments[i][0]
            r = segments[i][1]
            original_idx = segments[i][2]
            
            # إذا كانت بداية الفترة الحالية تتقاطع مع أقصى يمين المجموعة الأولى
            if l <= max_r:
                ans[original_idx] = 1
                max_r = max(max_r, r) # تمديد حدود المجموعة الأولى
            else:
                # إذا لم تتقاطع، فقد وجدنا فجوة! 
                # هذا يعني أن هذه الفترة وكل الفترات التي تليها يمكن وضعها في المجموعة 2 بأمان
                possible = True
                for j in range(i, n):
                    ans[segments[j][2]] = 2
                break # نوقف البحث لأننا قمنا بتوزيع المجموعتين بنجاح
                
        # 6. التحقق النهائي وإضافة النتيجة
        if possible:
            out.append(" ".join(map(str, ans)))
        else:
            out.append("-1")
            
    # طباعة كل النتائج دفعة واحدة
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()