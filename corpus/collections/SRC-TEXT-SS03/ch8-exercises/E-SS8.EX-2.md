---
schema: qual/card@1
id: E-SS8.EX-2
kind: problem
title: Orthogonal curves through a nondegenerate critical point of $F$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the zero of order two and its square root, the local
    biholomorphism $g$, the two preimage curves, their real values, and the orthogonality from conformality.
    No retained solution set covers this exercise (the collection retains the textbook, not a solutions
    manual), so the argument is the card's own; it was re-read for this pass.
---

::: {.exercise}
Suppose $F(z)$ is holomorphic near $z = z_0$ and $F(z_0) = F'(z_0) = 0$, while $F''(z_0) \neq 0$. Show that there are two curves $\Gamma_1$ and $\Gamma_2$ that pass through $z_0$, are orthogonal at $z_0$, and so that $F$ restricted to $\Gamma_1$ is real and has a minimum at $z_0$, while $F$ restricted to $\Gamma_2$ is also real but has a maximum at $z_0$.

[Hint: Write $F(z) = (g(z))^2$ for $z$ near $z_0$, and consider the mapping $z \mapsto g(z)$ and its inverse.]
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. The hint's device is used: write $F=g^{2}$ near $z_{0}$ and read the curves off from $g$.

::: pf

::: {.pf-step #sqrt}
Near $z_{0}$ there is a holomorphic $g$ with $F=g^{2}$, $g(z_{0})=0$ and $g'(z_{0})\ne0$.

::: pf-proof
Since $F$ vanishes to order exactly two at $z_{0}$, write $F(z)=(z-z_{0})^{2}h(z)$ with $h$ holomorphic and $h(z_{0})=\frac{F''(z_{0})}{2}\ne0$. On a small disc about $z_{0}$ the function $h$ has no zero, so it has a holomorphic square root $q$ there; set $g(z)=(z-z_{0})q(z)$. Then $g^{2}=F$, $g(z_{0})=0$, and $g'(z_{0})=q(z_{0})\ne0$ since $g'(z)=(q+(z-z_{0})q')$.
:::

:::

::: {.pf-step #biholomorphic}
After shrinking the disc, $g$ maps a neighbourhood $U$ of $z_{0}$ biholomorphically onto a disc $V$ about $0$.

::: pf-proof
$g$ is holomorphic near $z_{0}$ with $g'(z_{0})\ne0$, so the holomorphic inverse function theorem gives a neighbourhood $U$ of $z_{0}$ carried biholomorphically onto a neighbourhood $V$ of $g(z_{0})=0$; shrinking, $V$ may be taken to be a disc $\abs{w}<\eta$.
:::

:::

::: {.pf-step #curves}
$\Gamma_{1}=g^{-1}(V\cap\RR)$ and $\Gamma_{2}=g^{-1}(V\cap i\RR)$ are smooth curves through $z_{0}$.

::: pf-proof
$V\cap\RR$ is the horizontal diameter of the disc and $V\cap i\RR$ the vertical one; each is a smooth embedded curve through $0$, and the inverse of a biholomorphism carries smooth embedded curves to smooth embedded curves. Both contain $0$, so $\Gamma_{1},\Gamma_{2}$ contain $g^{-1}(0)=z_{0}$.
:::

:::

::: {.pf-step #values}
$F$ is real on both curves, with a strict minimum at $z_{0}$ along $\Gamma_{1}$ and a strict maximum along $\Gamma_{2}$.

::: pf-proof
On $\Gamma_{1}$ we have $g(z)=t\in\RR$, so $F(z)=g(z)^{2}=t^{2}\ge0=F(z_{0})$, with equality only at $t=0$, that is only at $z=z_{0}$; so $F$ is real there with a strict minimum at $z_{0}$. On $\Gamma_{2}$ we have $g(z)=it$ with $t\in\RR$, so $F(z)=(it)^{2}=-t^{2}\le0=F(z_{0})$, again with equality only at $z_{0}$; so $F$ is real there with a strict maximum.
:::

:::

::: {.pf-step}
$\Gamma_{1}$ and $\Gamma_{2}$ meet orthogonally at $z_{0}$.

::: pf-proof
The real and imaginary axes of the $w$-plane meet at right angles at $0$, and $g^{-1}$ is conformal at $0$ because $(g^{-1})'(0)=1/g'(z_{0})\ne0$. A conformal map preserves the angle between curves, so the images $\Gamma_{1}$ and $\Gamma_{2}$ meet at right angles at $z_{0}$. With step [](#values){.pf-ref} this gives the two curves required.
:::

:::

:::
:::
