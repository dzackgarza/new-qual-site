---
schema: qual/card@1
id: P-AGH2313FTPROPS
kind: problem
title: Permanence properties of morphisms of finite type
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms Of Schemes
  - Finite Type
  - Base Change
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.13 statement and the standard permanence properties of finite type morphisms.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Exercise II.3.13 as printed: the seven parts (a)-(g) match the
    text version of the book, and every argument is correct. (a) applies
    Exercise II.3.11(b) for the closed subscheme of an affine and Exercise
    II.3.3(b) for finite type; the empty generating set is legitimate because
    A -> A/I is surjective. (b) is the computation A_f = A[f^{-1}] on
    distinguished opens. (c) composes the affine charts supplied by Exercise
    II.3.1; with B = C[b_1,...,b_m] and A = B[a_1,...,a_n] one does get
    A = C[b_1,...,b_m,a_1,...,a_n]. (d) uses A tensor_B B' = B'[a_1 tensor 1,
    ..., a_n tensor 1], and the passage from affine charts to the general base
    change is left to the reader in one sentence but is standard. (f), the
    substantial part, applies the only-if direction of Exercise II.3.1 to g
    composed with f over an affine chart of Z and then shrinks to a
    distinguished affine U' inside U intersect f^{-1}(V); the equality
    B[alpha_1,...,alpha_n] = A_a holds because C[alpha] = A_a and B[alpha] is a
    subring of A_a. (g) is Hilbert's basis theorem applied to the finite affine
    charts of Exercise II.3.3(b), over the finite affine cover of a noetherian
    Y. Kim's published solution, PDF pp. 25-26 (page checked in the PDF
    itself), agrees part by part; Cais covers (a)-(c) in the same way. The
    citations II.3.1, II.3.2, II.3.3(a)-(c) and II.3.11(b) are exercises of
    section II.3, not the propositions numbered 3.1 and 3.2 there, which state
    unrelated criteria. Nothing in the statement or the proof was changed.
---

::: {.problem}
(a) A closed immersion is a morphism of finite type.

(b) A quasi-compact open immersion is of finite type.

(c) A composition of two morphisms of finite type is of finite type.

(d) Morphisms of finite type are stable under base extension.

(e) If $X$ and $Y$ are schemes of finite type over $S$, then $\fiberprod{X}{S}{Y}$ is of finite type over $S$.

(f) If $X \mapsvia{f} Y \mapsvia{g} Z$ are two morphisms, and if $f$ is quasi-compact and $g \circ f$ is of finite type, then $f$ is of finite type.

(g) If $f: X \to Y$ is a morphism of finite type and $Y$ is noetherian, then $X$ is noetherian.
:::

::: {.solution}
The proof is Yang Pi-Yeh, *Hartshorne Solutions*, Solution 2.3.13 (Properties of Morphisms of Finite Type), transcribed and checked against the exercise as printed: part (a), that a closed immersion is of finite type; part (b), the affine restatement with $f^{-1}(U)=\Spec A$ for $A$ a finitely generated $k$-algebra; part (c), that $f$ finite type and $Y$ quasi-compact give quasi-compactness; and (i) to (vi), that the property is local on the target.

::: pf

