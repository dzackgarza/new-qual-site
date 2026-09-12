---
schema: qual/card@1
id: P-BKS04-3A
kind: problem
title: UC Berkeley Spring 2004 prelim 3A
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
Let $a _ { 1 } , \ldots , a _ { n } , b _ { 1 } , \ldots , b _ { m }$ be distinct complex numbers, let $r _ { 1 } , \ldots , r _ { n }$ be nonnegative integers, and let $c _ { 1 } , \ldots , c _ { m }$ be complex numbers.
Prove that if $m \leq r _ { 1 } + \cdot \cdot \cdot + r _ { n } + 1$ , then there exists a rational function $F ( z ) \in \mathbb { C } ( z )$ satisfying all of the following:

1. $F ( z )$ is holomorphic at ∞ and everywhere in C except possibly at $a _ { 1 } , \ldots , a _ { n }$

2. ${ \mathrm { o r d } } _ { z = a _ { i } } F ( z ) \geq - r _ { i }$

3. $F ( b _ { j } ) = c _ { j } { \mathrm { ~ f o r ~ } } j = 1 , \ldots , m .$
:::

::: {.solution}
Write $\begin{array} { r } { F ( z ) = G ( z ) / \prod _ { i = 1 } ^ { n } ( z - a _ { i } ) ^ { r _ { i } } } \end{array}$ , where $G ( z ) \in \mathbb { C } ( z )$ is to be determined.
The condition that F be holomorphic on C except for poles of order at most $r _ { i }$ at $a _ { i }$ corresponds to the condition that $G ( z )$ be holomorphic on $\mathbb { C } ,$ , hence a polynomial.
The condition that $F ( z )$ be holomorphic at ∞ corresponds to the condition deg $G \leq r _ { 1 } + \cdots + r _ { n }$ . The m conditions $F ( b _ { j } ) = c _ { j }$ correspond to conditions $G ( b _ { j } ) = c _ { j } ^ { \prime }$ where $\begin{array} { r } { c _ { j } ^ { \prime } = c _ { j } \prod _ { i = 1 } ^ { n } ( b _ { j } - a _ { i } ) ^ { r _ { i } } } \end{array}$ . These m conditions can be satisfied by a polynomial of degree $m - 1$ (which is $\leq r _ { 1 } + \cdots + r _ { n } )$ , by the Lagrange interpolation formula.
Alternatively,

{ polynomials of degree $\leq m - 1 \}  \mathbb { C } ^ { m }$

$$
G ( z ) \mapsto ( G ( b _ { 1 } ) , \dots , G ( b _ { m } ) )
$$

is a linear map between C-vector spaces of the same finite dimension, and is injective (since a nonzero polynomial of degree $\leq m - 1$ has at most m − 1 zeros), so it is also surjective.
:::
