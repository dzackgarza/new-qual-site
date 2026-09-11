---
schema: qual/card@1
id: P-BKS04-8A
kind: problem
title: UC Berkeley Spring 2004 prelim 8A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let V and W be finite-dimensional vector spaces over a field k. Let $f \colon V ^ { n } \to W$ be a function such that

(a) For each fixed $i \in \{ 1 , \ldots , n \}$ and fixed $v _ { 1 } , \dots , v _ { i - 1 } , v _ { i + 1 } , \dots , v _ { n } \in V$ , the map

$$
\begin{array} { l } { V \to W } \\ { x \mapsto f ( v _ { 1 } , \dots , v _ { i - 1 } , x , v _ { i + 1 } , \dots , v _ { n } ) } \end{array}
$$

is a k-linear transformation; and

(b) $f ( v _ { 1 } , \ldots , v _ { n } ) = 0$ whenever $v _ { i } = v _ { i + 1 }$ for some $i \in \{ 1 , \ldots , n - 1 \}$

Prove that either dim $V \geq n$ or f is identically zero.
:::

::: {.solution}
Fix $i ,$ and $v _ { 1 } , \dots , v _ { i - 1 } , v _ { i + 2 } , \dots , v _ { n } \in V$ , and define $g ( x , y ) = f ( v _ { 1 } , \dots , v _ { i - 1 } , x , y , v _ { i + 2 } , \dots , v _ { n } )$ Then

$$
\begin{array} { l } { 0 = g ( x + y , x + y ) } \\ { \ } \\ { \displaystyle = g ( x + y , x ) + g ( x + y , y ) } \\ { \ } \\ { \displaystyle = g ( x , x ) + g ( y , x ) + g ( x , y ) + g ( y , y ) } \\ { \ } \\ { \displaystyle = g ( y , x ) + g ( x , y ) } \end{array}
$$

so interchanging adjacent arguments changes the sign of the value of $f .$ .

Suppose $v _ { 1 } , \ldots , v _ { n } \in V$ are such that $v _ { i } = v _ { j }$ for some $i < j$ Then we can interchange arguments repeatedly to move $v _ { j }$ to the $i + 1$ position, possibly changing the sign of the value of $f ( v _ { 1 } , \ldots , v _ { n } )$ as we go along. Since at the end the result is zero, we must have had $f ( v _ { 1 } , \ldots , v _ { n } ) = 0$ originally. Thus $f ( v _ { 1 } , \ldots , v _ { n } ) = 0$ whenever $v _ { i } = v _ { j }$ for some $i \neq j$

We now solve the problem. If the conclusion fails, we have dim $V < n$ and there exist $v _ { 1 } , \ldots , v _ { n } \in V$ with $f ( v _ { 1 } , \ldots , v _ { n } ) \neq 0$ Since dim $V \ < \ n$ , the vectors $v _ { 1 } , \ldots , v _ { n }$ must be linearly dependent. Thus for some i, we can write $\begin{array} { r } { v _ { i } = \sum _ { j \neq i } c _ { j } v _ { j } } \end{array}$ for some constants $c _ { j } \in k$ for $j \neq i$ . By linearity of $f$ in the i-th argument,

$$
\begin{array} { l } { f ( v _ { 1 } , \dots , v _ { n } ) = \displaystyle \sum _ { j \neq i } c _ { j } f ( v _ { 1 } , \dots , v _ { i - 1 } , v _ { j } , v _ { i + 1 } , \dots , v _ { n } ) } \\ { = \displaystyle \sum _ { j \neq i } c _ { j } \cdot 0 } \end{array}
$$

by the previous paragraph, since in each term some $v _ { j }$ appears twice as an argument. Thus $f ( v _ { 1 } , \ldots , v _ { n } ) = 0$ , a contradiction.
:::
