---
schema: qual/card@1
id: P-AMH-ALG-SG16-22
kind: problem
title: Reduced quotient rings and radical ideals
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
A nonzero element $a$ of a ring is said to be nilpotent if there is a positive integer $n\ge 1$ such that $a^n=0$.
(The element $0$ itself is not said to be nilpotent.)
Let $R$ be a commutative ring, and let $I\subseteq R$ be an ideal.
Prove that the following two statements are equivalent.
(a) The quotient ring $R/I$ contains no nilpotents.
(b) For every element $b\in R$ such that $b^m\in I$ for some positive integer $m\ge 1$, we have $b\in I$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
Assume (a).  If $b^m\in I$ for some $b\in R$ and $m\geq1$, then
$b\in I$.

::: pf-proof
In the quotient ring,
$$
(I+b)^m=I+b^m=I,
$$
so the coset $I+b$ has a positive power equal to zero.  Under the convention in
the problem, either $I+b$ is the zero element or it is a nonzero nilpotent.
Condition (a) excludes the second possibility.  Hence
$$
I+b=I,
$$
which is equivalent to $b\in I$.
:::

:::

::: {.pf-step #s1-2}
Therefore (a) implies (b).

::: pf-proof
Step [](#s1-1){.pf-ref} proves condition (b) for every $b\in R$ and every positive integer
$m$ with $b^m\in I$.
:::

:::

::: {.pf-step #s1-3}
Assume (b).  Then $R/I$ contains no nonzero nilpotent element.

::: pf-proof
Suppose, for contradiction, that $I+b$ is a nonzero nilpotent element of
$R/I$.  Then for some $m\geq1$,
$$
(I+b)^m=I.
$$
Since $(I+b)^m=I+b^m$, equality of these cosets gives
$$
b^m\in I.
$$
Condition (b) then implies $b\in I$, so
$$
I+b=I,
$$
contradicting the assumption that $I+b$ is nonzero.
:::

:::

::: {.pf-step #s1-4}
Therefore (b) implies (a).

::: pf-proof
Step [](#s1-3){.pf-ref} says exactly that the quotient ring contains no nilpotents under the
problem's convention that nilpotent elements are required to be nonzero.
:::

:::

::: pf-step
Hence (a) and (b) are equivalent.

::: pf-proof
Step [](#s1-2){.pf-ref} proves $(a)\Rightarrow(b)$ and step [](#s1-4){.pf-ref} proves
$(b)\Rightarrow(a)$.
:::

:::

:::

:::
