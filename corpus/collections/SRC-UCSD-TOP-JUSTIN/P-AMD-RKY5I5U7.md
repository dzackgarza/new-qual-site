---
schema: qual/card@1
id: P-AMD-RKY5I5U7
kind: problem
title: Hexagon with opposite sides glued by translations is a torus
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Surfaces
  - Homeomorphisms
relations: []
review: draft
---

::: {.problem}
Define the torus $T$ as the quotient of $\RR^2$ by the action of the integral translation group $\ZZ^2$.
Show that the space $X$, a solid hexagon whose sides are glued in pairs according to the labelled arrows of the source figure (each side glued to the opposite side, with the arrows pointing the same way), is homeomorphic to $T$. A clear description of the homeomorphism is enough.
:::

::: {.solution}

::: pf

::: {.pf-step #lattice}

Let $H\subset\RR^2$ be a regular hexagon with centre $0$ and inradius $r$, and let $u_1,u_2,u_3$ be the translations that carry the sides labelled $a$, $b$, $c$ onto their opposite sides. With suitable signs, $u_3=u_2-u_1$. The lattice $\Lambda=\ZZ u_1+\ZZ u_2$ contains all three, and the translates $H+\lambda$, $\lambda\in\Lambda$, tile $\RR^2$ with disjoint interiors.

::: pf-proof

Each $u_i$ is twice the vector from $0$ to the midpoint of a side, so the three vectors are $2r e^{i\theta}$ for $\theta=\pi/6,\pi/2,5\pi/6$, and $2re^{5\pi i/6}=2re^{\pi i/2}-2re^{\pi i/6}$. The tiling of the plane by regular hexagons has its centres at exactly this lattice.

:::

:::

::: {.pf-step #quot}

The composite $q:H\hookrightarrow\RR^2\to\RR^2/\Lambda$ induces a homeomorphism $X\to\RR^2/\Lambda$.

::: pf-proof

By Step [](#lattice){.pf-ref}, $H$ is a fundamental domain for $\Lambda$, so $q$ is surjective and injective on the interior of $H$. Two distinct boundary points have the same image exactly when they differ by an element of $\Lambda$; for points of $H$ these are the side pairings $\pm u_i$, together with their composites at the vertices, which fall into two classes of three. These are the identifications that define $X$, so $q$ induces a continuous bijection $X\to\RR^2/\Lambda$. Since $X$ is compact and $\RR^2/\Lambda$ is Hausdorff, it is a homeomorphism.

:::

:::

::: pf-qed

The linear map $A:\RR^2\to\RR^2$ with $Au_1=e_1$ and $Au_2=e_2$ carries $\Lambda$ onto $\ZZ^2$, so it induces a homeomorphism $\RR^2/\Lambda\to\RR^2/\ZZ^2=T$. With Step [](#quot){.pf-ref}, the homeomorphism $X\to T$ sends a point $p$ of the hexagon to the class of $Ap$.

:::

:::

:::
