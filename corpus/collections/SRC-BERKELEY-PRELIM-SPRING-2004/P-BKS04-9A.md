---
schema: qual/card@1
id: P-BKS04-9A
kind: problem
title: UC Berkeley Spring 2004 prelim 9A
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
Let $f \colon  { \mathbb { R } } ^ { n } \to  { \mathbb { R } } ^ { n }$ be a differentiable function, and let L be a nonnegative real number. Prove that the following are equivalent:

(i) For every $x , y \in \mathbb { R } ^ { n }$

$$
( f ( x ) - f ( y ) ) . ( x - y ) \leq L | x - y | ^ { 2 }
$$

(ii) For every $x , v \in \mathbb { R } ^ { n }$

$$
D f ( x ) v . v \leq L | v | ^ { 2 } ,
$$

where $D f ( x )$ is the derivative of f at x, and . denotes the standard inner product of vectors in $\mathbb { R } ^ { n }$
:::

::: {.solution}
(i) =⇒ (ii): Let $x = y + t v$ . Then (i) says

$$
t ( f ( y + t v ) - f ( y ) ) . v \leq L t ^ { 2 } | v | ^ { 2 } .
$$

Divide by $t ^ { 2 }$ and take the limit as $t \longrightarrow 0$ to deduce $D f ( y ) v . v \leq L | v | ^ { 2 }$

(ii) =⇒ (i): Let $\phi ( t ) = f ( y + t ( x - y ) )$ for $t \in \mathbb { R }$ . Then

$$
{ \begin{array} { r l } { f ( x ) - f ( y ) = \phi ( 1 ) - \phi ( 0 ) \qquad } & { } \\ { \qquad = \displaystyle \int _ { 0 } ^ { 1 } \phi ^ { \prime } ( t ) d t } \\ { \qquad = \displaystyle \int _ { 0 } ^ { 1 } D f ( y + t ( x - y ) ) ( x - y ) d t \qquad } & { { \mathrm { ( b y ~ t h e ~ C h a i n ~ R u l e ) } } . } \end{array} }
$$

so

$$
\begin{array} { l l l } { ( f ( x ) - f ( y ) ) . ( x - y ) = \displaystyle \int _ { 0 } ^ { 1 } D f ( y + t ( x - y ) ) ( x - y ) . ( x - y ) d t } \\ { \displaystyle \qquad \leq \displaystyle \int _ { 0 } ^ { 1 } L | x - y | ^ { 2 } d t } \\ { \displaystyle \qquad = L | x - y | ^ { 2 } . } \end{array}\tag{by (ii)}
$$
:::
