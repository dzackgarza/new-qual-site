---
schema: qual/card@1
id: P-ALGFINAL11-01
kind: problem
title: Classify groups of order 105
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let G be a group of order 105.

(a) Show that G has a normal subgroup of order 5 or 7. [points]:[4]

(b) Show that G has a cyclic normal subgroup of order 35. [4]

(c) Show that the Sylow 5- and 7-subgroups of G are both normal.
[3]

(d) Classify groups of order 105.
:::

::: {.solution}
(a) If a Sylow $5$-subgroup $F$ is not normal, then it has $1 + 5k$ conjugates where $k \geq 1$ and $1 + 5k$ divides $105/5 = 21$, whence $1 + 5k = 21$ and there are $21 \cdot 4 = 84$ elements of order $5$. Similarly if a Sylow $7$-subgroup $S$ is not normal, then there are $15 \cdot 6 = 90$ elements of order $7$. Since $84 + 90 > 105$, at least one of $F$ and $S$ must be normal.

(b) Since at least one of $F$ and $S$ is normal, and $\abs{F \cap S} = 1$ by Lagrange's theorem, $FS < G$ is a subgroup of order $35$. Since $5$ does not divide $7 - 1$, every group of order $35$ is cyclic.

(c) The cyclic group $FS$ has unique subgroups of orders $5$ and $7$, so it has $31$ elements of order $\neq 5$ and $29$ elements of order $\neq 7$. Since $\abs{G} = 105$, $G$ cannot have $84$ elements of order $5$ or $90$ of order $7$; so by the proof of (a), both $F$ and $S$ are normal.

(d) As in (b), if $T$ is a Sylow $3$-subgroup, then, since $S \triangleleft G$, $TS < G$ is a subgroup of order $21$, a complement of $F \triangleleft G$. Since $\abs{\Aut(F)} = 4$ is prime to $21$, any homomorphism $TS \to \Aut(F)$ is trivial; consequently $G$ is the direct product $TS \times F$. There are, up to isomorphism, just two groups of order $21$, and one of order $5$; correspondingly, there are just two possibilities for $G$.
:::
