---
schema: qual/card@1
id: P-BKF04-5B
kind: problem
title: Smallest field of characteristic $7$ containing a root of $x^{18}+x^{17}+\cdots+x+1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
What is the cardinality of the smallest field $F$ of characteristic $7$ such that the equation $x^{18}+x^{17}+\cdots+x+1=0$ has a solution $x\in F$?
:::

::: {.solution}
We have the identity

$$
(x-1)(x^{18}+x^{17}+\cdots+x+1)=x^{19}-1,
$$

and $x^{19}-1$ has no repeated factors over a field of characteristic $7$, since it has no factors in common with its derivative $19x^{18}$. So $1$ is not a root of $x^{18}+\cdots+x+1$, and the given condition is equivalent to the condition that the multiplicative group $F^*$ contain a nontrivial element of order dividing $19$. Since $19$ is prime and $F^*$ is a finite abelian group, this is equivalent to $19\mid\#F^*$. The size of $F$ is $7^m$ for some $m\geq1$, so the condition becomes $19\mid(7^m-1)$. We compute $7^2\equiv11\pmod{19}$ and $7^3\equiv1\pmod{19}$, so the smallest possible $m$ is $3$, and the smallest possible field $F$ satisfying the conditions is the field $\FF_{7^3}$ of $\boxed{7^3=343}$ elements.
:::
