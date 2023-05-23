# def a(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return a(n-1) + a(n-2)
    
# for i in range(0,4):
#     print(a(i), end=" ")

# class AA:
#     def __init__(self, x=0):
#         self.x = x
#     def doit(self, x):
#         self.x = self.x+2

# class BB(AA):
#     def __init__(self, y=0):
#         super().__init__(4)
#         self.y = y
#     def doit(self):
#         self.y += 3

# def main():
#     obj = BB()
#     obj.doit()
#     print(obj.x, obj.y)
# main()

a = "Hello World"
vowels = ('a','e','i','o','u')
print([c for c in a if c in vowels])