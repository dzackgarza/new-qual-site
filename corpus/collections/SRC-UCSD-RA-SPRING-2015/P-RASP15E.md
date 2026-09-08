---
schema: qual/card@1
id: P-RASP15E
kind: problem
title: "Integration by parts for functions of bounded variation"
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
  note: Checked against Problem 5 of the official UCSD Spring 2015 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f$ be a real-valued function of bounded variation on $\mathbb{R}$, and $g$ be a smooth function of compact support on $\mathbb{R}$.
Is the integration by parts
$$
\int_{-\infty}^{\infty} f(x) g'(x)\,dm(x) = -\int_{-\infty}^{\infty} f'(x) g(x)\,dm(x)
$$
always valid?

If yes, give a proof of it; if not, show a counterexample and find a condition under which it is valid (you need to justify your answer).
:::

::: solution
<1>1. The formula is not valid for every function of bounded variation.
::: proof
Let
\[
f(x)=\mathbf1_{[0,\infty)}(x).
\]
Then $f$ has bounded variation on $\mathbb R$, and its classical derivative satisfies
\[
f'(x)=0
\]
for almost every $x$.

Choose $g\in C_c^\infty(\mathbb R)$ with $g(0)\ne0$. Then
\[
\int_{-\infty}^{\infty}f(x)g'(x)\,dx
=\int_0^\infty g'(x)\,dx
=-g(0),
\]
because $g$ vanishes for large positive $x$. On the other hand,
\[
-\int_{-\infty}^{\infty}f'(x)g(x)\,dx=0.
\]
Thus the displayed identity fails whenever $g(0)\ne0$.
:::

<1>2. Explain the missing term for a general BV function.
::: proof
For a BV function, the distributional derivative $Df$ is a finite signed Radon measure, and the correct integration-by-parts identity is
\[
\int_{\mathbb R}f(x)g'(x)\,dx
=-\int_{\mathbb R}g\,d(Df).
\]
The absolutely continuous part of $Df$ is $f'(x)\,dx$, but $Df$ may also have jump and singular-continuous parts. In the Heaviside example,
\[
Df=\delta_0,
\]
which produces the missing term $-g(0)$.
:::

<1>3. Absolute continuity is a sufficient condition for the stated formula.
::: proof
Assume $f$ is absolutely continuous on $\mathbb R$; in fact it suffices that $f$ be absolutely continuous on an interval containing $\operatorname{supp}g$. Then
\[
f(b)-f(a)=\int_a^b f'(x)\,dx
\]
on every compact interval, and $Df=f'(x)\,dx$ there.

Choose $a<b$ so that $g$ is supported in $(a,b)$. The usual integration-by-parts formula for absolutely continuous functions gives
\[
\int_a^b f(x)g'(x)\,dx
=\bigl[f(x)g(x)\bigr]_a^b
-\int_a^b f'(x)g(x)\,dx.
\]
Since $g(a)=g(b)=0$, the boundary term vanishes. Hence
\[
\boxed{
\int_{-\infty}^{\infty}f(x)g'(x)\,dx
=-\int_{-\infty}^{\infty}f'(x)g(x)\,dx.}
\]
:::
:::
