---
schema: qual/card@1
id: P-RASP18E
kind: problem
title: "Convolution with a finite measure and Fourier multiplier"
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
  note: Checked against Problem 5 of the official UCSD Spring 2018 real-analysis qualifying exam, using the source Fourier normalization (2pi)^(-1/2).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $\mu$ be a finite positive measure on $(\mathbb{R}, \mathcal{B})$, $f : \mathbb{R} \to \mathbb{C}$ be a Borel measurable function, and for $x \in \mathbb{R}$, let
$$
(\mu * f)(x) := \begin{cases} \int_{\mathbb{R}} f(x - y)\,d\mu(y) & \text{if } \int_{\mathbb{R}} |f(x - y)|\,d\mu(y) < \infty, \\ 0 & \text{otherwise.} \end{cases}
$$

1. For $1 \leq p < \infty$ and $f \in L^p(m)$, show $\|\mu * f\|_{L^p(m)} \leq \mu(\mathbb{R}) \cdot \|f\|_{L^p(m)}$.

2. If $f \in L^1(\mathbb{R}, m)$, show $\widehat{\mu * f}(k) = \sqrt{2\pi}\,\hat{\mu}(k)\hat{f}(k)$ for all $k \in \mathbb{R}$.

3. If $f$ and $\hat{f}$ are in $L^1(\mathbb{R}, m)$, then
$$
(\mu * f)(x) = \int_{\mathbb{R}} \hat{\mu}(k)\hat{f}(k) e^{ikx}\,dk \quad \text{for } m\text{-a.e. } x.
$$
:::

::: {.solution}

::: pf

::: pf-step

Prove the \(L^p\) convolution bound.

::: pf-proof

For \(y\in\mathbb R\), let \(\tau_y f(x)=f(x-y)\). Translation invariance of Lebesgue measure gives
\[
\|\tau_y f\|_p=\|f\|_p.
\]
Minkowski's integral inequality therefore yields
\[
\begin{aligned}
\|\mu*f\|_p
&=\left\|\int_{\mathbb R}\tau_y f\,d\mu(y)\right\|_p\\
&\le \int_{\mathbb R}\|\tau_y f\|_p\,d\mu(y)\\
&=\mu(\mathbb R)\|f\|_p.
\end{aligned}
\]
In particular the defining integral is finite for almost every \(x\), and
\[
\boxed{\|\mu*f\|_p\le\mu(\mathbb R)\|f\|_p.}
\]

:::

:::

::: pf-step

Compute the Fourier transform.

::: pf-proof

Assume \(f\in L^1(\mathbb R)\). Part 1 gives \(\mu*f\in L^1\), and Tonelli--Fubini applies because
\[
\int_{\mathbb R}\int_{\mathbb R}|f(x-y)|\,d\mu(y)\,dx
=\mu(\mathbb R)\|f\|_1<\infty.
\]
Using
\[
\widehat h(k)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}h(x)e^{-ikx}\,dx,
\]
we obtain
\[
\begin{aligned}
\widehat{\mu*f}(k)
&=\frac1{\sqrt{2\pi}}
\int_{\mathbb R}\int_{\mathbb R}f(x-y)e^{-ikx}\,d\mu(y)\,dx\\
&=\frac1{\sqrt{2\pi}}
\int_{\mathbb R}e^{-iky}
\left(\int_{\mathbb R}f(u)e^{-iku}\,du\right)d\mu(y)\\
&=\sqrt{2\pi}\,\widehat\mu(k)\widehat f(k).
\end{aligned}
\]
Thus
\[
\boxed{\widehat{\mu*f}=\sqrt{2\pi}\,\widehat\mu\,\widehat f.}
\]

:::

:::

::: pf-step

Apply Fourier inversion.

::: pf-proof

Assume now that \(f,\widehat f\in L^1(\mathbb R)\). Since \(\mu\) is finite,
\[
|\widehat\mu(k)|
\le \frac{\mu(\mathbb R)}{\sqrt{2\pi}},
\]
so
\[
\widehat{\mu*f}
=\sqrt{2\pi}\,\widehat\mu\,\widehat f
\in L^1(\mathbb R).
\]
The Fourier inversion theorem applied to \(\mu*f\in L^1\) gives, for almost every \(x\),
\[
\begin{aligned}
(\mu*f)(x)
&=\frac1{\sqrt{2\pi}}
\int_{\mathbb R}\widehat{\mu*f}(k)e^{ikx}\,dk\\
&=\int_{\mathbb R}\widehat\mu(k)\widehat f(k)e^{ikx}\,dk.
\end{aligned}
\]
Hence
\[
\boxed{
(\mu*f)(x)=\int_{\mathbb R}\widehat\mu(k)\widehat f(k)e^{ikx}\,dk
\quad\text{for a.e. }x.}
\]

:::

:::

:::

:::
