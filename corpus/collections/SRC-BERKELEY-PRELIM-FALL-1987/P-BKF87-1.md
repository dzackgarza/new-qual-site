---
schema: qual/card@1
id: P-BKF87-1
kind: problem
title: Prove $(\cos\theta)^p\le\cos(p\theta)$ for $0<p<1$
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
<1>1. The function
$$
\phi(x)=\log(\cos x)
$$
is strictly concave on $[0,\pi/2)$ and satisfies $\phi(0)=0$.

::: {.proof}
For $0\leq x<\pi/2$,
$$
\phi''(x)=-\sec^2x<0.
$$
Hence $\phi$ is strictly concave on this interval. Also
$$
\phi(0)=\log1=0.
$$
:::

<1>2. If $0\leq\theta<\pi/2$ and $0<p<1$, then
$$
p\log(\cos\theta)\leq\log(\cos(p\theta)).
$$

::: {.proof}
Since
$$
p\theta=(1-p)\cdot0+p\theta,
$$
concavity from step <1>1 gives
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

<1>3. If $0\leq\theta<\pi/2$, then
$$
(\cos\theta)^p\leq\cos(p\theta).
$$

::: {.proof}
Exponentiating the inequality in step <1>2 gives
$$
\exp\bigl(p\log(\cos\theta)\bigr)
\leq
\exp\bigl(\log(\cos(p\theta))\bigr),
$$
which is exactly the asserted inequality.
:::

<1>4. The inequality also holds when $\theta=\pi/2$.

::: {.proof}
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

<1>5. Q.E.D.

::: {.proof}
Steps <1>3 and <1>4 cover the entire interval $0\leq\theta\leq\pi/2$.
:::
:::
