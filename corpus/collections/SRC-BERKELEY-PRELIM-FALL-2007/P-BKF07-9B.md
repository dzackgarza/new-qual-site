---
schema: qual/card@1
id: P-BKF07-9B
kind: problem
title: A holomorphic map with $\abs{f}\le1$ on the unit circle has a fixed point in the closed disk
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
    Independently checked the Rouché argument for the perturbed fixed-point
    equation and the compactness limit recovering a fixed point against the
    vendored solution.
---

::: {.problem}
Let \(f\) be holomorphic on a neighborhood of the closed unit disk
\[
\overline{B_1(0)}=\{z:|z|\le1\}.
\]
Suppose
\[
\max_{|z|=1}|f(z)|\le1.
\]
Prove that there exists \(z\) with \(|z|\le1\) such that
\[
f(z)=z.
\]
:::

::: {.solution}
For each integer $m\ge1$, set
$$
\alpha_m\coloneqq1+\frac1m
$$
and
$$
g_m(z)\coloneqq f(z)-\alpha_m z.
$$

<1>1. For every $m\ge1$, there exists $z_m$ with
$\abs{z_m}<1$ such that
$$
f(z_m)=\alpha_m z_m.
$$

::: {.proof}
On the unit circle,
$$
\abs{f(z)}\le1<\alpha_m=\abs{\alpha_m z}.
$$
Hence, by Rouché's theorem, the functions
$g_m(z)=f(z)-\alpha_m z$ and $-\alpha_m z$ have the same number of
zeros in the open unit disk, counted with multiplicity. The latter has
exactly one zero there. Therefore $g_m$ has a zero $z_m$ with
$\abs{z_m}<1$, and $g_m(z_m)=0$ is exactly
$f(z_m)=\alpha_m z_m$.
:::

<1>2. There are a subsequence $(z_{m_k})$ and a point $z$ with
$\abs{z}\le1$ such that
$$
z_{m_k}\longrightarrow z.
$$

::: {.proof}
Every $z_m$ lies in the closed unit disk, which is compact. Thus the
sequence $(z_m)$ has a convergent subsequence whose limit remains in
the closed unit disk.
:::

<1>3. The limit point $z$ from step <1>2 satisfies
$$
f(z)=z.
$$

::: {.proof}
Since $f$ is holomorphic on a neighborhood of the closed unit disk, it
is continuous there. Using step <1>1 along the subsequence from
step <1>2,
$$
\begin{aligned}
f(z)
&=\lim_{k\to\infty}f(z_{m_k})\\
&=\lim_{k\to\infty}\alpha_{m_k}z_{m_k}\\
&=1\cdot z=z,
\end{aligned}
$$
because $\alpha_m\to1$.
:::

<1>4. There exists $z$ with $\abs{z}\le1$ and
$$
\boxed{f(z)=z}.
$$

::: {.proof}
Step <1>2 gives $\abs{z}\le1$, and step <1>3 gives the fixed-point
identity.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
