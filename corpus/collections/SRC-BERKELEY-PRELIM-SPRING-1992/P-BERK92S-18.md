---
schema: qual/card@1
id: P-BERK92S-18
kind: problem
title: An entire upper-half-plane-preserving real function has positive derivative on $\mathbb R$
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
Let $f$ be entire, real-valued on the real axis, and suppose
\[
\operatorname{Im}f(z)>0
\]
whenever $\operatorname{Im}z>0$. Prove that
\[
f'(x)>0
\]
for every real $x$.
:::

::: {.solution}
Fix $x_0\in\RR$.

::: pf

::: {.pf-step #s1}

Every Taylor coefficient of $f$ at $x_0$ is real.

::: pf-proof

For each $m\ge0$, the complex derivative $f^{(m)}(x_0)$ can be
computed by taking difference quotients along the real axis. Since
$f$ is real-valued there, induction on $m$ gives
$$
f^{(m)}(x_0)\in\RR.
$$
Equivalently, the Taylor expansion of $f$ about $x_0$ has real
coefficients.

:::

:::

::: {.pf-step #s2}

$f'(x_0)\ge0$.

::: pf-proof

For $y>0$,
$$
f(x_0+iy)
=f(x_0)+iyf'(x_0)+O(y^2).
$$
By step [](#s1){.pf-ref}, both $f(x_0)$ and $f'(x_0)$ are real, so
$$
\operatorname{Im}f(x_0+iy)
=y f'(x_0)+O(y^2).
$$
The left-hand side is positive for every $y>0$. Dividing by $y$ and
letting $y\downarrow0$ gives $f'(x_0)\ge0$.

:::

:::

::: {.pf-step #s3}

$f'(x_0)\ne0$.

::: pf-proof

The function $f$ is not constant: a constant entire function that is
real on $\RR$ has imaginary part zero everywhere, contrary to the
hypothesis in the upper half-plane.

Suppose $f'(x_0)=0$. Let $m\ge2$ be the least integer such that
$f^{(m)}(x_0)\ne0$, and put
$$
c\coloneqq\frac{f^{(m)}(x_0)}{m!}\in\RR\setminus\{0\}.
$$
Then
$$
f(x_0+w)
=f(x_0)+cw^m+O(\abs{w}^{m+1}).
$$
If $c>0$, choose
$$
\theta=\frac{3\pi}{2m};
$$
if $c<0$, choose
$$
\theta=\frac{\pi}{2m}.
$$
In either case $0<\theta<\pi$ and
$$
c\sin(m\theta)<0.
$$
For $w=re^{i\theta}$ with $r>0$ small,
$$
\operatorname{Im}f(x_0+w)
=c r^m\sin(m\theta)+O(r^{m+1})<0,
$$
although $\operatorname{Im}w>0$. This contradicts the hypothesis.
Hence $f'(x_0)\ne0$.

:::

:::

::: {.pf-step #s4}

$f'(x_0)>0$.

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: pf-qed

The real point $x_0$ was arbitrary, so step [](#s4){.pf-ref} holds for every
$x_0\in\RR$.

:::

:::

:::
