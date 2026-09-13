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

::: problem
Let $X\in \Top$, $A\in \mathsf{Ab}\mathsf{Grp}$, $p\in X$, and define the skyscraper sheaf by
\[
\iota_p(A)(U) \da
\begin{cases}
A & p\in U  \\
0 & \text{else}.
\end{cases}
\]
Show that the stalk $\iota_p(A)_q = A$ when $q\in \cl_X(\ts{p})$ and $0$ otherwise, and that there is an equality of sheaves $\iota_p(A) = \iota_*(\underline{A})$ where $\iota: \cl_X(\ts{p}) \injects X$ is the inclusion.
:::

::: solution
Computation of stalks: see the preceding problem.

That $\iota_p A \da (U\mapsto A \chi_{p\in U})$ is *equal* to the pushforward sheaf $\iota_* \underline{A}$:

- Note that $\underline{A}$ on $\ts{p}$ is given by
\[
\underline{A}(U) \da \Top(U, A) =
\begin{cases}
A & U = \ts{p} \\
0 & U = \emptyset.
\end{cases}
\]

- Now check
\[
\iota_* \underline{A}(U) \da \underline{A} (\iota^{-1}(U))
&=
\begin{cases}
A & \iota^{-1}(U) = p  \\
0 & \iota^{-1}(U) = \emptyset
\end{cases}
\\
&=
\begin{cases}
A & U \ni \iota(p) = p \\
0 & U\not\ni \iota(p) = p.
\end{cases}
\]

- Now take the identity maps as the components of a morphism $\iota_p A\to \iota_* \underline{A}$, which induces the identity on stalks, making these sheaves equal.
:::
