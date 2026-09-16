---
schema: qual/card@1
id: D-ETFPPF
kind: definition
title: The étale and fppf topologies, and the small étale site
classification:
  areas:
  - algebraic-geometry
  topics:
  - Etale Topology
  - Fppf Topology
  - Grothendieck Topologies
relations:
- kind: uses
  target: D-GROTHTOP
- kind: uses
  target: D-MORETALE
- kind: uses
  target: D-MORFLAT
review: draft
prompts:
- What is the étale topology?
- What is the fppf topology?
- What is the étale site of a scheme?
---

Let $S$ be a scheme and $\Sch_{/S}$ the category of $S$-schemes.

::: {.definition title="Étale and fppf topologies"}
A family of $S$-morphisms $\{U_i \to U\}_i$ in $\Sch_{/S}$ is an

- \dfn{étale covering} if each $U_i \to U$ is étale and $\bigsqcup_i U_i \to U$ is surjective;

- \dfn{fppf covering} if each $U_i \to U$ is flat and locally of finite presentation and $\bigsqcup_i U_i \to U$ is surjective.

With these coverings $\Sch_{/S}$ is the \dfn{big étale site} $(\Sch_{/S})_{\mathrm{et}}$, respectively the \dfn{big fppf site} $(\Sch_{/S})_{\mathrm{fppf}}$.
:::

::: {.definition title="Small étale site"}
The \dfn{small étale site} $S_{\mathrm{et}}$ of $S$ is the full subcategory of $\Sch_{/S}$ whose objects are the étale morphisms $U \to S$, with the étale coverings as coverings.
:::

::: {.remark}
Every Zariski open covering is an étale covering, and every étale covering is an fppf covering, because étale morphisms are flat and locally of finite presentation.
So every fppf sheaf is an étale sheaf, and every étale sheaf restricts to a Zariski sheaf on each $S$-scheme.
:::

::: {.theorem title="Representable functors are sheaves"}
For every $S$-scheme $X$, the functor $h_X = \Hom_S(-, X)$ is a sheaf on $(\Sch_{/S})_{\mathrm{fppf}}$, hence on $(\Sch_{/S})_{\mathrm{et}}$.
For every quasicoherent $\OO_S$-module $\mathcal{M}$, the functor $(f \colon U \to S) \mapsto \Gamma(U, f^* \mathcal{M})$ is an fppf sheaf.
:::

::: {.example}
Let $n \geq 1$ be invertible on $S$.
On $S_{\mathrm{et}}$, the multiplicative group $\GG_m \colon U \mapsto \Gamma(U, \OO_U)^\times$ and its subgroup $\mu_n$ of $n$-th roots of unity fit into the \dfn{Kummer sequence}
$$1 \to \mu_n \to \GG_m \xrightarrow{\, u \mapsto u^n \,} \GG_m \to 1,$$
which is exact on $S_{\mathrm{et}}$: for a unit $u$ on $U$, the morphism $U' = \Spec_U \OO_U[z]/(z^n - u) \to U$ is étale and surjective, because $n$ and $u$ are invertible, and $u$ has the $n$-th root $z$ on $U'$.
The sequence is not exact for the Zariski topology.
For $S = U = \Spec \CC[t, t^{-1}]$ and $n = 2$, the unit $t$ is not a square on any nonempty Zariski open subset $V \subseteq U$: $V$ is dense and $\OO(V) \subseteq \CC(t)$, and $t$ is not a square in $\CC(t)$.
:::
