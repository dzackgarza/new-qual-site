---
schema: qual/card@1
id: P-RASP16H
kind: problem
title: "First moment condition makes the Fourier transform differentiable"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Differentiation
  - Dominated Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 8 of the official UCSD Spring 2016 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing dominated-difference-quotient proof reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $f \in L^1(\RR)$ and $x f(x) \in L^1(\RR)$.
Prove that the Fourier transform $\hat{f}$ is differentiable at every point $\xi \in \RR$, and
$$
\frac{d}{d\xi}\hat{f}(\xi) = \widehat{(-ixf)}(\xi) \qquad \forall \xi \in \RR.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

With the convention $\hat f(\xi) = \int_\RR f(x) e^{-ix\xi}\,dx$ of the formula to be proved, for $h \ne 0$
$$
\frac{\hat f(\xi+h)-\hat f(\xi)}{h} = \int_\RR f(x)\,e^{-ix\xi}\,\frac{e^{-ixh}-1}{h}\,dx.
$$

::: pf-proof

Linearity of the integral.

:::

:::

::: {.pf-step #s2}

The integrand converges pointwise to $-ixf(x)e^{-ix\xi}$ as $h \to 0$ and is bounded in absolute value by $\abs{xf(x)}$.

::: pf-proof

$\frac{d}{dh}e^{-ixh}\big|_{h=0} = -ix$, and $\abs{e^{-ixh}-1} = \abs{\int_0^h (-ix)e^{-ixt}\,dt} \le \abs{x}\abs{h}$.

:::

:::

::: {.pf-step #s3}

$\displaystyle\lim_{h\to0}\frac{\hat f(\xi+h)-\hat f(\xi)}{h} = \int_\RR (-ixf(x))e^{-ix\xi}\,dx = \widehat{(-ixf)}(\xi)$.

::: pf-proof

Dominated convergence along any sequence $h_n \to 0$, with dominating function $\abs{xf} \in L^1(\RR)$ (Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}).

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} shows $\hat f$ is differentiable at every $\xi$ with derivative $\widehat{(-ixf)}(\xi)$.

:::

:::

:::
