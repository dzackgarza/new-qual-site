---
schema: qual/card@1
id: P-AMH-ALG-SG16-21
kind: problem
title: Quotients by ideals containing all commutators are commutative
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
Let $I\subseteq R$ be an ideal of $R$, and suppose that $xy-yx\in I$ for every $x,y\in R$.
Prove that the quotient ring $R/I$ is commutative.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
For all $a,b\in R$,
$$
I+ab=I+ba
$$
in the quotient ring $R/I$.

::: pf-proof
By hypothesis,
$$
ab-ba\in I.
$$
Two elements of $R$ determine the same coset modulo $I$ exactly when their
difference lies in $I$.  Hence $ab$ and $ba$ determine the same coset:
$$
I+ab=I+ba.
$$
:::

:::

::: {.pf-step #s1-2}
Multiplication in $R/I$ is commutative.

::: pf-proof
Let $I+a,I+b\in R/I$.  Using the definition of multiplication in the quotient
ring and step [](#s1-1){.pf-ref},
$$
\begin{aligned}
(I+a)(I+b)
&=I+ab\\
&=I+ba\\
&=(I+b)(I+a).
\end{aligned}
$$
Thus any two elements of $R/I$ commute.
:::

:::

::: pf-step
Therefore
$$
\boxed{R/I\text{ is commutative}.}
$$

::: pf-proof
This is exactly the conclusion of step [](#s1-2){.pf-ref}.
:::

:::

:::

:::
