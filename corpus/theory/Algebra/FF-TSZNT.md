---
schema: qual/card@1
id: FF-TSZNT
kind: fact
title: Groups of order 4
prompts:
- What are the groups of order 4?
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
  - p-Groups
relations: []
review: draft
---

::: {.fact}
Up to isomorphism, the groups of order $4$ are $\ZZ/4\ZZ$ and $(\ZZ/2\ZZ)^2$.
Both are abelian.
:::

::: {.proof}
Let $\abs G=4$.
If $G$ has an element of order $4$, then $G\cong\ZZ/4\ZZ$.
Otherwise every nonidentity element has order $2$, so $g^{-1}=g$ for all $g$, and $ab=(ab)^{-1}=b^{-1}a^{-1}=ba$ for all $a,b\in G$.
Then $G$ is an abelian group of exponent $2$, that is, written additively, a $2$-dimensional $\FF_2$-vector space, and $G\cong(\ZZ/2\ZZ)^2$.
:::

::: {.remark}
The cycle graphs of $\ZZ/4\ZZ = \gens{g}$ and of $(\ZZ/2\ZZ)^2 = \theset{e, a, b, ab}$, with identity $e$:

\begin{tikzcd}
	& {g^2} &&&& a \\
	g && {g^3} &&& e \\
	& e &&&& b && ab
	\arrow[no head, from=3-2, to=2-1]
	\arrow[no head, from=2-1, to=1-2]
	\arrow[no head, from=1-2, to=2-3]
	\arrow[no head, from=2-3, to=3-2]
	\arrow[no head, from=2-6, to=1-6]
	\arrow[no head, from=2-6, to=3-5]
	\arrow[no head, from=2-6, to=3-7]
\end{tikzcd}
:::
