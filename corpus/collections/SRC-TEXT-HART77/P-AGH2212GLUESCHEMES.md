---
schema: qual/card@1
id: P-AGH2212GLUESCHEMES
kind: problem
title: Glueing a family of schemes along open subschemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Glueing
  - Disjoint Unions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.12 statement and source-order placement after II.2.11.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Generalize the glueing procedure of the text as follows.
Let $\theset{X_i}$ be a possibly infinite family of schemes.
For each $i \neq j$ suppose given an open subset $U_{ij} \subseteq X_i$ with its induced scheme structure.
Suppose also given for each $i \neq j$ an isomorphism of schemes $\phi_{ij}: U_{ij} \to U_{ji}$ such that

1. for each $i, j$, $\phi_{ji} = \inverseof{\phi_{ij}}$, and

2. for each $i, j, k$, $\phi_{ij}(U_{ij} \intersect U_{ik}) = U_{ji} \intersect U_{jk}$ and $\phi_{ik} = \phi_{jk} \circ \phi_{ij}$ on $U_{ij} \intersect U_{ik}$.

Then show that there is a scheme $X$, together with morphisms $\psi_i: X_i \to X$ for each $i$, such that

1. $\psi_i$ is an isomorphism of $X_i$ onto an open subscheme of $X$,

2. the $\psi_i(X_i)$ cover $X$,

3. $\psi_i(U_{ij}) = \psi_i(X_i) \intersect \psi_j(X_j)$, and

4. $\psi_i = \psi_j \circ \phi_{ij}$ on $U_{ij}$.

We say that $X$ is obtained by **glueing** the schemes $X_i$ along the isomorphisms $\phi_{ij}$.
An interesting special case is when the family $X_i$ is arbitrary but all the $U_{ij}$ and $\phi_{ij}$ are empty; then $X$ is called the **disjoint union** of the $X_i$ and is denoted $\coprod X_i$.
:::

::: {.solution}
For convenience set
\[
U_{ii}=X_i,
\qquad
\phi_{ii}=\operatorname{id}_{X_i}.
\]

::: pf

