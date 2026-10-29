---
schema: qual/card@1
id: PR-FULLOC
kind: proposition
title: Face charts are principal opens
slogan: 'A face inclusion is localization: invert its cutting character, and the face chart becomes a principal open in the cone chart.'
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
- What function is inverted when passing from $U_\sigma$ to $U_\tau$?
---

::: {.proposition title="Localisation at a face"}
Let $N$ be a lattice with dual lattice $M$, let $\sigma\subseteq N_\RR$ be a strongly convex rational polyhedral cone, and let $\tau\leq\sigma$ be a face. Choose
$$
u_\tau\in\operatorname{relint}(\sigma^\vee\cap\tau^\perp)\cap M,
$$
so that $\tau=\sigma\cap u_\tau^\perp$ and $u_\tau\in S_\sigma=\sigma^\vee\cap M$.
Then
$$
S_\tau = S_\sigma + \NN \cdot (-u_\tau) ,
$$
so
$$
k[S_\tau] = k[S_\sigma]\big[ \chi^{-u_\tau} \big] = k[S_\sigma]_{\chi^{u_\tau}} , \qquad U_\tau = D\big( \chi^{u_\tau} \big) \subseteq U_\sigma ,
$$
a principal open subset.
:::

::: {.remark title="Gluing along common faces"}
If $\sigma_1\cap\sigma_2=\tau$ is a common face in a fan, the proposition gives open immersions
$$
U_\tau\hookrightarrow U_{\sigma_1},\qquad
U_\tau\hookrightarrow U_{\sigma_2}.
$$
The toric variety $X_\Sigma$ is obtained by identifying these two copies of $U_\tau$ by the identity. For three cones, the corresponding localizations agree on the chart of their common intersection, giving the cocycle compatibility required for gluing schemes.

Face inclusion is contravariant on affine charts:
$$
\tau \leq \sigma \implies \dualof{\sigma} \subseteq \dualof{\tau} \implies U_\tau \subseteq U_\sigma .
$$
For the zero cone, $S_{\theset{0}}=M$ and $U_{\theset{0}}=\Spec k[M]=T_N$. This is a nonempty open subset of every irreducible affine chart $U_\sigma$, hence is dense in every chart and in $X_\Sigma$.
:::

::: {.example title="The plane, in two charts"}
Take $\sigma_1 = \Cone(e_1, e_2)$ and the face $\tau = \Cone(e_1)$, cut out by $u_\tau = \dualof{e_2}$.
Then $S_{\sigma_1} = \NN^2$ and
$$
S_\tau = \NN^2 + \NN \cdot (0,-1) = \NN \oplus \ZZ , \qquad U_\tau = \Spec k[x, y^{\pm 1}] = D(y) \subseteq \AA^2 .
$$
For $\PP^1$, the two maximal cones $\RR_{\geq 0}$ and $\RR_{\leq 0}$ share the face $\theset{0}$, whose chart is $\Spec k[x^{\pm 1}] = \GG_m$. It is obtained by localizing $k[x]$ at $x$ on one side and $k[\inverseof{x}]$ at $\inverseof{x}$ on the other, and the transition map sends $x\mapsto \inverseof{x}$.
:::
