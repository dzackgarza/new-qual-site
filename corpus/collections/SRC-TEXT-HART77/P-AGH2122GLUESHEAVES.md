---
schema: qual/card@1
id: P-AGH2122GLUESHEAVES
kind: problem
title: Glueing sheaves along an open cover with cocycle data
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Glueing
  - Descent
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.22 statement and source-order placement after II.1.21.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a topological space, let $\mathfrak{U} = \theset{U_i}$ be an open cover of $X$, and suppose we are given for each $i$ a sheaf $\mcf_i$ on $U_i$, and for each $i, j$ an isomorphism
\[
\phi_{ij}: \restrictionof{\mcf_i}{U_i \intersect U_j} \to \restrictionof{\mcf_j}{U_i \intersect U_j}
\]
such that

1. for each $i$, $\phi_{ii} = \id$, and

2. for each $i, j, k$, $\phi_{ik} = \phi_{jk} \circ \phi_{ij}$ on $U_i \intersect U_j \intersect U_k$.

Show that there exists a unique sheaf $\mcf$ on $X$, together with isomorphisms $\psi_i: \restrictionof{\mcf}{U_i} \to \mcf_i$, such that for each $i, j$ one has $\psi_j = \phi_{ij} \circ \psi_i$ on $U_i \intersect U_j$.
We say that $\mcf$ is obtained by **glueing** the sheaves $\mcf_i$ via the isomorphisms $\phi_{ij}$.
:::

::: {.solution}
First note that the cocycle conditions imply
\[
\phi_{ji}=\phi_{ij}^{-1}.
\]
Indeed, on $U_i\cap U_j$ one has
\[
\operatorname{id}
=\phi_{ii}
=\phi_{ji}\circ\phi_{ij}.
\]

::: pf

