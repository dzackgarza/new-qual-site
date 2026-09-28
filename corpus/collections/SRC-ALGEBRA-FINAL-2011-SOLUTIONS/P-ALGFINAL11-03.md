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
(a) By substituting $y$ for $\bar x$ in parts (a) and (b) of [[P-ALGFINAL11-02]], $N(xy) = N(x)N(y)$.

If $7 = xy$ with neither $x$ nor $y$ a unit, then $N(7) = 49 = N(x)N(y)$, and since $N(x) > 1$ and $N(y) > 1$ (units have norm $1$ by [[P-ALGFINAL11-02]]), $N(x) = N(y) = 7$. But $a^2 + 5b^2 = 7$ has no integer solution.
Thus $7$ is irreducible.

On the other hand, $7$ divides $(3 + \sqrt{-5})(3 - \sqrt{-5}) = 14$ without dividing either factor; so $7$ is not prime.

(b) $\mathbb Z[\sqrt{-5}]$ is not a principal ideal domain, because principal ideal domains are unique factorization domains, rings in which irreducible elements are always prime.
:::
