---
schema: qual/card@1
id: P-GRNXH
kind: problem
title: Holomorphic interpolation at sequences accumulating at zero
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is analytic on $\DD^\circ$.
Determine with proof which of the following are possible:

(a) $f\qty{1\over n} = (-1)^n$ for each $n>1$.

(b) $f\qty{1\over n} = e^{-n}$ for each even integer $n>1$ while $f\qty{1\over n} = 0$ for each odd integer $n>1$.

(c) $f\qty{1\over n^2} = {1\over n}$ for each integer $n>1$.

(d) $f\qty{1\over n} = {n-2 \over n-1}$ for each integer $n>1$.
:::

::: {.solution}
::: pf

::: pf-step
(a) is impossible.

::: pf-proof
$f$ is continuous at $0$ and $1/n\to 0$, so $f(1/n)$ would converge to $f(0)$; but $(-1)^n$ does not converge.
:::

:::

::: pf-step
(b) is impossible.

::: pf-proof
$f$ vanishes at $1/n$ for every odd $n>1$, and these points accumulate at $0\in\DD$. The identity theorem gives $f\equiv 0$, contradicting $f(1/n)=e^{-n}\neq 0$ for even $n$.
:::

:::

::: pf-step
(c) is impossible.

::: pf-proof
Since $f(1/n^2)=1/n\to 0$, continuity gives $f(0)=0$, and $f\not\equiv 0$. Let $m\geq 1$ be the order of the zero at $0$, so $f(z)=z^m g(z)$ with $g$ analytic and $g(0)\neq 0$. At $z=1/n^2$ this gives $g(1/n^2)=n^{2m-1}\to\infty$, contradicting $g(1/n^2)\to g(0)$.
:::

:::

::: pf-step
(d) is possible.

::: pf-proof
$f(z)=\dfrac{1-2z}{1-z}$ has its only pole at $z=1$, so it is analytic on $\DD$, and $f(1/n)=\dfrac{1-2/n}{1-1/n}=\dfrac{n-2}{n-1}$.
:::

:::

::: pf-step
Exactly $\boxed{\text{(d)}}$ is possible.

::: pf-proof
This collects the four preceding steps.
:::

:::

:::

:::
