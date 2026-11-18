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

::: {.problem}
Let $G \subset \CC$ be a bounded, simply connected region and let $f$ be an analytic self-map of $G$ (i.e. $f(G) \subset G$). Assume that $f$ has two fixed points.
Show that $f(z) = z$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the Riemann map, the normalisation to the disc, Schwarz's equality case and the second fixed point as separate steps.

Let $G\subset\CC$ be a bounded simply connected region and $f:G\to G$ analytic with two distinct fixed points.

::: pf

::: {.pf-step #conjugate}
There is a biholomorphism $\phi:G\to\DD$, and $F=\phi\circ f\circ\phi^{-1}$ is a holomorphic self-map of $\DD$ with two distinct fixed points.

::: pf-proof
$G$ is a bounded simply connected region, so the Riemann mapping theorem gives a biholomorphism $\phi:G\to\DD$. Then $F$ is holomorphic as a composite and maps $\DD$ into $\DD$. If $p\ne q$ are fixed points of $f$, then $F(\phi(p))=\phi(f(p))=\phi(p)$ and likewise for $q$, and $\phi(p)\ne\phi(q)$ by injectivity: so $F$ has the two distinct fixed points $\alpha=\phi(p)$, $\beta=\phi(q)$.
:::

:::

::: {.pf-step #normalise}
With $T$ a disc automorphism sending $\alpha$ to $0$, the map $H=T\circ F\circ T^{-1}$ fixes $0$ and the nonzero point $T(\beta)$.

::: pf-proof
Such a $T$ is $T(z)=e^{i\theta}\dfrac{z-\alpha}{1-\bar\alpha z}$ or simply $\dfrac{z-\alpha}{1-\bar\alpha z}$, a biholomorphism of $\DD$. Then $H(0)=T(F(T^{-1}(0)))=T(F(\alpha))=T(\alpha)=0$, and $H(T(\beta))=T(F(\beta))=T(\beta)$, where $T(\beta)\ne0$ since $T$ is injective and $T(\alpha)=0$.
:::

:::

::: {.pf-step #schwarz}
$H$ is the identity.

::: pf-proof
$H$ is a holomorphic self-map of $\DD$ with $H(0)=0$, so the Schwarz lemma gives $\abs{H(z)}\le\abs{z}$ for all $z\in\DD$. At the fixed point $w=T(\beta)\ne0$ of step [](#normalise){.pf-ref} one has $\abs{H(w)}=\abs{w}$, so the equality case of the Schwarz lemma applies and $H(z)=e^{i\theta}z$ for some $\theta$. Then $w=H(w)=e^{i\theta}w$ with $w\ne0$ forces $e^{i\theta}=1$, so $H(z)=z$.
:::

:::

::: {.pf-qed}
$H=\mathrm{id}$ by step [](#schwarz){.pf-ref}, hence $F=T^{-1}\circ H\circ T=\mathrm{id}$ and $f=\phi^{-1}\circ F\circ\phi=\mathrm{id}$: $f(z)=z$.
:::

:::

:::
