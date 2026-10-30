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

::: {.problem}
Suppose $\lambda \in \CC$ and $f \in L^1(m) = L^1(\RR, m)$ satisfies $f * f * f(x) = \lambda f * f(x)$ for $m$-a.e. $x$.
Show $f(x) = 0$ for $m$-a.e. $x$.

Recall that $\norm{f * g}_{L^1(m)} \leq \norm{f}_{L^1(m)} \norm{g}_{L^1(m)}$ for all $f, g \in L^1(m)$ and therefore $f * f$ and $f * f * f$ are still in $L^1(m)$.
:::

::: {.solution}

::: pf

::: pf-step

Take Fourier transforms of the convolution equation.

::: pf-proof

Since $f\in L^1(\RR)$, both $f*f$ and $f*f*f$ belong to $L^1(\RR)$. The Fourier transform converts convolution into multiplication, so the assumed identity gives
$$
\widehat f(\xi)^3
=\lambda\widehat f(\xi)^2
$$
for every $\xi\in\RR$. Thus
$$
\widehat f(\xi)^2\bigl(\widehat f(\xi)-\lambda\bigr)=0,
$$
and hence
$$
\widehat f(\xi)\in\{0,\lambda\}
\qquad\text{for every }\xi\in\RR.
$$

:::

:::

::: pf-step

Use continuity and decay of the Fourier transform.

::: pf-proof

If $\lambda=0$, Step 1 immediately gives
$$
\widehat f\equiv0.
$$

Assume $\lambda\ne0$. The Fourier transform of an $L^1$ function is continuous. Since $\RR$ is connected and the set $\{0,\lambda\}$ is disconnected, a continuous map
$$
\widehat f:\RR\to\{0,\lambda\}
$$
must be constant.

By the Riemann--Lebesgue lemma,
$$
\widehat f(\xi)\longrightarrow0
\qquad(\abs{\xi}\to\infty).
$$
Therefore the only possible constant is $0$, so again
$$
\widehat f\equiv0.
$$

:::

:::

::: pf-step

Invoke uniqueness of the Fourier transform.

::: pf-proof

The Fourier transform is injective on $L^1(\RR)$. Since
$$
\widehat f=0,
$$
we conclude
$$
\boxed{f=0\text{ almost everywhere}.}
$$

:::

:::

:::

:::
