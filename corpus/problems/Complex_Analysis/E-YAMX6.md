---
schema: qual/card@1
id: E-YAMX6
kind: problem
title: $\int_0^\infty x^\alpha/(1+x)^2\,dx$ for $0<\alpha<1$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
Compute
$$
I \coloneqq \int_0^\infty \frac{x^\alpha}{(1+x)^2}\,dx,
\qquad 0<\alpha<1.
$$
:::

::: {.solution}
Let $f(z)\coloneqq\dfrac{z^\alpha}{(1+z)^2}$ with $z^\alpha\coloneqq e^{\alpha\log z}$ on the branch $0<\arg z<2\pi$, and let $\Gamma_{\varepsilon,R}$ be the positively oriented keyhole contour around the positive real axis.

![Keyhole contour](../../assets/Complex_Analysis/040_Residues/figures/2021-12-24_04-00-31.png)

::: pf

::: {.pf-step #segments}
The two segments of $\Gamma_{\varepsilon,R}$ contribute $\qty(1-e^{2\pi i\alpha})\displaystyle\int_\varepsilon^R\frac{x^\alpha}{(1+x)^2}\,dx$.

::: pf-proof
On the upper bank $z^\alpha=x^\alpha$ and it is traversed from $\varepsilon$ to $R$; on the lower bank $z^\alpha=e^{2\pi i\alpha}x^\alpha$ and it is traversed from $R$ to $\varepsilon$.
:::

:::

::: {.pf-step #arcs}
The circular arcs contribute $o(1)$ as $\varepsilon\to0$ and $R\to\infty$.

::: pf-proof
The small circle has length $2\pi\varepsilon$ and $\abs f = O(\varepsilon^\alpha)$ on it, so it contributes $O(\varepsilon^{\alpha+1})$.
The large circle has length $2\pi R$ and $\abs f = O(R^{\alpha-2})$ on it, so it contributes $O(R^{\alpha-1})$.
Both tend to $0$ because $0<\alpha<1$.
:::

:::

::: {.pf-step #residue}
$\operatorname{Res}_{z=-1}f = -\alpha e^{i\pi\alpha}$.

::: pf-proof
$z=-1$ is a double pole, so the residue is $\frac{d}{dz}z^\alpha\big|_{z=-1} = \alpha e^{(\alpha-1)\log(-1)} = \alpha e^{i\pi(\alpha-1)}$, using $\arg(-1)=\pi$ on this branch.
:::

:::

::: pf-step
$I = \boxed{\dfrac{\pi\alpha}{\sin(\pi\alpha)}}$.

::: pf-proof
The pole $-1$ is the only singularity inside $\Gamma_{\varepsilon,R}$.
By the residue theorem and steps [](#segments){.pf-ref}, [](#arcs){.pf-ref} and [](#residue){.pf-ref}, in the limit $\qty(1-e^{2\pi i\alpha})I = -2\pi i\alpha e^{i\pi\alpha}$.
Since $1-e^{2\pi i\alpha} = -2ie^{i\pi\alpha}\sin(\pi\alpha)$ and $\sin(\pi\alpha)\neq0$, dividing gives the value.
:::

:::

:::

:::
