---
schema: qual/card@1
id: P-ALGF25F
kind: problem
title: Maximal abelian subextension as the fixed field of $[G,G]$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared the statement with Problem 6 on page 7 of the official FA25 algebra exam PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Re-derived both directions from the Galois correspondence and verified the normal-subgroup and quotient identifications.
---

::: problem
Let $E/F$ be a finite Galois extension with Galois group $G = \operatorname{Gal}(E/F)$, and let $[G,G]$ denote the derived subgroup of $G$.
Define the subfield
\[
F^{\mathrm{ab}} := \{e \in E \mid \theta(e) = e \text{ for all } \theta \in [G,G]\}.
\]
That is, $F^{\mathrm{ab}}$ is the fixed field of $[G,G]$.
Prove that an element $e \in E$ lies in $F^{\mathrm{ab}}$ if and only if the field extension $F[e]/F$ is Galois and its Galois group $\operatorname{Gal}(F[e]/F)$ is abelian.
:::

::: {.solution}
<1>1. The extension $F^{\mathrm{ab}}/F$ is Galois and abelian.
::: {.proof}
The commutator subgroup $[G,G]$ is characteristic in $G$, hence normal.
By the fundamental theorem of Galois theory, its fixed field
\[
F^{\mathrm{ab}}=E^{[G,G]}
\]
is Galois over $F$, with
\[
\operatorname{Gal}(F^{\mathrm{ab}}/F)\cong G/[G,G].
\]
The quotient $G/[G,G]$ is abelian, so $F^{\mathrm{ab}}/F$ is an abelian Galois extension.
:::

<1>2. If $F[e]/F$ is Galois with abelian Galois group, then $e\in F^{\mathrm{ab}}$.
::: {.proof}
Let
\[
H=\operatorname{Gal}(E/F[e]).
\]
Since $F[e]/F$ is Galois, the Galois correspondence gives $H\trianglelefteq G$ and
\[
G/H\cong\operatorname{Gal}(F[e]/F).
\]
The quotient is abelian, so every commutator of elements of $G$ lies in $H$; hence
\[
[G,G]\subseteq H.
\]
Taking fixed fields reverses inclusion and gives
\[
F[e]=E^H\subseteq E^{[G,G]}=F^{\mathrm{ab}}.
\]
In particular, $e\in F^{\mathrm{ab}}$.
:::

<1>3. If $e\in F^{\mathrm{ab}}$, then $F[e]/F$ is Galois and abelian.
::: {.proof}
By <1>1, the extension $F^{\mathrm{ab}}/F$ is finite Galois with abelian Galois group
\[
A=\operatorname{Gal}(F^{\mathrm{ab}}/F).
\]
The inclusions
\[
F\subseteq F[e]\subseteq F^{\mathrm{ab}}
\]
correspond to the subgroup
\[
K=\operatorname{Gal}(F^{\mathrm{ab}}/F[e])\le A.
\]
Since $A$ is abelian, $K$ is normal in $A$.
The Galois correspondence therefore shows that $F[e]/F$ is Galois and that
\[
\operatorname{Gal}(F[e]/F)\cong A/K.
\]
This quotient is abelian, proving the converse and hence the equivalence.
:::
:::
