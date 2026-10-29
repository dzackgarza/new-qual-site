---
schema: qual/card@1
id: P-AMH-ALG-SG16-25
kind: problem
title: Ideals properly containing an ideal with field quotient contain 1
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Suppose that $R$ is commutative and has a multiplicative identity $1$.
Let $I\subseteq J\subseteq R$ be ideals, and suppose that the quotient ring $R/I$ is a field.
If $I\subsetneq J$, prove that $1\in J$.
[In fact, it is a Theorem from Math 350 that $J=R$ in this case, but you are only being asked to prove that $1\in J$. In particular, however, you may not quote the $J=R$ theorem.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
There exists $r\in J$ such that the coset $I+r$ is nonzero in $R/I$.

::: pf-proof
Because $I\subsetneq J$, choose
$$
r\in J\setminus I.
$$
The zero element of $R/I$ is the coset $I$.  Since $r\notin I$,
$$
I+r\neq I,
$$
so $I+r$ is nonzero.
:::

:::

::: {.pf-step #s1-2}
There exists $s\in R$ such that
$$
I+rs=I+1.
$$

::: pf-proof
By hypothesis, $R/I$ is a field.  The nonzero element $I+r$ from step [](#s1-1){.pf-ref}
therefore has a multiplicative inverse.  Write that inverse as $I+s$ for some
$s\in R$.  Then
$$
(I+r)(I+s)=I+1.
$$
Multiplication in the quotient gives
$$
I+rs=I+1.
$$
:::

:::

::: {.pf-step #s1-3}
One has $1-rs\in J$.

::: pf-proof
The coset equality in step [](#s1-2){.pf-ref} is equivalent to
$$
1-rs\in I.
$$
Since $I\subseteq J$, it follows that $1-rs\in J$.
:::

:::

::: {.pf-step #s1-4}
One has $rs\in J$.

::: pf-proof
By step [](#s1-1){.pf-ref}, $r\in J$.  Since $J$ is an ideal and $s\in R$, the absorption
property gives
$$
rs\in J.
$$
:::

:::

::: pf-step
Therefore
$$
\boxed{1\in J}.
$$

::: pf-proof
By steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}, both $1-rs$ and $rs$ belong to $J$.  Since $J$ is
closed under addition,
$$
1=(1-rs)+rs\in J.
$$
:::

:::

:::

:::
