---
schema: qual/card@1
id: P-BKF04-8A
kind: problem
title: UC Berkeley Fall 2004 prelim 8A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\langle ~ , ~ \rangle$ be a positive-definite Hermitian inner product on a finite-dimensional complex vector space V . Suppose $T \colon V \to V$ is a C-linear map such that $\langle T v , v \rangle = 0$ for all $v \in V$ Prove that $T = 0$
:::

::: {.solution}
For $x , y \in V$ , expanding

$$
\langle T ( x + y ) , ( x + y ) \rangle - \langle T x , x \rangle - \langle T y , y \rangle = 0
$$

yields

$$
\langle T x , y \rangle + \langle T y , x \rangle = 0 .
$$

Substituting ix for x yields

$$
i \langle T x , y \rangle - i \langle T y , x \rangle = 0 .
$$

The previous two equalities imply $\langle T x , y \rangle = 0$ for all $x , y \in V$ . Taking $y = T x$ , we get $\langle T x , T x \rangle = 0$ . Since $\langle ~ , ~ \rangle$ is positive-definite, we get $T x = 0$ . This holds for all $x \in V$ , so $T = 0$

Remark: this proof works even when V is infinite-dimensional.
:::
