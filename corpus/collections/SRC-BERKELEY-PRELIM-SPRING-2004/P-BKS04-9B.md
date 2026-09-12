---
schema: qual/card@1
id: P-BKS04-9B
kind: problem
title: UC Berkeley Spring 2004 prelim 9B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $S_4$ be the group of permutations of $\{1,2,3,4\}$. Determine the order of $\operatorname{Aut}(S_4)$. Justify your answer.
:::

::: {.solution}
The center of $S_4$ is trivial, so conjugation embeds $S_4$ into $\operatorname{Aut}(S_4)$. It remains to show every automorphism is inner.

There are exactly four subgroups $H_i$ of order $3$, where $H_i$ consists of the identity and the two $3$-cycles fixing $i$. Any automorphism permutes these four subgroups. Inner automorphisms realize every permutation of them, so after composing with an inner automorphism we may assume an automorphism $\sigma$ fixes every $H_i$.

The transpositions form the unique conjugacy class of six elements of order $2$, so $\sigma$ preserves that class. A transposition $(ij)$ is characterized among transpositions by the property that it and $H_k$ generate $S_4$ exactly when $k\in\{i,j\}$. Since $\sigma$ fixes each $H_k$, it fixes every transposition. The transpositions generate $S_4$, hence $\sigma$ is the identity.

Therefore every automorphism of $S_4$ is inner, and
\[
|\operatorname{Aut}(S_4)|=|S_4|=24.
\]
:::
