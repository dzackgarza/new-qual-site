---
schema: qual/card@1
id: P-KSRING17-005
kind: problem
title: The unit group $U_{24}$ and whether it is cyclic
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 5 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
[NEW] Denote the set of invertible elements of the ring $\mathbb { Z } _ { n }$ by $U _ { n }$

(a) List all the elements of $U _ { 2 4 }$

(b) Is $U _ { 2 4 }$ a cyclic group under multiplication?
Justify your answer.
:::

::: {.solution}
<1>1. The unit group is
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

::: {.proof}
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

<1>2. Every element of $U_{24}$ has square equal to $\overline1$.

::: {.proof}
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

<1>3. The group $U_{24}$ is not cyclic.

::: {.proof}
By step <1>1,
$$
\abs{U_{24}}=8.
$$
A cyclic group of order $8$ must contain an element of order $8$. By step <1>2, every element of $U_{24}$ has order at most $2$. Therefore
$$
\boxed{
U_{24}\text{ is not cyclic.}
}
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 answers part (a), and step <1>3 answers part (b).
:::
:::
