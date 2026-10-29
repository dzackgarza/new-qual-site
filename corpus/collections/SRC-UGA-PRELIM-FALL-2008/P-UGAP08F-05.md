---
schema: qual/card@1
id: P-UGAP08F-05
kind: problem
title: Combine bases of subspaces with trivial intersection
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Suppose $U$ and $V$ are subspaces of a vector space $X$ with
$$
U\cap V=\{0\}.
$$
Define
$$
U+V=\{x\in X:x=u+v\text{ for some }u\in U,\ v\in V\}.
$$
If $\{u_1,\ldots,u_m\}$ is a basis for $U$ and $\{v_1,\ldots,v_n\}$ is a basis for $V$, prove that
$$
\{u_1,\ldots,u_m,v_1,\ldots,v_n\}
$$
is a basis for $U+V$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The set
$$
\mathcal B\coloneqq\{u_1,\ldots,u_m,v_1,\ldots,v_n\}
$$
spans $U+V$.


::: pf-proof

Let $x\in U+V$. By definition, there are $u\in U$ and $v\in V$ such that $x=u+v$. Since $\{u_1,\ldots,u_m\}$ is a basis of $U$ and $\{v_1,\ldots,v_n\}$ is a basis of $V$, there are scalars $a_1,\ldots,a_m,b_1,\ldots,b_n$ with
$$
u=\sum_{i=1}^m a_i u_i,
\qquad
v=\sum_{j=1}^n b_j v_j.
$$
Hence
$$
x=\sum_{i=1}^m a_i u_i+\sum_{j=1}^n b_j v_j,
$$
so $x$ lies in the span of $\mathcal B$.

:::

:::

::: {.pf-step #s1-2}

The set $\mathcal B$ is linearly independent.


::: pf-proof

Suppose
$$
\sum_{i=1}^m a_i u_i+\sum_{j=1}^n b_j v_j=0.
$$
Then
$$
\sum_{i=1}^m a_i u_i
=-
\sum_{j=1}^n b_j v_j.
$$
The left-hand side belongs to $U$ and the right-hand side belongs to $V$, so their common value lies in $U\cap V=\{0\}$. Thus
$$
\sum_{i=1}^m a_i u_i=0,
\qquad
\sum_{j=1}^n b_j v_j=0.
$$
Because the two original sets are bases, all $a_i$ and all $b_j$ are zero. Therefore $\mathcal B$ is linearly independent.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\{u_1,\ldots,u_m,v_1,\ldots,v_n\}}
$$
is a basis for $U+V$.


::: pf-proof

By step [](#s1-1){.pf-ref} the set spans $U+V$, and by step [](#s1-2){.pf-ref} it is linearly independent. These two properties are exactly the definition of a basis.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required conclusion.

:::

:::

:::
