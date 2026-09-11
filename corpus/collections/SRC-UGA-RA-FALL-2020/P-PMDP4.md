---
schema: qual/card@1
id: P-PMDP4
kind: problem
title: $F(y)=\int f(x)\cos(yx)\,dx$ is $C^1$ when $f,xf\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 4 of the official UGA Fall 2020 Real Analysis qualifying examination DOCX. The source assumes only xf in L1; that hypothesis is insufficient to define F(0), so the card correctly retains the repaired assumption f, xf in L1.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: "The stated hypothesis xf in L1 alone is insufficient: f(x)=x^{-1}1_(0,1) has xf in L1 but F(0) is undefined. The card is corrected to assume f and xf are in L1."
---

:::{.problem}
Prove that if $f,\,xf(x) \in L^1(\RR)$, then
\[
F(y) \da \int f(x)\cos(yx)\,dx
\]
defines a $C^1$ function.
:::

::: solution
For $y\in\mathbb R$ define
\[
F(y)=\int_{\mathbb R}f(x)\cos(yx)\,dx.
\]
This is well defined because $f\in L^1$.

Fix $y\in\mathbb R$. For $h\ne0$,
\[
\frac{F(y+h)-F(y)}{h}
=\int_{\mathbb R}f(x)
\frac{\cos((y+h)x)-\cos(yx)}{h}\,dx.
\]
For each $x$, the integrand tends to
\[
-xf(x)\sin(yx).
\]
By the mean value theorem,
\[
\left|\frac{\cos((y+h)x)-\cos(yx)}{h}\right|\le |x|,
\]
so the absolute value of the integrand is bounded by $|xf(x)|\in L^1$. Dominated convergence therefore gives
\[
F'(y)=-\int_{\mathbb R}xf(x)\sin(yx)\,dx.
\]

Now let $y_j\to y$. Then
\[
-xf(x)\sin(y_jx)\to -xf(x)\sin(yx)
\]
pointwise and is dominated by $|xf(x)|$. Another application of dominated convergence yields
\[
F'(y_j)\to F'(y).
\]
Thus $F'$ is continuous and
\[
\boxed{F\in C^1(\mathbb R).}
\]
:::
