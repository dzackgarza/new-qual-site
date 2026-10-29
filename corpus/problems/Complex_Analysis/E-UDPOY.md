---
schema: qual/card@1
id: E-UDPOY
kind: problem
title: A holomorphic function on $\Delta^*$ with nonnegative real part has a removable
  singularity at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Conformal Maps
  - Fractional Linear Transformations
  - Singularities
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source uses $\Delta^*$ without defining it; the statement now declares it as the punctured unit disc $0<\abs{z}<1$.'
---

::: {.problem}
Let $\Delta^* \coloneqq \theset{z \st 0<\abs{z}<1}$.
Suppose $f$ is holomorphic on $\Delta^*$ and $\Re(f) \geq 0$.
Show that $f$ has a removable singularity at $z=0$.
:::

::: {.solution}
Put $g \coloneqq 1/(1+f)$ on $\Delta^*$.

::: pf

::: {.pf-step #g-extends}
$g$ extends to a holomorphic function on $\Delta \coloneqq \theset{\abs{z}<1}$.

::: pf-proof
$\Re(1+f)\geq 1$, so $\abs{1+f}\geq 1$ and $g$ is holomorphic on $\Delta^*$ with $\abs{g}\leq 1$. By Riemann's removable singularity theorem, $g$ extends holomorphically over $0$.
:::

:::

::: {.pf-step #g-nonzero}
$g(0)\neq 0$.

::: pf-proof
$g$ has no zeros on $\Delta^*$, and $g\not\equiv 0$. If $g(0) = 0$, then $g$ has an isolated zero of some order $m\geq 1$ at $0$, and by the open mapping theorem $g(D_\delta(0))$ contains a disc about $0$ for each small $\delta>0$. So there is $z\in\Delta^*$ with $g(z) = w$, $\Re w<0$. Then $1+f(z) = 1/w$ has $\Re(1+f(z)) = \Re(\bar w)/\abs{w}^2 < 0$, contradicting $\Re(1+f)\geq 1$.
:::

:::

::: pf-step
$0$ is a removable singularity of $f$.

::: pf-proof
By steps [](#g-extends){.pf-ref} and [](#g-nonzero){.pf-ref}, $1/g - 1$ is holomorphic on a disc about $0$, and it agrees with $f$ on the punctured disc. So $f$ is bounded near $0$, and $0$ is removable.
:::

:::

:::

:::
