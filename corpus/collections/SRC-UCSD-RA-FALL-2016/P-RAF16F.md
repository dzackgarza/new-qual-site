---
schema: qual/card@1
id: P-RAF16F
kind: problem
title: "Vanishing of C^1 function from moment conditions"
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
  note: Checked against Problem 6 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f \in C^1([0,1])$ be such that $f(1) = 0$.
Assume
$$
\int_0^1 x^k f'(x)\,dx = 0 \qquad \forall k = 1, 2, \ldots.
$$
Prove that $f = 0$ identically on $[0,1]$.
:::

::: solution
<1>1. Convert the derivative moments into moments of $f$.
::: proof
Fix $k\ge1$. Integration by parts gives
\[
\int_0^1 x^k f'(x)\,dx
=\bigl[x^k f(x)\bigr]_0^1-k\int_0^1x^{k-1}f(x)\,dx.
\]
Because $f(1)=0$ and $k\ge1$, both boundary terms vanish. The hypothesis therefore implies
\[
\int_0^1x^{k-1}f(x)\,dx=0.
\]
Thus
\[
\int_0^1x^j f(x)\,dx=0
\qquad\text{for every }j\ge0.
\]
By linearity,
\[
\int_0^1 p(x)f(x)\,dx=0
\]
for every polynomial $p$.
:::

<1>2. Use polynomial density to test against $f$ itself.
::: proof
By the Weierstrass approximation theorem, there are polynomials $p_n$ such that
\[
\|p_n-f\|_\infty\longrightarrow0.
\]
Since $f$ is continuous, it is integrable, and
\[
\left|\int_0^1 f(x)(p_n(x)-f(x))\,dx\right|
\le \|p_n-f\|_\infty\int_0^1|f(x)|\,dx
\longrightarrow0.
\]
But Step 1 gives
\[
\int_0^1 f(x)p_n(x)\,dx=0
\]
for every $n$. Passing to the limit yields
\[
\int_0^1 f(x)^2\,dx=0.
\]
Hence $f=0$ almost everywhere. Since $f$ is continuous,
\[
\boxed{f\equiv0\text{ on }[0,1].}
\]
:::
:::
