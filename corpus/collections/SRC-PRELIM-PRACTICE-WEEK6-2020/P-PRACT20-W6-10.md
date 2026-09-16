---
schema: qual/card@1
id: P-PRACT20-W6-10
kind: problem
title: Functions not tending to $0$ at infinity despite integrability or vanishing along integer translates
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find continuous functions $f , g : [ 0 , \infty ) \to \mathbb { R }$ such that

(A) $\textstyle \int _ { 0 } ^ { \infty } f ( x ) d x$ converges but $f ( x ) \neq 0$ as $x \to \infty$ ,

(B) $\{ g ( t + n ) \} _ { n \in \mathbb { N } }$ converges to zero as $n \to \infty$ for any fixed $t \geq 0$ but $g ( x ) \not \to 0$ as $x \to \infty$ Bonus: show that neither of these is possible if we stipulate that $f , g$ are uniformly continuous.
:::

::: {.solution}
We can do these both with one example.

For $n \in \mathbb { N }$ , define the functions $f _ { n } : [ 0 , \infty ) \to \mathbb { R }$ by

$$
f _ { n } ( x ) = \left\{ \begin{array} { c c } { 2 n ^ { 2 } ( x - n ) , } & { n \leq x < n + \frac { 1 } { 2 n ^ { 2 } } , } \\ { } & { } \\ { 2 n ^ { 2 } \left( n + \frac { 1 } { n ^ { 2 } } - x \right) , } & { n + \frac { 1 } { 2 n ^ { 2 } } \leq x < n + \frac { 1 } { n ^ { 2 } } , } \\ { } & { } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.
$$

Then the graph of each $f _ { n }$ is a spike of height 1 on the interval $[ n , n + 1 / n ^ { 2 } )$ . Let $\textstyle f ( x ) = \sum _ { n = 1 } ^ { \infty } f _ { n } ( x )$ for $x \in [ 0 , \infty )$ , so that f has each one of these spikes [f is pictured in Figure 2 below]. Each spike has integral $\begin{array} { r } { \int _ { 0 } ^ { \infty } f _ { n } ( x ) d x = \frac { 1 } { 2 } \cdot \frac { 1 } { n ^ { 2 } } \cdot 1 = \frac { 1 } { 2 n ^ { 2 } } } \end{array}$ and so we see

$$
\int _ { 0 } ^ { \infty } f ( x ) d x = \sum _ { n = 1 } ^ { \infty } { \frac { 1 } { 2 n ^ { 2 } } } < \infty .
$$

Likewise if $t \ : = \ : 0 ,$ 1 then $t + n$ is an integer for any $n \in \mathbb N$ and so $f ( t + n ) = 0$ for all n so $\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } f ( t + n ) = 0 . \mathrm { I f ~ } t \in ( 0 , 1 ) } \end{array}$ , then there is some $N \in \mathbb { N }$ such that $t > 1 / N ^ { 2 }$ . But then $f ( t + n ) = 0$ for all $n \geq N$ and so $\textstyle \operatorname* { l i m } _ { n \to \infty } f ( t + n ) = 0$ . Hence $\{ f ( t + n ) \} _ { n \in \mathbb { N } }$ goes to zero for any $t \in [ 0 , 1 ]$

However, lim $_ { 1 x \to \infty } f ( x ) \neq 0$ because the sequence $\begin{array} { r } { x _ { n } = n + \frac { 1 } { 2 n ^ { 2 } } } \end{array}$ satisfies $x _ { n } \to \infty$ but $f ( x _ { n } ) = 1$ for all $n \in \mathbb { N }$ .
:::
