---
schema: qual/card@1
id: P-BKF87-1
kind: problem
title: $(\cos\theta)^p\le\cos(p\theta)$ for $0<p<1$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Prove that
\[
(\cos\theta)^p\le \cos(p\theta)
\]
for $0\le\theta\le\pi/2$ and $0<p<1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The function
$$
\phi(x)=\log(\cos x)
$$
is strictly concave on $[0,\pi/2)$ and satisfies $\phi(0)=0$.

::: pf-proof

For $0\leq x<\pi/2$,
$$
\phi''(x)=-\sec^2x<0.
$$
Hence $\phi$ is strictly concave on this interval. Also
$$
\phi(0)=\log1=0.
$$

:::

:::

::: {.pf-step #s2}

If $0\leq\theta<\pi/2$ and $0<p<1$, then
$$
p\log(\cos\theta)\leq\log(\cos(p\theta)).
$$

::: pf-proof

Since
$$
p\theta=(1-p)\cdot0+p\theta,
$$
concavity from step [](#s1){.pf-ref} gives
$$
\begin{aligned}
\phi(p\theta)
&\geq
(1-p)\phi(0)+p\phi(\theta)\\
&=
p\phi(\theta).
\end{aligned}
$$
Substituting the definition of $\phi$ gives the claim.

:::

:::

::: {.pf-step #s3}

If $0\leq\theta<\pi/2$, then
$$
(\cos\theta)^p\leq\cos(p\theta).
$$

::: pf-proof

Exponentiating the inequality in step [](#s2){.pf-ref} gives
$$
\exp\bigl(p\log(\cos\theta)\bigr)
\leq
\exp\bigl(\log(\cos(p\theta))\bigr),
$$
which is exactly the asserted inequality.

:::

:::

::: {.pf-step #s4}

The inequality also holds when $\theta=\pi/2$.

::: pf-proof

Since $0<p<1$,
$$
0<\frac{p\pi}{2}<\frac{\pi}{2},
$$
and therefore
$$
(\cos(\pi/2))^p=0
\leq
\cos(p\pi/2).
$$

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} cover the entire interval $0\leq\theta\leq\pi/2$.

:::

:::

:::
