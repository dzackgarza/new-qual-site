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

Let $\mathcal{B}(X; G)$ be the set of isomorphism classes of bundles of groups $E \to X$ with fiber $G$, and let $E_0 \to B\operatorname{Aut}(G)$ be the bundle corresponding to the "identity" action $\rho: \operatorname{Aut}(G) \to \operatorname{Aut}(G)$.
Show that the map $[X, B\operatorname{Aut}(G)] \to \mathcal{B}(X; G)$, $[f] \mapsto f^*(E_0)$, is a bijection if $X$ is a CW complex, where $[X, Y]$ denotes the set of homotopy classes of maps $X \to Y$.

::: {.solution}
Regard $\operatorname{Aut}(G)$ as a discrete group. Then
\[
B\operatorname{Aut}(G)=K(\operatorname{Aut}(G),1),
\]
and the bundle $E_0\to B\operatorname{Aut}(G)$ associated to the identity action is the universal bundle of groups with fiber $G$.

Assume first that $X$ is connected and choose a basepoint. A bundle of groups $E\to X$ with fiber $G$ has monodromy
\[
\rho_E:\pi_1(X)\longrightarrow\operatorname{Aut}(G),
\]
well-defined up to conjugation by an automorphism of the chosen fiber. Conversely, a homomorphism
\[
\rho:\pi_1(X)\to\operatorname{Aut}(G)
\]
defines the bundle
\[
\widetilde X\times_{\pi_1(X)}G\longrightarrow X,
\]
where the deck group acts on $G$ through $\rho$. These two constructions are inverse up to bundle isomorphism. Thus
\[
\mathcal B(X;G)
\cong
\operatorname{Hom}(\pi_1X,\operatorname{Aut}(G))/\text{conjugacy}.
\]

Since $B\operatorname{Aut}(G)$ is a $K(\operatorname{Aut}(G),1)$ and $X$ is a CW complex, the standard classification of maps into a $K(\pi,1)$ gives
\[
[X,B\operatorname{Aut}(G)]
\cong
\operatorname{Hom}(\pi_1X,\operatorname{Aut}(G))/\text{conjugacy}.
\]
Under this correspondence, a map $f:X\to B\operatorname{Aut}(G)$ corresponds to the monodromy homomorphism $f_*$. The pullback $f^*E_0$ has exactly this monodromy, so the displayed identification is precisely the map
\[
[f]\longmapsto f^*(E_0).
\]
Hence it is a bijection. For disconnected $X$, apply the same argument independently on each component.
:::
