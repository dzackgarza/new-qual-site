---
schema: qual/card@1
id: P-T7IKN
kind: problem
title: Nonempty closed convex sets in a Hilbert space have unique minimum-norm points
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
  date: 2026-09-09
  note: Checked against Problem 4 of the September 4, 2019 JHU Analysis Qualifying Exam appearance in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "The retained September 2019 Real Analysis 4 statement omits nonemptiness, although the existing proof assumes it; the empty set is a counterexample to the unqualified statement."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Retained the complete parallelogram-identity proof, reconciled its hypothesis with the statement and title, and justified existence of the minimizing sequence."
---

::: {.problem}
Prove that every nonempty closed convex subset of a Hilbert space has a unique element of minimal norm.
:::

::: {.remark}
Nonemptiness is necessary: the empty set is closed and convex but has no element of minimal norm.
:::

::: {.solution}
<1>1. Choose a minimizing sequence.
::: {.proof}
Let $C$ be a nonempty closed convex subset of a Hilbert space $H$, and set
\[
d:=\inf_{x\in C}\|x\|.
\]
Nonemptiness gives $0\leq d<\infty$. By the defining
property of the infimum, choose $x_n\in C$ with
$d\leq\|x_n\|<d+1/n$. Then
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
\left\|\frac{x_n-x_m}{2}\right\|^2
=\frac12\|x_n\|^2+\frac12\|x_m\|^2
-\left\|\frac{x_n+x_m}{2}\right\|^2.
\]
Therefore
\[
\frac14\|x_n-x_m\|^2
\le
\frac12\|x_n\|^2+\frac12\|x_m\|^2-d^2.
\]
The right-hand side tends to $0$ as $m,n\to\infty$. Hence $(x_n)$ is Cauchy.
:::

<1>3. Obtain existence of a minimum-norm point.
::: {.proof}
Since $H$ is complete, $x_n\to x$ for some $x\in H$. Because $C$ is closed,
\[
x\in C.
\]
Continuity of the norm gives
\[
\|x\|=d.
\]
Thus $x$ has minimal norm in $C$.
:::

<1>4. Prove uniqueness.
::: {.proof}
Suppose $x,y\in C$ both satisfy
\[
\|x\|=\|y\|=d.
\]
Again $(x+y)/2\in C$, hence
\[
\left\|\frac{x+y}{2}\right\|\ge d.
\]
The parallelogram identity gives
\[
\frac14\|x-y\|^2
=\frac12d^2+\frac12d^2
-\left\|\frac{x+y}{2}\right\|^2
\le0.
\]
Therefore $x=y$.

Hence every nonempty closed convex subset of a Hilbert space has a unique element of minimal norm.
:::
:::
