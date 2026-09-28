---
schema: qual/card@1
id: P-AGXHWSUPPORT
kind: problem
title: The support of a section is closed, while the support of a sheaf need not be
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Support
  - Skyscraper Sheaves
relations: []
review: draft
---

::: {.problem}
Let $\mcf\in \Sh(X)$ and $s\in \mcf(U)$ be a section, and define
\[
\supp s &\da \ts{p\in U \st s_p \neq 0} \subseteq U \\
\supp \mcf &\da \ts{p\in X \st \mcf_p\neq 0} \subseteq  X
,\]
where $s_p$ denotes the germ of $s$ in the stalk $\mcf_p$.
Show that $\supp s$ is closed in $U$ but $\supp \mcf$ need not be closed in $X$.
:::

::: {.solution}
**$\supp(s)$ is closed.**

- By definition,
\[
\supp(s) &\da \ts{p\in U \st \mcf\mid^U_p(s) \neq 0} \subseteq U \\
\implies \supp(s)^c \da U\sm \supp(s) &\da \ts{p\in U \st \mcf\mid^U_p(s) = 0} \subseteq U
.\]

- If $p\in U$ and $s=0$ in the stalk at $p$, then $s=0$ on an open neighborhood $W_p$ of $p$ with $W_p \subseteq U\sm \supp(s)$, so every such $p$ is interior. Hence $U\sm\supp(s)$ is open in $U$.

**$\supp(\mcf)$ need not be closed.**

- Fix $q\in X$ and an abelian group $A\neq 0$. The skyscraper sheaf $q_*\ul{A}$ is the pushforward of the constant sheaf on the point $q$ along the inclusion $q\injects X$:

\begin{tikzcd}
	{\ul{A}} & {q_* \ul{A}} \\
	q & X
	\arrow["{q_*}", from=1-1, to=1-2]
	\arrow["q", hook, from=2-1, to=2-2]
\end{tikzcd}


- Its sections and stalks are
\[
q_* \underline{A}(U) =
\begin{cases}
A & q\in U  \\
0 & \text{else},
\end{cases}
\qquad (q_* \underline{A})_p =
\begin{cases}
A & p=q  \\
0 & \text{else}.
\end{cases}
\]

- Exchange the roles of $A$ and $0$:
\[
\mcf \da \left( U \mapsto
\begin{cases}
A & q\not\in U  \\
0 & q\in U
\end{cases}
\right)^{\scriptscriptstyle \mathrm{sh}}
.\]

- The presheaf and its sheafification $\mcf$ have the same stalks, and a computation shows
\[
\mcf_p =
\begin{cases}
A & p\neq q \\
0 & p=q.
\end{cases}
\]

- Then for a fixed $q\in X$, $\supp \mcf = X \sm \cl_X(\ts{q})$.
  - If there is some neighborhood $U\ni p$ that does not contain $q$, then the presheaf takes value $A$ on every $V \subseteq U$, so the colimit stabilizes and equals $A$.
  - If every neighborhood of $p$ contains $q$, then the presheaf takes value $0$ on every neighborhood of $p$, so the colimit is zero.

- For example, take $X \da \AA^1\slice{k}$ and $q=0$; then $\ts{0} = V(x)$ for $x\in k[x]$ is closed, so $\cl_X(\ts{0}) = \ts{0}$.

- Thus
\[
\supp \mcf = \AA^1 \sm \cl_X(\ts{0}) = \AA^1\smz = D(x)
\]
is open and not closed when $k$ is infinite.
:::
