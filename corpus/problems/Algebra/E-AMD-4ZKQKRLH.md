---
schema: qual/card@1
id: E-AMD-4ZKQKRLH
kind: problem
title: A normal $p$-subgroup is contained in every Sylow $p$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that any normal $p\dash$subgroup of a finite group $G$ is contained in every Sylow $p\dash$subgroup of $G$.
:::

::: {.solution}
Let $G$ be a finite group, and let $N \normal G$ be a normal $p$-subgroup (so $|N| = p^k$ for some $k \geq 0$).
Let $S$ be an arbitrary Sylow $p$-subgroup of $G$.

**Method 1 (via Subgroup Product):**
1. Since $N \normal G$ and $S \leq G$, the product set $N S = \{ns \mid n \in N, s \in S\}$ is a subgroup of $G$.
2. The order of the product subgroup is given by:
   $$
   |N S| = \frac{|N| \cdot |S|}{|N \cap S|}.
   $$
   Since $|N|$ is a power of $p$ and $|S| = p^a$ is a power of $p$, $|N S|$ is a power of $p$.
3. Thus $N S$ is a $p$-subgroup of $G$ containing $S$.
4. By definition, a Sylow $p$-subgroup is a maximal $p$-subgroup of $G$.
   Since $S \subseteq N S$ and $N S$ is a $p$-subgroup, maximality of $S$ implies:
   $$
   N S = S.
   $$
5. Because $N \subseteq N S = S$, we conclude:
   $$
   N \subseteq S.
   $$

Since $S$ was an arbitrary Sylow $p$-subgroup of $G$, $N$ is contained in every Sylow $p$-subgroup of $G$.

*(Equivalently, $N \subseteq \bigcap_{P \in \operatorname{Syl}_p(G)} P = O_p(G)$, the $p$-core of $G$.)*
:::
