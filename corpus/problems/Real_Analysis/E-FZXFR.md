---
schema: qual/card@1
id: E-FZXFR
kind: problem
title: $f\in L^1$ need not imply $\hat f\in L^1$; if both, then $f$ is bounded, uniformly
  continuous, and vanishes at infinity
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - L¹
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Is it the case that $f\in L^1$ implies $\hat f\in L^1$?

- Show that if $f, \hat f \in L^1$ then $f$ is bounded, uniformly continuous, and vanishes at infinity.
:::

::: {.solution}
Use the convention $\hat f(\xi) = \int_\RR f(x) e^{-ix\xi}\,dx$, for which the inversion formula reads $f(x) = \frac{1}{2\pi}\int_\RR \hat f(\xi) e^{ix\xi}\,d\xi$.

::: pf

::: {.pf-step #s1}

$f \in L^1$ does not imply $\hat f \in L^1$.

::: pf-proof

::: {.pf-step #s1-1}

$f = \chi_{[-1,1]}$ is in $L^1(\RR)$ and $\hat f(\xi) = \frac{2\sin\xi}{\xi}$.

::: pf-proof

$\|f\|_1 = 2$, and $\hat f(\xi) = \int_{-1}^{1} e^{-ix\xi}\,dx = \frac{e^{i\xi} - e^{-i\xi}}{i\xi} = \frac{2\sin\xi}{\xi}$.

:::

:::

::: {.pf-step #s1-2}

$\frac{\sin\xi}{\xi} \notin L^1(\RR)$.

::: pf-proof

For $k \geq 1$, $|\sin\xi| \geq 1/2$ on $[k\pi + \pi/6, k\pi + 5\pi/6]$, an interval of length $2\pi/3$ on which $|\xi| \leq (k+1)\pi$. So $\int |\sin\xi/\xi|\,d\xi \geq \sum_{k\geq1} \frac{1}{3(k+1)} = \infty$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} exhibit an $L^1$ function whose Fourier transform is not in $L^1$.

:::

:::

:::

::: {.pf-step #s2}

Let $f, \hat f \in L^1$ and $g(x) \coloneqq \frac{1}{2\pi}\int \hat f(\xi) e^{ix\xi}\,d\xi$. Then $f = g$ a.e.

::: pf-proof

This is the Fourier inversion theorem, which applies because $f$ and $\hat f$ are integrable.

:::

:::

::: {.pf-step #s3}

$g$ is bounded by $\frac{1}{2\pi}\|\hat f\|_1$ and is uniformly continuous.

::: pf-proof

$|g(x)| \leq \frac{1}{2\pi}\int |\hat f(\xi)|\,d\xi$. For $h \in \RR$, $|g(x+h) - g(x)| \leq \frac{1}{2\pi}\int |\hat f(\xi)|\,|e^{ih\xi} - 1|\,d\xi$, a bound independent of $x$ that tends to $0$ as $h \to 0$ by dominated convergence with dominating function $2|\hat f|$.

:::

:::

::: {.pf-step #s4}

$g(x) \to 0$ as $|x| \to \infty$.

::: pf-proof

$g(x) = \frac{1}{2\pi}\widehat{\hat f}(-x)$ is a Fourier transform of the $L^1$ function $\hat f$, so the Riemann--Lebesgue lemma applies.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} answers the first question negatively. By step [](#s2){.pf-ref}, $f$ agrees a.e. with $g$, and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that $g$ is bounded, uniformly continuous, and vanishes at infinity; so $f$ has these properties after modification on a null set.

:::

:::

:::
