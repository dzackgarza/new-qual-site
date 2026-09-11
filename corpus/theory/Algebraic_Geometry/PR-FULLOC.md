---
schema: qual/card@1
id: PR-FULLOC
kind: proposition
title: A face gives a principal open subset, which is how the affine charts glue
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Cones
  - Affine Varieties
relations:
- kind: uses
  target: D-Q7Q2N
- kind: uses
  target: PR-FULFACET
review: draft
prompts:
- Why is the affine chart of a face an open subset of the chart of the cone?
- What function is inverted when passing from U_sigma to U_tau?
---

::: {.proposition title="Localisation at a face"}
Let $\tau \leq \sigma$ be a face, written $\tau = \sigma \intersect u_\tau^\perp$ for some $u_\tau \in S_\sigma = \sigma\dual \intersect M$.
Then
\[
S_\tau = S_\sigma + \NN \cdot (-u_\tau) ,
\]
so
\[
k[S_\tau] = k[S_\sigma]\big[ \chi^{-u_\tau} \big] = k[S_\sigma]_{\chi^{u_\tau}} , \qquad U_\tau = D\big( \chi^{u_\tau} \big) \subseteq U_\sigma ,
\]
a principal open subset.
:::

::: {.remark title="This is the gluing"}
The construction of $X_\Sigma$ says the $U_\sigma$ are glued along the charts of their common faces, and this proposition is what makes that meaningful.
If $\sigma_1 \intersect \sigma_2 = \tau$ is a common face, then $U_\tau$ sits inside each of $U_{\sigma_1}$ and $U_{\sigma_2}$ as a principal open subset, and the gluing is the identity on $U_\tau$.
Both inclusions are open immersions, so the result is a variety and not just a topological quotient, and the compatibility on triple overlaps is automatic because every chart is a localisation of the coordinate ring of the smallest cone.

The inclusion is order-reversing on cones: a smaller cone has a larger dual, hence a larger semigroup and a larger ring, hence a smaller variety.
\[
\tau \leq \sigma \implies \sigma\dual \subseteq \tau\dual \implies U_\tau \subseteq U_\sigma .
\]
The zero cone gives $S_{\ts{0}} = M$ and $U_{\ts{0}} = T$, which is therefore contained in every chart: that is why the torus is dense in $X_\Sigma$.
:::

::: {.example title="The plane, in two charts"}
Take $\sigma_1 = \Cone(e_1, e_2)$ and the face $\tau = \Cone(e_1)$, cut out by $u_\tau = e_2\dual$.
Then $S_{\sigma_1} = \NN^2$ and
\[
S_\tau = \NN^2 + \NN \cdot (0,-1) = \NN \oplus \ZZ , \qquad U_\tau = \Spec k[x, y^{\pm 1}] = D(y) \subseteq \AA^2 .
\]
For $\PP^1$, the two maximal cones $\RR_{\geq 0}$ and $\RR_{\leq 0}$ share the face $\ts{0}$, whose chart is $\Spec k[x^{\pm 1}] = \GG_m$, inverted from $k[x]$ on one side and from $k[x\inv]$ on the other; the gluing $x \mapsto x\inv$ is forced.
:::
