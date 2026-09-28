---
schema: qual/card@1
id: P-BKS04-2A
kind: problem
title: A countable abelian group with $2^{\aleph_0}$ endomorphisms
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
Find a countable abelian group whose endomorphism ring has the same cardinality as the set of real numbers.
Justify your answer.
:::

::: {.solution}
Let $G$ be a vector space of dimension $\aleph_0$ over $\FF_2$. Then $G$ is countable, since it is a countable union of finite subspaces.
Let $v_1,v_2,\ldots$ be a basis.
For each $S\subseteq\{1,2,3,\ldots\}$ there is an endomorphism of $G$ mapping each $v_i$ to $v_i$ or $0$ according to whether $i\in S$. Different subsets $S$ give different endomorphisms, so $\#\operatorname{End}G\geq2^{\aleph_0}$. On the other hand,

$$
\#\operatorname{End}G\leq(\#G)^{\#G}=\aleph_0^{\aleph_0}\leq(2^{\aleph_0})^{\aleph_0}=2^{\aleph_0\aleph_0}=2^{\aleph_0}.
$$

Thus $\#\operatorname{End}G=2^{\aleph_0}=\#\RR$.
:::
