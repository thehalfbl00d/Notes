call stack is just returning loops waiting for a value from the function it called.

recursion repeats code:

power algorithm:
```py
def power(x,y):
    if y == 0 or y ==1:
        return 1
    return x*power(x, y-1)

```

fibonnaci series:

```py
def fibonnaci:
    if x == 0 or x == 1:
        return 1
    else:
        return fibonnaci(x) + fibonnaci(x-1)
```

try making tree like diagram for this

# power hanoi game

can move the smallest disc, if current disc the smallest disk then move it, otherwise move things around.


