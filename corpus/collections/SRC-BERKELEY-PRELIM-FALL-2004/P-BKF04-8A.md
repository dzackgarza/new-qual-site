---
schema: qual/card@1
id: P-BKF04-8A
kind: problem
title: A complex linear map with $\langle Tv,v\rangle=0$ for all $v$ is zero
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\langle\ ,\ \rangle$ be a positive-definite Hermitian inner product on a finite-dimensional complex vector space $V$. Suppose $T\colon V\to V$ is a $\mathbb{C}$-linear map such that $\langle Tv,v\rangle=0$ for all $v\in V$. Prove that $T=0$.
:::

::: {.solution}
Take the inner product linear in the first variable and conjugate-linear in the second. For $x,y\in V$, expanding

$$
\langle T(x+y),x+y\rangle-\langle Tx,x\rangle-\langle Ty,y\rangle=0
$$

yields

$$
\langle Tx,y\rangle+\langle Ty,x\rangle=0.
$$

Substituting $ix$ for $x$ yields

$$
i\langle Tx,y\rangle-i\langle Ty,x\rangle=0.
$$

These two equalities imply $\langle Tx,y\rangle=0$ for all $x,y\in V$. Taking $y=Tx$ gives $\langle Tx,Tx\rangle=0$. Since $\langle\ ,\ \rangle$ is positive-definite, $Tx=0$. This holds for all $x\in V$, so $T=0$.
:::

::: {.remark}
The argument does not use $\dim V<\infty$, so the conclusion holds for every complex inner product space $V$.
:::
