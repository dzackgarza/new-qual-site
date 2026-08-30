---
schema: qual/card@1
id: E-SS10.PR-4
kind: exercise
title: "Invariant bounded holomorphic functions on the upper half plane are constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: exercise
4. Let $G$ denote the group of matrices given in the previous problem.
   Here we give an alternate proof of Theorem 3.4, that states that a function in H which is holomorphic, bounded, and invariant under G must be constant.

(a) Suppose that $f : \mathbb { H } \to \mathbb { C }$ is holomorphic, bounded, and that there exists a sequence of complex numbers $\tau _ { k } = x _ { k } + i y _ { k }$ such that

$$
f (\tau_ {k}) = 0, \quad \sum_ {k = 1} ^ {\infty} y _ {k} = \infty , \quad 0 <   y _ {k} \leq 1, \quad \text { and } \quad | x _ {k} | \leq 1.
$$

Then $f = 0$ . [Hint: When $x _ { k } = 0$ see Problem 5 in Chapter 8.]

(b) Given two relatively prime integers c and d with diferent parity, show that there exist integers a and b such that $\left( \begin{array} { c c } { { a } } & { { b } } \\ { { c } } & { { d } } \end{array} \right) \in G$ . [Hint: All the solutions of $x c + d y = 1$ take the form $x _ { 0 } + d t$ and $y _ { 0 } - c t$ where $x _ { 0 } , y _ { 0 }$ is a particular solution and $t \in \mathbb { Z } . ]$

(c) Prove that $\textstyle \sum { 1 } / ( c ^ { 2 } + d ^ { 2 } ) = \infty$ where the sum is taken over all c and d that are relatively prime and of opposite parity.
[Hint: Suppose not, and prove that $\textstyle \sum _ { ( a , b ) = 1 } 1 / ( a ^ { 2 } + b ^ { 2 } ) < \infty$ where the sum is over all relatively prime integers a and b. To do so, note that if a and b are both odd and relatively prime, then the two numbers c and d defined by $c = ( a + b ) / 2$ and $d = ( a - b ) / 2$ are relatively prime and of opposite parity.
Moreover, $c ^ { 2 } + d ^ { 2 } \leq A ( a ^ { 2 } + b ^ { 2 } )$ for some universal constant A. Therefore

$$
\sum_ {n \neq 0} \frac {1}{n ^ {2}} \sum_ {(a, b) = 1} \frac {1}{a ^ {2} + b ^ {2}} <   \infty ,
$$

hence $\sum 1 / ( k ^ { 2 } + \ell ^ { 2 } ) < \infty$ , where the sum is over all integers k and ℓ such that $k , \ell \neq 0$ . Why is this a contradiction?]

(d) Prove that if $F : \mathbb { H }  \mathbb { C }$ is holomorphic, bounded, and invariant under $G _ { i }$ , then $F$ is constant.
[Hint: Replace $F ( \tau )$ by $F ( \tau ) - F ( i )$ so that we can assume $F ( i ) = 0$ and prove $F = 0$ . For each relatively prime c and d with opposite parity, choose $g \in G$ so that $g ( i ) = x _ { c , d } + i \bar { / } ( \bar { c ^ { 2 } } + d ^ { 2 } )$ with $| x _ { c , d } | \leq 1 . ]$

$\mathbf { 5 . ^ { * } }$ In Chapter 9 we proved that the Weierstrass $\wp$ function satisfies the cubic equation

$$
\left(\wp^ {\prime}\right) ^ {2} = 4 \wp^ {3} - g _ {2} \wp - g _ {3},
$$

where $g _ { 2 } = 6 0 E _ { 4 } , \ g _ { 3 } = 1 4 0 E _ { 6 }$ , with $E _ { k }$ is the Eisenstein series of order $k$ . The discriminant of the cubic $y ^ { 2 } = 4 x ^ { 3 } - g _ { 2 } x - g _ { 3 }$ is defined by $\triangle = g _ { 2 } ^ { 3 } - 2 7 g _ { 3 } ^ { 2 }$ . Prove that

$$
\triangle (\tau) = (2 \pi) ^ {1 2} \eta^ {2 4} (\tau) \quad \text {   for   all   } \tau \in \mathbb {H}.
$$

[Hint: $\bigtriangleup$ and $\eta ^ { 2 4 }$ satisfy the same transformation laws under $\tau \mapsto \tau + 1$ and $\tau \mapsto$ $- 1 / \tau$ . Because of the fundamental domain described in Problem 2, it sufices then to investigate the behavior at the only cusp, which is at infinity.]

${ \bf 6 . ^ { * } }$ Here we will deduce the formula for $r _ { 8 } ( n )$ , which counts the number of representations of n as a sum of eight squares.
The method is parallel to that of $r _ { 4 } ( n )$ but the details are less delicate.

Theorem: $r _ { 8 } ( n ) = 1 6 \sigma _ { 3 } ^ { * } ( n )$
:::

::: {.solution}
<1>1. $G$ entire.
Proof: estimate.

<1>2. Q.E.D.
Proof: <1>1.
:::
