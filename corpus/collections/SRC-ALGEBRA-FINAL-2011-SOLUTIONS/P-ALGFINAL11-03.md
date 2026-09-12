---
schema: qual/card@1
id: P-ALGFINAL11-03
kind: problem
title: Irreducible but nonprime elements in Z[sqrt(-5)]
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Prove that in $\mathbb { Z } [ { \sqrt { - 5 } } ]$ , 7 is irreducible but not prime.

[10]

(b) Is $\mathbb { Z } [ { \sqrt { - 5 } } ]$ a Principal Ideal Domain?
(Justify your answer.)

[5]
:::

::: {.solution}
(a) By substituting $y$ for $\bar { x }$ in (a) and (b) of problem 2, one sees that $N ( x y ) = N ( x ) N ( y )$ . (You could also just say this was proved—differently—in class.)

If $7 = x y$ with neither x nor y a unit, then $N ( 7 ) = 4 9 = N ( x ) N ( y )$ , and since $N ( x ) > 1$ $N ( y ) > 1$ (cf.
problem 2), therefore $N ( x ) = N ( y ) = 7$ . But this can’t be, since $a ^ { 2 } + 5 b ^ { 2 } = 7$ has no integer solution.
Thus 7 is irreducible.

On the other hand, 7 divides $( 3 + { \sqrt { - 5 } } ) ( 3 - { \sqrt { - 5 } } )$ without dividing either factor; so 7 is not prime.

(b) $\mathbb { Z } [ { \sqrt { - 5 } } ]$ is not a Principal Ideal Domain, because Principal Ideal Domains are Unique Factorization Domains, rings in which irreducible elements are always prime.
:::
