---
schema: qual/card@1
id: P-BKS06-5B
kind: problem
title: UC Berkeley Spring 2006 prelim 5B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Prove that there exists no continuous bijection from (0, 1) to [0, 1]. (Recall that a bijection is a map that is both one-to-one and onto.)
:::

::: {.solution}
Suppose on the contrary that there exists a continuous bijection $f \colon ( 0 , 1 )$ $[ 0 , 1 ]$ . Then there exists $x \in ( 0 , 1 )$ such that $f ( x ) = 0$ . Let $A = ( 0 , x ) , B = ( x , 1 )$ . We have ${ \overset { \cdot } { A } } \cap B = \emptyset$ and since f is injective we have

$$
f ( A ) \cap f ( B ) = f ( A \cap B ) = \emptyset .\tag{∗}
$$

Since f is continuous and $( 0 , x ]$ is connected, $f ( \left( 0 , x \right] )$ contains an interval $[ 0 , a )$ for some $a > 0$ . Hence $f ( A )$ contains $( 0 , a )$ . Similarly, $f ( B )$ contains (0, b) for some $b > 0$ . This gives $f ( A ) \cap f ( B ) \neq \emptyset$ . Contradiction to (∗).
:::
