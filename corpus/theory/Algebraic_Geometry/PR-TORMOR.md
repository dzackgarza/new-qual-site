---
schema: qual/card@1
id: PR-TORMOR
kind: proposition
title: Toric morphisms, completeness, and invariants read off the fan
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Morphisms
  - Properness
relations:
- kind: uses
  target: PR-O8V3I
review: draft
prompts:
- What is a toric morphism, on lattices and on varieties?
- When is a toric variety complete, and why?
---

::: {.definition title="Toric morphism"}
A lattice map $\phi : N_1 \to N_2$ is **compatible** with fans $\Sigma_1, \Sigma_2$ if every $\sigma_1 \in \Sigma_1$ has some $\sigma_2 \in \Sigma_2$ with $\phi_\RR(\sigma_1) \subseteq \sigma_2$.
Such a $\phi$ induces $X_{\Sigma_1} \to X_{\Sigma_2}$ carrying $T_1$ into $T_2$ by a group homomorphism, and every equivariant morphism arises this way.
On affine pieces this is a semigroup map $S_2 \to S_1$ inducing $k[S_2] \to k[S_1]$.
:::

::: {.proposition title="Completeness"}
$X_\Sigma$ is complete iff $\abs{\Sigma} = N_\RR$.
More generally $\phi$ is proper iff $\phi_\RR\inv(\abs{\Sigma_2}) = \abs{\Sigma_1}$.
:::

::: {.remark title="Why, in one picture"}
Each $u \in N$ gives a one-parameter subgroup $\lambda^u : \GG_m \to T$, and the valuative criterion asks whether $\lim_{t \to 0} \lambda^u(t)$ exists in $X_\Sigma$.
It does exactly when $u$ lies in some cone of $\Sigma$, and the limit is the distinguished point $x_\sigma$ of the smallest cone containing $u$.
So full support means every one-parameter subgroup converges, which is completeness.

For $\PP^2$ with $T = \ts{(1 : s : t)}$ and $\lambda^u(t) = (1 : t^{u_1} : t^{u_2})$, the three maximal cones of the fan are precisely the three regions of $u$ sending the limit to each of the three coordinate points.
:::

::: {.remark title="Two cheap invariants"}
\[
\pi_1(X_\Sigma) \cong N / N', \qquad N' = \gens{ \sigma \intersect N \st \sigma \in \Sigma } ,
\]
so a fan whose rays generate $N$ gives a simply connected variety.
For $X_\Sigma$ smooth and complete, the topological Euler characteristic is the number of maximal cones,
\[
\chi(X_\Sigma) = \size \Sigma(n) ,
\]
because the torus orbits give a cell decomposition and only the fixed points contribute.
:::
