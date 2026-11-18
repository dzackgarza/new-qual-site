---
schema: qual/card@1
id: P-CAFA20A
kind: problem
title: '$\oint_{\abs{z-i/2}=1}\sin(i\pi z/2)/(z^2+1)\,dz$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $\gamma$ be the closed curve given by the circle $\abs{z - i/2} = 1$ traversed once in the positive (counterclockwise) direction.
Compute $$\int_\gamma \frac{\sin(i\pi z/2)}{z^2 + 1}\,dz.$$
:::

::: {.solution}

No retained solution set covers this exercise: the card's own residue computation follows, with the location of the poles, the residue and the final product as separate steps.

::: pf

::: {.pf-step #poles}
$\dfrac{\sin(i\pi z/2)}{z^{2}+1}$ has simple poles at $z=\pm i$, and only $z=i$ lies inside the circle $\abs{z-i/2}=1$.

::: pf-proof
$z^{2}+1=(z-i)(z+i)$ and the zeros $\pm i$ are simple, while $\sin(i\pi z/2)$ does not vanish at them: $\sin(i\pi(i)/2)=\sin(-\pi/2)=-1$ and $\sin(i\pi(-i)/2)=\sin(\pi/2)=1$. The centre is $i/2$, and $\abs{i-i/2}=1/2<1$ while $\abs{-i-i/2}=3/2>1$.
:::

:::

::: {.pf-step #residue}
$\operatorname{Res}_{z=i}\dfrac{\sin(i\pi z/2)}{z^{2}+1}=-\dfrac{1}{2i}$.

::: pf-proof
At a simple pole the residue is $\dfrac{\sin(i\pi z/2)}{z+i}$ evaluated at $z=i$, that is $\dfrac{\sin(-\pi/2)}{2i}=\dfrac{-1}{2i}$.
:::

:::

::: {.pf-qed}
By the residue theorem the integral is $2\pi i\cdot\Big(-\dfrac{1}{2i}\Big)=-\pi$: only the pole at $i$ contributes, by steps [](#poles){.pf-ref} and [](#residue){.pf-ref}.
:::

:::

:::
