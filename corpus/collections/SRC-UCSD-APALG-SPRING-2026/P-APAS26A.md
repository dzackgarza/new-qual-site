---
schema: qual/card@1
id: P-APAS26A
kind: problem
title: Operator norm on $\operatorname{Hom}(V,W)$ is not induced by a scalar product
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
  - Inner Product Spaces
relations: []
review: draft
---

::: {.problem}
Let $V$ and $W$ be Hilbert spaces, each of dimension at least two.
Prove that the operator norm on $\operatorname{Hom}(V, W)$ is not induced by any scalar product on $\operatorname{Hom}(V, W)$.

Note: On this exam, a Hilbert space is a finite-dimensional complex vector space equipped with a scalar product.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own parallelogram counterexample follows, with the choices, the four norms and the failure as separate steps.

Let $V,W$ be finite-dimensional complex Hilbert spaces of dimension at least $2$, and $\operatorname{Hom}(V,W)$ carry the operator norm.

::: pf

::: {.pf-step #parallel}
A norm induced by a scalar product satisfies the parallelogram identity $\norm{S+T}^{2}+\norm{S-T}^{2}=2\norm{S}^{2}+2\norm{T}^{2}$ for all $S,T$.

::: pf-proof
Expanding $\langle S+T,S+T\rangle$ and $\langle S-T,S-T\rangle$ in an inner product and adding gives $2\langle S,S\rangle+2\langle T,T\rangle$; if the norm comes from the scalar product, the left side is $\norm{S+T}^{2}+\norm{S-T}^{2}$ and the right side $2\norm{S}^{2}+2\norm{T}^{2}$.
:::

:::

::: {.pf-step #operators}
Choose orthonormal $e_{1},e_{2}\in V$ and $f_{1},f_{2}\in W$ and define $S,T$ by $Se_{1}=f_{1}$, $S=0$ on $e_{1}^{\perp}$, $Te_{2}=f_{2}$, $T=0$ on $e_{2}^{\perp}$. These are well defined linear maps.

::: pf-proof
$V=\CC e_{1}\oplus e_{1}^{\perp}$ and $V=\CC e_{2}\oplus e_{2}^{\perp}$, so prescribing a value on $e_{1}$ and on $e_{1}^{\perp}$ (resp. on $e_{2}$ and $e_{2}^{\perp}$) defines a linear map; the vectors exist because $\dim V,\dim W\ge2$.
:::

:::

::: {.pf-step #norms}
$\norm{S}=\norm{T}=\norm{S+T}=\norm{S-T}=1$.

::: pf-proof
$S$ carries the unit vector $e_{1}$ to the unit vector $f_{1}$ and annihilates $e_{1}^{\perp}$, so $\norm{Sv}\le\norm{v}$ with equality at $e_{1}$: $\norm{S}=1$; likewise $\norm{T}=1$. For $v=ae_{1}+be_{2}+w$ with $w\perp e_{1},e_{2}$, one has $Se_{1}=f_{1}$, $Te_{1}=0$ and $Se_{2}=0$, $Te_{2}=f_{2}$, so $(S+T)v=af_{1}+bf_{2}$ and $(S-T)v=af_{1}-bf_{2}$, both of norm $\sqrt{\abs{a}^{2}+\abs{b}^{2}}\le\norm{v}$ because $f_{1},f_{2}$ are orthonormal, with equality when $w=0$ and $\abs{a}^{2}+\abs{b}^{2}=1$.
:::

:::

::: {.pf-qed}
$\norm{S+T}^{2}+\norm{S-T}^{2}=1+1=2$ while $2\norm{S}^{2}+2\norm{T}^{2}=2+2=4$, so the parallelogram identity fails by steps [](#parallel){.pf-ref} and [](#norms){.pf-ref}. Hence the operator norm on $\operatorname{Hom}(V,W)$ is not induced by any scalar product.
:::

:::

:::
