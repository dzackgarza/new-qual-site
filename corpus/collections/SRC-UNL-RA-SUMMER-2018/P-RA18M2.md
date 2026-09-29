---
schema: qual/card@1
id: P-RA18M2
kind: problem
title: Domain and sum of the arctangent series, and a three-decimal approximation of $\pi$
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Convergence of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 2 of the preserved UNL May 31, 2018 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Verified the convergence and Abel/Leibniz arguments; corrected the term-count wording in the final approximation.
---

::: {.problem}
Find the domain of convergence and the sum of the series $$\sum_{n\ge0}(-1)^n\frac{x^{2n+1}}{2n+1}.$$

Show how one may use the sum of the series to provide an approximation for $\pi$ up to three decimals.
Be sure to provide all technical details.
:::

:::: {.solution}
**Goal:** Find the domain of convergence and the sum of $\sum_{n\ge 0}(-1)^n\frac{x^{2n+1}}{2n+1}$, and use it to approximate $\pi$ to three decimals.

::: pf

::: pf-step

The series is the Taylor series of $\arctan x$ at $0$: $\arctan x = \sum_{n\ge0}(-1)^n\frac{x^{2n+1}}{2n+1}$.
Proof: $\arctan' x = \frac{1}{1+x^2} = \sum_{n\ge0}(-1)^n x^{2n}$ (geometric series, $|x| < 1$), and termwise integration from $0$ to $x$ gives the claim.

:::

::: {.pf-step #s2}

Domain of convergence: $[-1, 1]$.

::: pf-proof

::: {.pf-step #s2-1}

For $|x| < 1$: absolute convergence.
Proof: $\left|(-1)^n\frac{x^{2n+1}}{2n+1}\right| \le |x|^{2n+1}$, geometric with ratio $|x|^2 < 1$.

:::

::: {.pf-step #s2-2}

At $x = 1$: the alternating series $\sum (-1)^n \frac{1}{2n+1}$ converges.
Proof: Leibniz test: $\frac{1}{2n+1} \downarrow 0$.

:::

::: {.pf-step #s2-3}

At $x = -1$: $\sum (-1)^n \frac{(-1)^{2n+1}}{2n+1} = \sum (-1)^{n+1}\frac{1}{2n+1}$, also an alternating series with terms decreasing to $0$: converges.
Proof: same Leibniz test.

:::

::: {.pf-step #s2-4}

For $|x| > 1$: the terms do not tend to $0$.
Proof: $\left|(-1)^n\frac{x^{2n+1}}{2n+1}\right| = \frac{|x|^{2n+1}}{2n+1} \to \infty$ (exponential beats linear), so the series diverges.

:::

::: pf-qed

Proof: steps [](#s2-1){.pf-ref}, [](#s2-2){.pf-ref}, [](#s2-3){.pf-ref} and [](#s2-4){.pf-ref} show the domain is $[-1, 1]$.

:::

:::

:::

::: pf-step

On $[-1,1]$ the sum equals $\arctan x$ (continuous extension).
Proof: the series converges uniformly on $[-r, r]$ for $r < 1$ and pointwise on $[-1,1]$ (by step [](#s2){.pf-ref}); Abel's theorem / continuity of the sum gives equality on the closed interval.
At $x = 1$: $\arctan 1 = \frac{\pi}{4}$.

:::

::: pf-step

Approximation of $\pi$: $\pi = 4\arctan 1 = 4\sum_{n\ge0}\frac{(-1)^n}{2n+1}$.

::: pf-proof

::: {.pf-step #s4-1}

The alternating series at $x = 1$ has error bounded by the first omitted term: $\left|\frac{\pi}{4} - \sum_{n=0}^{N}\frac{(-1)^n}{2n+1}\right| \le \frac{1}{2N+3}$.
Proof: alternating-series remainder bound.

:::

::: {.pf-step #s4-2}

To get $\pi$ to three decimals (error $< 0.0005$, i.e. $\pi/4$ to error $< 0.000125$), need $\frac{1}{2N+3} < 1.25\times10^{-4}$, i.e. $2N + 3 > 8000$, $N \ge 4000$.
Proof: solve the bound of step [](#s4-1){.pf-ref}: error in $\pi$ is $4/(2N+3) < 0.0005 \Leftrightarrow 2N + 3 > 8000$.

:::

::: {.pf-step #s4-3}

Compute: the partial sum through $n=4000$ (that is, $4001$ terms) gives $\pi \approx 3.141\ldots$; e.g. the partial sums oscillate around $\pi/4 \approx 0.785398$, and $\pi \approx 3.14159$.
Proof: the alternating-series bound of step [](#s4-1){.pf-ref} guarantees three-decimal accuracy: $|\pi - 4S_N| \le 4/(2N+3) < 0.0005$.
(This is the Leibniz formula for $\pi$; it converges slowly — $\sim 4000$ terms — but the bound is rigorous.)

:::

::: pf-qed

Proof: steps [](#s4-1){.pf-ref}, [](#s4-2){.pf-ref} and [](#s4-3){.pf-ref} give the approximation procedure with all details.

:::

:::

:::

:::

:::
