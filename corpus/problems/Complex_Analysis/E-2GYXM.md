---
schema: qual/card@1
id: E-2GYXM
kind: problem
title: $\sum_{k\in\ZZ}(z-k)^{-2}=\pi^2/\sin^2(\pi z)$
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Principal Parts
  - Poles
  - Trigonometry
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source states the identity with no domain for z; the statement restricts z to the complement of the integers, where both sides are defined.
---

::: {.exercise}
Show that for $z\in\CC\setminus\ZZ$,
$$
\sum_{k\in \ZZ}\frac{1}{(z-k)^2} = (\pi \csc(\pi z))^2 = \frac{\pi^2}{\sin^2(\pi z)}.
$$

:::

::: {.solution}
Fix $z\in\CC\setminus\ZZ$, let
$$
F(w)=\frac{\pi\cot(\pi w)}{(w-z)^2},
$$
and let $\Gamma_N$ be the positively oriented boundary of the square with vertices $(N+\tfrac12)(\pm1\pm i)$.

::: pf

::: {.pf-step #residues}
$\operatorname{Res}(F,k)=(z-k)^{-2}$ for each $k\in\ZZ$, and $\operatorname{Res}(F,z)=-\pi^2\csc^2(\pi z)$.

::: pf-proof
At an integer $k$, the function $\pi\cot(\pi w)$ has a simple pole with residue $1$, and $(w-z)^{-2}$ is holomorphic near $k$, so $\operatorname{Res}(F,k)=(k-z)^{-2}=(z-k)^{-2}$.
At $w=z$ the function $h(w)=\pi\cot(\pi w)$ is holomorphic, so $F$ has a pole of order at most $2$ with residue $h'(z)=-\pi^2\csc^2(\pi z)$.
:::

:::

::: {.pf-step #vanish}
$\int_{\Gamma_N}F(w)\,dw\to0$ as $N\to\infty$.

::: pf-proof
On $\Gamma_N$ the function $\abs{\cot(\pi w)}$ is bounded by a constant independent of $N$, and for $N\ge 2\abs{z}+1$ we have $\abs{w-z}\ge N/2$ on $\Gamma_N$.
The length of $\Gamma_N$ is $8N+4$, so the integral is $O(N\cdot N^{-2})=O(1/N)$.
:::

:::

::: pf-step
$\sum_{k\in\ZZ}(z-k)^{-2}=\pi^2\csc^2(\pi z)$.

::: pf-proof
For $N>\abs{z}+1$ the square $\Gamma_N$ encloses $z$ and the integers $-N,\ldots,N$, and no other pole of $F$.
By the residue theorem and step [](#residues){.pf-ref},
$$
\frac1{2\pi i}\int_{\Gamma_N}F(w)\,dw
=\sum_{k=-N}^N\frac1{(z-k)^2}-\pi^2\csc^2(\pi z).
$$
Letting $N\to\infty$ and applying step [](#vanish){.pf-ref} gives the identity; the series converges absolutely.
:::

:::

:::

:::
