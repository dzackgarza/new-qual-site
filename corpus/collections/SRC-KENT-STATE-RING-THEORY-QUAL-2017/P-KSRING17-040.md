---
schema: qual/card@1
id: P-KSRING17-040
kind: problem
title: An ideal is prime if and only if the quotient is an integral domain
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 40 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with 1. Show that an ideal P of R is prime if and only if $R / P$ is an integral domain.
:::

::: pf

::: pf-step

Assume $P$ is prime. Then $R/P$ is nonzero.


::: pf-proof

A prime ideal is proper, so $P\ne R$. Hence $1+P\ne0+P$, and therefore $R/P$ is nonzero.

:::

:::

::: pf-step

If $(a+P)(b+P)=0+P$, then $a+P=0+P$ or $b+P=0+P$.


::: pf-proof

The product equality means $ab\in P$. Since $P$ is prime, $a\in P$ or $b\in P$. This is exactly $a+P=0+P$ or $b+P=0+P$.

:::

:::

::: pf-step

Therefore $R/P$ is an integral domain.


::: pf-proof

The quotient is a nonzero commutative ring with identity, and step <1>2 shows that the product of two nonzero classes is nonzero.

:::

:::

::: pf-step

Conversely, assume $R/P$ is an integral domain. Then $P$ is proper.


::: pf-proof

An integral domain is nonzero, so $R/P\ne0$. Hence $P\ne R$.

:::

:::

::: pf-step

If $ab\in P$, then $a\in P$ or $b\in P$.


::: pf-proof

From $ab\in P$ one gets
$$
(a+P)(b+P)=0+P
$$
in $R/P$. Since $R/P$ is an integral domain, one of the two factors is zero. Thus $a\in P$ or $b\in P$.

:::

:::

::: pf-step

Therefore $P$ is prime.


::: pf-proof

Step <1>4 gives properness, and step <1>5 gives the defining product condition for a prime ideal.

:::

:::

::: pf-step

Hence
$$
\boxed{
P\text{ is prime}
\iff
R/P\text{ is an integral domain}.
}
$$


::: pf-proof

Steps <1>1--<1>3 prove the forward implication, and steps <1>4--<1>6 prove the converse.

:::

:::

::: pf-qed

Step <1>7 is the required equivalence.

:::

:::
