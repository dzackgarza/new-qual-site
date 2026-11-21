---
schema: qual/card@1
id: T-Y6RSP
kind: theorem
title: Cayley's theorem
slogan: 'Every group is a group of permutations of its own underlying set.'
prompts:
- What is Cayley's theorem?
classification:
  areas: [algebra]
  topics: [Groups, Permutations, Group Actions]
relations: []
review: draft
---

::: {.theorem}
Every group $G$ is isomorphic to a subgroup of the group of permutations of the set $G$; in particular a group of order $n$ embeds in $S_n$ [@Hun74, chapter I, §4, Corollary 4.6].
:::

::: {.proof}
For $g\in G$ left multiplication $\lambda_g\colon x\mapsto gx$ is a bijection of $G$ with inverse $\lambda_{\inverseof{g}}$, and $\lambda_{gh}=\lambda_g\circ\lambda_h$, so $g\mapsto\lambda_g$ is a homomorphism $G\to\Sym(G)$.
It is injective, since $\lambda_g(e)=g$ recovers $g$ from $\lambda_g$, so $G$ is isomorphic to the subgroup $\theset{\lambda_g \st g\in G}$ of $\Sym(G)$.
:::
