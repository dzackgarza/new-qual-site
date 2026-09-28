---
schema: qual/card@1
id: P-AGH2119EXTZERO
kind: problem
title: Extending a sheaf by zero outside a closed or an open subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Extension By Zero
  - Exact Sequences
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.19 statement and source-order placement after II.1.18.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a topological space, let $Z$ be a closed subset with inclusion $i: Z \to X$, let $U = X \sm Z$ be the complementary open subset, and let $j: U \to X$ be its inclusion.

a. Let $\mcf$ be a sheaf on $Z$.
Show that the stalk $(i_* \mcf)_P$ of the direct image sheaf on $X$ is $\mcf_P$ if $P \in Z$ and $0$ if $P \notin Z$.
Hence $i_* \mcf$ is called the sheaf obtained by **extending $\mcf$ by zero outside $Z$**.

b. Now let $\mcf$ be a sheaf on $U$.
Let $j_!(\mcf)$ be the sheaf on $X$ associated to the presheaf $V \mapsto \mcf(V)$ if $V \subseteq U$ and $V \mapsto 0$ otherwise.
Show that the stalk $(j_!(\mcf))_P$ equals $\mcf_P$ if $P \in U$ and $0$ if $P \notin U$, and show that $j_! \mcf$ is the only sheaf on $X$ with this property whose restriction to $U$ is $\mcf$.
We call $j_! \mcf$ the sheaf obtained by **extending $\mcf$ by zero outside $U$**.

c. Now let $\mcf$ be a sheaf on $X$.
Show that there is an exact sequence of sheaves on $X$,
\[
0 \to j_!\qty{\ro{\mcf}{U}} \to \mcf \to i_*\qty{\ro{\mcf}{Z}} \to 0.
\]
:::

::: {.solution}
<1>1. If $\mathcal F$ is a sheaf on the closed subspace $Z$, then for every $P\in Z$,
\[
\boxed{(i_*\mathcal F)_P\cong\mathcal F_P.}
\]
::: {.proof}
For an open set $V\subseteq X$,
\[
(i_*\mathcal F)(V)=\mathcal F(V\cap Z).
\]
Hence
\[
(i_*\mathcal F)_P
=
\varinjlim_{P\in V}\mathcal F(V\cap Z).
\]

The sets $V\cap Z$, as $V$ ranges over the open neighborhoods of $P$ in $X$, are exactly a cofinal family of open neighborhoods of $P$ in the subspace $Z$.  Therefore this direct limit is the stalk
\[
\mathcal F_P
=
\varinjlim_{P\in W\subseteq Z}\mathcal F(W).
\]
:::

<1>2. If $P\notin Z$, then
\[
\boxed{(i_*\mathcal F)_P=0.}
\]
::: {.proof}
Because $Z$ is closed, its complement
\[
U=X\setminus Z
\]
is an open neighborhood of $P$.  For every open neighborhood
\[
P\in V\subseteq U,
\]
one has
\[
V\cap Z=\varnothing,
\]
so
\[
(i_*\mathcal F)(V)=\mathcal F(\varnothing)=0.
\]
These neighborhoods are cofinal among all neighborhoods of $P$, hence the stalk is zero.
:::

<1>3. Thus $i_*\mathcal F$ is extension by zero outside $Z$:
\[
\boxed{
(i_*\mathcal F)_P
\cong
\begin{cases}
\mathcal F_P,&P\in Z,\\
0,&P\notin Z.
\end{cases}
}
\]
::: {.proof}
Combine <1>1 and <1>2.
:::

<1>4. Now let $\mathcal F$ be a sheaf on the open subspace $U$.  Define the presheaf $\mathcal P$ on $X$ by
\[
\mathcal P(V)=
\begin{cases}
\mathcal F(V),&V\subseteq U,\\
0,&V\not\subseteq U,
\end{cases}
\]
and let
\[
j_!\mathcal F=\mathcal P^+
\]
be its associated sheaf.  If $P\in U$, then
\[
\boxed{(j_!\mathcal F)_P\cong\mathcal F_P.}
\]
::: {.proof}
Sheafification does not change stalks, so
\[
(j_!\mathcal F)_P\cong\mathcal P_P.
\]
Since $U$ is open and contains $P$, the neighborhoods
\[
P\in V\subseteq U
\]
are cofinal among all neighborhoods of $P$ in $X$.  On them
\[
\mathcal P(V)=\mathcal F(V).
\]
Therefore
\[
\mathcal P_P
=\varinjlim_{P\in V\subseteq U}\mathcal F(V)
=\mathcal F_P.
\]
:::

<1>5. If $P\notin U$, then
\[
\boxed{(j_!\mathcal F)_P=0.}
\]
::: {.proof}
Every neighborhood $V$ of $P$ contains $P$, so no such $V$ can be contained in $U$.  Hence
\[
\mathcal P(V)=0
\]
for every neighborhood of $P$.  Thus
\[
\mathcal P_P=0,
\]
and sheafification preserves this stalk.
:::

