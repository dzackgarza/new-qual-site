---
schema: qual/card@1
id: D-MER2X
kind: definition
title: Inner automorphism group
prompts:
- What is an inner automorphism, and what is the inner automorphism group?
classification:
  areas: [algebra]
  topics: [Automorphisms, Conjugation, Subgroups]
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group with automorphism group $\Aut(G)$.
For $g\in G$ the \dfn{inner automorphism} $c_g$ is conjugation by $g$,
$$
\begin{aligned}
c_g\colon G&\longrightarrow G,\\
x&\longmapsto gx\inverseof{g},
\end{aligned}
$$
and the \dfn{inner automorphism group} is
$$
\Inn(G)\coloneqq\theset{c_g \st g\in G},
$$
the image of $g\mapsto c_g$, which is a subgroup of $\Aut(G)$.
:::

::: {.remark}
An automorphism of $G$ is inner exactly when it is conjugation by an element, so $\Inn(G)$ is trivial exactly when $G$ is abelian; the quotient is the [[D-XIKE1|outer automorphism group]].
:::
