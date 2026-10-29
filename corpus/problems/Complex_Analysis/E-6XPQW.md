---
schema: qual/card@1
id: E-6XPQW
kind: problem
title: $\sum_{k\in\ZZ}\frac{1}{(k-1/2)^2}=\pi^2$
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
$$
\sum_{k\in \ZZ} \frac{1}{\qty{k - \frac12}^2} = \pi^2.
$$
:::

::: {.solution}
For $N\ge1$, let $Q_N$ be the positively oriented boundary of the square $\abs{\Re z}\le N+\tfrac12$, $\abs{\Im z}\le N+\tfrac12$, and let
$$
F(z)=\frac{\pi\cot(\pi z)}{(z-\tfrac12)^2}.
$$

::: pf

::: {.pf-step #vanish}
$\oint_{Q_N}F(z)\,dz\to0$ as $N\to\infty$.

::: pf-proof

::: {.pf-step #vertical}
On the vertical sides of $Q_N$, $\abs{\cot(\pi z)}\le1$.

::: pf-proof
There $\Re z$ is a half-integer, so $\abs{\cot(\pi z)}=\abs{\tanh(\pi\Im z)}\le1$.
:::

:::

::: {.pf-step #horizontal}
On the horizontal sides of $Q_N$, $\abs{\cot(\pi z)}\le\coth(\pi/2)$.

::: pf-proof
For real $x$ and $y\neq0$, $\abs{\cot(x+iy)}^2=\frac{\cos^2x+\sinh^2y}{\sin^2x+\sinh^2y}\le\coth^2y$.
There $\abs{\Im z}=N+\tfrac12$, so $\abs{\cot(\pi z)}\le\coth(\pi(N+\tfrac12))\le\coth(\pi/2)$.
:::

:::

::: pf-qed
On $Q_N$ we have $\abs{z-\tfrac12}\ge N$, so by steps [](#vertical){.pf-ref} and [](#horizontal){.pf-ref}, $\abs{F}\le\pi\coth(\pi/2)/N^2$ there.
The length of $Q_N$ is $8N+4$, so the integral is $O(1/N)$.
:::

:::

:::

::: {.pf-step #residues}
The poles of $F$ inside $Q_N$ are the integers $k=-N,\ldots,N$, with $\Res_{z=k}F=\frac1{(k-1/2)^2}$, and $z=\tfrac12$, with $\Res_{z=1/2}F=-\pi^2$.

::: pf-proof
Since $\pi\cot(\pi z)$ has a simple pole with residue $1$ at every integer and $(z-\tfrac12)^{-2}$ is holomorphic there, $\Res_{z=k}F=(k-\tfrac12)^{-2}$.
Writing $w=z-\tfrac12$,
$$
\pi\cot(\pi z)=-\pi\tan(\pi w)=-\pi^2w+O(w^3),
$$
so $F(z)=-\pi^2/w+O(w)$ near $w=0$.
:::

:::

::: pf-step
$\sum_{k\in\ZZ}\frac1{(k-1/2)^2}=\pi^2$.

::: pf-proof
By the residue theorem and step [](#residues){.pf-ref},
$$
\frac1{2\pi i}\oint_{Q_N}F(z)\,dz
=\sum_{k=-N}^N\frac1{(k-1/2)^2}-\pi^2.
$$
Let $N\to\infty$ and apply step [](#vanish){.pf-ref}.
:::

:::

:::

:::
