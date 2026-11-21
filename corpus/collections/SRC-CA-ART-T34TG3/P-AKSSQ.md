---
schema: qual/card@1
id: P-AKSSQ
kind: problem
title: A nowhere-vanishing holomorphic function of constant modulus on $\partial D$
  is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.problem}
Let $f$ be analytic on a bounded domain $D$, and assume also that $f$ is continuous and nowhere zero on the closure $\bar{D}$.

Show that if $\abs{f(z)}=M$ (a constant) for $z$ on the boundary of $D$, then $f(z)=e^{i \theta} M$ for $z$ in $D$, where $\theta$ is a real constant.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the two maximum-modulus applications, the constancy of the modulus and the open mapping theorem as separate steps.

Let $D$ be a bounded domain, $f$ analytic on $D$ and continuous and nowhere zero on $\overline D$, with $\abs{f}=M$ on $\partial D$.

::: pf

::: {.pf-step #upper}
$\abs{f(z)}\le M$ for $z\in D$.

::: pf-proof
$f$ is analytic on the bounded domain $D$ and continuous on $\overline D$, so the maximum modulus principle gives $\abs{f(z)}\le\max_{\partial D}\abs{f}=M$ on $D$.
:::

:::

::: {.pf-step #lower}
$\abs{f(z)}\ge M$ for $z\in D$.

::: pf-proof
$f$ is nowhere zero on $\overline D$, so $M>0$ and $g=1/f$ is holomorphic on $D$ and continuous on $\overline D$, with $\abs{g}=1/M$ on $\partial D$. The maximum modulus principle applied to $g$ gives $\abs{g(z)}\le1/M$ on $D$, that is $\abs{f(z)}\ge M$.
:::

:::

::: {.pf-step #constant-modulus}
$\abs{f(z)}=M$ for every $z\in D$.

::: pf-proof
The two bounds of steps [](#upper){.pf-ref} and [](#lower){.pf-ref} coincide.
:::

:::

::: {.pf-step #constant}
$f$ is constant.

::: pf-proof
$f(D)$ is contained in the circle $\theset{\abs{w}=M}$, which has empty interior and so contains no nonempty open subset of $\CC$. The open mapping theorem says that a non-constant holomorphic function on a domain has open image, so $f$ cannot be non-constant: $f$ is constant, $f(z)=\lambda M$ with $\abs{\lambda}=1$.
:::

:::

::: {.pf-qed}
By step [](#constant){.pf-ref} there is $M>0$ and $\lambda$ with $\abs{\lambda}=1$ and $f\equiv\lambda M$; writing $\lambda=e^{i\theta}$ gives $f(z)=e^{i\theta}M$ on $D$.
:::

:::

:::
