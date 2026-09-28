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
<1>1. If the stated condition holds for every affine open $V\subseteq Y$, then $f$ is locally of finite type.
::: {.proof}
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

<1>2. Conversely, suppose $f$ is locally of finite type.  Fix an arbitrary affine open
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
::: {.proof}
This is the defining affine-cover condition for a locally finite type morphism: choose one target affine from a witnessing cover which contains $f(x)$, and then one source affine from the corresponding cover of its inverse image which contains $x$.
:::

<1>3. There is a distinguished open
\[
W=D(g)\subseteq V
\]
with
\[
f(x)\in W\subseteq V\cap V_i.
\]
::: {.proof}
The intersection $V\cap V_i$ is an open neighborhood of $f(x)$ inside the affine scheme $V=\Spec B$.  Distinguished opens form a basis for the topology of an affine scheme, so some
\[
D(g),\qquad g\in B,
\]
contains $f(x)$ and is contained in $V\cap V_i$.
:::

<1>4. There is a distinguished affine neighborhood
\[
U'=D(a)\subseteq U
\]
of $x$ such that
\[
U'\subseteq f^{-1}(W).
\]
::: {.proof}
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

<1>5. The affine neighborhood
\[
U'=\Spec A_a
\]
has coordinate ring finitely generated as a $B$-algebra.
::: {.proof}
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

<1>6. The inverse image $f^{-1}(V)$ is covered by affine opens whose coordinate rings are finitely generated $B$-algebras.
::: {.proof}
The point $x\in f^{-1}(V)$ was arbitrary.  Steps <1>2--<1>5 construct, around every such $x$, an affine open
\[
U'=\Spec A_a\subseteq f^{-1}(V)
\]
with $A_a$ finitely generated over $B$.  These neighborhoods therefore form the required affine cover.
:::

<1>7. Hence the two conditions are equivalent.
::: {.proof}
Step <1>1 proves one implication and steps <1>2--<1>6 prove the converse.
:::

<1>8. Q.E.D.
::: {.proof}
Step <1>7 is the claimed equivalence.
:::
:::
