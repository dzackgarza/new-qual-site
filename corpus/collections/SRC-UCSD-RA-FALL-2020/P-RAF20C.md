---
schema: qual/card@1
id: P-RAF20C
kind: problem
title: "Strict inequality for Fourier transform of positive L^1 function"
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
  note: Checked against Problem 3 of the official UCSD Fall 2020 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f \in L^1(\mathbb{R}^n)$ and $f > 0$ in $\mathbb{R}^n$.
Prove that the strict inequality $|\hat{f}(\xi)| < \hat{f}(0)$ holds for any $\xi \in \mathbb{R}^n$ with $\xi \neq 0$.
:::

::: solution
<1>1. Start from the ordinary Fourier-transform bound.
::: proof
Since $f>0$ and $f\in L^1(\mathbb R^n)$,
\[
\widehat f(0)=\int_{\mathbb R^n}f(x)\,dx>0.
\]
For any $\xi$,
\[
|\widehat f(\xi)|
=\left|\int f(x)e^{-i x\cdot\xi}\,dx\right|
\le \int f(x)\,dx
=\widehat f(0),
\]
with the harmless modification of the phase if a different Fourier normalization is used.
:::

<1>2. Analyze the equality case.
::: proof
Suppose for contradiction that $\xi\ne0$ and
\[
|\widehat f(\xi)|=\widehat f(0).
\]
Let
\[
c:=\frac{\widehat f(\xi)}{|\widehat f(\xi)|},
\qquad |c|=1.
\]
Then
\[
\begin{aligned}
\widehat f(0)
&=\operatorname{Re}\left(\overline c\,\widehat f(\xi)\right)\\
&=\int_{\mathbb R^n} f(x)\operatorname{Re}\left(\overline c\,e^{-ix\cdot\xi}\right)\,dx.
\end{aligned}
\]
Since
\[
\operatorname{Re}\left(\overline c\,e^{-ix\cdot\xi}\right)\le1
\]
everywhere and $f>0$, equality of the integrals forces
\[
\operatorname{Re}\left(\overline c\,e^{-ix\cdot\xi}\right)=1
\]
for almost every $x$. Hence
\[
e^{-ix\cdot\xi}=c
\]
for almost every $x$.
:::

<1>3. Rule out constant phase at nonzero frequency.
::: proof
For fixed $\xi\ne0$ and fixed $c\in\mathbb C$ with $|c|=1$, the set
\[
\{x\in\mathbb R^n:e^{-ix\cdot\xi}=c\}
\]
is a countable union of affine hyperplanes perpendicular to $\xi$. It therefore has Lebesgue measure zero.

Thus the phase cannot equal the constant $c$ almost everywhere. This contradicts Step 2. Hence
\[
\boxed{|\widehat f(\xi)|<\widehat f(0)\quad\text{for every }\xi\ne0.}
\]
:::
:::
