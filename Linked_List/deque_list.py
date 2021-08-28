from collections import deque

l = deque(["1", "2", "3"])
print(l)

l.append("d")
l.appendleft("l")

print(l)

l.pop()
l.popleft()
print(l)

#implementing queue usinge deque

que = deque()
que.append("heena")
que.append("meeta")
que.append("simran")

print("queue is ", que)

que.popleft()
que.popleft()
print("After pop", que)

#implememting stack using deque

st = deque()
st.appendleft("utkarsh")
st.appendleft("mridul")
st.appendleft("ritesh")

print("stack is", st)

st.popleft()
print("st is", st)