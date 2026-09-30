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
\[
\iota_p(A)(U) \definedas
\begin{cases}
A & p\in U  \\
0 & \text{else}.
\end{cases}
\]
Show that the stalk $\iota_p(A)_q = A$ when $q\in \cl_X(\theset{p})$ and $0$ otherwise, and that there is an equality of sheaves $\iota_p(A) = \iota_*(\underline{A})$ where $\iota: \cl_X(\theset{p}) \injects X$ is the inclusion.
:::

::: {.solution}
**Stalks.** The stalk is $\iota_p(A)_q = \colim_{U\ni q}\iota_p(A)(U)$.
If $q\in\cl_X(\theset{p})$, every open $U\ni q$ contains $p$, so every term of the colimit is $A$ with identity restriction maps, and $\iota_p(A)_q = A$.
If $q\notin\cl_X(\theset{p})$, some open $U\ni q$ omits $p$; then $\iota_p(A)(U)=0$, and $\iota_p(A)_q = 0$.

**Equality with the pushforward.** The sheaf $\iota_p A \definedas (U\mapsto A \chi_{p\in U})$ is equal to $\iota_* \underline{A}$:

- Let $Z\definedas\cl_X(\theset{p})$ with the subspace topology. An open $U\subseteq X$ meets $Z$ if and only if $p\in U$. Every nonempty open subset $V$ of $Z$ contains $p$, which is dense in $Z$, so $V$ is irreducible and hence connected. The constant sheaf $\underline{A}(V)\definedas\Top(V,A)$ of locally constant functions is therefore
\[
\underline{A}(V) =
\begin{cases}
A & V \neq \emptyset \\
0 & V = \emptyset,
\end{cases}
\]
with identity restriction maps between nonempty opens.

- Hence
\[
\iota_* \underline{A}(U) \definedas \underline{A} (U\cap Z)
=
\begin{cases}
A & p\in U \\
0 & p\notin U.
\end{cases}
\]

- The two sheaves have the same groups on every open set and the same restriction maps, so they are equal.
:::
