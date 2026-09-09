---
schema: qual/card@1
id: E-26QQP
kind: problem
title: $\sum_{k\in\mathbb{Z}}\frac{(-1)^k}{(k+a)^2}=\pi^2\cos(\pi a)\csc^2(\pi a)$
  for $a\in\mathbb{R}\setminus\mathbb{Z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Meromorphic Functions
  - Series of Numbers
  - Trigonometry
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
\sum_{k\in \mathbb{Z}} { (-1)^k \over (k+a)^2} = \pi^2 \cos(\pi a)\csc^2(\pi a) \quad \text{for } a\in \mathbb{R}\setminus\mathbb{Z}
.\]

:::

::: solution
Fix $a\in\mathbb R\setminus\mathbb Z$ and set
$$
F(z)=\frac{\pi\csc(\pi z)}{(z+a)^2}.
$$
Integrate over the squares $\Gamma_N$ with vertices $(N+\tfrac12)(\pm1\pm i)$. On $\Gamma_N$, $|\csc(\pi z)|$ is uniformly bounded, while $|z+a|\gg N$ and the contour length is $O(N)$, so
$$
\int_{\Gamma_N}F(z)\,dz\to0.
$$

<1>1. At an integer $k$,
$$
\operatorname{Res}(F,k)=\frac{(-1)^k}{(k+a)^2}.
$$
At the double pole $z=-a$,
$$
\operatorname{Res}(F,-a)
=\left.\frac{d}{dz}(\pi\csc(\pi z))\right|_{z=-a}
=-\pi^2\csc(\pi a)\cot(\pi a)
=-\pi^2\cos(\pi a)\csc^2(\pi a).
$$

<1>2. For large $N$, the residue theorem gives
$$
\frac1{2\pi i}\int_{\Gamma_N}F(z)\,dz
=\sum_{k=-N}^N\frac{(-1)^k}{(k+a)^2}
-\pi^2\cos(\pi a)\csc^2(\pi a).
$$
Letting $N\to\infty$ yields
$$
\sum_{k\in\mathbb Z}\frac{(-1)^k}{(k+a)^2}
=\pi^2\cos(\pi a)\csc^2(\pi a).
$$
:::