<1>6. The restriction of $j_!\mathcal F$ to $U$ is naturally isomorphic to $\mathcal F$.
::: {.proof}
On the open subspace $U$, the presheaf $\mathcal P$ restricts to the sheaf $\mathcal F$ itself: for every open
\[
V\subseteq U,
\]
one has
\[
\mathcal P(V)=\mathcal F(V),
\]
with the same restriction maps.  Therefore sheafification does nothing after restricting to $U$, and
\[
(j_!\mathcal F)|_U\cong\mathcal F.
\]
:::

<1>7. The sheaf $j_!\mathcal F$ is unique, up to unique isomorphism compatible with the given identification on $U$, among sheaves $\mathcal G$ on $X$ such that
\[
\mathcal G|_U\cong\mathcal F
\qquad\text{and}\qquad
\mathcal G_P=0\quad(P\notin U).
\]
::: {.proof}
Fix an identification
\[
\theta_U:\mathcal F\xrightarrow{\sim}\mathcal G|_U.
\]
Define a morphism of presheaves
\[
\mathcal P\longrightarrow\mathcal G
\]
as follows.  If $V\subseteq U$, use
\[
\mathcal P(V)=\mathcal F(V)
\xrightarrow{\theta_U(V)}
\mathcal G(V).
\]
If $V\not\subseteq U$, use the unique zero map
\[
0=\mathcal P(V)\longrightarrow\mathcal G(V).
\]
These maps commute with restrictions.  Indeed, the only mixed case is
\[
W\subseteq V,
\qquad
W\subseteq U,
\qquad
V\not\subseteq U,
\]
and there the section from $\mathcal P(V)=0$ restricts to zero in both presheaves.

By the universal property of sheafification this induces
\[
\theta:j_!\mathcal F=\mathcal P^+\longrightarrow\mathcal G.
\]

For $P\in U$, the map on stalks is the isomorphism
\[
\mathcal F_P\xrightarrow{\sim}\mathcal G_P
\]
induced by $\theta_U$.  For $P\notin U$, both stalks are zero by <1>5 and the hypothesis on $\mathcal G$.  Hence $\theta$ is an isomorphism on every stalk, and therefore an isomorphism of sheaves.

Any isomorphism compatible with the fixed identification on $U$ must induce the same stalk maps at every point: those in $U$ are prescribed, and those outside $U$ are maps $0\to0$.  A morphism of sheaves is determined by its stalk maps, so this isomorphism is unique.
:::

<1>8. Let $\mathcal F$ now be a sheaf on all of $X$.  There is a natural morphism
\[
\alpha:
j_!(\mathcal F|_U)
\longrightarrow
\mathcal F
\]
which is the identity on stalks over $U$ and the zero map on stalks over $Z$.
::: {.proof}
Let $\mathcal P$ be the presheaf defining
\[
j_!(\mathcal F|_U).
\]
If $V\subseteq U$, define
\[
\mathcal P(V)=\mathcal F(V)
\longrightarrow\mathcal F(V)
\]
to be the identity.  If $V\not\subseteq U$, the source is zero, so use the zero map.  These maps define a presheaf morphism
\[
\mathcal P\to\mathcal F,
\]
which sheafifies to $\alpha$.

The stalk description follows from <1>4--<1>5 and the construction.
:::

<1>9. There is a natural morphism
\[
\beta:
\mathcal F
\longrightarrow
i_*(\mathcal F|_Z)
\]
which is the identity on stalks over $Z$ and has zero target on stalks over $U$.
::: {.proof}
For the closed inclusion
\[
i:Z\hookrightarrow X,
\]
the restriction sheaf on $Z$ is $i^{-1}\mathcal F$.  The unit of the adjunction
\[
i^{-1}\dashv i_*
\]
gives
\[
\beta:\mathcal F\longrightarrow i_*i^{-1}\mathcal F
=i_*(\mathcal F|_Z).
\]

By <1>1--<1>2, the target stalk is $\mathcal F_P$ at $P\in Z$ and zero at $P\in U$.  At a point of $Z$, the adjunction unit is induced by restricting a local section to smaller neighborhoods in the subspace $Z$, so the induced map on the stalk is the identity under the natural identification
\[
(i_*i^{-1}\mathcal F)_P\cong\mathcal F_P.
\]
:::

<1>10. The sequence
\[
\boxed{
0
\longrightarrow
j_!(\mathcal F|_U)
\xrightarrow{\alpha}
\mathcal F
\xrightarrow{\beta}
i_*(\mathcal F|_Z)
\longrightarrow0
}
\]
is exact.
::: {.proof}
Exactness of sheaves of abelian groups may be checked on stalks.

If $P\in U$, then <1>4--<1>5 and <1>3 identify the stalk sequence with
\[
0\longrightarrow
\mathcal F_P
\xrightarrow{\operatorname{id}}
\mathcal F_P
\longrightarrow0
\longrightarrow0,
\]
which is exact.

If $P\in Z$, the stalk sequence is
\[
0\longrightarrow0
\longrightarrow
\mathcal F_P
\xrightarrow{\operatorname{id}}
\mathcal F_P
\longrightarrow0,
\]
which is also exact.

Thus the original sequence is exact at every stalk and hence exact as a sequence of sheaves.
:::

<1>11. Q.E.D.
::: {.proof}
Steps <1>1--<1>3 prove part (a), <1>4--<1>7 prove part (b), and <1>8--<1>10 prove part (c).
:::
:::
