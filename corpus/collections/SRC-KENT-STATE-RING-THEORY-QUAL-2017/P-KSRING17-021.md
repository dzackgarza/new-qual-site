---
schema: qual/card@1
id: P-KSRING17-021
kind: problem
title: An ideal is comaximal with the intersection of ideals comaximal to it
classification:
  areas: [algebra]
  topics:
  - Comaximal Ideals
  - Chinese Remainder Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 21 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source prints $I_i+\bigcap I_j=R$, which fails whenever $I_i\neq R$ because $\bigcap_j I_j\subseteq I_i$. The statement now intersects over $j\neq i$.
---

::: {.problem}
Let $R$ be a commutative ring with identity and let $I_{1}, I_{2}, \ldots, I_{n}$ be pairwise comaximal ideals of $R$ (i.e., $I_{i} + I_{j} = R$ if $i \neq j$). Show that $I_{i} + \bigcap_{j \neq i} I_{j} = R$ for all $i$.
:::

::: {.solution}

Fix
$$
i\in\{1,\ldots,n\}.
$$

::: pf

::: {.pf-step #s1-1}

For each
$$
j\ne i,
$$
there exist
$$
a_j\in I_i,
\qquad
b_j\in I_j
$$
such that
$$
a_j+b_j=1.
$$

::: pf-proof

Pairwise comaximality gives
$$
I_i+I_j=R
$$
for every $j\ne i$. Hence
$$
1\in I_i+I_j,
$$
so one can write
$$
1=a_j+b_j
$$
with
$$
a_j\in I_i,
\qquad
b_j\in I_j.
$$

:::

:::

::: {.pf-step #s1-2}

Define
$$
b
\coloneqq
\prod_{j\ne i}b_j.
$$
Then
$$
b\in\bigcap_{j\ne i}I_j.
$$

::: pf-proof

Fix
$$
k\ne i.
$$
The product defining $b$ contains the factor
$$
b_k\in I_k.
$$
Since $I_k$ is an ideal, multiplying $b_k$ by the remaining factors keeps the result in $I_k$. Therefore
$$
b\in I_k.
$$
As this holds for every $k\ne i$,
$$
b\in\bigcap_{j\ne i}I_j.
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
1-b\in I_i.
$$

::: pf-proof

By step [](#s1-1){.pf-ref},
$$
b_j
=
1-a_j
\equiv
1
\pmod{I_i}
$$
for every $j\ne i$. Therefore
$$
b
=
\prod_{j\ne i}b_j
\equiv
1
\pmod{I_i}.
$$
Hence
$$
1-b\in I_i.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
I_i
+
\bigcap_{j\ne i}I_j
=
R.
}
$$

::: pf-proof

By step [](#s1-2){.pf-ref},
$$
b\in\bigcap_{j\ne i}I_j,
$$
and by step [](#s1-3){.pf-ref},
$$
1-b\in I_i.
$$
Thus
$$
1
=
(1-b)+b
\in
I_i+\bigcap_{j\ne i}I_j.
$$
Any ideal containing $1$ is the whole ring, so the sum equals $R$.

:::

:::

::: pf-qed

The index $i$ was arbitrary, so step [](#s1-4){.pf-ref} proves the conclusion for every $i$.

:::

:::

:::
