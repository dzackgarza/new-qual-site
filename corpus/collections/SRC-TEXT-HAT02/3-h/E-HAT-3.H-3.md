---
schema: qual/card@1
id: E-HAT-3.H-3
kind: problem
title: "Classification of group bundles via $B\\operatorname{Aut}(G)$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.H, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $\mathcal{B}(X; G)$ be the set of isomorphism classes of bundles of groups $E \to X$ with fiber $G$, and let $E_0 \to B\operatorname{Aut}(G)$ be the bundle corresponding to the "identity" action $\rho: \operatorname{Aut}(G) \to \operatorname{Aut}(G)$.
Show that the map $[X, B\operatorname{Aut}(G)] \to \mathcal{B}(X; G)$, $[f] \mapsto f^*(E_0)$, is a bijection if $X$ is a CW complex, where $[X, Y]$ denotes the set of homotopy classes of maps $X \to Y$.
:::

::: {.solution}
Regard $\Gamma:=\operatorname{Aut}(G)$ as a discrete group and take $B\Gamma$ to be a $K(\Gamma,1)$; by Theorem 1B.8 (p. 90) its homotopy type is determined by $\Gamma$. Then
$$
B\operatorname{Aut}(G)=K(\operatorname{Aut}(G),1),
$$
and the bundle $E_0\to B\operatorname{Aut}(G)$ associated to the identity action is the universal bundle of groups with fiber $G$.

Assume first that $X$ is connected and choose a basepoint. A bundle of groups $E\to X$ with fiber $G$ has monodromy
$$
\rho_E:\pi_1(X)\longrightarrow\operatorname{Aut}(G),
$$
well-defined up to conjugation by an automorphism of the chosen fiber. Conversely, a homomorphism
$$
\rho:\pi_1(X)\to\operatorname{Aut}(G)
$$
defines the bundle
$$
\widetilde X\times_{\pi_1(X)}G\longrightarrow X,
$$
where the deck group acts on $G$ through $\rho$. These two constructions are inverse. Indeed, the dictionary is stated in §3.H (p. 331): covering spaces that are bundles of groups with fiber $G$ are equivalent to actions of $\pi_1(X)$ on $G$ by automorphisms of $G$, that is, to homomorphisms $\pi_1(X)\to\operatorname{Aut}(G)$; it rests on the classification of covering spaces of §1.3 (Theorem 1.38, p. 67; the permutation description, pp. 68-70). An isomorphism of bundles of groups over $X$ between $\widetilde X\times_\rho G$ and $\widetilde X\times_{\rho'}G$ is a $\pi_1(X)$-equivariant family of group automorphisms of the fiber, i.e. an element $c\in\operatorname{Aut}(G)$ with $c\,\rho(\gamma)=\rho'(\gamma)\,c$ for all $\gamma$, so $\rho'=c\rho c^{-1}$: the ambiguity is conjugation *in the group $\operatorname{Aut}(G)$*, by its own elements. Thus
$$
\mathcal B(X;G)
\cong
\operatorname{Hom}(\pi_1X,\operatorname{Aut}(G))/\text{conjugacy in }\operatorname{Aut}(G).
$$

Since $B\operatorname{Aut}(G)$ is a $K(\Gamma,1)$ with $\Gamma=\operatorname{Aut}(G)$ and $X$ is a connected CW complex, Proposition 1B.9 (p. 90) gives the classification of maps into such a space: every homomorphism $\pi_1(X)\to\Gamma$ is induced by a map $X\to B\Gamma$, uniquely up to homotopy relative to the basepoint. Dropping the basepoint replaces "unique up to based homotopy" by "unique up to homotopy and conjugation in $\Gamma$", because transporting the image of the basepoint along a path in $B\Gamma$ conjugates $f_*$ by the class of that path (Proposition 1B.9, p. 90; $\Gamma$ is not assumed abelian). Hence
$$
[X,B\operatorname{Aut}(G)]
\cong
\operatorname{Hom}(\pi_1X,\operatorname{Aut}(G))/\text{conjugacy in }\operatorname{Aut}(G).
$$
Under this correspondence, a map $f:X\to B\operatorname{Aut}(G)$ corresponds to the monodromy homomorphism $f_*$: pulling back commutes with monodromy, so the bundle $f^*E_0$ has monodromy $\mathrm{id}_\Gamma\circ f_*=f_*$ and these are the same quotient set on the two sides. Since the displayed identification is precisely the map
$$
[f]\longmapsto f^*(E_0),
$$
it is a bijection. For disconnected $X$, apply the same argument independently on each component: both $\mathcal B(X;G)$ and $[X,B\operatorname{Aut}(G)]$ split as products over the components of $X$.
:::
