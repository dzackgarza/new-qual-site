---
schema: qual/card@1
id: P-JHUMAY10ANF
kind: problem
title: "if are fixed then there is a constant A such that $$ \| f * \varphi \| _ { L ^ {"
classification:
  areas:
  - real-analysis
  topics:
  - real-analysis-topics
solved: false
relations: []
review: draft
---

6. Let $\varphi : \mathbb { R }  \mathbb { R }$ be a continuous function with compact support.

a) Prove that if $1 \leq p \leq q \leq \infty$ are fixed then there is a constant A such that

$$
\| f * \varphi \| _ { L ^ { q } } \leq A \| f \| _ { L ^ { p } } , \quad { \mathrm { f o r ~ a l l } } \quad f \in L ^ { p } .
$$

If you use Young’s (convolution) inequality, you should prove it.

b) Show by example that such a general inequality cannot hold for $p > q$

## 7. Suppose that

$$
f : [ 0 , 1 ] \times [ 0 , 1 ] \to \mathbb { R }
$$

is continuous and has the property that for each x the map $t \to f ( x , t )$ is differentiable and that $\begin{array} { r } { \left| \frac { \partial f } { \partial t } ( x , t ) \right| \le g ( x ) } \end{array}$ for some measurable function statisfying $\textstyle \int _ { 0 } ^ { 1 } g ( x ) d x < \infty$ Carefully prove that $\textstyle F ( t ) = \int _ { 0 } ^ { 1 } f ( x , t )$ dx satisfies

$$
F ^ { \prime } ( t ) = \int _ { 0 } ^ { 1 } { \frac { \partial f } { \partial t } } ( x , t ) d x .
$$

## 8. Let E be a measurable subset of the line.

a) Let $\chi _ { E } : \mathbb { R } \to \mathbb { R }$ be the characteristic function of $E ~ ( \mathrm { i . e . } ~ \chi _ { E } ( x ) = 1$ when $x \in E$ and $\chi _ { E } ( x ) = 0$ when $x \notin E )$ . If E has finite Lebesgue measure, show that the function $f : \mathbb { R } \to \mathbb { R }$ defined by

$$
f ( x ) = \int _ { \mathbb { R } } \chi _ { E } ( y ) \chi _ { E } ( y - x ) d y
$$

is continuous.

b) Suppose instead that E has positive Lebesgue measure $0 < | E | \le \infty$ . Using a), show that the set $E - E = \{ x - y : x , y \in E \}$ contains an open interval $( - \varepsilon , \varepsilon )$ for some $\varepsilon > 0$
