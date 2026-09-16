---
schema: qual/card@1
id: PR-CZS5F
kind: proposition
title: Finite unions of nowhere dense sets are nowhere dense
classification:
  areas:
  - real-analysis
  topics:
  - Density
relations: []
review: draft
---

::: {.proposition}
Let $X$ be a topological space and let $S_1,\ldots,S_k\subseteq X$ be [[D-2MJRE|nowhere dense]].
Then $S_1\cup\cdots\cup S_k$ is nowhere dense.
:::

::: {.proof}
By induction it suffices to treat $k=2$.
Since $\overline{S_1\cup S_2}=\overline{S_1}\cup\overline{S_2}$, it suffices to show that a union of two closed sets $F_1,F_2$ with empty interior has empty interior.
Let $U\subseteq F_1\cup F_2$ be open.
Then $U\setminus F_1$ is open and contained in $F_2$, so $U\setminus F_1=\emptyset$ and $U\subseteq F_1$; hence $U=\emptyset$.
:::

::: {.example}
The statement fails for countable unions: $\QQ=\bigcup_{q\in\QQ}\theset{q}$ is a countable union of nowhere dense subsets of $\RR$, but $\QQ$ is [[D-KJBAK|dense]] in $\RR$.
:::
