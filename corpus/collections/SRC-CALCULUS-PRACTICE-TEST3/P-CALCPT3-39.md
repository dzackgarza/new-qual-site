---
schema: qual/card@1
id: P-CALCPT3-39
kind: problem
title: "When $\\log(1+\\sin 2\\pi x)$ is not real"
classification:
  areas: [prelim]
  topics: [Trigonometry]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 39 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
---

::: {.problem}
For a real number $x$, $\log(1+\sin 2\pi x)$ is *not* a real number if and only if $x$ is

(A) an integer
(B) nonpositive
(C) equal to $\frac{2n-1}{2}$ for some integer $n$
(D) equal to $\frac{4n-1}{4}$ for some integer $n$
(E) any real number
:::

::: {.solution}
Here $\log$ is the real natural logarithm, which is a real number exactly when its argument is positive.

::: pf

::: {.pf-step #nonneg}
$1+\sin2\pi x\ge0$ for every real $x$, with equality exactly when $\sin2\pi x=-1$.

::: pf-proof
$\sin2\pi x\ge-1$.
:::

:::

::: {.pf-step #zeros}
$\sin2\pi x=-1$ exactly when $x=\frac{4n-1}4$ for some integer $n$.

::: pf-proof
$\sin\theta=-1$ exactly when $\theta=-\frac\pi2+2\pi n$ with $n\in\ZZ$. With $\theta=2\pi x$ this is $x=n-\frac14=\frac{4n-1}4$.
:::

:::

::: pf-step
The answer is choice (D).

::: pf-proof
By steps [](#nonneg){.pf-ref} and [](#zeros){.pf-ref}, the logarithm fails to be real exactly at $x=\frac{4n-1}4$. The other choices fail: at an integer or at $x=\frac{2n-1}2$ the argument is $1$ and $\log1=0$, which rules out (A), (C), and (E); and $x=-1$ is nonpositive with $\log1=0$, which rules out (B).
:::

:::

:::

:::
