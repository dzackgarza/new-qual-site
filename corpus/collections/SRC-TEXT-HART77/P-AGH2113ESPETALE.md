---
schema: qual/card@1
id: P-AGH2113ESPETALE
kind: problem
title: Sheafification as the sheaf of continuous sections of the espace étalé
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Sheafification
  - Espace Etale
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.13 statement and source-order placement after II.1.12.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Given a presheaf $\mcf$ on $X$, define a topological space $\operatorname{Spe}(\mcf)$, called the **espace étalé** of $\mcf$, as follows.
As a set, $\operatorname{Spe}(\mcf) = \Union_{P \in X} \mcf_P$.
Define a projection map $\pi: \operatorname{Spe}(\mcf) \to X$ by sending $s \in \mcf_P$ to $P$.
For each open set $U \subseteq X$ and each section $s \in \mcf(U)$ we obtain a map $\bar{s}: U \to \operatorname{Spe}(\mcf)$ sending $P \mapsto s_P$, the germ of $s$ at $P$.
This map satisfies $\pi \circ \bar{s} = \id$, so it is a section of $\pi$ over $U$.
Give $\operatorname{Spe}(\mcf)$ the strongest topology such that all the maps $\bar{s}$, for all $U$ and all $s \in \mcf(U)$, are continuous.

Show that the sheaf $\mcf^{+}$ associated to $\mcf$ can be described as follows: for any open $U \subseteq X$, the group $\mcf^{+}(U)$ is the set of continuous sections of $\operatorname{Spe}(\mcf)$ over $U$.

In particular, the original presheaf $\mcf$ was a sheaf if and only if for each $U$ the group $\mcf(U)$ equals the set of all continuous sections of $\operatorname{Spe}(\mcf)$ over $U$.
:::

::: {.remark}
This exercise connects Hartshorne's definition of a sheaf with the espace étalé definition used elsewhere in the literature, for example in Godement.
:::

::: {.solution}
Write
\[
E=\operatorname{Spe}(\mcf)=\coprod_{P\in X}\mcf_P
\]
and let
\[
\pi:E\longrightarrow X
\]
be the projection.  For $s\in\mcf(U)$ write
\[
\bar s:U\longrightarrow E,
\qquad
P\longmapsto s_P.
\]

::: pf

