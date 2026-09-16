---
schema: qual/card@1
id: P-PCOHF
kind: problem
title: 'Every closed convex subset of a Hilbert space has a unique element of minimal norm'
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Real Analysis Problem 4 of the September 4, 2019 JHU analysis qualifying exam in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

4. Prove that every closed convex subset of a Hilbert space has a unique element of minimal norm.

## Part II. Complex Analysis

Choose three of four problems and show all work with each problem on a new page.

::: {.solution}
<1>1. Choose a minimizing sequence.
::: {.proof}
Let $C$ be a nonempty closed convex subset of a Hilbert space $H$, and set
\[
d:=\inf_{x\in C}\|x\|.
\]
Choose $x_n\in C$ so that
\[
\|x_n\|^2\longrightarrow d^2.
\]
:::

<1>2. Prove that the minimizing sequence is Cauchy.
::: {.proof}
By convexity,
\[
\frac{x_n+x_m}{2}\in C,
\]
so
\[
\left\|\frac{x_n+x_m}{2}\right\|\ge d.
\]
The parallelogram identity gives
\[
\|x_n-x_m\|^2
=2\|x_n\|^2+2\|x_m\|^2-\|x_n+x_m\|^2.
\]
Since
\[
\|x_n+x_m\|^2
=4\left\|\frac{x_n+x_m}{2}\right\|^2
\ge4d^2,
\]
we obtain
\[
\|x_n-x_m\|^2
\le2\|x_n\|^2+2\|x_m\|^2-4d^2.
\]
The right-hand side tends to $0$ as $m,n\to\infty$. Thus $(x_n)$ is Cauchy.
:::

<1>3. Obtain a minimum-norm point.
::: {.proof}
Since $H$ is complete, $x_n\to x$ for some $x\in H$. Since $C$ is closed, $x\in C$. Continuity of the norm gives
\[
\|x\|=\lim_n\|x_n\|=d.
\]
Thus $x$ has minimum norm in $C$.
:::

<1>4. Prove uniqueness.
::: {.proof}
Suppose $x,y\in C$ both satisfy
\[
\|x\|=\|y\|=d.
\]
Again $(x+y)/2\in C$, so its norm is at least $d$. The parallelogram identity yields
\[
\begin{aligned}
\|x-y\|^2
&=2\|x\|^2+2\|y\|^2-\|x+y\|^2\\
&\le4d^2-4d^2=0.
\end{aligned}
\]
Hence $x=y$. Therefore every nonempty closed convex subset of a Hilbert space has a unique element of minimum norm.
:::
:::
