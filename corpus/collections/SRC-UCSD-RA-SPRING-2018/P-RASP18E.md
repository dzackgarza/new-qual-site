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
Let $\mu$ be a finite positive measure on $(\RR, \mathcal{B})$, $f : \RR \to \CC$ be a Borel measurable function, and for $x \in \RR$, let
$$
(\mu * f)(x) := \begin{cases} \int_{\RR} f(x - y)\,d\mu(y) & \text{if } \int_{\RR} |f(x - y)|\,d\mu(y) < \infty, \\ 0 & \text{otherwise.} \end{cases}
$$

1. For $1 \leq p < \infty$ and $f \in L^p(m)$, show $\|\mu * f\|_{L^p(m)} \leq \mu(\RR) \cdot \|f\|_{L^p(m)}$.

2. If $f \in L^1(\RR, m)$, show $\widehat{\mu * f}(k) = \sqrt{2\pi}\,\hat{\mu}(k)\hat{f}(k)$ for all $k \in \RR$.

3. If $f$ and $\hat{f}$ are in $L^1(\RR, m)$, then
$$
(\mu * f)(x) = \int_{\RR} \hat{\mu}(k)\hat{f}(k) e^{ikx}\,dk \quad \text{for } m\text{-a.e. } x.
$$
:::

::: {.solution}

::: pf

::: pf-step

Prove the \(L^p\) convolution bound.

::: pf-proof

For \(y\in\RR\), let \(\tau_y f(x)=f(x-y)\). Translation invariance of Lebesgue measure gives
\[
\|\tau_y f\|_p=\|f\|_p.
\]
Minkowski's integral inequality therefore yields
\[
\begin{aligned}
\|\mu*f\|_p
&=\left\|\int_{\RR}\tau_y f\,d\mu(y)\right\|_p\\
&\le \int_{\RR}\|\tau_y f\|_p\,d\mu(y)\\
&=\mu(\RR)\|f\|_p.
\end{aligned}
\]
In particular the defining integral is finite for almost every \(x\), and
\[
\boxed{\|\mu*f\|_p\le\mu(\RR)\|f\|_p.}
\]

:::

:::

::: pf-step

Compute the Fourier transform.

::: pf-proof

Assume \(f\in L^1(\RR)\). Part 1 gives \(\mu*f\in L^1\), and Tonelli--Fubini applies because
\[
\int_{\RR}\int_{\RR}|f(x-y)|\,d\mu(y)\,dx
=\mu(\RR)\|f\|_1<\infty.
\]
Using
\[
\widehat h(k)=\frac1{\sqrt{2\pi}}\int_{\RR}h(x)e^{-ikx}\,dx,
\]
we obtain
\[
\begin{aligned}
\widehat{\mu*f}(k)
&=\frac1{\sqrt{2\pi}}
\int_{\RR}\int_{\RR}f(x-y)e^{-ikx}\,d\mu(y)\,dx\\
&=\frac1{\sqrt{2\pi}}
\int_{\RR}e^{-iky}
\left(\int_{\RR}f(u)e^{-iku}\,du\right)d\mu(y)\\
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

Assume now that \(f,\widehat f\in L^1(\RR)\). Since \(\mu\) is finite,
\[
|\widehat\mu(k)|
\le \frac{\mu(\RR)}{\sqrt{2\pi}},
\]
so
\[
\widehat{\mu*f}
=\sqrt{2\pi}\,\widehat\mu\,\widehat f
\in L^1(\RR).
\]
The Fourier inversion theorem applied to \(\mu*f\in L^1\) gives, for almost every \(x\),
\[
\begin{aligned}
(\mu*f)(x)
&=\frac1{\sqrt{2\pi}}
\int_{\RR}\widehat{\mu*f}(k)e^{ikx}\,dk\\
&=\int_{\RR}\widehat\mu(k)\widehat f(k)e^{ikx}\,dk.
\end{aligned}
\]
Hence
\[
\boxed{
(\mu*f)(x)=\int_{\RR}\widehat\mu(k)\widehat f(k)e^{ikx}\,dk
\quad\text{for a.e. }x.}
\]

:::

:::

:::

:::
