---
schema: qual/card@1
id: P-RAF24D
kind: problem
title: No uniform rate in the Riemann–Lebesgue lemma on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Integrals
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Fall 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Recall that the Riemann–Lebesgue lemma implies that for all $f \in L^1([0,1], m)$,
\[
\lim_{n \to \infty} \int_0^1 f(x) e^{inx}\, dx = 0.
\]
Show that there is no rate of convergence for the above limit that is independent of $f$.
Specifically, show that there cannot exist any sequence of positive numbers $(a_n)$ such that $a_n \to \infty$ and for every $f \in L^1([0,1], m)$ there is a constant $C_f < \infty$ with
\[
\left| \int_0^1 f(x) e^{inx}\, dx \right| \le \frac{C_f}{a_n}
\quad\text{for each } n \in \mathbb{N}.
\]
Hint: If such $(a_n)$ existed, find a sequence of linear functionals that yields a contradiction.
:::

::: solution
<1>1. Assume a uniform rate exists and define the associated functionals.
::: proof
Suppose there were positive numbers $a_n\to\infty$ such that for every $f\in L^1([0,1])$ there is $C_f<\infty$ with
\[
\left|\int_0^1 f(x)e^{inx}\,dx\right|
\le \frac{C_f}{a_n}
\qquad\text{for every }n.
\]
Define
\[
T_n:L^1([0,1])\to\mathbb C,
\qquad
T_n(f):=a_n\int_0^1f(x)e^{inx}\,dx.
\]
Each $T_n$ is a bounded linear functional.
:::

<1>2. The family is pointwise bounded.
::: proof
For every fixed $f\in L^1([0,1])$, the assumed estimate gives
\[
|T_n(f)|
\le C_f
\qquad\text{for every }n.
\]
Hence
\[
\sup_n|T_n(f)|<\infty
\qquad\text{for every }f\in L^1([0,1]).
\]
Since $L^1([0,1])$ is Banach, the Uniform Boundedness Principle implies
\[
\sup_n\|T_n\|<\infty.
\]
:::

<1>3. Compute the operator norms and obtain the contradiction.
::: proof
The functional
\[
f\longmapsto\int_0^1f(x)e^{inx}\,dx
\]
is represented by the $L^\infty$ function $e^{inx}$, whose essential supremum norm is $1$. Therefore
\[
\|T_n\|=a_n.
\]
But $a_n\to\infty$, contradicting Step 2.

Hence no sequence $(a_n)$ with the stated property can exist. Equivalently, the Riemann--Lebesgue lemma admits no convergence rate uniform over all $f\in L^1([0,1])$.
:::
:::
