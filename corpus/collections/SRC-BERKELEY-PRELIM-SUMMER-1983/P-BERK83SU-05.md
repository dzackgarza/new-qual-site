---
schema: qual/card@1
id: P-BERK83SU-05
kind: problem
title: Density of quotients from a slowly varying increasing sequence
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For a target x>1, choose n far enough out that every subsequent
    consecutive ratio b_{k+1}/b_k is close to 1, then take m minimal
    with b_m/b_n>=x. Minimality gives b_{m-1}/b_n<x, so b_m/b_n is at
    most one small consecutive-ratio factor above x. This approximates
    every x>1 arbitrarily closely.
---

::: {.problem}
Let $0<b_1<b_2<\cdots$ be real numbers such that
\[
b_n\to\infty,
\qquad
\frac{b_n}{b_{n+1}}\to1.
\]
Prove that
\[
\left\{\frac{b_m}{b_n}:1\le n<m\right\}
\]
is dense in $(1,\infty)$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

One has
$$
\frac{b_{n+1}}{b_n}\longrightarrow1.
$$

::: pf-proof

The hypotheses give
$$
\frac{b_n}{b_{n+1}}\longrightarrow1.
$$
All these numbers are positive, so taking reciprocals yields
$$
\frac{b_{n+1}}{b_n}
=
\left(\frac{b_n}{b_{n+1}}\right)^{-1}
\longrightarrow1.
$$

:::

:::

::: {.pf-step #s2}

Fix $x>1$ and $\varepsilon>0$. There is $N$ such that for every
$k\geq N$,
$$
1<\frac{b_{k+1}}{b_k}
<
1+\frac{\varepsilon}{x}.
$$

::: pf-proof

The lower inequality follows from the strict increase of $(b_k)$. The
upper inequality holds for all sufficiently large $k$ by step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

Fix any $n\geq N$. There exists a least integer $m>n$ such that
$$
\frac{b_m}{b_n}\geq x.
$$

::: pf-proof

Since $b_j\to\infty$ while $b_n$ is fixed,
$$
\frac{b_j}{b_n}\longrightarrow\infty
$$
as $j\to\infty$. Hence the set of integers $j>n$ satisfying
$$
\frac{b_j}{b_n}\geq x
$$
is nonempty and therefore has a least element $m$.

:::

:::

::: {.pf-step #s4}

For the indices $n<m$ from step [](#s3){.pf-ref},
$$
x
\leq
\frac{b_m}{b_n}
<
x+\varepsilon.
$$

::: pf-proof

The first inequality is the definition of $m$. By minimality,
$$
\frac{b_{m-1}}{b_n}<x.
$$
Since $m-1\geq n\geq N$, step [](#s2){.pf-ref} gives
$$
\frac{b_m}{b_{m-1}}
<
1+\frac{\varepsilon}{x}.
$$
Therefore
$$
\begin{aligned}
\frac{b_m}{b_n}
&=
\frac{b_m}{b_{m-1}}
\frac{b_{m-1}}{b_n}\\
&<
\left(1+\frac{\varepsilon}{x}\right)x\\
&=
x+\varepsilon.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

The set
$$
\left\{\frac{b_m}{b_n}:1\leq n<m\right\}
$$
is dense in $(1,\infty)$.

::: pf-proof

Given arbitrary $x>1$ and $\varepsilon>0$, step [](#s4){.pf-ref} produces an
element of the displayed set in
$$
[x,x+\varepsilon).
$$
Thus every point of $(1,\infty)$ can be approximated arbitrarily
closely by elements of the set, which is exactly density.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
