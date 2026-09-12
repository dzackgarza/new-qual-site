---
schema: qual/card@1
id: P-RAF17F
kind: problem
title: "Triple convolution equation implies vanishing"
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
  note: Checked against Problem 6 of the official UCSD Fall 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Suppose $\lambda \in \mathbb{C}$ and $f \in L^1(m) = L^1(\mathbb{R}, m)$ satisfies $f * f * f(x) = \lambda f * f(x)$ for $m$-a.e. $x$.
Show $f(x) = 0$ for $m$-a.e. $x$.

Recall that $\|f * g\|_{L^1(m)} \leq \|f\|_{L^1(m)} \|g\|_{L^1(m)}$ for all $f, g \in L^1(m)$ and therefore $f * f$ and $f * f * f$ are still in $L^1(m)$.
:::

::: solution
<1>1. Take Fourier transforms of the convolution equation.
::: proof
Since $f\in L^1(\mathbb R)$, both $f*f$ and $f*f*f$ belong to $L^1(\mathbb R)$. The Fourier transform converts convolution into multiplication, so the assumed identity gives
\[
\widehat f(\xi)^3
=\lambda\widehat f(\xi)^2
\]
for every $\xi\in\mathbb R$. Thus
\[
\widehat f(\xi)^2\bigl(\widehat f(\xi)-\lambda\bigr)=0,
\]
and hence
\[
\widehat f(\xi)\in\{0,\lambda\}
\qquad\text{for every }\xi\in\mathbb R.
\]
:::

<1>2. Use continuity and decay of the Fourier transform.
::: proof
If $\lambda=0$, Step 1 immediately gives
\[
\widehat f\equiv0.
\]

Assume $\lambda\ne0$. The Fourier transform of an $L^1$ function is continuous. Since $\mathbb R$ is connected and the set $\{0,\lambda\}$ is disconnected, a continuous map
\[
\widehat f:\mathbb R\to\{0,\lambda\}
\]
must be constant.

By the Riemann--Lebesgue lemma,
\[
\widehat f(\xi)\longrightarrow0
\qquad(|\xi|\to\infty).
\]
Therefore the only possible constant is $0$, so again
\[
\widehat f\equiv0.
\]
:::

<1>3. Invoke uniqueness of the Fourier transform.
::: proof
The Fourier transform is injective on $L^1(\mathbb R)$. Since
\[
\widehat f=0,
\]
we conclude
\[
\boxed{f=0\text{ almost everywhere}.}
\]
:::
:::
