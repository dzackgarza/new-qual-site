---
schema: qual/card@1
id: P-TOPSU15H
kind: problem
title: 'A CW complex with $\pi_1\cong\ZZ^2$ and no higher homotopy is $S^1\times S^1$; surface groups have no $\ZZ^2$ subgroups'
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Homotopy Type
  - Fundamental Group
  - Surfaces
relations: []
review: draft
---

::: problem
Suppose $X$ is a path-connected CW-complex with $\pi_1(X) \cong \mathbb{Z}^2$ and $\pi_{\geq 2}(X) = 0$.
Show that $X$ is homotopy-equivalent to $S^1 \times S^1$.
Use this to show that the fundamental group of a closed orientable surface $\Sigma_g$ of genus $g \geq 2$ cannot contain a subgroup isomorphic to $\mathbb{Z}^2$.
:::::: {.solution}
<1>1. Choose loops in $X$ representing a basis of $\pi_1(X)\cong\mathbb Z^2$. Since their commutator is null-homotopic, these loops extend across the standard $2$-cell of the torus to a map
$$f:T^2\to X$$
which induces an isomorphism on $\pi_1$.
::: {.proof}
The standard CW presentation of the torus is one $0$-cell, two $1$-cells $a,b$, and one $2$-cell attached by the commutator $aba^{-1}b^{-1}$. The chosen loops commute in $\pi_1(X)$, so the attaching loop maps null-homotopically and the map on the $1$-skeleton extends.
:::

<1>2. The map $f$ is an isomorphism on every homotopy group.
::: {.proof}
It is an isomorphism on $\pi_1$ by construction. Both $T^2$ and $X$ have vanishing $\pi_k$ for $k\ge2$: the torus has universal cover $\mathbb R^2$, while this vanishing is assumed for $X$.
:::

<1>3. Therefore
$$\boxed{X\simeq T^2=S^1\times S^1.}$$
::: {.proof}
Both spaces are CW complexes, so Whitehead's theorem applies to the weak homotopy equivalence in <1>2.
:::

<1>4. Now suppose $\pi_1(\Sigma_g)$ contained a subgroup $H\cong\mathbb Z^2$. Let $p:\widetilde\Sigma\to\Sigma_g$ be the connected covering corresponding to $H$.
::: {.proof}
Closed orientable surfaces are path connected, locally path connected, and semilocally simply connected, so the subgroup-covering correspondence applies.
:::

<1>5. The covering surface $\widetilde\Sigma$ is aspherical and has $\pi_1(\widetilde\Sigma)\cong\mathbb Z^2$, hence by <1>1--<1>3
$$\widetilde\Sigma\simeq T^2.$$
::: {.proof}
The universal cover of $\widetilde\Sigma$ is also the universal cover of $\Sigma_g$, namely the plane, so all higher homotopy groups vanish.
:::

<1>6. The cover cannot have finite degree.
::: {.proof}
If it had degree $d$, then
$$\chi(\widetilde\Sigma)=d\chi(\Sigma_g)=d(2-2g)<0,$$
whereas homotopy equivalence to $T^2$ gives Euler characteristic $0$.
:::

<1>7. The cover cannot have infinite degree either.
::: {.proof}
An infinite-sheeted connected cover of the compact surface $\Sigma_g$ is noncompact. Every connected noncompact surface has $H_2(-;\mathbb Z)=0$, while <1>5 gives $H_2(\widetilde\Sigma;\mathbb Z)\cong H_2(T^2;\mathbb Z)\cong\mathbb Z$.
:::

<1>8. Hence
$$\boxed{\pi_1(\Sigma_g)\text{ contains no subgroup isomorphic to }\mathbb Z^2\quad(g\ge2).}$$
::: {.proof}
The finite- and infinite-index cases in <1>6--<1>7 exhaust all possibilities.
:::
:::

