---
schema: qual/card@1
id: P-BKF07-6A
kind: problem
title: Count zeros of a quartic in an annulus
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Rouche count on |z|=1 and the direct
    nonvanishing estimate on |z|<=1/2.
---

::: {.problem}
Let
\[
f(z)=z^4+\frac{z^3}{4}-\frac14.
\]
How many zeros does \(f\) have in
\[
\left\{z\in\mathbb C:\frac12<|z|<1\right\}?
\]
:::

::: {.solution}
<1>1. The polynomial $f$ has exactly four zeros, counted with
multiplicity, in the disk $\abs z<1$.

::: {.proof}
On $\abs z=1$,
$$
\begin{aligned}
\abs{f(z)-z^4}
&=
\left|\frac{z^3}{4}-\frac14\right|
\\
&\le
\frac14+\frac14
\\
&=
\frac12
<
1
=
\abs{z^4}.
\end{aligned}
$$
By Rouché's theorem, $f$ and $z^4$ have the same number of zeros in
$\abs z<1$. The polynomial $z^4$ has four zeros there, counted with
multiplicity.
:::

<1>2. The polynomial $f$ has no zero in the closed disk
$$
\abs z\le\frac12.
$$

::: {.proof}
If $\abs z\le1/2$, then the reverse triangle inequality gives
$$
\begin{aligned}
\abs{f(z)}
&=
\left|z^4+\frac{z^3}{4}-\frac14\right|
\\
&\ge
\frac14-\abs z^4-\frac{\abs z^3}{4}
\\
&\ge
\frac14-\frac1{16}-\frac1{32}
\\
&=
\frac5{32}
>
0.
\end{aligned}
$$
Thus $f(z)\ne0$ throughout the closed disk.
:::

<1>3. Every zero of $f$ in the unit disk lies in the annulus
$$
\frac12<\abs z<1.
$$

::: {.proof}
Step <1>2 excludes all zeros with $\abs z\le1/2$, while step <1>1
counts the zeros with $\abs z<1$. Hence the four zeros counted in
step <1>1 all lie in the stated annulus.
:::

<1>4. Therefore the number of zeros in the annulus, counted with
multiplicity, is
$$
\boxed{4}.
$$

::: {.proof}
This is exactly the count from step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 answers the problem.
:::
:::
