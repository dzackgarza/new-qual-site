---
schema: qual/card@1
id: P-AGH2117SKYSCRAPER
kind: problem
title: Skyscraper sheaves as pushforwards from the closure of a point
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Skyscraper Sheaves
  - Direct Image
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.1.17 statement and source-order placement after II.1.16.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a topological space, let $P$ be a point, and let $A$ be an abelian group.
Define a sheaf $i_P(A)$ on $X$ by $i_P(A)(U) = A$ if $P \in U$ and $0$ otherwise.

Verify that the stalk of $i_P(A)$ is $A$ at every point $Q \in \cl\qty{\ts{P}}$ and $0$ elsewhere, where $\cl\qty{\ts{P}}$ denotes the closure of the set consisting of the point $P$.
Hence the name "skyscraper sheaf".

Show that this sheaf can also be described as $i_*(A)$, where $A$ denotes the constant sheaf $A$ on the closed subspace $\cl\qty{\ts{P}}$ and $i: \cl\qty{\ts{P}} \to X$ is the inclusion.
:::

::: {.solution}
Let
\[
\mathcal S=i_P(A).
\]
Thus
\[
\mathcal S(U)=
\begin{cases}
A,&P\in U,\\
0,&P\notin U,
\end{cases}
\]
with the evident restriction maps: identity when both opens contain $P$, and the zero map whenever the smaller open does not contain $P$.

<1>1. The presheaf $\mathcal S$ is a sheaf.
::: {.proof}
Let
\[
U=\bigcup_\alpha U_\alpha
\]
be an open cover.

If $P\notin U$, then $P\notin U_\alpha$ for every $\alpha$, so every group of sections involved is zero and the sheaf axiom is trivial.

Suppose $P\in U$.  Choose an index $\alpha_0$ with
\[
P\in U_{\alpha_0}.
\]
A compatible family of sections has a component
\[
a_{\alpha_0}\in A.
\]
For every other $\alpha$ containing $P$, the overlap
\[
U_\alpha\cap U_{\alpha_0}
\]
contains $P$, so compatibility forces
\[
a_\alpha=a_{\alpha_0}.
\]
For indices not containing $P$, the only section is zero.  Hence the family glues uniquely to the element
\[
a_{\alpha_0}\in\mathcal S(U)=A.
\]
Thus $\mathcal S$ is a sheaf.
:::

<1>2. If
\[
Q\in\overline{\{P\}},
\]
then every open neighborhood of $Q$ contains $P$.
::: {.proof}
The condition
\[
Q\in\overline{\{P\}}
\]
means exactly that every open neighborhood of $Q$ meets the set $\{P\}$.  Meeting that singleton means containing $P$.
:::

<1>3. For every
\[
Q\in\overline{\{P\}},
\]
one has
\[
\boxed{\mathcal S_Q\cong A.}
\]
::: {.proof}
By <1>2, every neighborhood $U$ of $Q$ contains $P$, so
\[
\mathcal S(U)=A.
\]
Every restriction map between such neighborhoods is the identity on $A$.  Therefore the stalk, which is the direct limit over all neighborhoods of $Q$, is
\[
\mathcal S_Q
=\varinjlim_{Q\in U}A
\cong A.
\]
:::

<1>4. If
\[
Q\notin\overline{\{P\}},
\]
then
\[
\boxed{\mathcal S_Q=0.}
\]
::: {.proof}
Choose an open neighborhood
\[
Q\in V
\]
with
\[
P\notin V.
\]
Then
\[
\mathcal S(V)=0.
\]

Any germ in $\mathcal S_Q$ is represented by a section over some neighborhood $U$ of $Q$.  Restrict that representative to
\[
U\cap V,
\]
which is still a neighborhood of $Q$ but does not contain $P$.  The restriction lands in
\[
\mathcal S(U\cap V)=0,
\]
so the germ is zero.  Hence the entire stalk is zero.
:::

<1>5. Thus the stalks are
\[
\boxed{
(i_P(A))_Q
\cong
\begin{cases}
A,&Q\in\overline{\{P\}},\\
0,&Q\notin\overline{\{P\}}.
\end{cases}
}
\]
::: {.proof}
Combine <1>3 and <1>4.
:::

<1>6. Put
\[
Z=\overline{\{P\}}
\]
with its subspace topology.  Then $P$ belongs to every nonempty open subset of $Z$.
::: {.proof}
Let $W\subseteq Z$ be nonempty and open, and choose $Q\in W$.  Write
\[
W=V\cap Z
\]
for some open $V\subseteq X$ containing $Q$.  Since
\[
Q\in Z=\overline{\{P\}},
\]
step <1>2 says every neighborhood of $Q$ in $X$, in particular $V$, contains $P$.  Since $P\in Z$ as well,
\[
P\in V\cap Z=W.
\]
:::

<1>7. Let
\[
i:Z\hookrightarrow X
\]
be the inclusion and let $\underline A_Z$ be the constant sheaf with value $A$ on $Z$.  Then
\[
\boxed{i_*\underline A_Z\cong i_P(A).}
\]
::: {.proof}
For an open $U\subseteq X$,
\[
(i_*\underline A_Z)(U)
=\underline A_Z(U\cap Z).
\]

If $P\in U$, then
\[
U\cap Z
\]
is a nonempty open subset of $Z$.  By <1>6 it contains the generic point $P$, and $Z$ is irreducible because it is the closure of one point.  Hence the constant sheaf has
\[
\underline A_Z(U\cap Z)=A.
\]

If $P\notin U$, then
\[
U\cap Z=\varnothing.
\]
Indeed, if $Q\in U\cap Z$, then $Q\in\overline{\{P\}}$, so <1>2 would force the neighborhood $U$ of $Q$ to contain $P$, contradiction.  Hence
\[
\underline A_Z(U\cap Z)=0.
\]

Therefore
\[
(i_*\underline A_Z)(U)
=
\begin{cases}
A,&P\in U,\\
0,&P\notin U,
\end{cases}
\]
with exactly the same restriction maps as $i_P(A)$.  The two sheaves are canonically isomorphic.
:::

<1>8. Q.E.D.
::: {.proof}
Step <1>5 gives the stalk calculation, and <1>7 gives the pushforward description.
:::
:::
