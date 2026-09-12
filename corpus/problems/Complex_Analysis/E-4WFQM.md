---
schema: qual/card@1
id: E-4WFQM
kind: problem
title: $\sum_{k\geq 1}\frac{1}{k^2+a^2}=\frac{\pi\coth(\pi a)}{2a}-\frac{1}{2a^2}$
  for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Series of Numbers
  - Hyperbolic Functions
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

:::{.exercise}
Show that
\[
\sum_{k\geq 1}{1\over k^2 + a^2} = {1\over 2}{\pi \coth(\pi a)\over a} - {1\over 2a^2} \qquad a>0
.\]

:::

::: solution
Fix $a>0$ and set
$$
F(z)=\frac{\pi\cot(\pi z)}{z^2+a^2}.
$$
For $N>a$, integrate over the square $\Gamma_N$ with vertices $(N+\tfrac12)(\pm1\pm i)$. On these contours $|\cot(\pi z)|$ is bounded independently of $N$, while $|z^2+a^2|\gg N^2$ and $\operatorname{length}(\Gamma_N)=O(N)$. Hence
$$
\int_{\Gamma_N}F(z)\,dz\longrightarrow0.
$$

<1>1. At each integer $k$,
$$
\operatorname{Res}(F,k)=\frac1{k^2+a^2}.
$$
At $z=ia$ and $z=-ia$,
$$
\operatorname{Res}(F,ia)=\operatorname{Res}(F,-ia)
=-\frac{\pi}{2a}\coth(\pi a),
$$
using $\cot(iu)=-i\coth u$.

<1>2. The residue theorem therefore gives, after $N\to\infty$,
$$
\sum_{k\in\mathbb Z}\frac1{k^2+a^2}
=\frac{\pi}{a}\coth(\pi a).
$$
Since
$$
\sum_{k\in\mathbb Z}\frac1{k^2+a^2}
=\frac1{a^2}+2\sum_{k=1}^\infty\frac1{k^2+a^2},
$$
we obtain
$$
\sum_{k=1}^\infty\frac1{k^2+a^2}
=\frac{\pi\coth(\pi a)}{2a}-\frac1{2a^2}.
$$
:::
