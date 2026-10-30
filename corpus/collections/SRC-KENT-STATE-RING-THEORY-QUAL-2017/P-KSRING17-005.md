---
schema: qual/card@1
id: P-KSRING17-005
kind: problem
title: The unit group $U_{24}$ and whether it is cyclic
classification:
  areas: [algebra]
  topics:
  - Units
  - Cyclic Groups
  - Integers Modulo n
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 5 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Denote the set of invertible elements of the ring $\ZZ_{n}$ by $U_{n}$.

(a) List all the elements of $U_{24}$.

(b) Is $U_{24}$ a cyclic group under multiplication? Justify your answer.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The unit group is
$$
\boxed{
U_{24}
=
\{
\overline1,
\overline5,
\overline7,
\overline{11},
\overline{13},
\overline{17},
\overline{19},
\overline{23}
\}.
}
$$


::: pf-proof

A residue class
$$
\overline a\in\ZZ/24\ZZ
$$
is invertible exactly when
$$
\gcd(a,24)=1.
$$
Since
$$
24=2^3\cdot3,
$$
the representatives between $0$ and $23$ relatively prime to $24$ are exactly
$$
1,5,7,11,13,17,19,23.
$$

:::

:::

::: {.pf-step #s1-2}

Every element of $U_{24}$ has square equal to $\overline1$.


::: pf-proof

Directly modulo $24$,
$$
\begin{aligned}
5^2&=25\equiv1,\\
7^2&=49\equiv1,\\
11^2&=121\equiv1,\\
13^2&=169\equiv1,\\
17^2&=289\equiv1,\\
19^2&=361\equiv1,\\
23^2&=529\equiv1.
\end{aligned}
$$
The identity also squares to itself. Hence every group element has order dividing $2$.

:::

:::

::: {.pf-step #s1-3}

The group $U_{24}$ is not cyclic.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\abs{U_{24}}=8.
$$
A cyclic group of order $8$ must contain an element of order $8$. By step [](#s1-2){.pf-ref}, every element of $U_{24}$ has order at most $2$. Therefore
$$
\boxed{
U_{24}\text{ is not cyclic.}
}
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), and step [](#s1-3){.pf-ref} answers part (b).

:::

:::

:::
