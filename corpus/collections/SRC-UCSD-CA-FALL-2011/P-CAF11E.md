---
schema: qual/card@1
id: P-CAF11E
kind: problem
title: "A continuous function harmonic on the punctured disk is harmonic on the full disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
Let $u$ be a real-valued continuous function on $\overline{\DD}$, and assume that $u$ is harmonic in $\DD \setminus \{0\}$.
Prove that $u$ is harmonic in $\DD$.

Hint: Consider $v(r) := \int_{-\pi}^{\pi} u(re^{i\theta})\,d\theta$.
You may use without proof Laplace's equation in polar coordinates: $$r\frac{\partial}{\partial r}\!\left(r\frac{\partial U}{\partial r}\right) + \frac{\partial^2 U}{\partial \theta^2} = 0,$$ where $U(r, \theta) = u(re^{i\theta})$.
You may also use without proof the fact that a harmonic function in $\DD \setminus \{0\}$ that depends only on $\abs{z}$ is necessarily of the form $u(z) = a\log\abs{z} + b$, where $a$ and $b$ are real constants.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own comparison argument follows, with the Poisson solution, the difference and its boundary values, the log barrier and the limit as separate steps.

Let $u$ be continuous on $\overline{\DD}$ and harmonic on $\DD\setminus\{0\}$.

::: pf

::: {.pf-step #poisson}
For $0<R<1$ there is $h$ harmonic in $B(0,R)$ and continuous on its closure with $h=u$ on $\abs{z}=R$.

::: pf-proof
$u$ is continuous on the circle $\abs{z}=R$, a compact set, so its boundary values are continuous and the Poisson integral of those values is harmonic in $B(0,R)$ with those boundary values.
:::

:::

::: {.pf-step #difference}
$w=u-h$ is harmonic on $0<\abs{z}<R$, bounded, and vanishes on $\abs{z}=R$.

::: pf-proof
Both summands are harmonic on the punctured disc, $u$ is bounded (continuous on the compact $\overline\DD$) and $h$ is bounded on the compact closure of the disc, and the boundary values agree on $\abs{z}=R$.
:::

:::

::: {.pf-step #barrier}
For $0<\varepsilon<\abs{z}<R$, $\abs{w(z)}\le M\dfrac{\log(R/\abs{z})}{\log(R/\varepsilon)}$ with $M=\sup\abs w$.

::: pf-proof
$\phi_{\varepsilon}(z)=\log(R/\abs z)/\log(R/\varepsilon)$ is harmonic on the annulus (a logarithm of $\abs z$ rescaled), equal to $1$ on $\abs z=\varepsilon$ and $0$ on $\abs z=R$. The maximum principle applied to $\pm w-M\phi_{\varepsilon}$, which is harmonic and $\le0$ on both boundary circles, gives $\abs{w}\le M\phi_{\varepsilon}$.
:::

:::

::: {.pf-step #extend}
$u=h$ on $0<\abs z<R$, hence $u$ is harmonic in $\DD$.

::: pf-proof
Fix $z$ with $0<\abs z<R$; letting $\varepsilon\to0$ in step [](#barrier){.pf-ref} gives $w(z)=0$ since $\log(R/\varepsilon)\to\infty$ with the numerator fixed. So $u=h$ on the punctured disc, and $h$ is harmonic in the whole disc $B(0,R)$; as $R<1$ was arbitrary, $u$ coincides with a harmonic function near every point of $\DD$, so $u$ is harmonic on $\DD$.
:::

:::

::: {.pf-qed}
$u$ is harmonic on $\DD$ by step [](#extend){.pf-ref}.
:::

:::

:::
