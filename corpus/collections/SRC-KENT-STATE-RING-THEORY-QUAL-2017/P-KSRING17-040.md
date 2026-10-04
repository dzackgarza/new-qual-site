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

::: {.solution}
<1>1. Assume $P$ is prime. Then $R/P$ is nonzero.

::: {.proof}
A prime ideal is proper, so $P\ne R$. Hence $1+P\ne0+P$, and therefore $R/P$ is nonzero.
:::

<1>2. If $(a+P)(b+P)=0+P$, then $a+P=0+P$ or $b+P=0+P$.

::: {.proof}
The product equality means $ab\in P$. Since $P$ is prime, $a\in P$ or $b\in P$. This is exactly $a+P=0+P$ or $b+P=0+P$.
:::

<1>3. Therefore $R/P$ is an integral domain.

::: {.proof}
The quotient is a nonzero commutative ring with identity, and step <1>2 shows that the product of two nonzero classes is nonzero.
:::

<1>4. Conversely, assume $R/P$ is an integral domain. Then $P$ is proper.

::: {.proof}
An integral domain is nonzero, so $R/P\ne0$. Hence $P\ne R$.
:::

<1>5. If $ab\in P$, then $a\in P$ or $b\in P$.

::: {.proof}
From $ab\in P$ one gets
$$
(a+P)(b+P)=0+P
$$
in $R/P$. Since $R/P$ is an integral domain, one of the two factors is zero. Thus $a\in P$ or $b\in P$.
:::

<1>6. Therefore $P$ is prime.

::: {.proof}
Step <1>4 gives properness, and step <1>5 gives the defining product condition for a prime ideal.
:::

<1>7. Hence
$$
\boxed{
P\text{ is prime}
\iff
R/P\text{ is an integral domain}.
}
$$

::: {.proof}
Steps <1>1--<1>3 prove the forward implication, and steps <1>4--<1>6 prove the converse.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required equivalence.
:::
:::
