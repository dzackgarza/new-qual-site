---
schema: qual/card@1
id: P-AGXHWSKYSCRAPER
kind: problem
title: Stalks of the skyscraper sheaf and its description as a pushforward
classification:
  areas:
  - algebraic-geometry
  topics:
  - Skyscraper Sheaves
  - Pushforward
  - Stalks
relations: []
review: draft
---

::: {.problem}
Let $X\in \Top$, $A\in \mathsf{Ab}\mathsf{Grp}$, $p\in X$, and define the skyscraper sheaf by
$$
\iota_p(A)(U) \coloneqq
\begin{cases}
A & p\in U  \\
0 & \text{else}.
\end{cases}
$$
Show that the stalk $\iota_p(A)_q = A$ when $q\in \cl_X(\theset{p})$ and $0$ otherwise, and that there is an equality of sheaves $\iota_p(A) = \iota_*(\underline{A})$ where $\iota: \cl_X(\theset{p}) \injects X$ is the inclusion.
:::

::: {.solution}
Write $Z \coloneqq \cl_X(\theset{p})$ with the subspace topology.
The restriction maps of $\iota_p(A)$ are the identity of $A$ between opens that contain $p$, and zero otherwise.

::: pf

::: pf-step
The stalk $\iota_p(A)_q$ is $A$ if $q \in Z$ and $0$ otherwise.

::: pf-proof
The stalk is $\iota_p(A)_q = \colim_{U \ni q} \iota_p(A)(U)$.
If $q \in Z$, every open $U \ni q$ contains $p$.
So every term of the colimit is $A$, with identity transition maps, and the colimit is $A$.
If $q \notin Z$, some open $U \ni q$ omits $p$, so $\iota_p(A)(U) = 0$.
The opens inside $U$ are cofinal, so the colimit is $0$.
:::

:::

::: {.pf-step #constant-on-z}
For an open $V \subseteq Z$, $\underline{A}(V) = A$ if $V \neq \emptyset$ and $\underline{A}(V) = 0$ if $V = \emptyset$, with identity restriction maps between nonempty opens.

::: pf-proof
Every nonempty open $V \subseteq Z$ contains $p$, because $p$ is dense in $Z$.
So $p$ is dense in $V$, and $V$ is irreducible and hence connected.
The sections $\underline{A}(V)$ are the locally constant functions $V \to A$, which on a connected $V$ are the constant functions.
:::

:::

::: pf-step
$\iota_p(A) = \iota_* \underline{A}$.

::: pf-proof
An open $U \subseteq X$ meets $Z$ if and only if $p \in U$, because $p$ is dense in $Z$.
So by step [](#constant-on-z){.pf-ref},
$$
\iota_* \underline{A}(U) = \underline{A}(U \cap Z) =
\begin{cases}
A & p \in U \\
0 & p \notin U,
\end{cases}
$$
with identity restriction maps between opens that contain $p$.
The two sheaves have the same groups and the same restriction maps on every open set, so they are equal.
:::

:::

:::
:::
