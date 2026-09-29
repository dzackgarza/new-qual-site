---
schema: qual/card@1
id: P-AGH231LOCFINTYPE
kind: problem
title: Locally of finite type can be checked on every open affine of the target
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms Of Schemes
  - Finite Type
  - Affine Covers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.1 statement and the repository definition of locally finite type morphisms.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Show that a morphism $f: X \to Y$ is locally of finite type if and only if for every open affine subset $V = \Spec B$ of $Y$, the preimage $\inverseof{f}(V)$ can be covered by open affine subsets $U_j = \Spec A_j$ where each $A_j$ is a finitely generated $B$-algebra.
:::

::: {.solution}

::: pf

::: {.pf-step #condition-implies-locally-finite-type}
If the stated condition holds for every affine open $V\subseteq Y$, then $f$ is locally of finite type.

::: pf-proof
Choose any affine open cover
\[
Y=\bigcup_i V_i.
\]
By hypothesis, for each affine $V_i=\Spec B_i$, the inverse image $f^{-1}(V_i)$ has an affine cover by
\[
U_{ij}=\Spec A_{ij}
\]
with each $A_{ij}$ a finitely generated $B_i$-algebra.
This is exactly the definition of $f$ being locally of finite type.
:::

:::

::: {.pf-step #choose-affine-neighborhoods}
Conversely, suppose $f$ is locally of finite type.  Fix an arbitrary affine open
\[
V=\Spec B\subseteq Y
\]
and a point
\[
x\in f^{-1}(V).
\]
There is an affine open $V_i=\Spec B_i\subseteq Y$ containing $f(x)$ and an affine open
\[
U=\Spec A\subseteq f^{-1}(V_i)
\]
containing $x$ such that $A$ is a finitely generated $B_i$-algebra.

::: pf-proof
This is the defining affine-cover condition for a locally finite type morphism: choose one target affine from a witnessing cover which contains $f(x)$, and then one source affine from the corresponding cover of its inverse image which contains $x$.
:::

:::

::: {.pf-step #distinguished-open-w}
There is a distinguished open
\[
W=D(g)\subseteq V
\]
with
\[
f(x)\in W\subseteq V\cap V_i.
\]

::: pf-proof
The intersection $V\cap V_i$ is an open neighborhood of $f(x)$ inside the affine scheme $V=\Spec B$.  Distinguished opens form a basis for the topology of an affine scheme, so some
\[
D(g),\qquad g\in B,
\]
contains $f(x)$ and is contained in $V\cap V_i$.
:::

:::

::: {.pf-step #distinguished-neighborhood-uprime}
There is a distinguished affine neighborhood
\[
U'=D(a)\subseteq U
\]
of $x$ such that
\[
U'\subseteq f^{-1}(W).
\]

::: pf-proof
The set
\[
U\cap f^{-1}(W)
\]
is an open neighborhood of $x$ inside the affine scheme $U=\Spec A$.  Again using the distinguished-open basis, choose $a\in A$ such that
\[
x\in D(a)\subseteq U\cap f^{-1}(W).
\]
Set $U'=D(a)$.
:::

:::

::: {.pf-step #uprime-finitely-generated-over-b}
The affine neighborhood
\[
U'=\Spec A_a
\]
has coordinate ring finitely generated as a $B$-algebra.

::: pf-proof
Because $W=D(g)\subseteq V=\Spec B$,
\[
W\cong\Spec B_g.
\]
Since $U'$ maps into $W$, the structural ring map factors as
\[
B\longrightarrow B_g\longrightarrow A_a.
\]

Write
\[
A=B_i[\alpha_1,\ldots,\alpha_n].
\]
Localizing at $a$ gives
\[
A_a=B_i[\alpha_1,\ldots,\alpha_n,a^{-1}].
\]
The image of $B_i$ in $A_a$ factors through the coordinate ring $B_g$ of $W$, because the morphism $U'\to V_i$ factors through $W$.
Hence the same elements
\[
\alpha_1,\ldots,\alpha_n,a^{-1}
\]
generate $A_a$ as a $B_g$-algebra.

Finally $B_g$ is generated as a $B$-algebra by $g^{-1}$.  Therefore
\[
A_a
=B[g^{-1},\alpha_1,\ldots,\alpha_n,a^{-1}],
\]
so $A_a$ is a finitely generated $B$-algebra.
:::

:::

::: {.pf-step #preimage-v-covered-by-fg-affines}
The inverse image $f^{-1}(V)$ is covered by affine opens whose coordinate rings are finitely generated $B$-algebras.

::: pf-proof
The point $x\in f^{-1}(V)$ was arbitrary.  Steps [](#choose-affine-neighborhoods){.pf-ref}, [](#distinguished-open-w){.pf-ref}, [](#distinguished-neighborhood-uprime){.pf-ref} and [](#uprime-finitely-generated-over-b){.pf-ref} construct, around every such $x$, an affine open
\[
U'=\Spec A_a\subseteq f^{-1}(V)
\]
with $A_a$ finitely generated over $B$.  These neighborhoods therefore form the required affine cover.
:::

:::

::: {.pf-step #two-conditions-equivalent}
Hence the two conditions are equivalent.

::: pf-proof
Step [](#condition-implies-locally-finite-type){.pf-ref} proves one implication and steps [](#choose-affine-neighborhoods){.pf-ref}, [](#distinguished-open-w){.pf-ref}, [](#distinguished-neighborhood-uprime){.pf-ref}, [](#uprime-finitely-generated-over-b){.pf-ref} and [](#preimage-v-covered-by-fg-affines){.pf-ref} prove the converse.
:::

:::

::: pf-qed
Step [](#two-conditions-equivalent){.pf-ref} is the claimed equivalence.
:::

:::

:::
