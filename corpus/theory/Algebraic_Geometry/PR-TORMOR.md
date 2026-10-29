---
schema: qual/card@1
id: PR-TORMOR
kind: definition
title: Toric morphisms, completeness, and topological invariants
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

A toric variety is complete exactly when its fan fills the lattice space; toric properness is the same support condition after pullback.

::: {.definition title="Toric morphism"}
A lattice map $\phi : N_1 \to N_2$ is \dfn{compatible} with fans $\Sigma_1, \Sigma_2$ if every $\sigma_1 \in \Sigma_1$ has some $\sigma_2 \in \Sigma_2$ with $\phi_\RR(\sigma_1) \subseteq \sigma_2$.
Such a $\phi$ induces $X_{\Sigma_1} \to X_{\Sigma_2}$ carrying $T_1$ into $T_2$ by a group homomorphism, and every equivariant morphism arises this way.
On affine pieces this is a semigroup map $S_2 \to S_1$ inducing $k[S_2] \to k[S_1]$.
:::

::: {.proposition title="Completeness"}
$X_\Sigma$ is complete iff $\abs{\Sigma} = N_\RR$.
More generally $\phi$ is proper iff $\inverseof{\phi_\RR}(\abs{\Sigma_2}) = \abs{\Sigma_1}$.
:::

::: {.remark title="One-parameter subgroups"}
Each $u \in N$ gives a one-parameter subgroup $\lambda^u : \GG_m \to T$, and the valuative criterion asks whether $\lim_{t \to 0} \lambda^u(t)$ exists in $X_\Sigma$.
It does exactly when $u$ lies in some cone of $\Sigma$, and the limit is the distinguished point $x_\sigma$ of the smallest cone containing $u$.
Thus $\abs\Sigma=N_\RR$ exactly when every one-parameter subgroup extends across $0$.

For $\PP^2$ with $T = \theset{(1 : s_1 : s_2)}$ and $\lambda^u(t) = (1 : t^{u_1} : t^{u_2})$, the three maximal cones of the fan are precisely the three regions of $u$ sending the limit to each of the three coordinate points.
:::

::: {.remark title="Topology over $\CC$"}
Assume $k=\CC$ and give $X_\Sigma(\CC)$ its classical topology.
Let
$$
N_\Sigma\coloneqq\generators{\sigma\cap N\st\sigma\in\Sigma}\subseteq N.
$$
Then
$$
\pi_1\bigl(X_\Sigma(\CC)\bigr)\cong N/N_\Sigma
$$
[@Ful93, §3.2].
In particular, if $N_\Sigma=N$, then $X_\Sigma(\CC)$ is simply connected.

If $X_\Sigma$ is complete of dimension $n$, additivity of the topological Euler characteristic across the torus-orbit decomposition gives
$$
\chi\bigl(X_\Sigma(\CC)\bigr)=\size{\Sigma(n)},
$$
because an orbit of positive dimension is isomorphic to $(\CC^\times)^r$ for some $r>0$ and has Euler characteristic $0$, while each zero-dimensional orbit contributes $1$ [@Ful93, §3.2].
:::
