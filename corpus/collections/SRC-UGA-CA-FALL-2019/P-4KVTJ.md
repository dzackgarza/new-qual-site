---
schema: qual/card@1
id: P-4KVTJ
kind: problem
title: 'Exterior Cauchy formula: the Cauchy integral equals $A$ inside $\gamma$ and $A-f(z)$ outside when $f\to A$ at $\infty$'
classification:
  areas:
    - complex-analysis
  topics:
    - Cauchy Integral Formula
    - Residues
    - Contour Integration
relations: []
review: draft
---

::: {.problem}
Let $\gamma$ be a positively oriented (counterclockwise) piecewise smooth simple closed curve in $\CC$ with interior $\Omega_1$ and exterior $\Omega_2$.
Assume $f$ is holomorphic on an open set containing $\gamma \cup \Omega_2$, with $\lim_{z \to \infty} f(z) = A$.

Prove that the Cauchy integral
$$
F(z) = \frac{1}{2\pi i} \int_{\gamma} \frac{f(\xi)}{\xi - z} \, d\xi = \begin{cases} A & \text{if } z \in \Omega_1, \\ -f(z) + A & \text{if } z \in \Omega_2. \end{cases}
$$
:::

::: {.solution}

For $R>0$ let $C_R$ be the circle $\abs{\xi}=R$, oriented counterclockwise. Fix $z\notin\gamma$ and take $R$ so large that $\gamma$ and $z$ lie in $\abs{\xi}<R$. Let $U_R=\Omega_2\cap\{\abs{\xi}<R\}$; its oriented boundary is $C_R-\gamma$, and $f$ is holomorphic on a neighborhood of $\overline{U_R}$.

::: pf

::: {.pf-step #large}

$\displaystyle\lim_{R\to\infty}\frac1{2\pi i}\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi=A$.

::: pf-proof

Since $\abs{z}<R$, $\frac1{2\pi i}\int_{C_R}\frac{d\xi}{\xi-z}=1$, so
$$
\frac1{2\pi i}\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi-A=\frac1{2\pi i}\int_{C_R}\frac{f(\xi)-A}{\xi-z}\,d\xi.
$$
Given $\varepsilon>0$, choose $R_0$ with $\abs{f(\xi)-A}<\varepsilon$ for $\abs{\xi}\ge R_0$. For $R\ge R_0$ the right side has modulus at most $\frac{1}{2\pi}\cdot\frac{\varepsilon}{R-\abs{z}}\cdot2\pi R$, which tends to $\varepsilon$ as $R\to\infty$.

:::

:::

::: {.pf-step #inside}

If $z\in\Omega_1$, then $F(z)=A$.

::: pf-proof

Here $z\notin\overline{U_R}$, so $\xi\mapsto f(\xi)/(\xi-z)$ is holomorphic on a neighborhood of $\overline{U_R}$, and Cauchy's theorem on $U_R$ gives $\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi=\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi$. The right side does not depend on $R$; let $R\to\infty$ and use Step [](#large){.pf-ref}.

:::

:::

::: {.pf-step #outside}

If $z\in\Omega_2$, then $F(z)=-f(z)+A$.

::: pf-proof

Here $z\in U_R$, and Cauchy's integral formula on $U_R$ gives
$$
\frac1{2\pi i}\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi-\frac1{2\pi i}\int_\gamma\frac{f(\xi)}{\xi-z}\,d\xi=f(z).
$$
So $F(z)=-f(z)+\frac1{2\pi i}\int_{C_R}\frac{f(\xi)}{\xi-z}\,d\xi$; let $R\to\infty$ and use Step [](#large){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#inside){.pf-ref} and [](#outside){.pf-ref} are the two cases of the formula.

:::

:::

:::
