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
Show that the stalk $\iota_p(A)_q=A$ when $q\in\cl_X(\{p\})$ and $0$ otherwise, and that there is an equality of sheaves $\iota_p(A)=\iota_*(\underline A)$ where $\iota:\cl_X(\{p\})\injects X$ is the inclusion.
:::

::: {.solution}
Let $Z=\cl_X(\{p\})$.

<1>1. If $q\in Z$, then every open neighborhood of $q$ contains $p$.

::: {.proof}
By definition, $q\in\cl_X(\{p\})$ means every open neighborhood of $q$ meets $\{p\}$. Meeting the singleton $\{p\}$ is equivalent to containing $p$.
:::

<1>2. If $q\in Z$, then
$$
\boxed{(\iota_p(A))_q\cong A}.
$$

::: {.proof}
By step <1>1, every open neighborhood $U$ of $q$ contains $p$. Hence $\iota_p(A)(U)=A$ for every object in the directed system defining the stalk, and every restriction map is the identity on $A$. Therefore
$$
(\iota_p(A))_q
=\varinjlim_{q\in U}\iota_p(A)(U)
\cong A.
$$
:::

<1>3. If $q\notin Z$, then
$$
\boxed{(\iota_p(A))_q=0}.
$$

::: {.proof}
Since $q\notin\cl_X(\{p\})$, there is an open neighborhood $V$ of $q$ with $p\notin V$. The neighborhoods $U$ of $q$ contained in $V$ are cofinal among all neighborhoods of $q$, and $p\notin U$ for each of them. Thus $\iota_p(A)(U)=0$ on a cofinal subsystem, so the stalk is zero.
:::

<1>4. Every nonempty open subset of $Z$ contains $p$.

::: {.proof}
Let $W\subseteq Z$ be nonempty and open in the subspace topology. Write $W=O\cap Z$ for some open $O\subseteq X$, and choose $q\in W$. Since $q\in Z$, step <1>1 implies that the open neighborhood $O$ of $q$ contains $p$. Because $p\in Z$, it follows that $p\in O\cap Z=W$.
:::

<1>5. For every open subset $U\subseteq X$,
$$
(\iota_*\underline A)(U)
=
\begin{cases}
A,&p\in U,\\
0,&p\notin U.
\end{cases}
$$

::: {.proof}
By definition of direct image,
$$
(\iota_*\underline A)(U)=\underline A(U\cap Z).
$$
If $p\notin U$, then $U\cap Z$ must be empty: otherwise it would be a nonempty open subset of $Z$, and step <1>4 would force $p\in U\cap Z$. Hence the constant sheaf has the zero group of sections there.

If $p\in U$, then $U\cap Z$ is nonempty. By step <1>4, every nonempty open subset of $U\cap Z$ contains $p$, so $U\cap Z$ is connected. Sections of the constant sheaf $\underline A$ on a connected nonempty open set are constant, giving
$$
\underline A(U\cap Z)\cong A.
$$
The restriction maps under these identifications are the identity maps on $A$ whenever both source and target are nonempty.
:::

<1>6. The sheaves satisfy
$$
\boxed{\iota_p(A)\cong\iota_*(\underline A)}.
$$

::: {.proof}
Step <1>5 gives the same section group as the defining formula for $\iota_p(A)$ on every open $U\subseteq X$, with the same restriction maps. These identifications therefore assemble to an isomorphism of sheaves.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 compute every stalk, and step <1>6 gives the pushforward description.
:::
:::
