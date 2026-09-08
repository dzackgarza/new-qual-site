---
schema: qual/card@1
id: P-RAF04B
kind: problem
title: "Limit of the integral of g(x) sin^2(nx) as n goes to infinity"
classification:
  areas:
  - real-analysis
  topics:
  - Riemann-Lebesgue Lemma
  - L1 Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $g \in L^1(\mathbb{R}, m)$ be chosen so that $\int_\mathbb{R} g(x) \, dx = 3$.
Find, with justification, the following limit:
$$
\lim_{n \to \infty} \int_\mathbb{R} g(x) \sin^2(nx) \, dx.
$$
:::

::: solution
<1>1. Rewrite the oscillatory factor.
::: proof
The identity
\[
\sin^2(nx)=\frac{1-\cos(2nx)}2
\]
gives
\[
\int_{\mathbb R}g(x)\sin^2(nx)\,dx
=\frac12\int_{\mathbb R}g(x)\,dx
-\frac12\int_{\mathbb R}g(x)\cos(2nx)\,dx.
\]
The first integral is $3$, so it remains to control the oscillatory term.
:::

<1>2. Apply the Riemann--Lebesgue lemma.
::: proof
Because $g\in L^1(\mathbb R)$, the Riemann--Lebesgue lemma implies
\[
\int_{\mathbb R}g(x)e^{2inx}\,dx\longrightarrow0.
\]
Taking real parts yields
\[
\int_{\mathbb R}g(x)\cos(2nx)\,dx\longrightarrow0.
\]
Therefore
\[
\boxed{
\lim_{n\to\infty}\int_{\mathbb R}g(x)\sin^2(nx)\,dx=\frac32.}
\]
:::
:::
