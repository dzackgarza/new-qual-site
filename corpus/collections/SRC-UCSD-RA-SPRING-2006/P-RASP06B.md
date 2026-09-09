---
schema: qual/card@1
id: P-RASP06B
kind: problem
title: "Absolutely continuous functions with L^1 convergent derivatives"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Spring 2006 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\{f_j\}$ be a sequence of functions in $AC([0,1])$ such that $f_j' \to g$ in $L^1([0,1], dx)$ and $\lim_{j \to \infty} f_j(0) = c$.

(a) Show that $f(x) = \lim_{j \to \infty} f_j(x)$ exists for all $x \in [0,1]$.

(b) Show that $f \in AC([0,1])$ and $f' = g$ a.e. ($m$).
:::

::: solution
<1>1. Identify the pointwise limit explicitly.
::: proof
Since each $f_j$ is absolutely continuous,
\[
f_j(x)=f_j(0)+\int_0^x f_j'(t)\,dt.
\]
Define
\[
F(x):=c+\int_0^x g(t)\,dt.
\]
Then for every $x\in[0,1]$,
\[
\begin{aligned}
|f_j(x)-F(x)|
&\le |f_j(0)-c|
+\left|\int_0^x(f_j'(t)-g(t))\,dt\right|\\
&\le |f_j(0)-c|+\|f_j'-g\|_1.
\end{aligned}
\]
The right side tends to $0$, independently of $x$. Hence $f_j\to F$ uniformly, so the pointwise limit exists everywhere and
\[
\boxed{f(x)=c+\int_0^x g(t)\,dt.}
\]
:::

<1>2. Prove absolute continuity and identify the derivative.
::: proof
Because $g\in L^1([0,1])$, the function
\[
x\longmapsto c+\int_0^x g(t)\,dt
\]
is absolutely continuous. By the Lebesgue Fundamental Theorem of Calculus,
\[
f'(x)=g(x)
\]
for almost every $x\in[0,1]$. Thus
\[
\boxed{f\in AC([0,1]),\qquad f'=g\text{ a.e.}}
\]
as required.
:::
:::
