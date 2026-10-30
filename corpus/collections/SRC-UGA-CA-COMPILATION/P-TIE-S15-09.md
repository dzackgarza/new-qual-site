---
schema: qual/card@1
id: P-TIE-S15-09
kind: problem
title: Zeros of analytic functions accumulating at the boundary and the identity theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 9.
---

::: {.problem}
(1) Explicitly write down an example of a non-zero analytic function in $\abs{ z } < 1$ which has infinitely zeros in $\abs{ z } < 1$ .

(2) Why does not the phenomenon in (1) contradict the uniqueness theorem?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Define
$$
f(z)
\coloneqq
\sin\left(\frac1{1-z}\right).
$$
Then $f$ is analytic and nonzero on the unit disk.


::: pf-proof

For $\abs{z}<1$, one has $z\ne1$, so
$$
z\longmapsto\frac1{1-z}
$$
is holomorphic on the unit disk. Since $\sin$ is entire, their composition $f$ is holomorphic there.

The function is not identically zero; for example,
$$
f(0)=\sin(1)\ne0.
$$

:::

:::

::: {.pf-step #s1-2}

For every positive integer $n$,
$$
z_n
\coloneqq
1-\frac1{n\pi}
$$
lies in the unit disk and satisfies
$$
f(z_n)=0.
$$


::: pf-proof

Since $n\pi>1$,
$$
0
<
1-\frac1{n\pi}
<
1,
$$
so $\abs{z_n}<1$. Moreover,
$$
\frac1{1-z_n}
=
n\pi,
$$
and therefore
$$
f(z_n)
=
\sin(n\pi)
=0.
$$
The points $z_n$ are distinct, so this gives infinitely many zeros in the unit disk.

:::

:::

::: {.pf-step #s1-3}

The zeros $z_n$ accumulate only at the boundary point $1$:
$$
z_n\longrightarrow1.
$$


::: pf-proof

Since
$$
\frac1{n\pi}\longrightarrow0,
$$
the definition of $z_n$ gives
$$
z_n
=
1-\frac1{n\pi}
\longrightarrow1.
$$
The point $1$ is not contained in the open unit disk.

:::

:::

::: {.pf-step #s1-4}

This does not contradict the identity theorem.


::: pf-proof

The identity theorem says that a holomorphic function on a region is identically zero if its zeros have an accumulation point inside that region. By step [](#s1-3){.pf-ref}, the zero sequence constructed here accumulates at $1$, which lies on the boundary and not in the domain $\abs{z}<1$. Hence the hypothesis of the identity theorem is not satisfied.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give the requested nonzero analytic function with infinitely many zeros, and step [](#s1-4){.pf-ref} explains why there is no contradiction with uniqueness.

:::

:::

:::
