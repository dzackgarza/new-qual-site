---
schema: qual/card@1
id: P-AGH2115SHEAFHOM
kind: problem
title: Local morphisms between two sheaves form a sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Sheaf Hom
  - Restriction
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.15 statement and source-order placement after II.1.14.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $\mcf, \mcg$ be sheaves of abelian groups on $X$.
For any open set $U \subseteq X$, show that the set $\Hom(\ro{\mcf}{U}, \ro{\mcg}{U})$ of morphisms of the restricted sheaves has a natural structure of abelian group.
Show that the presheaf
\[
U \mapsto \Hom(\ro{\mcf}{U}, \ro{\mcg}{U})
\]
is a sheaf.
It is called the **sheaf of local morphisms of $\mcf$ into $\mcg$**, or "sheaf hom" for short, and is denoted $\sheafhom(\mcf, \mcg)$.
:::

::: {.solution}
For an open set $U\subseteq X$, write
\[
\mathcal H(U)
=\operatorname{Hom}(\mathcal F|_U,\mathcal G|_U).
\]

<1>1. The set $\mathcal H(U)$ is naturally an abelian group.
::: {.proof}
Let
\[
\phi,\psi:\mathcal F|_U\longrightarrow\mathcal G|_U
\]
be morphisms of sheaves of abelian groups.  Define
\[
(\phi+\psi)_V:\mathcal F(V)\longrightarrow\mathcal G(V)
\]
for every open $V\subseteq U$ by
\[
(\phi+\psi)_V(s)=\phi_V(s)+\psi_V(s).
\]

Because the restriction maps of $\mathcal G$ are homomorphisms and both $\phi$ and $\psi$ commute with restrictions, so does $\phi+\psi$.  Hence it is a morphism of sheaves.

The zero morphism is defined sectionwise by zero, and
\[
(-\phi)_V(s)=-\phi_V(s).
\]
All abelian-group identities hold sectionwise in the groups $\mathcal G(V)$.  Thus $\mathcal H(U)$ is an abelian group.
:::

<1>2. If $V\subseteq U$, restriction of sheaf morphisms defines a homomorphism
\[
\rho_{UV}:\mathcal H(U)\longrightarrow\mathcal H(V),
\qquad
\phi\longmapsto\phi|_V.
\]
These maps make $\mathcal H$ a presheaf of abelian groups.
::: {.proof}
Restricting
\[
\phi:\mathcal F|_U\to\mathcal G|_U
\]
to the open subspace $V$ gives
\[
\phi|_V:\mathcal F|_V\to\mathcal G|_V.
\]
Restriction respects sums by the sectionwise definition in <1>1.  Also
\[
\phi|_U=\phi,
\qquad
(\phi|_V)|_W=\phi|_W
\]
for $W\subseteq V\subseteq U$.  These are exactly the presheaf identities.
:::

<1>3. Let
\[
U=\bigcup_iU_i
\]
and suppose morphisms
\[
\phi_i:\mathcal F|_{U_i}\longrightarrow\mathcal G|_{U_i}
\]
agree on every overlap:
\[
\phi_i|_{U_i\cap U_j}
=
\phi_j|_{U_i\cap U_j}.
\]
For every open $V\subseteq U$ and every section $s\in\mathcal F(V)$, the local sections
\[
t_i
:=
(\phi_i)_{V\cap U_i}(s|_{V\cap U_i})
\in
\mathcal G(V\cap U_i)
\]
agree on overlaps.
::: {.proof}
On
\[
V\cap U_i\cap U_j,
\]
the restrictions of $\phi_i$ and $\phi_j$ are the same morphism.  Therefore
\[
t_i|_{V\cap U_i\cap U_j}
=
(\phi_i)(s|_{V\cap U_i\cap U_j})
=
(\phi_j)(s|_{V\cap U_i\cap U_j})
=
t_j|_{V\cap U_i\cap U_j}.
\]
:::

<1>4. The sections in <1>3 glue uniquely to a section
\[
\phi_V(s)\in\mathcal G(V).
\]
This defines a homomorphism
\[
\phi_V:\mathcal F(V)\longrightarrow\mathcal G(V).
\]
::: {.proof}
The opens
\[
V\cap U_i
\]
cover $V$.  By <1>3, the sections $t_i$ are compatible, so the sheaf axiom for $\mathcal G$ gives a unique section
\[
t\in\mathcal G(V)
\]
restricting to every $t_i$.  Define
\[
\phi_V(s)=t.
\]

For $s,s'\in\mathcal F(V)$, the restrictions of
\[
\phi_V(s+s')
\]
and
\[
\phi_V(s)+\phi_V(s')
\]
to every $V\cap U_i$ are equal because $(\phi_i)_{V\cap U_i}$ is a homomorphism.  Uniqueness in the sheaf axiom gives
\[
\phi_V(s+s')=\phi_V(s)+\phi_V(s').
\]
Similarly $\phi_V(0)=0$, so $\phi_V$ is a group homomorphism.
:::

<1>5. The homomorphisms $\phi_V$ commute with restrictions, so they define a sheaf morphism
\[
\phi:\mathcal F|_U\longrightarrow\mathcal G|_U.
\]
::: {.proof}
Let $W\subseteq V\subseteq U$ and $s\in\mathcal F(V)$.  Compare
\[
\phi_V(s)|_W
\qquad\text{and}\qquad
\phi_W(s|_W).
\]
On each open
\[
W\cap U_i,
\]
both restrict to
\[
(\phi_i)_{W\cap U_i}(s|_{W\cap U_i}),
\]
because each local morphism $\phi_i$ commutes with restrictions.  Since the $W\cap U_i$ cover $W$, uniqueness for the sheaf $\mathcal G$ gives
\[
\phi_V(s)|_W=\phi_W(s|_W).
\]
Thus the family $(\phi_V)$ is a morphism of sheaves.
:::

<1>6. The morphism $\phi$ restricts to $\phi_i$ on every $U_i$.
::: {.proof}
Let $V\subseteq U_i$ and $s\in\mathcal F(V)$.  In the construction of $\phi_V(s)$, one of the local sections is
\[
(\phi_i)_V(s).
\]
The glued section restricts to this section on $V$ itself, hence
\[
\phi_V(s)=(\phi_i)_V(s).
\]
Therefore
\[
\phi|_{U_i}=\phi_i.
\]
:::

<1>7. The morphism $\phi$ is the unique morphism on $U$ restricting to all the $\phi_i$.
::: {.proof}
If
\[
\psi:\mathcal F|_U\to\mathcal G|_U
\]
has the same restrictions, then for every open $V\subseteq U$ and $s\in\mathcal F(V)$ the two sections
\[
\phi_V(s),\quad\psi_V(s)\in\mathcal G(V)
\]
have equal restrictions on every $V\cap U_i$.  Since those opens cover $V$ and $\mathcal G$ is a sheaf,
\[
\phi_V(s)=\psi_V(s).
\]
Thus $\phi=\psi$.
:::

<1>8. Consequently
\[
\boxed{
U\longmapsto
\operatorname{Hom}(\mathcal F|_U,\mathcal G|_U)
}
\]
is a sheaf of abelian groups, denoted
\[
\mathcal Hom(\mathcal F,\mathcal G).
\]
::: {.proof}
Step <1>2 gives the presheaf structure, while <1>3--<1>7 prove existence and uniqueness of gluing for arbitrary open covers.
:::

<1>9. Q.E.D.
::: {.proof}
Steps <1>1 and <1>8 are exactly the two assertions of the exercise.
:::
:::
