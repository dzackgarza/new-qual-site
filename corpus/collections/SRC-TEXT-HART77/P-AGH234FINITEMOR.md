---
schema: qual/card@1
id: P-AGH234FINITEMOR
kind: problem
title: Finiteness of a morphism can be checked on every open affine of the target
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms Of Schemes
  - Finite Morphisms
  - Affine Covers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.4 statement and the repository definition of finite morphisms.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Show that a morphism $f: X \to Y$ is finite if and only if for every open affine subset $V = \Spec B$ of $Y$, the preimage $\inverseof{f}(V)$ is affine, equal to $\Spec A$, where $A$ is a finite $B$-module.
:::

::: {.solution}

::: pf

::: {.pf-step #condition-implies-finite}
If the stated condition holds for every affine open $V\subseteq Y$, then $f$ is finite.

::: pf-proof
Choose any affine open cover of $Y$.
On every member $V=\Spec B$ of that cover, the hypothesis says
\[
f^{-1}(V)=\Spec A
\]
with $A$ finite as a $B$-module.
This is exactly the definition of a finite morphism.
:::

:::

::: {.pf-step #finite-cover-witness}
Conversely, suppose $f$ is finite and fix an arbitrary affine open
\[
V=\Spec B\subseteq Y.
\]
Choose an affine cover
\[
Y=\bigcup_iV_i,
\qquad
V_i=\Spec B_i,
\]
witnessing finiteness, so
\[
f^{-1}(V_i)=\Spec A_i
\]
with $A_i$ a finite $B_i$-module.

::: pf-proof
This is the defining affine-cover condition for a finite morphism.
:::

:::

::: {.pf-step #common-distinguished-neighborhood}
Every point $y\in V$ has an open neighborhood
\[
W_y\subseteq V\cap V_i
\]
for some $i$ which is distinguished in both $V$ and $V_i$.

::: pf-proof
Choose $i$ with $y\in V_i$.  Inside the affine $V$, choose
\[
y\in D_V(b)\subseteq V\cap V_i.
\]
Inside the affine $V_i$, choose
\[
y\in D_{V_i}(c)\subseteq D_V(b).
\]
The regular function $c$ on $D_V(b)$ is an element of $B_b$, so write
\[
c=d/b^m,
\qquad d\in B.
\]
Then
\[
D_{V_i}(c)=D_V(b)\cap D_V(d)=D_V(bd).
\]
Thus this neighborhood is distinguished in both affines.  Denote it by $W_y$.
:::

:::

::: {.pf-step #preimage-wy-finite-affine}
For every neighborhood $W_y$ from step [](#common-distinguished-neighborhood){.pf-ref}, the inverse image $f^{-1}(W_y)$ is affine and finite over $W_y$.

::: pf-proof
Write $W_y=D_{V_i}(c)$ inside the witnessing affine $V_i=\Spec B_i$.
Then
\[
f^{-1}(W_y)=D_{\Spec A_i}(\phi_i(c))
\cong
\Spec (A_i)_c,
\]
where $\phi_i:B_i\to A_i$ is the structural ring map.

Since $A_i$ is a finite $B_i$-module, localization gives $(A_i)_c$ as a finite $(B_i)_c$-module.  But
\[
(B_i)_c\cong\Gamma(W_y,\mathcal O_Y).
\]
Thus $f^{-1}(W_y)$ is affine and finite over $W_y$.
:::

:::

::: {.pf-step #finite-subcover-of-v}
There are finitely many such common distinguished opens
\[
W_j=D_V(b_j)
\]
which cover $V$.

::: pf-proof
The neighborhoods from step [](#common-distinguished-neighborhood){.pf-ref} cover $V$.  Since $V$ is affine, it is quasi-compact, so a finite subcover suffices.  Express each chosen member in its distinguished form inside $V$.
:::

:::

::: {.pf-step #bj-generate-unit-ideal}
The elements $b_1,\ldots,b_r\in B$ generate the unit ideal.

::: pf-proof
The distinguished opens $D(b_j)$ cover $\Spec B$, so
\[
V(b_1,\ldots,b_r)=\varnothing.
\]
Hence
\[
(b_1,\ldots,b_r)=B.
\]
:::

:::

::: {.pf-step #aj-generate-unit-ideal-and-affine-loci}
Put
\[
X_V=f^{-1}(V),
\qquad
A=\Gamma(X_V,\mathcal O_{X_V}),
\]
and let $a_j\in A$ be the pullback of $b_j$.
Then
\[
(a_1,\ldots,a_r)=A
\]
and
\[
(X_V)_{a_j}=f^{-1}(W_j)
\]
is affine for every $j$.

::: pf-proof
Choose $d_j\in B$ with
\[
\sum_jd_jb_j=1.
\]
Pulling this identity back to $A$ gives
\[
\sum_jf^*(d_j)a_j=1,
\]
so the $a_j$ generate the unit ideal.

A point of $X_V$ belongs to the nonvanishing locus of $a_j=f^*b_j$ exactly when its image in $V$ belongs to $D(b_j)=W_j$.  Hence
\[
(X_V)_{a_j}=f^{-1}(W_j),
\]
which is affine by step [](#preimage-wy-finite-affine){.pf-ref}.
:::

:::

::: {.pf-step #xv-is-affine}
The scheme $X_V=f^{-1}(V)$ is affine.

::: pf-proof
The global functions $a_j$ generate the unit ideal in $A$, and their nonvanishing loci are affine by step [](#aj-generate-unit-ideal-and-affine-loci){.pf-ref}.  Hartshorne II.2.17(b) therefore gives
\[
X_V\cong\Spec A.
\]
:::

:::

::: {.pf-step #localization-finite}
For every $j$, the localization $A_{a_j}$ is a finite $B_{b_j}$-module.

::: pf-proof
Since $X_V=\Spec A$, the distinguished open $(X_V)_{a_j}$ has coordinate ring $A_{a_j}$.  By step [](#aj-generate-unit-ideal-and-affine-loci){.pf-ref} it equals $f^{-1}(W_j)$, and by step [](#preimage-wy-finite-affine){.pf-ref} the coordinate ring of that inverse image is finite over
\[
\Gamma(W_j,\mathcal O_Y)=B_{b_j}.
\]
Thus $A_{a_j}$ is finite as a $B_{b_j}$-module.
:::

:::

::: {.pf-step #module-lemma}
We use the following module lemma.
Let $B\to A$ be a ring map and let $b_1,\ldots,b_r\in B$ generate the unit ideal.
If every
\[
A_{b_j}
\]
is a finite $B_{b_j}$-module, then $A$ is a finite $B$-module.

::: pf-proof
For each $j$, choose finitely many generators of the $B_{b_j}$-module $A_{b_j}$ and write them as fractions whose numerators lie in $A$.
Let
\[
M\subseteq A
\]
be the $B$-submodule generated by all these finitely many numerators.
Then
\[
M_{b_j}=A_{b_j}
\]
for every $j$.

Set $Q=A/M$.  Then $Q_{b_j}=0$ for every $j$.  For $q\in Q$, there is therefore an exponent $N_j$ with
\[
b_j^{N_j}q=0.
\]
Choose a common $N$ at least all $N_j$.  Then $b_j^Nq=0$ for all $j$.  Since the $b_j$ generate the unit ideal, the powers $b_j^N$ do as well.  Hence some $c_j\in B$ satisfy
\[
\sum_jc_jb_j^N=1.
\]
It follows that
\[
q=\sum_jc_jb_j^Nq=0.
\]
Thus $Q=0$, so $A=M$ is generated by finitely many elements as a $B$-module.
:::

:::

::: {.pf-step #a-finite-b-module}
The ring $A=\Gamma(X_V,\mathcal O_{X_V})$ is a finite $B$-module.

::: pf-proof
The elements $b_j$ generate the unit ideal by step [](#bj-generate-unit-ideal){.pf-ref}.  Localizing $A$ at $b_j$ is the same as localizing at its image $a_j$, and step [](#localization-finite){.pf-ref} shows that this localization is finite over $B_{b_j}$.  Apply the module lemma step [](#module-lemma){.pf-ref}.
:::

:::

::: {.pf-step #finite-over-affine-open}
Hence for every affine open $V=\Spec B\subseteq Y$,
\[
f^{-1}(V)=\Spec A
\]
with $A$ finite as a $B$-module.

::: pf-proof
Step [](#xv-is-affine){.pf-ref} proves affineness and step [](#a-finite-b-module){.pf-ref} proves module finiteness.  The affine open $V$ was arbitrary.
:::

:::

::: pf-qed
Step [](#condition-implies-finite){.pf-ref} proves one implication and steps [](#finite-cover-witness){.pf-ref}, [](#common-distinguished-neighborhood){.pf-ref}, [](#preimage-wy-finite-affine){.pf-ref}, [](#finite-subcover-of-v){.pf-ref}, [](#bj-generate-unit-ideal){.pf-ref}, [](#aj-generate-unit-ideal-and-affine-loci){.pf-ref}, [](#xv-is-affine){.pf-ref}, [](#localization-finite){.pf-ref}, [](#module-lemma){.pf-ref}, [](#a-finite-b-module){.pf-ref}, and [](#finite-over-affine-open){.pf-ref} prove the converse.
:::

:::
:::
