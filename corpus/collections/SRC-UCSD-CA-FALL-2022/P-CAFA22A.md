---
schema: qual/card@1
id: P-CAFA22A
kind: problem
title: "Analytic self-map with two fixed points is the identity"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G \subset \mathbb{C}$ be a bounded, simply connected region and let $f$ be an analytic self-map of $G$ (i.e. $f(G) \subset G$). Assume that $f$ has two fixed points.
Show that $f(z) = z$.
:::

::: solution
By the Riemann mapping theorem choose a biholomorphism $\phi:G\to\mathbb D$.
Then $F=\phi\circ f\circ\phi^{-1}$ is a holomorphic self-map of $\mathbb D$
with two distinct fixed points $\alpha,\beta\in\mathbb D$.

Let $T$ be a disk automorphism with $T(\alpha)=0$. Then
$H=T\circ F\circ T^{-1}$ fixes $0$ and the nonzero point $T(\beta)$.
Schwarz's lemma gives $|H(z)|\le |z|$. Since equality holds at the nonzero
fixed point, the equality case gives $H(z)=e^{i\theta}z$. That same fixed point
forces $e^{i\theta}=1$. Hence $H$, then $F$, then $f$, is the identity.
:::
