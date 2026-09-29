---
schema: qual/card@1
id: P-JHUSP02CAA
kind: problem
title: "Entire functions whose image omits a ray"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Open Mapping Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
1. Let f be an entire function such that the image of f does not intersect $\{ z \in \mathbb { R } : z \geq 5 \}$ . Prove that $f$ is a constant.
:::

::: {.solution}

::: pf

::: pf-step

The entire function $5-f$ takes values in $\CC\setminus(-\infty,0]$.

::: pf-proof

By hypothesis $f(z)\notin[5,\infty)$ for every $z$, so $5-f(z)\notin(-\infty,0]$. Thus the entire function $5-f$ takes values in $\mathbb C\setminus(-\infty,0]$.

:::

:::

::: pf-step

The principal square root $g=\sqrt{5-f}$ is entire and satisfies $\operatorname{Re}g>0$.

::: pf-proof

The plane minus the nonpositive real axis is simply connected and does not contain $0$. On this domain the principal branch of the square root is holomorphic. Since $5-f$ is entire and maps into that domain, the composition $g(z)=\sqrt{5-f(z)}$ is entire, and its square is $5-f$. Moreover $\operatorname{Re}g(z)>0$ for every $z$, because a square root of a point off $(-\infty,0]$ lies in the open right half-plane.

:::

:::

::: pf-step

A Cayley transform of $g$ is a bounded entire function.

::: pf-proof

The map $\phi(w)=(w-1)/(w+1)$ sends the open right half-plane biholomorphically onto the unit disk, since for $\operatorname{Re}w>0$ one has $|w+1|^2-|w-1|^2=4\operatorname{Re}w>0$. The denominator $g(z)+1$ never vanishes because $\operatorname{Re}g(z)>0$. Hence $\phi\circ g$ is an entire function with $|\phi(g(z))|<1$ for all $z$.

:::

:::

::: pf-step

Liouville's theorem forces $f$ to be constant.

::: pf-proof

The entire function $\phi\circ g$ is bounded, so by Liouville's theorem it is constant [@SS03]. Because $\phi$ is injective, $g$ is constant, and therefore $5-f=g^2$ is constant. Hence $f$ itself is constant.

:::

:::

:::

:::
