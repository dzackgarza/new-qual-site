---
schema: qual/card@1
id: P-BKS04-6B
kind: problem
title: UC Berkeley Spring 2004 prelim 6B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $( u _ { n } ( x , y ) ) _ { n \geq 1 }$ be a sequence of functions that are defined and harmonic for $( x , y )$ in an open neighborhood of the upper half plane $\mathbb { R } \times \mathbb { R } _ { \geq 0 }$ . Suppose that $\begin{array} { r } { \frac { \partial u _ { n } } { \partial y } ( x , 0 ) = \dot { 0 } } \end{array}$ for all $x \in \mathbb { R }$ , and $u _ { n } ( x , 0 )$ converges to 0 as $n \to \infty$ uniformly for $x \in \mathbb { R }$ . Must $u _ { n } ( x , y )  0$ as $n \to \infty$ for every $( x , y ) \in \mathbb { R } \times \mathbb { R } _ { > 0 } ?$
:::

::: {.solution}
No. Let $u _ { n } = \cosh ( n y ) \cos ( n x ) / n$ Since $u _ { n }$ is the real part of the holomorphic function $\cos ( n z ) / n$ , it is harmonic on the entire plane.
Then $\begin{array} { r } { \frac { \partial u _ { n } } { \partial y } ( x , 0 ) = - \sinh ( 0 ) \cos ( n x ) = } \end{array}$ 0, and $u _ { n } ( x , 0 ) = \cos ( n x ) / n \to 0 { \mathrm { ~ a s ~ } } n \to \infty$ uniformly for $x \in R$ . But $u _ { n } ( 0 , 1 ) = \cosh ( n ) / n$ does not tend to 0 as $n \to \infty$
:::
