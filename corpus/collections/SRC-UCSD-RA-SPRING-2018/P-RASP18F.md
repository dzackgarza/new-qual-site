---
schema: qual/card@1
id: P-RASP18F
kind: problem
title: "Layer-cake representation and Chebyshev inequality"
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
  note: Checked against Problem 6 of the official UCSD Spring 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f : \mathbb{R} \to [0,1]$ be a Borel measurable function.
For $t \geq 0$, let $\varphi(t) = m(\{x \in \mathbb{R} : f(x) \geq t\})$.

1. Assume that $f \in L^1(\mathbb{R}, m)$.
   Prove that $\varphi(t) \leq \frac{1}{t}\|f\|_1$ for all $t > 0$.

2. Prove that $\int_{\mathbb{R}} f\,dm = \int_0^\infty \varphi(t)\,dt$.

3. Assume that $\varphi(t) \leq \frac{1}{\sqrt{t}}$ for all $t > 0$.
   Prove that $f \in L^1(\mathbb{R}, m)$.
:::


::: solution
<1>1. Prove the distribution-function bound.
::: proof
For \(t>0\), on the set \(\{f\ge t\}\) we have \(f\ge t\). Hence
\[
t\,\varphi(t)
=t\,m(\{f\ge t\})
\le \int_{\{f\ge t\}}f\,dm
\le \|f\|_1.
\]
Therefore
\[
\boxed{\varphi(t)\le \frac{\|f\|_1}{t}.}
\]
:::

<1>2. Prove the layer-cake formula.
::: proof
For every \(x\), since \(f(x)\ge0\),
\[
f(x)=\int_0^\infty \mathbf1_{\{t\le f(x)\}}\,dt.
\]
The integrand is nonnegative and measurable on \(\mathbb R\times(0,\infty)\). Tonelli's theorem gives
\[
\begin{aligned}
\int_{\mathbb R}f(x)\,dx
&=\int_0^\infty
m(\{x:f(x)\ge t\})\,dt\\
&=\int_0^\infty\varphi(t)\,dt.
\end{aligned}
\]
Thus
\[
\boxed{\int_{\mathbb R}f\,dm=\int_0^\infty\varphi(t)\,dt.}
\]
:::

<1>3. Deduce integrability from the assumed distribution bound.
::: proof
Because \(0\le f\le1\),
\[
\varphi(t)=0
\qquad(t>1).
\]
Using Step 2 and the hypothesis,
\[
\int_{\mathbb R}f\,dm
=\int_0^1\varphi(t)\,dt
\le \int_0^1 t^{-1/2}\,dt
=2.
\]
Hence
\[
\boxed{f\in L^1(\mathbb R).}
\]
:::
:::
