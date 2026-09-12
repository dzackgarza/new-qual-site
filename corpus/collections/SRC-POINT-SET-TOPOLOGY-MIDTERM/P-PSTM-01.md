---
schema: qual/card@1
id: P-PSTM-01
kind: problem
title: Continuity descended through a closed quotient map
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f \colon X \to Y$ be a continuous surjection, and suppose f is a closed map.
Let $g \colon Y \to Z$ be a function so that $g \circ f \colon X \to Z$ is continuous.
Show that g is continuous.
:::

::: {.solution}
It is enough to show: For every closed subset $F \subset Z$ , the subset $g ^ { - 1 } ( F ) \subset$ Y is closed.

Now, by continuity of $g \circ f$ , we know that $( g \circ f ) ^ { - 1 } ( F ) = f ^ { - 1 } ( g ^ { - 1 } ( F ) )$ is a closed subset of X. Since f is a closed map, it takes this closed subset of X to a closed subset of Y . But

$$
f ( ( g \circ f ) ^ { - 1 } ( F ) ) = f ( f ^ { - 1 } ( g ^ { - 1 } ( F ) ) ) = g ^ { - 1 } ( F ) ,
$$

since f is surjective.
Hence, $g ^ { - 1 } ( F )$ is closed.
:::