::: {.pf-step #s1}

A subset $W\subseteq E$ is open in the specified topology if and only if
\[
\bar t^{-1}(W)
\]
is open for every open $V\subseteq X$ and every $t\in\mcf(V)$.

::: pf-proof

This is exactly the definition of the strongest, or final, topology on $E$ for which every map
\[
\bar t:V\to E
\]
is continuous.

:::

:::

::: {.pf-step #s2}

For every $s\in\mcf(U)$, the image
\[
\bar s(U)\subseteq E
\]
is open.

::: pf-proof

By step [](#s1){.pf-ref}, it is enough to show that for every $t\in\mcf(V)$ the subset
\[
\bar t^{-1}(\bar s(U))
\]
is open in $V$.

A point $P\in V$ belongs to this inverse image exactly when
\[
P\in U\cap V
\qquad\text{and}\qquad
t_P=s_P
\]
as germs in $\mcf_P$.

If $t_P=s_P$, then by definition of equality in the stalk there is an open neighborhood
\[
P\in W_P\subseteq U\cap V
\]
such that
\[
t|_{W_P}=s|_{W_P}.
\]
For every $Q\in W_P$, therefore,
\[
t_Q=s_Q,
\]
so
\[
W_P\subseteq\bar t^{-1}(\bar s(U)).
\]
Thus every point of the inverse image has an open neighborhood contained in it, proving that the inverse image is open.

:::

:::

::: pf-step

The projection
\[
\pi:E\longrightarrow X
\]
is continuous, and for every $s\in\mcf(U)$ the map
\[
\bar s:U\longrightarrow\bar s(U)
\]
is a homeomorphism with inverse $\pi|_{\bar s(U)}$.

::: pf-proof

Let $U\subseteq X$ be open.  For every $t\in\mcf(V)$,
\[
\bar t^{-1}(\pi^{-1}(U))
=V\cap U,
\]
which is open.  By step [](#s1){.pf-ref}, $\pi^{-1}(U)$ is open, so $\pi$ is continuous.

By construction,
\[
\pi\circ\bar s=\operatorname{id}_U.
\]
The map $\bar s$ is injective because its values lie in different fibres of $\pi$ at different points.  Its image is open by step [](#s2){.pf-ref}.  Hence
\[
\bar s:U\to\bar s(U)
\]
is a continuous bijection whose inverse is the continuous restriction of $\pi$.  It is therefore a homeomorphism.

:::

:::

::: {.pf-step #s4}

Let $\sigma:U\to E$ satisfy
\[
\pi\circ\sigma=\operatorname{id}_U.
\]
If $\sigma$ is continuous, then every point $P\in U$ has a neighborhood $W\subseteq U$ and a section $s\in\mcf(V)$ on an open $V\subseteq X$ such that
\[
W\subseteq V
\qquad\text{and}\qquad
\sigma|_W=\bar s|_W.
\]

::: pf-proof

Fix $P\in U$.  The point
\[
\sigma(P)\in E_P=\mcf_P
\]
is a germ, so choose an open neighborhood $V$ of $P$ and a section
\[
s\in\mcf(V)
\]
representing that germ.  Thus
\[
\sigma(P)=s_P\in\bar s(V).
\]

By step [](#s2){.pf-ref}, $\bar s(V)$ is an open neighborhood of $\sigma(P)$ in $E$.  Since $\sigma$ is continuous,
\[
W:=\sigma^{-1}(\bar s(V))
\]
is an open neighborhood of $P$ in $U$.

For $Q\in W$, the point $\sigma(Q)$ belongs to $\bar s(V)$.  Because $\sigma$ is a section of $\pi$,
\[
\pi(\sigma(Q))=Q.
\]
The unique point of $\bar s(V)$ lying over $Q$ is $s_Q$.  Therefore
\[
\sigma(Q)=s_Q.
\]
In particular $Q\in V$, so $W\subseteq V$, and
\[
\sigma|_W=\bar s|_W.
\]

:::

:::

::: {.pf-step #s5}

Conversely, any section $\sigma:U\to E$ which is locally of the form $\bar s$ for sections of the presheaf $\mcf$ is continuous.

::: pf-proof

Suppose $U$ has an open cover $\{U_\alpha\}$ such that
\[
\sigma|_{U_\alpha}=\bar s_\alpha|_{U_\alpha}
\]
for suitable presheaf sections $s_\alpha$.  Each $\bar s_\alpha$ is continuous by the definition of the topology on $E$.  Hence every restriction
\[
\sigma|_{U_\alpha}
\]
is continuous.

Continuity is local on the source: for any open $W\subseteq E$,
\[
\sigma^{-1}(W)
=\bigcup_\alpha
(\sigma|_{U_\alpha})^{-1}(W),
\]
which is open in $U$.  Thus $\sigma$ is continuous.

:::

:::

::: {.pf-step #s6}

Therefore the continuous sections of $\pi$ over $U$ are exactly the functions
\[
\sigma:U\longrightarrow\coprod_{P\in U}\mcf_P
\]
such that
\[
\sigma(P)\in\mcf_P
\]
and $\sigma$ is locally represented by a section of the presheaf $\mcf$.

::: pf-proof

The forward implication is step [](#s4){.pf-ref}, and the reverse implication is step [](#s5){.pf-ref}.

:::

:::

::: pf-step

The assignment
\[
U\longmapsto
\{\text{continuous sections }U\to E\text{ of }\pi\}
\]
is a sheaf.

::: pf-proof

Uniqueness is pointwise: two sections agreeing on an open cover have the same value at every point.

For gluing, let continuous sections
\[
\sigma_\alpha:U_\alpha\to E
\]
agree on overlaps.  Define
\[
\sigma(P)=\sigma_\alpha(P)
\]
for any $\alpha$ with $P\in U_\alpha$.  Agreement on overlaps makes this well-defined, and clearly
\[
\pi\circ\sigma=\operatorname{id}.
\]
The restriction of $\sigma$ to each $U_\alpha$ is the continuous map $\sigma_\alpha$, so step [](#s5){.pf-ref}'s locality argument shows that $\sigma$ is continuous.

:::

:::

::: {.pf-step #s8}

The canonical map
\[
\mcf(U)\longrightarrow
\{\text{continuous sections of }E\text{ over }U\},
\qquad
s\longmapsto\bar s,
\]
is the sheafification map, and the target is naturally $\mcf^+(U)$.

::: pf-proof

By step [](#s6){.pf-ref}, the target consists exactly of locally representable choices of germs.  This is the standard germ description of the associated sheaf.

For completeness, it has the sheafification universal property.  Let
\[
\phi:\mcf\longrightarrow\mcg
\]
be a presheaf morphism to a sheaf $\mcg$.  Given a continuous germ section $\sigma$ over $U$, choose an open cover $U=\bigcup U_\alpha$ and sections
\[
s_\alpha\in\mcf(V_\alpha)
\]
such that
\[
\sigma|_{U_\alpha}=\bar s_\alpha|_{U_\alpha}.
\]

On an overlap, the germs of $s_\alpha$ and $s_\beta$ agree at every point.  Hence they agree locally near every point of the overlap.  Applying $\phi$, the sections
\[
\phi(s_\alpha),\quad\phi(s_\beta)
\]
agree locally; since $\mcg$ is a sheaf, they agree on the whole overlap.  They therefore glue uniquely to a section of $\mcg(U)$.

This construction gives a unique sheaf morphism from the continuous-section sheaf to $\mcg$ extending $\phi$.  Thus the continuous-section sheaf satisfies the universal property of $\mcf^+$ and is canonically isomorphic to it.

:::

:::

::: {.pf-step #s9}

Hence
\[
\boxed{
\mcf^+(U)
=
\{\sigma:U\to\operatorname{Spe}(\mcf)
\mid
\pi\circ\sigma=\operatorname{id}_U,
\ \sigma\text{ continuous}\}.
}
\]

::: pf-proof

This is the identification established in step [](#s8){.pf-ref}.

:::

:::

::: {.pf-step #s10}

In particular, $\mcf$ is already a sheaf if and only if every continuous section of the espace étalé over every open $U$ is of the form $\bar s$ for a unique
\[
s\in\mcf(U).
\]

::: pf-proof

A presheaf is a sheaf exactly when its canonical map to its sheafification is an isomorphism.  Under step [](#s9){.pf-ref}, this canonical map is
\[
s\longmapsto\bar s.
\]
Therefore it is an isomorphism on every open set exactly under the stated condition.

:::

:::

::: pf-qed

Steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} identify continuity with local representability by germs, steps [](#s8){.pf-ref} and [](#s9){.pf-ref} identify those sections with the associated sheaf, and step [](#s10){.pf-ref} gives the final characterization of when $\mcf$ was already a sheaf.

:::

:::

:::
