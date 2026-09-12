---
schema: qual/card@1
id: P-BKS06-3A
kind: problem
title: UC Berkeley Spring 2006 prelim 3A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $S = \{ ( x _ { 1 } , \ldots , x _ { n } ) \in \mathbb { R } ^ { n } \mid x _ { 1 } + \cdot \cdot \cdot + x _ { n } = 0 \}$ . Find (with justification) the $n \times n$ matrix P of the orthogonal projection from $\mathbb { R } ^ { n }$ onto S. That is, P has image S, and $P ^ { 2 } = P = P ^ { T }$
:::

::: {.solution}
The orthogonal complement of S is one-dimensional, and spanned by the unit vector $\begin{array} { r } { w = \frac { 1 } { \sqrt { n } } ( 1 , \dots , 1 ) } \end{array}$ , because $v \in S \Leftrightarrow \langle v , w \rangle = 0$ . So the orthogonal projection is given by $\begin{array} { r } { P v = v \dot { - } \langle v , w \rangle w = v - \frac { v _ { 1 } + \dots + v _ { n } } { n } ( 1 , \dots , 1 ) } \end{array}$ . Therefore

$$
P = \operatorname { I d } - w ^ { T } w = \left( \begin{array} { c c c c } { \frac { n - 1 } { n } } & { \frac { - 1 } { n } } & { \cdot \cdot } & { \frac { - 1 } { n } } \\ { \frac { - 1 } { n } } & { \frac { n - 1 } { n } } & { \cdot \cdot } & { \frac { - 1 } { n } } \\ { \vdots } & { \cdot } & { \vdots } \\ { \frac { - 1 } { n } } & { \frac { - 1 } { n } } & { \cdot \cdot } & { \frac { n - 1 } { n } } \end{array} \right) .
$$
:::
