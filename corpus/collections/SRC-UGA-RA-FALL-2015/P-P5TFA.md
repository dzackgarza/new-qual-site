---
schema: qual/card@1
id: P-P5TFA
kind: problem
title: $\lim_{x\to\infty}f(x)\le 1+\frac\pi 4$ when $f(1)=1$ and $f'=1/(x^2+f^2)$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Limits
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the UGA Fall 2015 real-analysis qualifying exam recorded by SRC-UGA-RA-FALL-2015.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $f: [1, \infty) \to \RR$ such that $f(1) = 1$ and
\[
f^{\prime}(x)= \frac{1} {x^{2}+f(x)^{2}}
\]

Show that the following limit exists and satisfies the equality
\[
\lim _{x \rightarrow \infty} f(x) \leq 1 + \frac \pi 4
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$f$ is strictly increasing on $[1,\infty)$.

::: pf-proof

$f'(x) = 1/(x^2 + f(x)^2) > 0$ for every $x \ge 1$.

:::

:::

::: {.pf-step #s2}

Hence $f(x) \ge f(1) = 1$ for all $x \ge 1$.

::: pf-proof

Step [](#s1){.pf-ref} and $f(1) = 1$.

:::

:::

::: {.pf-step #s3}

$f'(x) \le 1/(x^2+1)$ for all $x \ge 1$.

::: pf-proof

$f(x)^2 \ge 1$ by step [](#s2){.pf-ref}, so $x^2 + f(x)^2 \ge x^2 + 1$; inverting gives $f'(x) = 1/(x^2+f(x)^2) \le 1/(x^2+1)$.

:::

:::

::: {.pf-step #s4}

$f(x) \le 1 + \pi/4$ for all $x \ge 1$.

::: pf-proof

integrate step [](#s3){.pf-ref} from $1$ to $x$: \[ f(x) - f(1) = \int_1^x f'(t)\,dt \le \int_1^x \frac{dt}{1+t^2} = \arctan x - \frac{\pi}{4} < \frac{\pi}{2} - \frac{\pi}{4} = \frac{\pi}{4}. \] Adding $f(1) = 1$ gives the claim.

:::

:::

::: pf-step

$\lim_{x\to\infty} f(x)$ exists and is $\le 1 + \pi/4$.

::: pf-proof

$f$ is increasing (step [](#s1){.pf-ref}) and bounded above by $1+\pi/4$ (step [](#s4){.pf-ref}), so the monotone convergence theorem for functions of a real variable applies: the limit exists and is at most the bound.

:::

:::

:::

:::
