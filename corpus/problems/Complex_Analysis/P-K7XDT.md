---
schema: qual/card@1
id: P-K7XDT
kind: problem
title: A conformal map from $\{\Re z>0,\ |z-i|>1\}$ onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Find a conformal map from $\Omega = \{z\in \mathbb{C} \mid |z-i| > 1,\, \operatorname{Re}(z) > 0\}$ to $\mathbb{H} = \{w \in \mathbb{C} \mid \operatorname{Im}(w) > 0\}$.
:::

::: solution
Define
$$
T(z)=\frac{z}{z-2i}.
$$
The boundary line $\Re z=0$ and the circle $|z-i|=1$ both pass through $0$ and $2i$, so $T$ sends them to straight lines through $0$ and $\infty$.

Write $z=x+iy$. A direct computation gives
$$
T(z)=\frac{|z-i|^2-1+2ix}{|z-2i|^2}.
$$
Thus, for $z\in\Omega$,
$$
\Re T(z)>0
\quad\text{and}\quad
\Im T(z)>0.
$$
Hence $T(\Omega)$ lies in the first quadrant
$$
Q=\{w:\Re w>0,\ \Im w>0\}.
$$
Conversely, $T$ is a Möbius transformation and the two boundary arcs of $\Omega$ map to the two boundary rays of $Q$; equivalently, solving
$$
z=\frac{2iw}{w-1}
$$
shows that every $w\in Q$ has a preimage in $\Omega$. Therefore $T$ maps $\Omega$ biholomorphically onto $Q$.

The squaring map is biholomorphic from $Q$ onto the upper half-plane. Consequently
$$
F(z)=T(z)^2=\left(\frac{z}{z-2i}\right)^2
$$
is a conformal map from $\Omega$ onto $\mathbb H$.
:::
