---
schema: qual/card@1
id: P-K2AR1
kind: problem
title: $\lim_{R'\to\infty}\int_{L_{R'}}f(z)\,dz=i\theta k$ when $zf(z)\to k$ in a sector
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Let $f$ be continuous on
$$
D=\{z:\abs{z}>R,\ 0\le\arg z\le\theta\},\qquad 0\le\theta\le2\pi,
$$
and suppose $zf(z)\to k$ as $z\to\infty$ in $D$. If $L_{R'}$ is the part of $\abs{z}=R'$ lying in $D$, show that
$$
\lim_{R'\to\infty}\int_{L_{R'}}f(z)\,dz=i\theta k.
$$
:::

::: {.solution}
::: pf

::: {.pf-step #parametrize}
For $R' > R$,
$$
\int_{L_{R'}}f(z)\,dz - i\theta k =i\int_0^\theta \bigl(R'e^{it}f(R'e^{it}) - k\bigr)\,dt.
$$

::: pf-proof
Parametrize $L_{R'}$ by $z=R'e^{it}$, $0\le t\le\theta$, so $dz = iR'e^{it}\,dt$, and write $i\theta k = i\int_0^\theta k\,dt$.
:::

:::

::: pf-step
$\lim_{R'\to\infty}\int_{L_{R'}}f(z)\,dz=i\theta k$.

::: pf-proof
Let $\varepsilon > 0$.
Since $zf(z)\to k$ as $z \to \infty$ in $D$, there is $R_\varepsilon$ with $\abs{zf(z) - k} < \varepsilon$ for $z \in D$, $\abs{z} > R_\varepsilon$.
For $R' > \max(R, R_\varepsilon)$, step [](#parametrize){.pf-ref} gives $\abs{\int_{L_{R'}}f(z)\,dz - i\theta k} \leq \theta\varepsilon$.
:::

:::

:::
:::
