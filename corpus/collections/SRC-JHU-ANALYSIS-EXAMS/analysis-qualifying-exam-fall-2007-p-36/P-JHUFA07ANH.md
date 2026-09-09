---
schema: qual/card@1
id: P-JHUFA07ANH
kind: problem
title: 'Compactly supported $L^1$ convolution need not be uniformly continuous'
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the JHU Analysis Qualifying Exam, Fall 2007, in the preserved exam compilation. The source asks for a proof that the convolution of two compactly supported L1 functions is uniformly continuous, but that claim is false as written; the card is corrected to ask for the validity of the claim.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose that $f,g\in L^1(\mathbb R)$ have compact support, and define
\[
h(x)=(f*g)(x)=\int_{\mathbb R} f(x-y)g(y)\,dy.
\]
The source asks to prove that $h$ is uniformly continuous. Is this claim true? Prove it or give a counterexample.
:::

::: {.solution}
<1>1. Choose compactly supported $L^1$ functions with an integrable singularity.
::: {.proof}
Let
\[
f(x)=g(x)=x^{-2/3}\mathbf 1_{(0,1)}(x).
\]
Then $f,g\in L^1(\mathbb R)$ because
\[
\int_0^1 x^{-2/3}\,dx=3<\infty,
\]
and both supports are contained in the compact interval $[0,1]$.
:::

<1>2. Compute the convolution near the origin.
::: {.proof}
For $0<x<1$, the integrand is nonzero exactly when $0<y<x$, so
\[
(f*g)(x)
=\int_0^x (x-y)^{-2/3}y^{-2/3}\,dy.
\]
With the substitution $y=xu$,
\[
(f*g)(x)
=x^{-1/3}\int_0^1 (1-u)^{-2/3}u^{-2/3}\,du.
\]
The integral is the finite positive beta value $B(1/3,1/3)$. Hence
\[
(f*g)(x)=B(1/3,1/3)x^{-1/3}
\qquad(0<x<1).
\]
Thus $(f*g)(x)\to\infty$ as $x\downarrow0$. In particular $f*g$ is not continuous, and therefore cannot be uniformly continuous.

So the source claim is false as stated.
:::
:::
