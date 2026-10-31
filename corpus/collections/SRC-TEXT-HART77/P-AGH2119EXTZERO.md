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

(a) Let $\mcf$ be a sheaf on $Z$.
Show that the stalk $(i_* \mcf)_P$ of the direct image sheaf on $X$ is $\mcf_P$ if $P \in Z$ and $0$ if $P \notin Z$.
Hence $i_* \mcf$ is called the sheaf obtained by \dfn{extending $\mcf$ by zero outside $Z$}.

(b) Now let $\mcf$ be a sheaf on $U$.
Let $j_!(\mcf)$ be the sheaf on $X$ associated to the presheaf $V \mapsto \mcf(V)$ if $V \subseteq U$ and $V \mapsto 0$ otherwise.
Show that the stalk $(j_!(\mcf))_P$ equals $\mcf_P$ if $P \in U$ and $0$ if $P \notin U$, and show that $j_! \mcf$ is the only sheaf on $X$ with this property whose restriction to $U$ is $\mcf$.
We call $j_! \mcf$ the sheaf obtained by \dfn{extending $\mcf$ by zero outside $U$}.

(c) Now let $\mcf$ be a sheaf on $X$.
Show that there is an exact sequence of sheaves on $X$,
$$
0 \to j_!\qty{\restrictionof{\mcf}{U}} \to \mcf \to i_*\qty{\restrictionof{\mcf}{Z}} \to 0.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $\mcf$ is a sheaf on the closed subspace $Z$, then for every $P\in Z$,
$$
\boxed{(i_*\mcf)_P\cong\mcf_P.}
$$

::: pf-proof

For an open set $V\subseteq X$,
$$
(i_*\mcf)(V)=\mcf(V\cap Z).
$$
Hence
$$
(i_*\mcf)_P
=
\varinjlim_{P\in V}\mcf(V\cap Z).
$$

The sets $V\cap Z$, as $V$ ranges over the open neighborhoods of $P$ in $X$, are exactly a cofinal family of open neighborhoods of $P$ in the subspace $Z$.  Therefore this direct limit is the stalk
$$
\mcf_P
=
\varinjlim_{P\in W\subseteq Z}\mcf(W).
$$

:::

:::

