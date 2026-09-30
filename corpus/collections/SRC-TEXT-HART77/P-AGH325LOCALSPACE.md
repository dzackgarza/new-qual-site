---
schema: qual/card@1
id: P-AGH325LOCALSPACE
kind: problem
title: Local cohomology at a point is computed on the local space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Local Cohomology
  - Zariski Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the whole statement with the retained Hartshorne Chapter III section 2 transcription and read the Zariski-space prerequisite. The proof establishes the neighborhood-section comparison and preservation of flasqueness for this particular nonopen inclusion before comparing supported resolutions.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a Zariski space (II, Ex. 3.17).
Let $P \in X$ be a closed point, and let $X_P$ be the subset of $X$ consisting of all points $Q \in X$ such that $P \in \bar{\theset{Q}}$.
We call $X_P$ the **local space** of $X$ at $P$, and give it the induced topology.

Let $j: X_P \to X$ be the inclusion, and for any sheaf $\mcf$ of abelian groups on $X$, let $\mcf_P=j^* \mcf$.
Show that for all $i\ge0$ and $\mcf$, we have
$$
H_P^i(X, \mcf)=H_P^i(X_P, \mcf_P).
$$
:::

::: {.solution}
Put $S=X_P$ and write $j^{-1}$ for the inverse-image functor on abelian sheaves, denoted $j^*$ in the statement.
Thus $\mcf_P$ denotes an entire sheaf on $S$, not the stalk of $\mcf$ at $P$.
Write $\Gamma_P$ for sections supported in the closed singleton $\{P\}$, as in [[P-AGH323SUPPORTS]].
A [[P-AGH2317ZARISKISPACE|Zariski space]] is noetherian and has a unique generic point for every nonempty irreducible closed subset.

::: pf

