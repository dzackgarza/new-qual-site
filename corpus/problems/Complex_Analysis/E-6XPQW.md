---
schema: qual/card@1
id: E-6XPQW
kind: problem
title: $\sum_{k\in\mathbb{Z}}\frac{1}{(k-1/2)^2}=\pi^2$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Series of Numbers
  - Trigonometry
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that
\[
\sum_{k\in \ZZ} {1\over \qty{ k - {1\over 2}}^2 } = \pi^2
.\]

:::

::: {.solution}
For $N\ge1$, let $Q_N$ be the positively oriented square
\[
|\Re z|\le N+\tfrac12,
\qquad
|\Im z|\le N+\tfrac12,
\]
and consider
\[
F(z)=\frac{\pi\cot(\pi z)}{(z-\tfrac12)^2}.
\]

::: pf

::: pf-step
On $\partial Q_N$, $|\cot(\pi z)|$ is bounded by a constant independent of $N$.

::: pf-proof

::: pf-step
On the vertical sides, $\Re z$ is a half-integer, so $|\cot(\pi z)|=|\tanh(\pi\Im z)|\le1$.
:::

::: pf-step
On the horizontal sides, $|\Im z|=N+1/2$. For real $x$ and $y\neq0$, $\abs{\cot(x+iy)}^2=\frac{\cos^2x+\sinh^2y}{\sin^2x+\sinh^2y}\le\coth^2y$, so $\abs{\cot(\pi z)}\le\coth(\pi(N+\tfrac12))\le\coth(\pi/2)$.
:::

::: pf-step
Also $|z-1/2|\ge N$ on $\partial Q_N$, while the perimeter is $O(N)$. Hence
\[
\oint_{\partial Q_N}F(z)\,dz\longrightarrow0.
\]
:::

:::

:::

::: pf-step
The poles inside $Q_N$ are the integers $k=-N,\dots,N$ and $z=1/2$.

::: pf-proof

::: pf-step
Since $\pi\cot(\pi z)$ has residue $1$ at every integer,
\[
\operatorname{Res}(F;k)=\frac1{(k-1/2)^2}.
\]
:::

::: pf-step
Writing $w=z-1/2$,
\[
\pi\cot(\pi z)=-\pi\tan(\pi w)=-\pi^2w+O(w^3),
\]
so
\[
F(z)=-\frac{\pi^2}{w}+O(w),
\]
and therefore
\[
\operatorname{Res}(F;1/2)=-\pi^2.
\]
:::

:::

:::

::: pf-step
The residue theorem gives
\[
\frac1{2\pi i}\oint_{\partial Q_N}F(z)\,dz
=\sum_{k=-N}^N\frac1{(k-1/2)^2}-\pi^2.
\]
Letting $N\to\infty$ yields
\[
\sum_{k\in\mathbb Z}\frac1{(k-1/2)^2}=\pi^2.
\]
:::

:::

:::

