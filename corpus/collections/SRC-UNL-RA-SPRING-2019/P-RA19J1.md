---
schema: qual/card@1
id: P-RA19J1
kind: problem
title: Pointwise but not uniform convergence of $1/(1+n^2x^2)$ and $nx(1-x)^n$, and equicontinuity
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
  - Equicontinuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 1 in the preserved UNL January 2019 qualifying-exam PDF/extraction.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
(a) Let $$f_n(x)=\frac{1}{1+n^2x^2}\qquad\text{and}\qquad g_n(x)=nx(1-x)^n,\qquad x\in[0,1].$$ Prove that $\{f_n\}$ and $\{g_n\}$ converge pointwise but not uniformly on $[0,1]$.

(b) Are the families $\{f_n\}$, respectively $\{g_n\}$ given in part (a) equicontinuous?
Clearly motivate your answer.
:::

:::: {.solution}
**Goal:** (a) Prove $f_n(x) = \frac{1}{1+n^2x^2}$ and $g_n(x) = nx(1-x)^n$ converge pointwise but not uniformly on $[0,1]$; (b) decide equicontinuity of the two families.

::: pf

::: pf-step

(a) $f_n$ converges pointwise to $f(x) = 1$ at $x = 0$ and $f(x) = 0$ on $(0,1]$.
Proof: $f_n(0) = 1$ for all $n$; for $x > 0$, $n^2x^2 \to \infty$, so $f_n(x) \to 0$.

:::

::: pf-step

$f_n$ does not converge uniformly on $[0,1]$.
Proof: the pointwise limit $f$ is discontinuous at $0$, while each $f_n$ is continuous; a uniform limit of continuous functions is continuous.
Equivalently $\|f_n - f\|_\infty = 1$ for all $n$ (as $x \to 0^+$, $f_n(x) \to 1$ while $f(0) = 1$ and $f_n(0) = 1$: the sup of $|f_n - f|$ is approached, e.g. $\|f_n - f\|_\infty \ge \lim_{x \to 0^+}|f_n(x) - f(x)|$).

:::

::: pf-step

(a) $g_n$ converges pointwise to $g \equiv 0$.
Proof: $g_n(1) = 0$ and $g_n(0) = 0$; for $x \in (0,1)$, $nx(1-x)^n \to 0$ since exponential decay beats linear growth.

:::

::: {.pf-step #s4}

$g_n$ does not converge uniformly.

::: pf-proof

::: {.pf-step #s4-1}

$g_n$ attains its maximum at $x_n = \frac{1}{n+1}$ with $g_n(x_n) = \frac{n}{n+1}\left(1 - \frac{1}{n+1}\right)^n \to e^{-1} \neq 0$.
Proof: $\frac{d}{dx}nx(1-x)^n = n(1-x)^{n-1}(1 - (n+1)x)$, zero at $x = 1/(n+1)$; the value tends to $e^{-1}$.

:::

::: pf-qed

Proof: step [](#s4-1){.pf-ref} gives $\|g_n\|_\infty \to e^{-1} > 0$, so $g_n \not\to 0$ uniformly.

:::

:::

:::

::: pf-step

(b) Neither family is equicontinuous on $[0,1]$.

::: pf-proof

::: {.pf-step #s5-1}

$\{f_n\}$ fails equicontinuity at $0$: $f_n(1/n) = \frac{1}{1 + n^2/n^2} = \frac12$ while $f_n(0) = 1$, so $|f_n(1/n) - f_n(0)| = 1/2$ even though $1/n \to 0$.
Proof: no $\delta > 0$ can force $|f_n(x) - f_n(0)| < 1/4$ for all $n$ simultaneously, since $x = 1/n < \delta$ eventually but the difference stays $1/2$.

:::

::: {.pf-step #s5-2}

$\{g_n\}$ fails equicontinuity at $0$: $g_n(x_n) \to e^{-1} \neq 0$ at $x_n = 1/(n+1) \to 0$ while $g_n(0) = 0$.
Proof: by step [](#s4){.pf-ref}step [](#s5-1){.pf-ref}, $|g_n(x_n) - g_n(0)| \to e^{-1} > 0$ with $x_n \to 0$; again no $\delta$ works for all $n$.

:::

::: pf-qed

Proof: steps [](#s5-1){.pf-ref} and [](#s5-2){.pf-ref} show both families fail the equicontinuity definition at $0$.

:::

:::

:::

:::

:::