::: {.pf-step #sim-is-equivalence-relation}
On the disjoint union of underlying sets
\[
S=\coprod_i|X_i|
\]
define a relation by declaring, for $x\in X_i$ and $y\in X_j$,
\[
x\sim y
\quad\Longleftrightarrow\quad
x\in U_{ij}
\text{ and }
y=\phi_{ij}(x).
\]
Then $\sim$ is an equivalence relation.

::: pf-proof
Reflexivity follows from
\[
U_{ii}=X_i,
\qquad
\phi_{ii}=\operatorname{id}.
\]

If
\[
y=\phi_{ij}(x),
\]
then
\[
x=\phi_{ji}(y)
\]
because
\[
\phi_{ji}=\phi_{ij}^{-1},
\]
so the relation is symmetric.

For transitivity, suppose
\[
y=\phi_{ij}(x),
\qquad
z=\phi_{jk}(y),
\]
with
\[
x\in U_{ij},
\qquad
y\in U_{jk}.
\]
Since also
\[
y\in U_{ji},
\]
one has
\[
y\in U_{ji}\cap U_{jk}.
\]
The overlap hypothesis says
\[
U_{ji}\cap U_{jk}
=
\phi_{ij}(U_{ij}\cap U_{ik}).
\]
Since $\phi_{ij}$ is injective and $y=\phi_{ij}(x)$, it follows that
\[
x\in U_{ik}.
\]
On this overlap the cocycle condition gives
\[
z
=\phi_{jk}(\phi_{ij}(x))
=\phi_{ik}(x).
\]
Thus $x\sim z$.
:::

:::

::: {.pf-step #psi-i-injective}
Let
\[
|X|=S/\!\sim
\]
and give it the quotient topology.  Let
\[
q:S\longrightarrow|X|
\]
be the quotient map, and put
\[
\psi_i=q|_{X_i}:|X_i|\longrightarrow|X|.
\]
Each $\psi_i$ is injective.

::: pf-proof
If
\[
x,x'\in X_i
\]
have the same image in the quotient, then
\[
x\sim x'.
\]
By the definition with $i=j$,
\[
x'=\phi_{ii}(x)=x.
\]
Thus $\psi_i$ is injective.
:::

:::

::: {.pf-step #vi-open-in-x}
The image
\[
V_i:=\psi_i(X_i)
\]
is open in $|X|$.

::: pf-proof
By definition of the quotient topology, it is enough to show that
\[
q^{-1}(V_i)
\]
is open in the disjoint union $S$.

Its intersection with the component $X_i$ is all of $X_i$.  For $j\ne i$, a point
\[
y\in X_j
\]
maps into $V_i$ exactly when it is equivalent to some point of $X_i$, which by definition is exactly when
\[
y\in U_{ji}.
\]
Hence
\[
q^{-1}(V_i)
=
X_i
\amalg
\coprod_{j\ne i}U_{ji}.
\]
Every $U_{ji}$ is open in $X_j$, so this is open in the disjoint-union topology.  Therefore $V_i$ is open.
:::

:::

::: {.pf-step #psi-i-homeomorphism-onto-vi}
The map
\[
\psi_i:X_i\longrightarrow V_i
\]
is a homeomorphism.

::: pf-proof
It is already a continuous bijection by step [](#psi-i-injective){.pf-ref} and the definition of the quotient topology.
We show it is open.

Let
\[
W\subseteq X_i
\]
be open.
The inverse image in $S$ of
\[
\psi_i(W)
\]
has, in the component $X_j$, the subset
\[
\phi_{ij}(W\cap U_{ij})
\subseteq U_{ji}
\]
for $j\ne i$, and has $W$ in the component $X_i$.
Each of these sets is open because
\[
\phi_{ij}:U_{ij}\xrightarrow{\sim}U_{ji}
\]
is a homeomorphism.
Thus
\[
q^{-1}(\psi_i(W))
\]
is open in $S$, so $\psi_i(W)$ is open in $|X|$.

Hence $\psi_i$ is an open continuous bijection and therefore a homeomorphism onto $V_i$.
:::

:::

::: {.pf-step #vi-cover-and-overlap-formula}
The opens $V_i$ cover $|X|$, and
\[
\boxed{
V_i\cap V_j
=\psi_i(U_{ij})
=\psi_j(U_{ji}).
}
\]
Moreover,
\[
\boxed{
\psi_i
=\psi_j\circ\phi_{ij}
\quad\text{on }U_{ij}.
}
\]

::: pf-proof
The images cover because every equivalence class has a representative in some component $X_i$.

A point of $V_i$ belongs to $V_j$ exactly when its representative
\[
x\in X_i
\]
is equivalent to some point of $X_j$.  By definition, this is exactly the condition
\[
x\in U_{ij},
\]
and the corresponding representative in $X_j$ is
\[
\phi_{ij}(x).
\]
This proves both the intersection formula and
\[
\psi_i(x)=\psi_j(\phi_{ij}(x)).
\]
:::

:::

::: {.pf-step #gi-sheaves-and-overlap-isos}
Transport the structure sheaf $\mathcal O_{X_i}$ along the homeomorphism
\[
\psi_i:X_i\xrightarrow{\sim}V_i
\]
to obtain a sheaf $\mathcal G_i$ of rings on $V_i$.
The scheme isomorphisms $\phi_{ij}$ induce compatible sheaf isomorphisms
\[
\mathcal G_i|_{V_i\cap V_j}
\xrightarrow{\sim}
\mathcal G_j|_{V_i\cap V_j}.
\]

::: pf-proof
Define
\[
\mathcal G_i=(\psi_i)_*\mathcal O_{X_i}
\]
on $V_i$, using the homeomorphism $\psi_i$.

By step [](#vi-cover-and-overlap-formula){.pf-ref}, the overlap $V_i\cap V_j$ corresponds under $\psi_i$ to $U_{ij}$ and under $\psi_j$ to $U_{ji}$.
The scheme isomorphism
\[
\phi_{ij}:U_{ij}\xrightarrow{\sim}U_{ji}
\]
therefore transports the structure sheaf from the $i$-description of the overlap to the $j$-description.

The inverse condition
\[
\phi_{ji}=\phi_{ij}^{-1}
\]
and the triple-overlap cocycle
\[
\phi_{ik}=\phi_{jk}\circ\phi_{ij}
\]
imply the corresponding inverse and cocycle identities for these sheaf isomorphisms.
:::

:::

::: {.pf-step #gi-glue-to-ox}
The local sheaves $\mathcal G_i$ glue to a sheaf of rings
\[
\mathcal O_X
\]
on $|X|$, together with isomorphisms
\[
\mathcal O_X|_{V_i}
\xrightarrow{\sim}
\mathcal G_i.
\]

::: pf-proof
Apply the sheaf-gluing theorem of Hartshorne II.1.22 to the open cover
\[
|X|=\bigcup_iV_i
\]
and the compatible sheaf isomorphisms from step [](#gi-sheaves-and-overlap-isos){.pf-ref}.
:::

:::

::: {.pf-step #x-is-scheme-psi-i-iso}
The locally ringed space
\[
X=(|X|,\mathcal O_X)
\]
is a scheme, and each
\[
\psi_i:X_i\longrightarrow X
\]
is an isomorphism of schemes onto the open subscheme $V_i$.

::: pf-proof
By construction,
\[
(V_i,\mathcal O_X|_{V_i})
\cong
(X_i,\mathcal O_{X_i})
\]
as locally ringed spaces.
Thus every $V_i$ is itself a scheme and $\psi_i$ is an isomorphism onto it.

The opens $V_i$ cover $X$.  Each $X_i$ has an affine open cover, and transporting all those affine opens through the $\psi_i$ gives an affine open cover of $X$.  Hence $X$ is a scheme.
:::

:::

::: {.pf-step #four-properties-hold}
The maps $\psi_i$ satisfy all four required properties:
\[
\begin{aligned}
&\psi_i:X_i\xrightarrow{\sim}V_i\subseteq X,\\
&X=\bigcup_iV_i,\\
&V_i\cap V_j=\psi_i(U_{ij}),\\
&\psi_i=\psi_j\circ\phi_{ij}\text{ on }U_{ij}.
\end{aligned}
\]

::: pf-proof
The first property is step [](#x-is-scheme-psi-i-iso){.pf-ref}, and the remaining three are step [](#vi-cover-and-overlap-formula){.pf-ref}.
:::

:::

::: {.pf-step #glued-scheme-unique}
The glued scheme is unique up to a unique isomorphism compatible with the maps $\psi_i$.

::: pf-proof
Suppose
\[
X'
\]
with maps
\[
\psi_i':X_i\to X'
\]
has the same four properties.
On the open subset
\[
V_i=\psi_i(X_i)\subseteq X,
\]
define
\[
F_i
=
\psi_i'\circ\psi_i^{-1}:
V_i\longrightarrow X'.
\]
On
\[
V_i\cap V_j=\psi_i(U_{ij}),
\]
the compatibility conditions give
\[
\psi_i
=\psi_j\phi_{ij},
\qquad
\psi_i'
=\psi_j'\phi_{ij},
\]
so
\[
F_i=F_j
\]
on the overlap.
Hence the morphisms $F_i$ glue to a morphism
\[
F:X\to X'.
\]

Reversing the roles of $X$ and $X'$ gives
\[
G:X'\to X.
\]
Both composites restrict to the identity on the open covers by the $V_i$ and $V_i'$, hence
\[
GF=\operatorname{id}_X,
\qquad
FG=\operatorname{id}_{X'}.
\]
Thus $F$ is an isomorphism.  Any compatible isomorphism must agree with $F_i$ on every $V_i$, so it is unique.
:::

:::

::: {.pf-step #disjoint-union-case}
If all $U_{ij}$ for $i\ne j$ are empty, then no distinct components are identified and
\[
\boxed{
X=\coprod_iX_i
}
\]
is their disjoint union as a scheme.

::: pf-proof
The equivalence relation of step [](#sim-is-equivalence-relation){.pf-ref} becomes equality within each component and makes no cross-component identifications, so the underlying space is the topological disjoint union.

There are no nontrivial overlap isomorphisms of structure sheaves to impose.  Thus $\mathcal O_X$ restricts independently to $\mathcal O_{X_i}$ on each open-and-closed component.  This is precisely the scheme-theoretic disjoint union.
:::

:::

::: pf-qed
Steps [](#sim-is-equivalence-relation){.pf-ref}, [](#psi-i-injective){.pf-ref}, [](#vi-open-in-x){.pf-ref}, [](#psi-i-homeomorphism-onto-vi){.pf-ref}, [](#vi-cover-and-overlap-formula){.pf-ref}, [](#gi-sheaves-and-overlap-isos){.pf-ref}, [](#gi-glue-to-ox){.pf-ref}, [](#x-is-scheme-psi-i-iso){.pf-ref} and [](#four-properties-hold){.pf-ref} construct the required scheme and maps, step [](#glued-scheme-unique){.pf-ref} gives the expected uniqueness, and step [](#disjoint-union-case){.pf-ref} identifies the disjoint-union special case.
:::

:::

:::
