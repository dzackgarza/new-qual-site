---
schema: qual/card@1
id: P-BERK92S-05
kind: problem
title: A map constrained to a regular level set has zero Jacobian determinant
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f:\mathbb R^n\to\mathbb R^n$ be differentiable. Suppose there is a differentiable function $g:\mathbb R^n\to\mathbb R$ with no critical points such that
\[
g\circ f=0
\]
identically. Prove that the Jacobian determinant of $f$ vanishes identically.
:::

::: {.solution}
Fix $x\in\RR^n$.

::: pf

::: {.pf-step #s1}

The derivatives satisfy
$$
Dg(f(x))\circ Df(x)=0.
$$

::: pf-proof

Since $g\circ f$ is the constant zero function, its derivative at $x$
is zero. The chain rule gives
$$
D(g\circ f)(x)=Dg(f(x))\circ Df(x),
$$
which proves the claim.

:::

:::

::: {.pf-step #s2}

$Df(x)$ is not invertible.

::: pf-proof

The function $g$ has no critical points, so
$$
Dg(f(x))\ne0.
$$
If $Df(x)$ were invertible, step [](#s1){.pf-ref} could be composed on the right
with $Df(x)^{-1}$, giving $Dg(f(x))=0$, a contradiction. Hence
$Df(x)$ is singular.

:::

:::

::: {.pf-step #s3}

$\det Df(x)=0$ for every $x\in\RR^n$.

::: pf-proof

By step [](#s2){.pf-ref}, $Df(x)$ is singular, so its determinant is zero. Since
$x$ was arbitrary, the Jacobian determinant of $f$ vanishes
identically.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
