---
schema: qual/card@1
id: D-SHFFINE
kind: definition
title: Soft and fine sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaf Cohomology
  - Acyclic Sheaves
  - Partitions of Unity
relations:
- kind: related-to
  target: D-COHFLQ
review: draft
prompts:
- What is a fine sheaf?
- What is a soft sheaf?
- What is a c-soft sheaf?
---

::: {.definition title="Soft and fine sheaves"}
Let $X$ be a locally compact paracompact Hausdorff space and $\mathcal{F}$ a sheaf of abelian groups on $X$.

- $\mathcal{F}$ is \dfn{soft} if for every closed $Z \subseteq X$ the restriction $\Gamma(X, \mathcal{F}) \to \Gamma(Z, \mathcal{F}\restrict_Z)$ is surjective.

- $\mathcal{F}$ is \dfn{c-soft} if for every compact $K \subseteq X$ the restriction
  $$
  \Gamma_c(X,\mathcal F)
  \longrightarrow
  \Gamma(K,\mathcal F\restrict_K)
  $$
  is surjective, where $\Gamma_c(X,\mathcal F)$ denotes the global sections with compact support.

- $\mathcal{F}$ is \dfn{fine} if for every locally finite open cover $\{U_i\}$ of $X$ there are sheaf endomorphisms $\eta_i \colon \mathcal{F} \to \mathcal{F}$ with the support of $\eta_i$ contained in $U_i$ and $\sum_i \eta_i = \id_{\mathcal{F}}$.
:::

::: {.proposition}
1. A flasque sheaf is soft.

2. On a paracompact Hausdorff space, a fine sheaf is soft.

3. On a paracompact Hausdorff space, a soft sheaf is acyclic: $H^i(X, \mathcal{F}) = 0$ for $i > 0$, so a resolution of a sheaf by fine sheaves computes its cohomology.

4. On a locally compact Hausdorff space, a c-soft sheaf is acyclic for compactly supported sections:
$$
R^i\Gamma_c(X,\mathcal F)=0
\qquad(i>0).
$$
:::

::: {.proof}
**(1)**
Let $\mathcal{F}$ be flasque and $Z\subseteq X$ closed; no hypothesis on $X$ is used.
Because $Z$ is closed and sections of a sheaf agree on overlaps, a section of $\restrictionof{\mathcal{F}}{Z}$ is a section over an open neighbourhood:
$$
\Gamma(Z,\restrictionof{\mathcal{F}}{Z})=\colim_{U\supseteq Z}\mathcal{F}(U),
$$
the colimit over the open neighbourhoods of $Z$.
So $s\in\Gamma(Z,\restrictionof{\mathcal{F}}{Z})$ is represented by $s_U\in\mathcal{F}(U)$ for some open $U\supseteq Z$, and flasqueness of $\mathcal{F}$ gives $t\in\mathcal{F}(X)$ restricting to $s_U$, hence to $s$.

**(2)**
Let $\mathcal{F}$ be fine, $Z\subseteq X$ closed, and $s\in\Gamma(Z,\restrictionof{\mathcal{F}}{Z})$.
Each point of $Z$ has an open neighbourhood over which $s$ is the restriction of a section of $\mathcal{F}$, so some open cover $\mathfrak{U}$ of $X$ has $s$ extend over $Z\cap U$ for every $U\in\mathfrak{U}$; adjoin $X\sm Z$ to that cover.
By paracompactness $\mathfrak{U}$ has a locally finite open refinement $\{U_i\}_{i\in I}$, and fineness of $\mathcal{F}$ gives endomorphisms $\eta_i\colon\mathcal{F}\to\mathcal{F}$ with $\supp\eta_i\subseteq U_i$ and $\sum_i\eta_i=\id$.

For each $i$ choose $t_i\in\mathcal{F}(U_i)$ restricting to $s$ on $Z\cap U_i$.
The section $\eta_i(t_i)$ of $\mathcal{F}$ over $U_i$ vanishes off $\supp\eta_i$, so it and the zero section agree on the overlap of $\{U_i, X\sm\supp\eta_i\}$, and the sheaf axiom glues them to a global section; the resulting family is locally finite, so
$$
t\coloneqq\sum_i\eta_i(t_i)
$$
is a well-defined global section.
For $x\in Z$ the sum has finitely many nonzero terms, and for each of them $x\in U_i$, so $(t_i)_x=s_x$ and
$$
t_x=\sum_i(\eta_i)_x(s_x)=(\textstyle\sum_i\eta_i)_x(s_x)=s_x .
$$
Hence $t$ restricts to $s$, and $\mathcal{F}$ is soft.

**(3) and (4) are not argued here.** They are the two instances in use of a theorem on families of supports, stated in the remark below.
No converse is claimed: a soft sheaf need not be flasque, the sheaf of smooth functions on a manifold being soft and not flasque.
:::

::: {.remark title="Support for (3) and (4)"}
Let $\Phi$ be a paracompactifying family of supports on $X$ and $\mathcal{A}$ a sheaf of abelian groups; then $H_\Phi^n(X,\mathcal{A})=0$ for every $n\ge1$ if $\mathcal{A}$ is flasque, and also if $\mathcal{A}$ is $\Phi$-soft (Godement, *Topologie algébrique et théorie des faisceaux*, Chapitre II, Théorème 4.4.3).
Taking $\Phi$ to be the family of all closed subsets, $\Phi$-soft means soft and $H_\Phi$ is ordinary sheaf cohomology, which gives (3); taking $\Phi$ to be the relatively compact subsets, $\Phi$-soft means $c$-soft and $H_\Phi$ is the cohomology of $\Gamma_c$, which gives (4) and asks only for local compactness of $X$.
A resolution by $\Phi$-soft sheaves computes $H_\Phi$ (Godement, Chapitre II, Théorème 4.6.2 and §4.7), so a fine resolution computes ordinary cohomology and a $c$-soft resolution computes compactly supported cohomology.
:::

::: {.example}
On a smooth manifold $M$, the sheaf $\mathcal{C}^\infty_M$ of smooth functions is fine, using a smooth partition of unity subordinate to the cover, and so is every sheaf of $\mathcal{C}^\infty_M$-modules, such as the sheaves $\mathcal{A}^p$ of smooth $p$-forms.
The de Rham complex $0 \to \underline{\RR} \to \mathcal{A}^0 \to \mathcal{A}^1 \to \cdots$ is a fine resolution of the constant sheaf, which proves $H^p(M, \RR) \cong H^p_{\mathrm{dR}}(M)$.
The sheaf of holomorphic functions on $\CC$ is not soft: a function holomorphic near the closed set $\{0, 1\}$, equal to $0$ near $0$ and $1$ near $1$, does not extend to an entire function.
:::
