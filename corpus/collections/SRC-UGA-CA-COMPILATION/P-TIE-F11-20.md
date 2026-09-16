---
schema: qual/card@1
id: P-TIE-F11-20
kind: problem
title: Uniform continuity of $z^2$ and ill-posedness of the Cauchy problem for Laplace's equation
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 20.
---

::: {.problem}
Show that $f ( z ) = z ^ { 2 }$ is uniformly continuous in any open disk $| z | < R$ , where $R > 0$ is fixed, but it is not uniformly continuous on C.

(1) Show that the function $u = u ( x , y )$ given by

$$
u ( x , y ) = { \frac { e ^ { n y } - e ^ { - n y } } { 2 n ^ { 2 } } } \sin n x \quad { \mathrm { f o r ~ } } n \in \mathbf { N }
$$

is the solution on $D = \{ ( x , y ) ~ | x ^ { 2 } + y ^ { 2 } < 1 \}$ of the Cauchy problem for the Laplace equation

$$
\frac { \partial ^ { 2 } u } { \partial x ^ { 2 } } + \frac { \partial ^ { 2 } u } { \partial y ^ { 2 } } = 0 , \quad u ( x , 0 ) = 0 , \quad \frac { \partial u } { \partial y } ( x , 0 ) = \frac { \sin n x } { n } .
$$

(2) Show that there exist points $( x , y ) \in D$ such that $\operatorname* { l i m } _ { n \longrightarrow \infty } | u ( x , y ) | = \infty$
:::
