n = input()
st = input()

lst = st.split()
lst = map(int, lst)

t = tuple(lst)
print(hash(t))
