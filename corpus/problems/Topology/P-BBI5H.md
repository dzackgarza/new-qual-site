---
schema: qual/card@1
id: P-BBI5H
kind: problem
title: $\pi_1(X\times Y)\cong\pi_1(X)\times\pi_1(Y)$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Product Topology
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The problem block held a numbered, unfinished solution draft (loops in X x Y as pairs of loops via the projections, with the injectivity argument left as '...?') instead of a question. The statement now asks for the isomorphism; the solution carries the projection argument."
---

::: {.problem}
Let $X$ and $Y$ be topological spaces with $x_0\in X$ and $y_0\in Y$. Show that $\pi_1(X\cross Y,(x_0,y_0))\cong\pi_1(X,x_0)\cross\pi_1(Y,y_0)$.
:::

::: {.solution}

Let $p_X$ and $p_Y$ be the projections of $X\times Y$.

::: pf

::: {.pf-step #phi}

$\Phi:\pi_1(X\times Y,(x_0,y_0))\to\pi_1(X,x_0)\times\pi_1(Y,y_0)$, $[\alpha]\mapsto([p_X\alpha],[p_Y\alpha])$, is a well-defined homomorphism.

::: pf-proof

Composing a based homotopy with $p_X$ or $p_Y$ gives a based homotopy, and $p_X(\alpha*\beta)=(p_X\alpha)*(p_X\beta)$, likewise for $p_Y$.

:::

:::

::: {.pf-step #psi}

$\Psi([a],[b])=[t\mapsto(a(t),b(t))]$ is a well-defined map $\pi_1(X,x_0)\times\pi_1(Y,y_0)\to\pi_1(X\times Y,(x_0,y_0))$.

::: pf-proof

A map into a product is continuous if and only if its coordinates are, so $(a,b)$ is a loop at $(x_0,y_0)$; based homotopies $a\simeq a'$ and $b\simeq b'$ combine coordinatewise to a based homotopy $(a,b)\simeq(a',b')$.

:::

:::

::: pf-step

$\Phi$ is an isomorphism with inverse $\Psi$.

::: pf-proof

A loop in $X\times Y$ is the pair of its coordinate loops, so $\Psi\Phi[\alpha]=[(p_X\alpha,p_Y\alpha)]=[\alpha]$ and $\Phi\Psi([a],[b])=([a],[b])$. By steps [](#phi){.pf-ref} and [](#psi){.pf-ref}, $\Phi$ is a bijective homomorphism.

:::

:::

:::

:::
