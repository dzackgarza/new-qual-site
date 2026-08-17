---
schema: qual/card@1
id: P-PKXBP
kind: problem
title: "Let $G$ be a finite group whose order is divisible by a prime\u2026"
classification:
  areas:
  - algebra
  topics:
  - sylow-theory
  - normal-subgroups
  - p-groups
relations: []
review: draft
solved: true
---
Let $G$ be a finite group whose order is divisible by a prime number $p$.
Let $P$ be a normal $p\dash$subgroup of $G$
(so $\abs P = p^c$ for some $c$).

a.
Show that $P$ is contained in every Sylow $p\dash$subgroup of $G$.

b.
Let $M$ be a maximal proper subgroup of $G$. Show that either $P \subseteq M$ or $|G/M | = p^b$ for some $b \leq c$.

:::{.concept}
\envlist

- Sylow 2: All Sylow $p\dash$subgroups are conjugate.
- $\abs{HK} = \abs{H} \abs{K} / \abs{H\intersect K}$.
- Lagrange's Theorem: $H\leq G \implies \abs{H} \divides \abs{G}$

:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Every $p\dash$subgroup is contained in some Sylow $p\dash$subgroup, so $P \subseteq S_p^i$ for some $S_p^i \in \mathrm{Syl}_p(G)$.

- $P \normal G \iff gPg\inv = P$ for all $g\in G$.

- Let $S_p^j$ be any other Sylow $p\dash$subgroup, 
- Since Sylow $p\dash$subgroups are all conjugate $gS_p^i g\inv = S_p^j$ for *some* $g\in G$.

- Then 
\[
P = gPg\inv \subseteq gS_p^i g\inv = S_p^j
.\]

:::

:::{.proof title="of b"}
\envlist

- If $P$ is not contained in $M$, then $M < MP$ is a proper subgroup
- By maximality of $M$, $MP = G$
- Note that $M\intersect P \leq P$ and $\abs{P} = p^c$ implies $\abs{M\intersect P} = p^a$ for some $a\leq c$ by Lagrange
- Then write
  \[
  G = MP
  &\iff \abs{G} = \frac{\abs{M} \abs{P}}{\abs{M\intersect P}} \\ \\
  &\iff { \abs{G} \over \abs{M}} = {\abs{P}  \over \abs{M\intersect P}} = {p^c \over p^a} = p^{c-a} \definedas p^b
  \]

  where $a\leq c \implies 0 \leq c-b \leq c$ so $0\leq b \leq c$.

:::

:::

