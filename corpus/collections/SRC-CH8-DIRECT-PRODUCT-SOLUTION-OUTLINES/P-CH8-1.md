---
schema: qual/card@1
id: P-CH8-1
kind: problem
title: Chapter 8 exercise 1
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Prove that the external direct product of any finite number of groups is a group.
:::

::: {.solution}
Proof.
Let $G = G _ { 1 } \oplus G _ { 2 } \oplus \cdot \cdot \cdot \oplus G _ { n }$ , where each $G _ { i }$ is a group, and let the operation $*$ on G be defined component-wise (as in the definition of external direct product).
Since each operation in $G _ { i }$ is associative, $*$ is associative on G. [This is clear since $a * ( b * c ) = a * ( b _ { 1 } * c _ { 1 } , b _ { 2 } * c _ { 2 } , . . . b _ { n } * c _ { n } ) = ( a _ { 1 } * ( b _ { 1 } * c _ { 1 } ) , a _ { 2 } * ( b _ { 2 } * c _ { 2 } ) , . . . , a _ { n } * ( b _ { n } * c _ { n } ) ) = ( ( a _ { 1 } * b _ { 1 } ) * c _ { 1 } , ( a _ { 2 } * b _ { 2 } ) * c _ { 2 } , \ldots , ( a _ { n } * b _ { n } ) * c _ { n } ) = ( a _ { 1 } * b _ { 1 } , a _ { 2 } * b _ { 2 } , \ldots , a _ { n } * b _ { n } ) * c = ( a * b ) * c .$ Similarly, we can see that G is closed since $a * b = ( a _ { 1 } * b _ { 1 } , a _ { 2 } * b _ { 2 } , \ldots , a _ { n } * b _ { n } )$ and $a _ { i } b _ { i } \in G _ { i }$ by closure of $G _ { i }$ . The previous calculation also verifies that the identity in G is $e = ( e _ { 1 } , e _ { 2 } , \ldots , e _ { n } )$ where $e _ { i }$ is the identity in $G _ { i }$ and that the inverse of a is $a ^ { - 1 } = ( a _ { 1 } ^ { - 1 } , a _ { 2 } ^ { - 1 } , \dots , a _ { n } ^ { - 1 } )$ . Since each $G _ { i }$ is a group, both e and $a ^ { - 1 }$ are in G. □
:::
