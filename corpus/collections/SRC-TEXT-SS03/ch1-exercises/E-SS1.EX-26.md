---
schema: qual/card@1
id: E-SS1.EX-26
kind: problem
title: Primitives of a continuous function differ by a constant
classification:
  areas:
    - complex-analysis
  topics: [Contour Integration, Primitives]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
---

::: {.exercise}
Suppose $f$ is continuous in a region $\Omega$. Prove that any two primitives of $f$ (if they exist) differ by a constant.
:::

::: {.solution}

The argument is the card's own: the difference of two primitives has zero derivative, and a function with zero derivative on a region is constant.

::: pf

::: {.pf-step #difference}

If $F$ and $G$ are primitives of $f$ on $\Omega$ then $H=F-G$ is holomorphic on $\Omega$ with $H'(z)=0$ everywhere.

::: pf-proof

A primitive of $f$ on $\Omega$ is a holomorphic $F$ with $F'=f$; so $F$ and $G$ are holomorphic, and $H=F-G$ is holomorphic as a difference of holomorphic functions. At each $z\in\Omega$, $H'(z)=F'(z)-G'(z)=f(z)-f(z)=0$ by linearity of the derivative.

:::

:::

::: {.pf-step #local}

$H$ is constant on some disc around each point, hence locally constant.

::: pf-proof

Fix $z_{0}\in\Omega$. Since $\Omega$ is open, some disc $D(z_{0},r)\subset\Omega$. For $z\in D(z_{0},r)$ the segment $\gamma(t)=z_{0}+t(z-z_{0})$, $0\le t\le1$, lies in the disc and hence in $\Omega$, because a disc is convex. The function $t\mapsto H(\gamma(t))$ is differentiable on $[0,1]$ with derivative $H'(\gamma(t))\,(z-z_{0})=0$ by the chain rule and step [](#difference){.pf-ref}; a differentiable function with zero derivative on an interval is constant, so $H(z)=H(z_{0})$. Thus $H$ is constant on $D(z_{0},r)$, that is $H$ is locally constant.

:::

:::

::: {.pf-step #constant}

A locally constant function on a region is constant.

::: pf-proof

For a value $c$, the level set $H^{-1}(c)=\{z:H(z)=c\}$ is open, because around each of its points $H$ is constant on a disc; and it is closed in $\Omega$, because around each point of its complement $H$ is constant on a disc with value $\ne c$, so the complement is open too. A region is connected, so the only subsets that are both open and closed are $\varnothing$ and $\Omega$. Taking $c=H(z_{0})$, the level set is nonempty, hence equals $\Omega$.

:::

:::

::: {.pf-step #conclusion}

Any two primitives of $f$ on $\Omega$ differ by a constant.

::: pf-proof

With $H=F-G$, steps [](#difference){.pf-ref}, [](#local){.pf-ref} and [](#constant){.pf-ref} show $H$ is constant on $\Omega$, so $F=G+c$ for some $c\in\CC$:
$$
\boxed{F-G\ \text{is constant on } \Omega.}
$$
The hypothesis that $\Omega$ is a region, that is connected, is what step [](#constant){.pf-ref} uses; on a disconnected open set two primitives may differ by different constants on different components.

:::

:::

:::

:::
