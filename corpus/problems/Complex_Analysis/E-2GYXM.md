---
schema: qual/card@1
id: E-2GYXM
kind: problem
title: 'Sum formulas: 1/(n-a)^2'
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
---

:::{.exercise}
Show that
\[
\sum_{k\in \mathbb{Z}}{1\over (z-k)^2} = (\pi \csc(\pi z))^2 = \frac{\pi^2}{\sin^2(\pi z)}
.\]

:::

::: solution
Fix $z\notin\mathbb Z$ and consider, as a function of $w$,
$$
F(w)=\frac{\pi\cot(\pi w)}{(w-z)^2}.
$$
Integrate over the square $\Gamma_N$ with vertices $(N+\tfrac12)(\pm1\pm i)$. On $\Gamma_N$, $|\cot(\pi w)|$ is bounded independently of $N$, while $|w-z|\gg N$, so
$$
\int_{\Gamma_N}F(w)\,dw\longrightarrow0.
$$

<1>1. At each integer $k$,
$$
\operatorname{Res}(F,k)=\frac1{(k-z)^2}=\frac1{(z-k)^2}.
$$
At the double pole $w=z$, writing $h(w)=\pi\cot(\pi w)$ gives
$$
\operatorname{Res}(F,z)=h'(z)=-\pi^2\csc^2(\pi z).
$$

<1>2. For $N$ sufficiently large, $\Gamma_N$ encloses $z$ and the integers $-N,\ldots,N$. The residue theorem therefore yields
$$
\frac1{2\pi i}\int_{\Gamma_N}F(w)\,dw
=\sum_{k=-N}^N\frac1{(z-k)^2}-\pi^2\csc^2(\pi z).
$$
Letting $N\to\infty$ gives
$$
\sum_{k\in\mathbb Z}\frac1{(z-k)^2}
=\pi^2\csc^2(\pi z).
$$
:::