::: {.pf-step #closed-immersion-finite-type}
A closed immersion is of finite type.

::: pf-proof
Let
$$
i:Z\hookrightarrow X
$$
be a closed immersion and let
$$
U=\Spec A\subseteq X
$$
be affine.  By Hartshorne II.3.11(b),
$$
i^{-1}(U)=\Spec(A/I)
$$
for some ideal $I\subseteq A$.

The quotient map $A\to A/I$ is surjective, so $A/I$ is generated as an $A$-algebra by the empty set; in particular it is finitely generated.  Hartshorne II.3.3(b) shows that $i$ is of finite type.
:::

:::

::: {.pf-step #open-immersion-locally-finite-type}
An open immersion is locally of finite type.

::: pf-proof
Let
$$
j:U\hookrightarrow X
$$
be an open immersion and let $u\in U$.  Choose an affine neighborhood
$$
V=\Spec A\subseteq X
$$
of $u$.  The intersection $U\cap V$ is open in $V$, so choose a distinguished neighborhood
$$
u\in D(f)\subseteq U\cap V.
$$
Then
$$
D(f)\cong\Spec A_f,
$$
and $A_f=A[f^{-1}]$ is generated as an $A$-algebra by the single element $f^{-1}$.  Hence $j$ is locally of finite type.
:::

:::

::: {.pf-step #qc-open-immersion-finite-type}
A quasi-compact open immersion is of finite type.

::: pf-proof
By step [](#open-immersion-locally-finite-type){.pf-ref} it is locally of finite type.  It is quasi-compact by hypothesis.  Hartshorne II.3.3(a) therefore implies that it is of finite type.
:::

:::

::: {.pf-step #composition-locally-finite-type}
The composition of two locally finite type morphisms is locally of finite type.

::: pf-proof
Let
$$
X\xrightarrow{f}Y\xrightarrow{g}Z
$$
be locally of finite type.  Take an affine open
$$
W=\Spec C\subseteq Z.
$$
By Hartshorne II.3.1, $g^{-1}(W)$ has an affine cover
$$
V_j=\Spec B_j
$$
with every $B_j$ finitely generated over $C$.

Again by II.3.1, each $f^{-1}(V_j)$ has an affine cover
$$
U_{jk}=\Spec A_{jk}
$$
with $A_{jk}$ finitely generated over $B_j$.

If
$$
B_j=C[b_1,\ldots,b_m]
$$
and
$$
A_{jk}=B_j[a_1,\ldots,a_n],
$$
then
$$
A_{jk}=C[b_1,\ldots,b_m,a_1,\ldots,a_n].
$$
Thus $A_{jk}$ is finitely generated over $C$.  These affines cover $(g\circ f)^{-1}(W)$, proving local finite type.
:::

:::

::: {.pf-step #composition-quasicompact}
The composition of two quasi-compact morphisms is quasi-compact.

::: pf-proof
Let $W\subseteq Z$ be affine.  Since $g$ is quasi-compact,
$$
g^{-1}(W)
$$
is quasi-compact.  Cover it by finitely many affine opens
$$
V_1,\ldots,V_r.
$$
Since $f$ is quasi-compact, every $f^{-1}(V_i)$ is quasi-compact.  Their finite union is
$$
(g\circ f)^{-1}(W),
$$
so this inverse image is quasi-compact.  Hartshorne II.3.2 gives the assertion.
:::

:::

::: {.pf-step #composition-finite-type}
The composition of two finite type morphisms is of finite type.

::: pf-proof
By Hartshorne II.3.3(a), finite type means locally finite type plus quasi-compact.  Apply step [](#composition-locally-finite-type){.pf-ref} to the local finite type parts and step [](#composition-quasicompact){.pf-ref} to the quasi-compact parts.
:::

:::

::: {.pf-step #base-change-locally-finite-type}
A base change of a locally finite type morphism is locally of finite type.

::: pf-proof
It is enough to work affinely.  Suppose
$$
\Spec A\longrightarrow\Spec B
$$
comes from a finitely generated $B$-algebra $A$, and let
$$
\Spec B'\longrightarrow\Spec B
$$
be any affine base change.  Then the pullback is
$$
\Spec(A\otimes_BB')\longrightarrow\Spec B'.
$$
If
$$
A=B[a_1,\ldots,a_n],
$$
then
$$
A\otimes_BB'=B'[a_1\otimes1,\ldots,a_n\otimes1].
$$
Thus the base-changed algebra is finitely generated.  Covering source and target by such affine charts gives the general statement.
:::

:::

::: {.pf-step #base-change-quasicompact}
A base change of a quasi-compact morphism is quasi-compact.

::: pf-proof
Let $f:X\to Y$ be quasi-compact and $Y'\to Y$ any morphism.  It is enough to test the base change
$$
f':X\times_YY'\longrightarrow Y'
$$
over an affine open $V'\subseteq Y'$.  Cover the image of $V'$ in $Y$ by affine opens $V_i$ and shrink to a finite cover of $V'$ by distinguished affine opens mapping into individual $V_i$.

Over such an affine $W'\to V_i$, the preimage is the base change of the quasi-compact scheme $f^{-1}(V_i)$ along $W'\to V_i$.  Choose a finite affine cover of $f^{-1}(V_i)$; its base changes are affine and finitely many, so the preimage over $W'$ is quasi-compact.  A finite union gives quasi-compactness over $V'$.
:::

:::

::: {.pf-step #base-change-finite-type}
A base change of a finite type morphism is of finite type.

::: pf-proof
Finite type is locally finite type plus quasi-compact by II.3.3(a).  Apply steps [](#base-change-locally-finite-type){.pf-ref} and [](#base-change-quasicompact){.pf-ref}.
:::

:::

::: {.pf-step #product-finite-type-over-s}
If $X$ and $Y$ are of finite type over $S$, then
$$
X\times_SY\longrightarrow S
$$
is of finite type.

::: pf-proof
The projection
$$
X\times_SY\longrightarrow Y
$$
is the base change of $X\to S$, so it is of finite type by step [](#base-change-finite-type){.pf-ref}.  The morphism $Y\to S$ is finite type by hypothesis.  Their composition is the structure morphism
$$
X\times_SY\to S,
$$
which is finite type by step [](#composition-finite-type){.pf-ref}.
:::

:::

::: {.pf-step #f-locally-finite-type-from-composite}
Suppose
$$
X\xrightarrow{f}Y\xrightarrow{g}Z
$$
and $g\circ f$ is locally of finite type.  Then $f$ is locally of finite type.

::: pf-proof
Fix $x\in X$.  Choose an affine open
$$
W=\Spec C\subseteq Z
$$
containing $g(f(x))$.  Since $g\circ f$ is locally of finite type, choose an affine neighborhood
$$
U=\Spec A\subseteq(g\circ f)^{-1}(W)
$$
of $x$ such that $A$ is finitely generated over $C$.

Choose an affine neighborhood
$$
V=\Spec B\subseteq g^{-1}(W)
$$
of $f(x)$.  Shrink $U$ to a distinguished affine neighborhood
$$
U'=\Spec A_a\subseteq U\cap f^{-1}(V)
$$
of $x$.

The ring maps factor as
$$
C\longrightarrow B\longrightarrow A_a.
$$
Since $A$ is finitely generated over $C$, so is $A_a=A[a^{-1}]$, say
$$
A_a=C[\alpha_1,\ldots,\alpha_n],
$$
the same elements also generate it over $B$:
$$
B[\alpha_1,\ldots,\alpha_n]
\supseteq
C[\alpha_1,\ldots,\alpha_n]
=A_a,
$$
while the left side is a subring of $A_a$, so equality holds.  Thus $f$ is locally of finite type at $x$.  Since $x$ was arbitrary, $f$ is locally of finite type.
:::

:::

::: {.pf-step #f-finite-type-from-composite-qc}
If $f$ is quasi-compact and $g\circ f$ is of finite type, then $f$ is of finite type.

::: pf-proof
The composite $g\circ f$ is locally of finite type, so step [](#f-locally-finite-type-from-composite){.pf-ref} shows that $f$ is locally of finite type.  Together with the assumed quasi-compactness of $f$, II.3.3(a) gives that $f$ is of finite type.
:::

:::

::: {.pf-step #x-has-noetherian-affine-cover}
Let $f:X\to Y$ be finite type and let $Y$ be noetherian.  Then $X$ has a finite affine cover
$$
X=\bigcup_{i,j}\Spec A_{ij}
$$
in which every $A_{ij}$ is noetherian.

::: pf-proof
Because $Y$ is noetherian, it is quasi-compact and has a finite affine cover
$$
Y=\bigcup_{i=1}^mV_i,
\qquad
V_i=\Spec B_i,
$$
with every $B_i$ noetherian.

By II.3.3(b), each $f^{-1}(V_i)$ has a finite affine cover
$$
\Spec A_{ij}
$$
with each $A_{ij}$ finitely generated over $B_i$.  Hilbert's basis theorem therefore implies that each $A_{ij}$ is noetherian.  Altogether these form a finite affine cover of $X$.
:::

:::

::: {.pf-step #x-is-noetherian}
The scheme $X$ in step [](#x-has-noetherian-affine-cover){.pf-ref} is noetherian.

::: pf-proof
Each affine chart $\Spec A_{ij}$ is a noetherian topological space because $A_{ij}$ is a noetherian ring.  A finite union of noetherian open subspaces is noetherian.  Thus the underlying topological space of $X$ is noetherian, and its affine coordinate rings are noetherian.  Hence $X$ is a noetherian scheme.
:::

:::

::: pf-qed
Steps [](#closed-immersion-finite-type){.pf-ref}, [](#qc-open-immersion-finite-type){.pf-ref}, [](#composition-finite-type){.pf-ref}, [](#base-change-finite-type){.pf-ref}, [](#product-finite-type-over-s){.pf-ref}, [](#f-finite-type-from-composite-qc){.pf-ref} and [](#x-is-noetherian){.pf-ref} prove parts (a)--(g), respectively.
:::

:::

:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter II §3, Exercise 3.13, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: Kim gives one line per part: $\Spec A/\mathfrak a$ for a closed immersion, a finite union of $\Spec A_{f_i}$ for a quasi-compact open immersion, generators $b_i\otimes1$ for base change, the chain $A\to B\to C$ for (f), and Hilbert's basis theorem for (g).
The proof above keeps those arguments and supplies what the one-line versions leave to the reader: quasi-compactness of a composition and of a base change, and the affine-chart reduction in (f) at a point $x$ together with an affine neighbourhood of $f(x)$ inside the same chart of $Z$.
Agree.
:::
