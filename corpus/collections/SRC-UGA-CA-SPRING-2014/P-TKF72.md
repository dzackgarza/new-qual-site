---
schema: qual/card@1
id: P-TKF72
kind: problem
title: The integral of $f$ over a large circular arc of angle $\alpha$ tends to $iA\alpha$
  when $zf(z)\to A$
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
Let $0\leq \alpha \leq 2\pi$ be a fixed angle.
Suppose $f$ is continuous on the region $\Omega = \theset{\abs{z} \geq R, \Arg(z) \in [0, \alpha]}$ and $\lim_{z\to \infty} zf(z) = A$.
Show that
$$
\lim_{z\to \infty} \int_{\gamma_R} f(z) \dz = iA\alpha
,$$
where $\gamma_R \coloneqq \theset{ \abs{z} = R, \Arg(z) \in [0, \alpha]}$ is an arc.
:::

::: {.solution}
::: pf

::: {.pf-step #parametrize}
For $R' > R$,
$$
\int_{\gamma_{R'}}f(z)\,dz - i\alpha A =i\int_0^\alpha \bigl(R'e^{it}f(R'e^{it}) - A\bigr)\,dt.
$$

::: pf-proof
Parametrize $\gamma_{R'}$ by $z=R'e^{it}$, $0\le t\le\alpha$, so $dz = iR'e^{it}\,dt$, and write $i\alpha A = i\int_0^\alpha A\,dt$.
:::

:::

::: pf-step
$\lim_{R'\to\infty}\int_{\gamma_{R'}}f(z)\,dz=i\alpha A$.

::: pf-proof
Let $\varepsilon > 0$.
Since $zf(z)\to A$ as $z \to \infty$ in $\Omega$, there is $R_\varepsilon$ with $\abs{zf(z) - A} < \varepsilon$ for $z \in \Omega$, $\abs{z} > R_\varepsilon$.
For $R' > \max(R, R_\varepsilon)$, step [](#parametrize){.pf-ref} gives $\abs{\int_{\gamma_{R'}}f(z)\,dz - i\alpha A} \leq \alpha\varepsilon$.
:::

:::

:::
:::
