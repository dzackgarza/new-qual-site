---
schema: qual/card@1
id: P-PRACT20-W6-27
kind: problem
title: "Week 6: Miscellaneous Topics, problem 27"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
What is the output of the following algorithms?

(A)
```text
a = 273
b = 110
while b > 0
    r = a (mod b)
    a = b
    b = r
    print r
end
```

(B)
```text
n = 88
i = 1
while i < n
    i = i+1
    k = n
    while k >= i
        if i=k then print i
        k = k - 1
    end
end
```

(C)
```text
n = 123456
while n > 0
    j = n (mod 100)
    print j
    n = floor(n/100)
end
```
:::
