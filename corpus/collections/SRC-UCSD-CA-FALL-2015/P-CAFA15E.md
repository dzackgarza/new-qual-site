---
schema: qual/card@1
id: P-CAFA15E
kind: problem
title: "A bounded harmonic function on a punctured disk extends harmonically to the full disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
If $u$ is harmonic and bounded in $0 < \abs{z} < \rho$, then show that $u$ may be extended to a harmonic function on the whole disk $\abs{z} < \rho$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own comparison argument follows, with the Poisson solution, the barrier function and the limiting step separated.

Let $u$ be harmonic and bounded in $0<\abs{z}<\rho$, and fix $0<R<\rho$.

::: pf

::: {.pf-step #poisson}
There is $h$ harmonic in $\abs{z}<R$, continuous on the closed disc, with $h=u$ on $\abs{z}=R$; it is given by the Poisson integral of the boundary values of $u$.

::: pf-proof
$u$ is harmonic and hence continuous on the circle $\abs{z}=R$, which is compact, so its boundary values are continuous; the Poisson integral of those values defines a harmonic function in the disc with the prescribed boundary values (solution of the Dirichlet problem in a disc).
:::

:::

::: {.pf-step #difference}
$w=u-h$ is harmonic in $0<\abs{z}<R$, bounded, and $w=0$ on $\abs{z}=R$.

::: pf-proof
Both $u$ and $h$ are harmonic on the punctured disc, so $w$ is; $u$ is bounded by hypothesis and $h$ is continuous on the closed disc, hence bounded; and the boundary values agree by construction.
:::

:::

::: {.pf-step #barrier}
For $0<\varepsilon<\abs{z}<R$ one has $\abs{w(z)}\le M\dfrac{\log(R/\abs{z})}{\log(R/\varepsilon)}$, where $M=\sup\abs{w}$.

::: pf-proof
$\phi_{\varepsilon}(z)=\dfrac{\log(R/\abs{z})}{\log(R/\varepsilon)}$ is harmonic on the annulus $\varepsilon<\abs{z}<R$, being a logarithm of $\abs{z}$ rescaled, with $\phi_{\varepsilon}=1$ on $\abs{z}=\varepsilon$ and $\phi_{\varepsilon}=0$ on $\abs{z}=R$. The functions $\pm w-M\phi_{\varepsilon}$ are harmonic on the annulus and at most $0$ on its boundary: at $\abs{z}=\varepsilon$ they are $\pm w-M\le0$, at $\abs{z}=R$ they are $\pm w-0\le0$ since $w=0$ there. The maximum principle gives $\pm w-M\phi_{\varepsilon}\le0$ inside, that is $\abs{w}\le M\phi_{\varepsilon}$.
:::

:::

::: {.pf-step #limit}
$w=0$ on $0<\abs{z}<R$.

::: pf-proof
Fix $z$ with $0<\abs{z}<R$. For every $\varepsilon<\abs{z}$ step [](#barrier){.pf-ref} gives $\abs{w(z)}\le M\dfrac{\log(R/\abs{z})}{\log(R/\varepsilon)}$, and the right side tends to $0$ as $\varepsilon\to0$ because the numerator is fixed and $\log(R/\varepsilon)\to\infty$.
:::

:::

::: {.pf-qed}
$u=h$ on $0<\abs{z}<R$ by step [](#limit){.pf-ref}, so $u$ extends to the harmonic function $h$ on $\abs{z}<R$; since $R<\rho$ was arbitrary and the extensions agree on overlaps, $u$ extends to a harmonic function on $\abs{z}<\rho$.
:::

:::

:::
