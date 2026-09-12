---
schema: qual/card@1
id: P-BKS03-4B
kind: problem
title: A nonabelian simple group embeds normally in its automorphism group
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Suppose $G$ is a nonabelian simple group and $A=\operatorname{Aut}(G)$. Show that $A$ contains a normal subgroup isomorphic to $G$.
:::

::: {.solution}
For $g$ in $G ,$ let $c _ { g } : G \to G$ be the inner automorphism $c _ { g } ( h ) = g h g ^ { - 1 }$ Then it is easy to check that $g \mapsto c _ { g }$ defines a homomorphism $G  A$ . It is nontrivial since $G$ is nonabelian, and thus an injection since G is simple. Let B be the image, so $B \simeq G$ . If $\alpha \in A$ and $g , h \in G$ , then

$$
\alpha ( c _ { g } ( h ) ) = \alpha ( g h g ^ { - 1 } ) = \alpha ( g ) \alpha ( h ) \alpha ( g ) ^ { - 1 } = c _ { \alpha ( g ) } ( \alpha ( h ) ) ,
$$

so α $\circ c _ { g } = c _ { \alpha ( g ) }$ ◦ α in A. Thus $\alpha \circ c _ { g } \circ \alpha ^ { - 1 } = c _ { \alpha ( g ) }$ , so $B$ is normal in $G .$
:::
