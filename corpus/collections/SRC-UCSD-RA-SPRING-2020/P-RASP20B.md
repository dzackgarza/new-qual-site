---
schema: qual/card@1
id: P-RASP20B
kind: problem
title: "Calculations: convolution limit, Lebesgue-Stieltjes measure, and oscillatory integral"
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
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Spring 2020 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
(1) Let $f \in L^\infty(\mathbb{R})$ and $g \in L^1(\mathbb{R})$.
Assume that $f$ is continuous at $x = 1$ with $f(1) = \pi$ and that $g \geq 0$ on $\mathbb{R}$ and $\|g\|_{L^1(\mathbb{R})} = 2$.
Calculate
$$
\lim_{k \to +\infty} \int_{[-k,k]} f\!\left(1 + \frac{x^2}{k}\right) g(x)\,dm(x).
$$

(2) Let $\mu$ be the Lebesgue-Stieltjes measure associated to $F(x) = \begin{cases} 0 & x < 0, \\ x+2 & 0 \leq x < 1, \\ 4x^2 & 1 \leq x < \infty. \end{cases}$ Calculate $\mu((-\infty, 0])$, $\mu(\{1\})$, and $\mu([1,2])$.

(3) Let $E$ be a Lebesgue-measurable subset of $[0,1]$ with $m(E) = 1/2$.
Let $u_k \in \mathbb{R}$ ($k = 1, 2, \ldots$). Calculate
$$
\lim_{k \to \infty} \int_E \cos^2(k\pi x + u_k)\,dm(x).
$$
:::


::: solution
<1>1. Compute the convolution-type limit.
::: proof
For fixed \(x\in\mathbb R\), eventually \(|x|\le k\), and
\[
1+\frac{x^2}{k}\longrightarrow1.
\]
Since \(f\) is continuous at \(1\),
\[
f\!\left(1+\frac{x^2}{k}\right)\longrightarrow f(1)=\pi.
\]
Moreover,
\[
\left|\mathbf1_{[-k,k]}(x)f\!\left(1+\frac{x^2}{k}\right)g(x)\right|
\le \|f\|_\infty |g(x)|,
\]
and the right side is integrable. Dominated convergence therefore gives
\[
\lim_{k\to\infty}\int_{[-k,k]}f\!\left(1+\frac{x^2}{k}\right)g(x)\,dx
=\pi\int_\mathbb R g(x)\,dx.
\]
Since \(g\ge0\) and \(\|g\|_1=2\),
\[
\boxed{L=2\pi.}
\]
:::

<1>2. Compute the Lebesgue--Stieltjes masses.
::: proof
For a Lebesgue--Stieltjes measure associated to the increasing right-continuous function \(F\),
\[
\mu((a,b])=F(b)-F(a),
\qquad
\mu(\{x\})=F(x)-F(x-).
\]
At \(0\),
\[
F(0)=2,
\qquad
F(0-)=0,
\]
so
\[
\boxed{\mu(( -\infty,0])=2.}
\]
At \(1\),
\[
F(1)=4,
\qquad
F(1-)=3,
\]
so
\[
\boxed{\mu(\{1\})=1.}
\]
Finally,
\[
\mu([1,2])=F(2)-F(1-)=16-3=13,
\]
so
\[
\boxed{\mu([1,2])=13.}
\]
:::

<1>3. Compute the oscillatory integral over \(E\).
::: proof
Using
\[
\cos^2\theta=\frac12+\frac12\cos(2\theta),
\]
we get
\[
\int_E\cos^2(k\pi x+u_k)\,dx
=\frac12m(E)+\frac12\operatorname{Re}\left(
e^{2iu_k}\int_Ee^{2\pi ikx}\,dx\right).
\]
Since \(\mathbf1_E\in L^1([0,1])\), the Riemann--Lebesgue lemma gives
\[
\int_Ee^{2\pi ikx}\,dx\longrightarrow0.
\]
The phase factor \(e^{2iu_k}\) has modulus \(1\), so the oscillatory term still tends to \(0\). Since \(m(E)=1/2\),
\[
\boxed{
\lim_{k\to\infty}\int_E\cos^2(k\pi x+u_k)\,dx=\frac14.}
\]
:::
:::