::: {.pf-step #s1}

For every open set $V\subseteq X$, define
\[
\mathcal F(V)
\]
to be the set of tuples
\[
(s_i)_i,
\qquad
s_i\in\mathcal F_i(V\cap U_i),
\]
such that for every pair $i,j$,
\[
\boxed{
\phi_{ij}
\bigl(s_i|_{V\cap U_i\cap U_j}\bigr)
=
s_j|_{V\cap U_i\cap U_j}.
}
\]

::: pf-proof

This is the natural compatibility condition saying that the local sections $s_i$ describe the same putative global section after the prescribed identifications of the sheaves on overlaps.

:::

:::

::: {.pf-step #s2}

Componentwise restriction makes $\mathcal F$ a presheaf on $X$.

::: pf-proof

Let $W\subseteq V$ and let
\[
s=(s_i)_i\in\mathcal F(V).
\]
Define
\[
s|_W
=
\bigl(s_i|_{W\cap U_i}\bigr)_i.
\]

For every $i,j$, restriction of the compatibility equation from step [](#s1){.pf-ref} gives
\[
\phi_{ij}
\bigl(s_i|_{W\cap U_i\cap U_j}\bigr)
=
s_j|_{W\cap U_i\cap U_j},
\]
because $\phi_{ij}$ is a morphism of sheaves and hence commutes with restrictions.  Thus the restricted tuple lies in $\mathcal F(W)$.

Identity and composition laws hold componentwise, so these maps define a presheaf.

:::

:::

::: {.pf-step #s3}

The presheaf $\mathcal F$ satisfies the sheaf uniqueness axiom.

::: pf-proof

Let
\[
V=\bigcup_\alpha V_\alpha
\]
and suppose
\[
s=(s_i)_i,
\qquad
t=(t_i)_i
\]
in $\mathcal F(V)$ have equal restrictions to every $V_\alpha$.

Fix $i$.  Then
\[
s_i|_{V_\alpha\cap U_i}
=
t_i|_{V_\alpha\cap U_i}
\]
for every $\alpha$.  The opens $V_\alpha\cap U_i$ cover $V\cap U_i$, and $\mathcal F_i$ is a sheaf, so
\[
s_i=t_i.
\]
This holds for every $i$, hence $s=t$.

:::

:::

::: {.pf-step #s4}

The presheaf $\mathcal F$ satisfies the sheaf gluing axiom.

::: pf-proof

Let
\[
V=\bigcup_\alpha V_\alpha
\]
and suppose compatible sections
\[
s^{(\alpha)}
=
(s_i^{(\alpha)})_i
\in\mathcal F(V_\alpha)
\]
are given.

Fix $i$.  The sections
\[
s_i^{(\alpha)}
\in
\mathcal F_i(V_\alpha\cap U_i)
\]
agree on overlaps because the tuples $s^{(\alpha)}$ do.  Since $\mathcal F_i$ is a sheaf, they glue uniquely to
\[
s_i\in\mathcal F_i(V\cap U_i).
\]

We must check that the tuple
\[
s=(s_i)_i
\]
satisfies the compatibility condition of step [](#s1){.pf-ref}.  Fix $i,j$.  On every open
\[
V_\alpha\cap U_i\cap U_j,
\]
one has
\[
\phi_{ij}(s_i)
=
\phi_{ij}(s_i^{(\alpha)})
=
s_j^{(\alpha)}
=
s_j.
\]
These opens cover
\[
V\cap U_i\cap U_j,
\]
so uniqueness in the sheaf $\mathcal F_j$ gives
\[
\phi_{ij}(s_i)=s_j
\]
on the whole overlap.  Thus
\[
s\in\mathcal F(V).
\]

By construction it restricts to every $s^{(\alpha)}$, and uniqueness follows from step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Hence $\mathcal F$ is a sheaf on $X$.

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} give the presheaf structure and both sheaf axioms.

:::

:::

::: {.pf-step #s6}

For every $i$, projection to the $i$th component defines a morphism of sheaves on $U_i$,
\[
\psi_i:
\mathcal F|_{U_i}
\longrightarrow
\mathcal F_i.
\]

::: pf-proof

If
\[
V\subseteq U_i
\]
and
\[
s=(s_j)_j\in\mathcal F(V),
\]
define
\[
(\psi_i)_V(s)=s_i.
\]
These projections commute with restriction because restrictions in $\mathcal F$ are componentwise.

:::

:::

::: {.pf-step #s7}

Each $\psi_i$ is an isomorphism.

::: pf-proof

Fix
\[
V\subseteq U_i.
\]
Given
\[
t\in\mathcal F_i(V),
\]
define for every $j$
\[
s_j
=
\phi_{ij}
\bigl(t|_{V\cap U_j}\bigr)
\in
\mathcal F_j(V\cap U_j).
\]
Here on $V\cap U_j$ the map $\phi_{ij}$ is understood after restricting to
\[
U_i\cap U_j;
\]
this is legitimate since $V\subseteq U_i$.

For $j,k$, the cocycle condition gives
\[
\phi_{jk}(s_j)
=
\phi_{jk}\phi_{ij}(t)
=
\phi_{ik}(t)
=
s_k
\]
on $V\cap U_j\cap U_k$.  Thus
\[
(s_j)_j\in\mathcal F(V).
\]

Its $i$th component is
\[
s_i
=\phi_{ii}(t)=t,
\]
so this construction is a right inverse to $(\psi_i)_V$.

Conversely, if $s=(s_j)_j\in\mathcal F(V)$, compatibility with the $i$th component says
\[
s_j
=
\phi_{ij}(s_i)
\]
on $V\cap U_j$.  Thus the whole tuple is uniquely reconstructed from $s_i$, and the same construction is a left inverse.  Hence $(\psi_i)_V$ is bijective for every $V\subseteq U_i$, naturally in $V$, so $\psi_i$ is an isomorphism of sheaves.

:::

:::

::: {.pf-step #s8}

On every overlap $U_i\cap U_j$, the local identifications satisfy
\[
\boxed{
\psi_j
=
\phi_{ij}\circ\psi_i.
}
\]

::: pf-proof

For a compatible tuple $s=(s_k)_k$, the defining condition of $\mathcal F$ gives
\[
s_j=\phi_{ij}(s_i)
\]
on the overlap.  Since $\psi_i$ and $\psi_j$ are the corresponding component projections, this is exactly the displayed identity.

:::

:::

::: {.pf-step #s9}

The pair
\[
(\mathcal F,\{\psi_i\})
\]
is unique up to a unique isomorphism compatible with all the $\psi_i$.

::: pf-proof

Suppose $\mathcal G$ is another sheaf on $X$ with isomorphisms
\[
\chi_i:\mathcal G|_{U_i}\xrightarrow{\sim}\mathcal F_i
\]
satisfying
\[
\chi_j=\phi_{ij}\circ\chi_i
\]
on every overlap.

For an open $V\subseteq X$ and a section
\[
t\in\mathcal G(V),
\]
define
\[
\Theta_V(t)
=
\left(
\chi_i(t|_{V\cap U_i})
\right)_i.
\]
The overlap condition on the $\chi_i$ says exactly that this tuple is compatible in the sense of step [](#s1){.pf-ref}.  Hence
\[
\Theta_V(t)\in\mathcal F(V).
\]
The construction commutes with restrictions, so it defines a sheaf morphism
\[
\Theta:\mathcal G\longrightarrow\mathcal F.
\]

On $U_i$ one has
\[
\psi_i\circ\Theta|_{U_i}
=\chi_i.
\]
Since both $\psi_i$ and $\chi_i$ are isomorphisms, $\Theta$ restricts to an isomorphism on every member of the cover.  A morphism of sheaves which is locally an isomorphism on an open cover is an isomorphism globally.

If
\[
\Theta':\mathcal G\to\mathcal F
\]
is another morphism compatible with all local identifications, then
\[
\Theta'|_{U_i}
=\psi_i^{-1}\chi_i
=\Theta|_{U_i}
\]
for every $i$.  Since the $U_i$ cover $X$, the two sheaf morphisms are equal.  Thus the compatible isomorphism is unique.

:::

:::

::: {.pf-step #s10}

Therefore the sheaves $\mathcal F_i$ glue along the cocycle $\phi_{ij}$ to a sheaf $\mathcal F$ on $X$, uniquely up to the unique compatible isomorphism:
\[
\boxed{
\mathcal F|_{U_i}\cong\mathcal F_i,
\qquad
\psi_j=\phi_{ij}\psi_i.
}
\]

::: pf-proof

Existence is steps [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} and uniqueness is step [](#s9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s10){.pf-ref} is precisely the sheaf-gluing assertion of the exercise.

:::

:::

:::
