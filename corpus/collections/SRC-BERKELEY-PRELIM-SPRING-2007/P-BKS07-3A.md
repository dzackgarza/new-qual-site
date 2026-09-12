---
schema: qual/card@1
id: P-BKS07-3A
kind: problem
title: UC Berkeley Spring 2007 prelim 3A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose $f : \mathbb { R } \to \mathbb { R }$ is real analytic and periodic with period 2π. Prove that $f$ has an analytic continuation F defined on a strip

$$
S = \{ x + i y \in \mathbb { C } ~ : ~ | y | < \rho \}
$$

with $\rho > 0$ , and that $F ( z + 2 \pi ) = F ( z )$ for $z \in S$
:::

::: {.solution}
Since f is real analytic, it possesses derivatives of all orders and agrees with its (convergent) Taylor series on a neighborhood $( x - r _ { x } , x + r _ { x } )$ of every point $x \in \mathbb { R }$ . The same power series may be used to define F on the complex neighborhood $B ( x , r _ { x } )$ of radius $r _ { x }$ centered at x. Since $f$ is periodic, the coefficients of the Taylor series at $x + 2 \pi$ are the same as those at $x ,$ so we may assume that $r _ { x + 2 \pi } = r _ { x }$ for all $x \in \mathbb { R }$ . Let us cover the compact interval $[ - \pi , \pi ] \subset \mathbb { C }$ with open squares $\begin{array} { r } { U _ { x } = \left( x - \frac { 1 } { 2 } r _ { x } , x + \frac { 1 } { 2 } r _ { x } \right) \times \left( - \frac { 1 } { 2 } r _ { x } , \frac { 1 } { 2 } r _ { x } \right) } \end{array}$ and choose a finite sub-cover $U _ { x _ { 1 } } , . . . , U _ { x _ { n } } \mathrm { o f } [ - \pi , \pi ]$ . We now define

$$
\rho = \operatorname* { m i n } \left\{ { \frac { 1 } { 2 } } r _ { x _ { i } } : 1 \leq i \leq n \right\}
$$

and note that since each square $U _ { x _ { i } }$ has half-height $\geq \rho$ and satisfies $U _ { x _ { i } } \subset B ( x _ { i } , r _ { x _ { i } } )$ , the balls $\{ B ( x _ { i k } , r _ { x _ { i } } ) : x _ { i k } = x _ { i } + 2 \pi k , 1 \leq i \leq n , k \in \mathbb { Z } \}$ cover the strip S. For any $z \in S$ , we define $F ( z )$ using the Taylor series at any $x _ { i k }$ for which $z \in B ( x _ { i k } , r _ { x _ { i } } )$ . A different choice of $x _ { i k }$ will yield the same value $F ( z )$ since the intersection of two balls containing z will contain a positive interval of the real axis on which the Taylor expansions agree with $f ,$ s o they represent the same analytic function on this intersection.
F satisfies $F ( z + 2 \pi ) = F ( z )$ for $z \in S$ since the Taylor expansion centered at $x _ { i k }$ defining F at $z \in B ( x _ { i k } , r _ { x _ { i } } )$ has the same coefficients as the one centered at $x _ { i , k + 1 }$ defining $F$ at $z + 2 \pi$
:::
