---
schema: qual/card@1
id: D-TORSOR
kind: definition
title: Torsors under a sheaf of groups
classification:
  areas:
  - algebraic-geometry
  topics:
  - Torsors
  - Grothendieck Topologies
  - Picard Group
relations:
- kind: uses
  target: D-GROTHTOP
- kind: related-to
  target: PR-DIVLB
review: draft
prompts:
- What is a torsor?
- How are torsors classified by cohomology?
---

::: {.definition title="Torsor"}
Let $\mathcal{C}$ be a site with a terminal object $X$, and $\mathcal{G}$ a sheaf of groups on $\mathcal{C}$.
A \dfn{$\mathcal{G}$-torsor} is a sheaf of sets $\mathcal{P}$ on $\mathcal{C}$ with a right action $\mathcal{P} \times \mathcal{G} \to \mathcal{P}$ such that

1. there is a covering $\{U_i \to X\}$ with $\mathcal{P}(U_i) \neq \emptyset$ for every $i$, and

2. the morphism $\mathcal{P} \times \mathcal{G} \to \mathcal{P} \times \mathcal{P}$, $(p, g) \mapsto (p, pg)$, is an isomorphism of sheaves.

A morphism of $\mathcal{G}$-torsors is a $\mathcal{G}$-equivariant morphism of sheaves.
The \dfn{trivial torsor} is $\mathcal{G}$ acting on itself by right multiplication.
:::

::: {.proposition}
A $\mathcal{G}$-torsor $\mathcal{P}$ is trivial exactly when $\mathcal{P}(X) \neq \emptyset$, and every morphism of $\mathcal{G}$-torsors is an isomorphism.
Isomorphism classes of $\mathcal{G}$-torsors trivialized on a covering $\mathfrak{U} = \{U_i \to X\}$ are in bijection with the Čech cohomology set $\check{H}^1(\mathfrak{U}, \mathcal{G})$, and all torsors with $\check{H}^1(X, \mathcal{G}) = \varinjlim_{\mathfrak{U}} \check{H}^1(\mathfrak{U}, \mathcal{G})$; for $\mathcal{G}$ abelian this is $H^1(X, \mathcal{G})$.
:::

::: {.example}
On a scheme $X$ with the Zariski topology, a $\GG_m = \OO_X^\times$-torsor is the sheaf of nowhere-vanishing local sections of an invertible sheaf $\mathcal{L}$, so $\Pic X \cong H^1(X, \OO_X^\times)$ ([[PR-DIVLB]]).
Likewise $\operatorname{GL}_n$-torsors correspond to locally free sheaves of rank $n$, through their sheaves of local frames.
:::

::: {.example}
Let $k$ be a field and $n$ invertible in $k$.
On $(\Spec k)_{\mathrm{et}}$, the Kummer sequence of [[D-ETFPPF]] and $H^1((\Spec k)_{\mathrm{et}}, \GG_m) = 0$ (Hilbert's Theorem 90) give $H^1((\Spec k)_{\mathrm{et}}, \mu_n) \cong k^\times / (k^\times)^n$.
The torsor corresponding to $a \in k^\times$ is $\Spec k[z]/(z^n - a)$ with $\mu_n$ acting by $z \mapsto \zeta z$.
:::