::: {.pf-step #s2}

If $P\notin Z$, then
$$
\boxed{(i_*\mcf)_P=0.}
$$

::: pf-proof

Because $Z$ is closed, its complement
$$
U=X\setminus Z
$$
is an open neighborhood of $P$.  For every open neighborhood
$$
P\in V\subseteq U,
$$
one has
$$
V\cap Z=\varnothing,
$$
so
$$
(i_*\mcf)(V)=\mcf(\varnothing)=0.
$$
These neighborhoods are cofinal among all neighborhoods of $P$, hence the stalk is zero.

:::

:::

::: {.pf-step #s3}

Thus $i_*\mcf$ is extension by zero outside $Z$:
$$
\boxed{
(i_*\mcf)_P
\cong
\begin{cases}
\mcf_P,&P\in Z,\\
0,&P\notin Z.
\end{cases}
}
$$

::: pf-proof

Combine steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Now let $\mcf$ be a sheaf on the open subspace $U$.  Define the presheaf $\mcp$ on $X$ by
$$
\mcp(V)=
\begin{cases}
\mcf(V),&V\subseteq U,\\
0,&V\not\subseteq U,
\end{cases}
$$
and let
$$
j_!\mcf=\mcp^+
$$
be its associated sheaf.  If $P\in U$, then
$$
\boxed{(j_!\mcf)_P\cong\mcf_P.}
$$

::: pf-proof

Sheafification does not change stalks, so
$$
(j_!\mcf)_P\cong\mcp_P.
$$
Since $U$ is open and contains $P$, the neighborhoods
$$
P\in V\subseteq U
$$
are cofinal among all neighborhoods of $P$ in $X$.  On them
$$
\mcp(V)=\mcf(V).
$$
Therefore
$$
\mcp_P
=\varinjlim_{P\in V\subseteq U}\mcf(V)
=\mcf_P.
$$

:::

:::

::: {.pf-step #s5}

If $P\notin U$, then
$$
\boxed{(j_!\mcf)_P=0.}
$$

::: pf-proof

Every neighborhood $V$ of $P$ contains $P$, so no such $V$ can be contained in $U$.  Hence
$$
\mcp(V)=0
$$
for every neighborhood of $P$.  Thus
$$
\mcp_P=0,
$$
and sheafification preserves this stalk.

:::

:::

::: {.pf-step #s6}

The restriction of $j_!\mcf$ to $U$ is naturally isomorphic to $\mcf$.

::: pf-proof

On the open subspace $U$, the presheaf $\mcp$ restricts to the sheaf $\mcf$ itself: for every open
$$
V\subseteq U,
$$
one has
$$
\mcp(V)=\mcf(V),
$$
with the same restriction maps.  Therefore sheafification does nothing after restricting to $U$, and
$$
(j_!\mcf)\restrict_U\cong\mcf.
$$

:::

:::

::: {.pf-step #s7}

The sheaf $j_!\mcf$ is unique, up to unique isomorphism compatible with the given identification on $U$, among sheaves $\mcg$ on $X$ such that
$$
\mcg\restrict_U\cong\mcf
\qquad\text{and}\qquad
\mcg_P=0\quad(P\notin U).
$$

::: pf-proof

Fix an identification
$$
\theta_U:\mcf\xrightarrow{\sim}\mcg\restrict_U.
$$
Define a morphism of presheaves
$$
\mcp\longrightarrow\mcg
$$
as follows.  If $V\subseteq U$, use
$$
\mcp(V)=\mcf(V)
\xrightarrow{\theta_U(V)}
\mcg(V).
$$
If $V\not\subseteq U$, use the unique zero map
$$
0=\mcp(V)\longrightarrow\mcg(V).
$$
These maps commute with restrictions.  Indeed, the only mixed case is
$$
W\subseteq V,
\qquad
W\subseteq U,
\qquad
V\not\subseteq U,
$$
and there the section from $\mcp(V)=0$ restricts to zero in both presheaves.

By the universal property of sheafification this induces
$$
\theta:j_!\mcf=\mcp^+\longrightarrow\mcg.
$$

For $P\in U$, the map on stalks is the isomorphism
$$
\mcf_P\xrightarrow{\sim}\mcg_P
$$
induced by $\theta_U$.  For $P\notin U$, both stalks are zero by step [](#s5){.pf-ref} and the hypothesis on $\mcg$.  Hence $\theta$ is an isomorphism on every stalk, and therefore an isomorphism of sheaves.

Any isomorphism compatible with the fixed identification on $U$ must induce the same stalk maps at every point: those in $U$ are prescribed, and those outside $U$ are maps $0\to0$.  A morphism of sheaves is determined by its stalk maps, so this isomorphism is unique.

:::

:::

::: {.pf-step #s8}

Let $\mcf$ now be a sheaf on all of $X$.  There is a natural morphism
$$
\alpha:
j_!(\mcf\restrict_U)
\longrightarrow
\mcf
$$
which is the identity on stalks over $U$ and the zero map on stalks over $Z$.

::: pf-proof

Let $\mcp$ be the presheaf defining
$$
j_!(\mcf\restrict_U).
$$
If $V\subseteq U$, define
$$
\mcp(V)=\mcf(V)
\longrightarrow\mcf(V)
$$
to be the identity.  If $V\not\subseteq U$, the source is zero, so use the zero map.  These maps define a presheaf morphism
$$
\mcp\to\mcf,
$$
which sheafifies to $\alpha$.

The stalk description follows from steps [](#s4){.pf-ref} and [](#s5){.pf-ref} and the construction.

:::

:::

::: {.pf-step #s9}

There is a natural morphism
$$
\beta:
\mcf
\longrightarrow
i_*(\mcf\restrict_Z)
$$
which is the identity on stalks over $Z$ and has zero target on stalks over $U$.

::: pf-proof

For the closed inclusion
$$
i:Z\hookrightarrow X,
$$
the restriction sheaf on $Z$ is $i^{-1}\mcf$.  The unit of the adjunction
$$
i^{-1}\dashv i_*
$$
gives
$$
\beta:\mcf\longrightarrow i_*i^{-1}\mcf
=i_*(\mcf\restrict_Z).
$$

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the target stalk is $\mcf_P$ at $P\in Z$ and zero at $P\in U$.  At a point of $Z$, the adjunction unit is induced by restricting a local section to smaller neighborhoods in the subspace $Z$, so the induced map on the stalk is the identity under the natural identification
$$
(i_*i^{-1}\mcf)_P\cong\mcf_P.
$$

:::

:::

::: {.pf-step #s10}

The sequence
$$
\boxed{
0
\longrightarrow
j_!(\mcf\restrict_U)
\xrightarrow{\alpha}
\mcf
\xrightarrow{\beta}
i_*(\mcf\restrict_Z)
\longrightarrow0
}
$$
is exact.

::: pf-proof

Exactness of sheaves of abelian groups may be checked on stalks.

If $P\in U$, then steps [](#s4){.pf-ref} and [](#s3){.pf-ref} identify the stalk sequence with
$$
0\longrightarrow
\mcf_P
\xrightarrow{\id}
\mcf_P
\longrightarrow0
\longrightarrow0,
$$
which is exact.

If $P\in Z$, steps [](#s5){.pf-ref} and [](#s3){.pf-ref} identify the stalk sequence with
$$
0\longrightarrow0
\longrightarrow
\mcf_P
\xrightarrow{\id}
\mcf_P
\longrightarrow0,
$$
which is also exact.

Thus the original sequence is exact at every stalk and hence exact as a sequence of sheaves.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (a), steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (b), and steps [](#s8){.pf-ref}, [](#s9){.pf-ref} and [](#s10){.pf-ref} prove part (c).

:::

:::

:::
