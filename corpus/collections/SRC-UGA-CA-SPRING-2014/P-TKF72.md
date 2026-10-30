---
schema: qual/card@1
id: P-TKF72
kind: problem
title: The integral of $f$ over a large circular arc of angle $\theta$ tends to $i\theta k$
  when $zf(z)\to k$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Laurent Series
relations: []
review: draft
---

::: {.problem}
Let $f$ be a continuous function in the region
$$
D=\theset{z \suchthat \abs z>1,\ 0\leq \arg z\leq \theta}, \quad\text{where } 0\leq \theta \leq 2\pi.
$$
Suppose that there exists $k$ such that $\lim_{z\to \infty} zf(z)=k$ for $z$ in the region $D$.
Show that
$$
\lim_{R\to \infty} \int_{L} f(z) \dz = i\theta k,
$$
where $L$ is the part of the circle $\abs z=R$ which lies in the region $D$.
:::

::: {.solution}
For $R>1$ write $L_R$ for the arc $L$ of the circle $\abs z=R$.

::: pf

::: {.pf-step #parametrize}
For $R > 1$,
$$
\int_{L_R}f(z)\,dz - i\theta k =i\int_0^\theta \bigl(Re^{it}f(Re^{it}) - k\bigr)\,dt.
$$

::: pf-proof
Parametrize $L_R$ by $z=Re^{it}$, $0\le t\le\theta$, so $dz = iRe^{it}\,dt$, and write $i\theta k = i\int_0^\theta k\,dt$.
:::

:::

::: pf-step
$\lim_{R\to\infty}\int_{L_R}f(z)\,dz=i\theta k$.

::: pf-proof
Let $\varepsilon > 0$.
Since $zf(z)\to k$ as $z \to \infty$ in $D$, there is $R_\varepsilon$ with $\abs{zf(z) - k} < \varepsilon$ for $z \in D$, $\abs{z} > R_\varepsilon$.
For $R > \max(1, R_\varepsilon)$, step [](#parametrize){.pf-ref} gives $\abs{\int_{L_R}f(z)\,dz - i\theta k} \leq \theta\varepsilon$.
:::

:::

:::
:::
