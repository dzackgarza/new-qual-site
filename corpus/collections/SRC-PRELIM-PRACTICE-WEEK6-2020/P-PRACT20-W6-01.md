---
schema: qual/card@1
id: P-PRACT20-W6-01
kind: problem
title: "Week 6: Miscellaneous Topics, problem 1"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Where is the function $f ( x ) = { \left\{ \begin{array} { l l } { x / 2 , } & { x \in \mathbb { Q } } \\ { x / 3 , } & { x \in \mathbb { R } \setminus \mathbb { Q } } \end{array} \right\} }$ continuous?
:::

::: {.solution}
The given function is continuous only at $x \ = \ 0$ Indeed, if $x \neq 0$ , then take two sequences $\{ q _ { n } \} \subset \mathbb { Q }$ and $\{ r _ { n } \} \subset \mathbb { R } \setminus \mathbb { Q }$ approaching x (we can find each sequence since both $\mathbb { Q }$ and R \ Q are dense in R) and we will find that

$$
{ \frac { x } { 2 } } = \operatorname* { l i m } _ { n \to \infty } f ( q _ { n } ) \neq \operatorname* { l i m } _ { n \to \infty } f ( r _ { n } ) = { \frac { x } { 3 } } ,
$$

which shows that f is discontinuous by the sequential criterion theorem.
Now at $x = 0$ , we can take any $\varepsilon > 0$ and set $\delta = \varepsilon / 3$ to find that $| f ( x ) - f ( 0 ) | < \varepsilon$ when $| x - 0 | < \delta$ , which shows that $f$ is continuous at $x = 0$

More generally, if $D \subset \mathbb { R }$ is such that D and $\mathbb { R } \backslash D$ are both dense in R (which is true when $D = \mathbb { Q } )$ and we define

$$
f ( x ) = { \left\{ \begin{array} { l l } { g ( x ) , } & { x \in D } \\ { h ( x ) , } & { x \in \mathbb { R } \setminus D } \end{array} \right\} }
$$

where $g , h : \mathbb { R }  \mathbb { R }$ are continuous, then f will be continuous at $x \in \mathbb { R } { \mathrm { ~ i f f ~ } } g ( x ) = h ( x )$
:::
