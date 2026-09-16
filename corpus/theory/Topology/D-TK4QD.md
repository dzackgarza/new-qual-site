---
schema: qual/card@1
id: D-TK4QD
kind: definition
title: Intersection product and intersection pairing
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Cohomology
  - Manifolds
relations: []
review: draft
---

::: {.definition}
Let $M$ be a closed connected oriented $n$-manifold with fundamental class $[M]\in H_n(M;\ZZ)$, and let $D\colon H^k(M;\ZZ)\to H_{n-k}(M;\ZZ)$, $D(\varphi)=[M]\frown\varphi$, be the [[D-QP7WI|Poincaré duality]] isomorphism.
The \dfn{intersection product} is the bilinear map
$$
H_i(M;\ZZ)\times H_j(M;\ZZ)\to H_{i+j-n}(M;\ZZ),\qquad \alpha\cdot\beta\coloneqq[M]\frown\qty{D\inv(\alpha)\smile D\inv(\beta)},
$$
using the [[D-B2JER|cup product]] and the [[D-RQS4J|cap product]].
For $j=n-i$, composing with $H_0(M;\ZZ)\cong\ZZ$ gives the \dfn{intersection pairing} $H_i(M;\ZZ)\times H_{n-i}(M;\ZZ)\to\ZZ$.
:::

::: {.proposition}
The intersection pairing vanishes when either argument is a torsion class, and the induced pairing
$$
H_i(M;\ZZ)/\mathrm{torsion}\times H_{n-i}(M;\ZZ)/\mathrm{torsion}\to\ZZ
$$
is nondegenerate: its adjoint is an isomorphism onto $\Hom(H_{n-i}(M;\ZZ)/\mathrm{torsion},\ZZ)$.
This is the cup product pairing of [@Hat02, Prop. 3.38] transported by $D$.
:::

::: {.remark}
If $A,B\subseteq M$ are closed oriented submanifolds of dimensions $i$ and $j$ that intersect transversely, with fundamental classes representing $\alpha$ and $\beta$, then $\alpha\cdot\beta$ is represented by the submanifold $A\cap B$ of dimension $i+j-n$ with its induced orientation.
When $i+j=n$, the intersection $A\cap B$ is a finite set of points and $\alpha\cdot\beta\in\ZZ$ is the number of intersection points counted with signs given by the orientations.
:::