::: {.pf-step #s1}

Every open neighborhood of $P$ contains $S$.
If $V\subseteq X$ is open and $C\subseteq V$ is relatively closed with $C\cap S=\varnothing$, there is an open neighborhood $U$ of $P$ such that $U\cap V\cap C=\varnothing$.

::: pf-proof

If $Q\in S$, every open neighborhood of the specialization $P$ contains $Q$.
This proves the first assertion.

The closed subset $C$ of the noetherian space $V$ has finitely many irreducible components $C_1,\ldots,C_t$.
Each has a generic point $\eta_a\in C_a$.
Indeed, the closure of $C_a$ in $X$ has a generic point, and its intersection with $V$ is the nonempty open subset $C_a$; the generic point belongs to this intersection.
If $P$ belonged to $\overline{C_a}$, it would belong to $\overline{\{\eta_a\}}$, giving $\eta_a\in S\cap C$, a contradiction.
Consequently
$$
U=X\setminus\bigcup_{a=1}^t\overline{C_a}
$$
is a neighborhood of $P$ disjoint from $C$.
This includes $C=\varnothing$, when $U=X$.

Equivalently, if $W\subseteq V$ is open and contains $S\cap V$, then some neighborhood $U$ of $P$ satisfies $U\cap V\subseteq W$.
We will use this form both to cover a neighborhood and to make finitely many local sections agree.

:::

:::

::: {.pf-step #s2}

For every abelian sheaf $A$ on $X$ and open $V\subseteq X$, the natural map
$$
\varinjlim_{U\ni P}\Gamma(U\cap V,A)
\longrightarrow\Gamma(S\cap V,j^{-1}A)
$$
is an isomorphism, where the transition maps are restriction to smaller neighborhoods $U$ of $P$.

::: pf-proof

Every subspace of a noetherian space is noetherian, so $S\cap V$ is quasi-compact.
For example, this follows by extending a cover of the subspace to opens in $X$ and using quasi-compactness of their union, an open subset of a noetherian space.

Take a section of $j^{-1}A$ on $S\cap V$.
By the construction of inverse image, it is locally represented by sections $a_i\in A(V_i)$ for opens $V_i\subseteq V$.
Choose finitely many of these opens covering $S\cap V$.
On $V_i\cap V_h$, the germs of $a_i-a_h$ are zero at every point of $S$ in this overlap.
The zero-germ locus of a section is open, so step [](#s1){.pf-ref} gives a neighborhood $U_{ih}$ of $P$ on whose intersection with $V_i\cap V_h$ the two sections agree.
The same step gives a neighborhood $U_0$ with $U_0\cap V\subseteq\bigcup_iV_i$.
Intersect these finitely many neighborhoods and call the result $U$.
The $a_i$ now glue on $U\cap V$ and represent the given section on $S\cap V$.
This proves surjectivity.

For injectivity, let $a\in A(U\cap V)$ restrict to zero on $S\cap V$.
Its zero-germ locus is an open subset of $U\cap V$ containing $S\cap V$, since $S\subseteq U$.
Step [](#s1){.pf-ref}, applied inside $U\cap V$, gives a smaller neighborhood $U'$ of $P$ on which $a|_{U'\cap U\cap V}=0$.
Thus $a$ is already zero in the indicated direct limit.
All the constructions use the natural restriction map, so the isomorphism is natural in $A$ and compatible with restriction in $V$.

:::

:::

::: {.pf-step #s3}

If $A$ is flasque on $X$, then $j^{-1}A$ is flasque on $S$.

::: pf-proof

Let $T\subseteq T'$ be open subsets of $S$ and choose an open $V\subseteq X$ with $T=S\cap V$.
A section on $T$ is represented, by step [](#s2){.pf-ref}, by a section of $A$ on $U\cap V$ for some neighborhood $U$ of $P$.
Flasqueness extends this section to all of $X$.
Its inverse-image section on $S$, restricted to $T'$, extends the original section on $T$.
Thus every restriction map on $j^{-1}A$ is surjective.
This conclusion has been proved for the present inclusion; it is not an assertion that arbitrary inverse images preserve flasqueness.

:::

:::

::: {.pf-step #s4}

For every abelian sheaf $A$, restriction gives a natural isomorphism
$$
\Gamma_P(X,A)\xrightarrow{\cong}\Gamma_P(S,j^{-1}A).
$$

::: pf-proof

A section supported at $P$ restricts to one with that support on $S$.
If this restriction is zero, its germ at $P$ is zero, because $(j^{-1}A)_P\cong A_P$.
All its other germs were already zero by the support condition, so the original section is zero.
This proves injectivity.

Conversely, represent a section on $S$ supported at $P$ by $a\in A(U)$ using step [](#s2){.pf-ref} with $V=X$.
Its restriction to $S\setminus\{P\}$ is zero.
Apply the injectivity in step [](#s2){.pf-ref} with the open set $V=X\setminus\{P\}$.
After shrinking the neighborhood $U$ of $P$, it follows that $a|_{U\setminus\{P\}}=0$.
Glue $a$ on $U$ with zero on $X\setminus\{P\}$.
These opens cover $X$, so this gives a global section supported at $P$ with the prescribed restriction.
The construction is inverse to restriction and hence natural.

:::

:::

::: {.pf-step #s5}

The supported cohomology groups are naturally isomorphic in every degree.

::: pf-proof

Choose an injective resolution $\mcf\to I^\bullet$ on $X$.
Its terms are flasque [@Har10a, Lemma III.2.4].
Inverse image of abelian sheaves is exact, as follows from its stalk formula $(j^{-1}A)_x=A_x$ for $x\in S$ and stalkwise exactness.
Thus $j^{-1}I^\bullet$ resolves $\mcf_P$.
By step [](#s3){.pf-ref} all its terms are flasque, and hence acyclic for sections supported at $P$ by [[P-AGH323SUPPORTS]], part (c).
It therefore computes $H_P^i(S,\mcf_P)$.

Apply the natural isomorphism of step [](#s4){.pf-ref} to every $I^q$.
It commutes with the differentials and identifies the complexes
$$
\Gamma_P(X,I^\bullet)\cong\Gamma_P(S,j^{-1}I^\bullet).
$$
The first computes $H_P^i(X,\mcf)$ by definition; the second computes the groups just identified.
Taking cohomology gives
$$
\boxed{H_P^i(X,\mcf)\xrightarrow{\cong}H_P^i(X_P,\mcf_P)\qquad(i\ge0).}
$$
Naturality follows from the natural maps on sections and comparison of resolutions [@Har10a, Chapter III, §1].

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} establish the restriction and flasqueness comparisons for the local space, and step [](#s5){.pf-ref} proves the required isomorphism in every degree.

:::

:::

:::
