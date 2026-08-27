---
schema: qual/card@1
id: E-AMD-3MQL7TPB
kind: exercise
title: $O_p(G)$ is the unique maximal normal $p$-subgroup of $G$
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
Let $O_p(G)$ be the intersection of all Sylow $p\dash$subgroups of $G$.
Show that $O_p(G) \normal G$, and that it is the unique maximal normal $p\dash$subgroup of $G$ (containing all other normal $p$-subgroups).
:::

::: {.solution}
Let $G$ be a finite group, and let $\operatorname{Syl}_p(G) = \{P_1, P_2, \ldots, P_k\}$ be the set of all Sylow $p$-subgroups of $G$.
Define:
$$
O_p(G) = \bigcap_{P \in \operatorname{Syl}_p(G)} P.
$$

**(1) Show $O_p(G) \normal G$:**
- For any $g \in G$ and any $P \in \operatorname{Syl}_p(G)$, the conjugate $g P g^{-1}$ is also a Sylow $p$-subgroup of $G$.
- By Sylow's Conjugacy Theorem, the conjugation action $P \mapsto g P g^{-1}$ is a permutation of the set $\operatorname{Syl}_p(G)$.
- Therefore:
  $$
  g O_p(G) g^{-1} = g \left( \bigcap_{P \in \operatorname{Syl}_p(G)} P \right) g^{-1} = \bigcap_{P \in \operatorname{Syl}_p(G)} g P g^{-1} = \bigcap_{Q \in \operatorname{Syl}_p(G)} Q = O_p(G).
  $$
Thus $O_p(G) \normal G$.

**(2) Show $O_p(G)$ is a $p$-group:**
Since $O_p(G) \subseteq P_1$ where $P_1$ is a $p$-group, by Lagrange's Theorem every element in $O_p(G)$ has order dividing $|P_1| = p^a$, so $O_p(G)$ is a $p$-subgroup of $G$.

**(3) Show $O_p(G)$ contains every normal $p$-subgroup of $G$:**
Let $N \normal G$ be any normal $p$-subgroup of $G$.
- Since $N$ is a $p$-subgroup, by the Second Sylow Theorem $N$ is contained in at least one Sylow $p$-subgroup $P_0 \in \operatorname{Syl}_p(G)$.
- Since $N \normal G$, for every $g \in G$, $N = g N g^{-1} \subseteq g P_0 g^{-1}$.
- By Sylow's Theorem, every Sylow $p$-subgroup of $G$ is of the form $g P_0 g^{-1}$ for some $g \in G$.
- Therefore, $N \subseteq P$ for **all** $P \in \operatorname{Syl}_p(G)$.
- Hence $N \subseteq \bigcap_{P \in \operatorname{Syl}_p(G)} P = O_p(G)$.

Thus $O_p(G)$ is normal in $G$, is a $p$-group, and contains all normal $p$-subgroups of $G$, making it the unique maximal normal $p$-subgroup of $G$ (the **$p$-core** of $G$).
:::
