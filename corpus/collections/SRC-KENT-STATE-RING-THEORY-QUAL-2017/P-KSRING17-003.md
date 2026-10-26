---
schema: qual/card@1
id: P-KSRING17-003
kind: problem
title: Ideals of $\mathbb Z/90\mathbb Z$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 3 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
[NEW] How many ideals does the ring $\mathbb Z/90\mathbb Z$ have?
Explain your answer.
:::

::: pf

::: pf-step

Ideals of $\ZZ/90\ZZ$ are in bijection with positive divisors of $90$.


::: pf-proof

Let
$$
\pi:\ZZ\to\ZZ/90\ZZ
$$
be the quotient map. By the correspondence theorem, ideals of the quotient are in bijection with ideals
$$
J\subseteq\ZZ
$$
containing
$$
(90).
$$
Every ideal of $\ZZ$ is principal, say
$$
J=(d)
$$
with $d\ge0$. The inclusion
$$
(90)\subseteq(d)
$$
holds exactly when
$$
d\mid90.
$$
Under the quotient map, $(d)$ corresponds to the ideal
$$
(\overline d)
\subseteq
\ZZ/90\ZZ.
$$
Thus the ideals of $\ZZ/90\ZZ$ are parametrized by the positive divisors of $90$.

:::

:::

::: pf-step

The integer $90$ has exactly
$$
12
$$
positive divisors.


::: pf-proof

The prime factorization is
$$
90
=
2^1\cdot3^2\cdot5^1.
$$
Every positive divisor therefore has the form
$$
2^a3^b5^c
$$
where
$$
0\le a\le1,
\qquad
0\le b\le2,
\qquad
0\le c\le1.
$$
There are
$$
(1+1)(2+1)(1+1)
=
12
$$
choices.

:::

:::

::: pf-step

Hence
$$
\boxed{
\ZZ/90\ZZ
\text{ has exactly }12\text{ ideals.}
}
$$


::: pf-proof

Combine steps <1>1 and <1>2.

:::

:::

::: pf-qed

Step <1>3 answers the problem.

:::

:::
