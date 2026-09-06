---
schema: qual/card@1
id: P-UCLA-RA-S10-07
kind: problem
title: A closed convex subset of a Hilbert space has a unique minimum-norm element
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Convex Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Restored official problem 7 of the UCLA Analysis Qualifying Exam, Spring 2010. The collection originally cross-referenced P-PCOHF, which lives in a JHU collection; that phantom pointer was removed in commit 21de3b779 without replacing the genuine UCLA source occurrence locally.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used a minimizing sequence and the parallelogram identity. Convexity makes midpoints admissible, forcing the minimizing sequence to be Cauchy; completeness and closedness give existence, and the same identity applied to two minimizers gives uniqueness. The statement requires E to be nonempty, as is standard in the projection theorem.
---

::: {.problem}
Let $H$ be a Hilbert space and let $E$ be a closed convex subset of $H$.
Prove that there exists a unique element $x\in E$ such that
\[
\|x\|=\inf_{y\in E}\|y\|.
\]
:::

::: {.solution}
If the empty set is admitted as a convex set, the printed statement requires the additional hypothesis $E\ne\varnothing$; otherwise there is no element whose norm can attain the infimum. We therefore prove the intended assertion for nonempty $E$.

Set
\[
d=\inf_{y\in E}\|y\|.
\]
Because $E$ is nonempty, $d<\infty$.

<1>1. There is a sequence $\{x_n\}\subseteq E$ such that
\[
\|x_n\|^2\longrightarrow d^2.
\]
::: {.proof}
For every $n\ge1$, by the definition of the infimum choose $x_n\in E$ with
\[
d\le \|x_n\|<d+\frac1n.
\]
Then $\|x_n\|\to d$, hence
\[
\|x_n\|^2\to d^2.
\]
:::

<1>2. The sequence $\{x_n\}$ is Cauchy in $H$.
::: {.proof}
For every $m,n$, convexity of $E$ gives
\[
\frac{x_n+x_m}{2}\in E.
\]
Therefore, by the definition of $d$,
\[
\left\|\frac{x_n+x_m}{2}\right\|\ge d.
\]
The parallelogram identity gives
\[
\|x_n-x_m\|^2
=2\|x_n\|^2+2\|x_m\|^2-\|x_n+x_m\|^2.
\]
Using
\[
\|x_n+x_m\|^2
=4\left\|\frac{x_n+x_m}{2}\right\|^2
\ge4d^2,
\]
we obtain
\[
0\le\|x_n-x_m\|^2
\le
2\|x_n\|^2+2\|x_m\|^2-4d^2.
\]
By <1>1, the right-hand side tends to $0$ as $m,n\to\infty$.
Hence $\{x_n\}$ is Cauchy.
:::

<1>3. There exists $x\in E$ with $\|x\|=d$.
::: {.proof}
Since $H$ is complete, <1>2 gives an element $x\in H$ such that
\[
x_n\longrightarrow x
\]
in norm.
The set $E$ is closed and every $x_n$ lies in $E$, so $x\in E$.
Norm is continuous, hence by <1>1,
\[
\|x\|=\lim_{n\to\infty}\|x_n\|=d.
\]
Thus the minimum norm is attained.
:::

<1>4. The minimum-norm element is unique.
::: {.proof}
Suppose $x,y\in E$ both satisfy
\[
\|x\|=\|y\|=d.
\]
By convexity,
\[
\frac{x+y}{2}\in E,
\]
so
\[
\left\|\frac{x+y}{2}\right\|\ge d.
\]
The parallelogram identity gives
\[
\begin{aligned}
\|x-y\|^2
&=2\|x\|^2+2\|y\|^2-\|x+y\|^2\\
&=4d^2-4\left\|\frac{x+y}{2}\right\|^2\\
&\le0.
\end{aligned}
\]
Since a squared norm is nonnegative,
\[
\|x-y\|^2=0,
\]
so $x=y$.
:::
:::
