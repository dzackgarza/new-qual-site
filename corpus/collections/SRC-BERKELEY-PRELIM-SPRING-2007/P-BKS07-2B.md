---
schema: qual/card@1
id: P-BKS07-2B
kind: problem
title: UC Berkeley Spring 2007 prelim 2B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Given any real number $a _ { 0 }$ , define $a _ { 1 } , a _ { 2 } , \dotsc$ . by the rule $a _ { n + 1 } = \cos a _ { n }$ for all $n \geq 0$ . Prove that the sequence $\left( a _ { n } \right)$ converges, and that the limit is the unique solution of the equation $\cos x = x$
:::

::: {.solution}
Let $g ( x ) = \cos x - x$ . Then $g ( 1 ) < 0$ , and since cos x is decreasing on $[ 0 , \pi ]$ , we have cos $; ( 1 / 2 ) > \cos ( \pi / 3 ) = 1 / 2$ , that is, $g ( 1 / 2 ) > 0$ By the Intermediate Value Theorem, there exists $1 / 2 < a < 1$ such that cos $a = a$ . To see that this a is the unique solution of $\cos x = x$ , observe first that any solution must clearly lie in $[ - 1 , 1 ]$ . On $[ - 1 , 0 )$ we have $x < 0 <$ cos x, so all solutions lie in [0, 1]. But $g ( x )$ is strictly decreasing on [0, 1], so the solution is unique.

Consider any function f which is differentiable and satisfies $| f ^ { \prime } ( x ) | < c$ for all x in an interval $( a - d , a + d )$ , where $c < 1$ 1, and $f ( a ) = a$ . For any $a _ { 0 } \in ( a - d , a + d )$ define a sequence $\left( a _ { n } \right)$ by $a _ { n + 1 } = f ( a _ { n } )$ . It follows easily by induction on n using the Mean Value Theorem that $| a _ { n + 1 } - a | < c | a _ { n } - a |$ for all n, hence $\left( a _ { n } \right)$ converges to a.

We’ll apply this with $f ( x ) = \cos x .$ , a the solution of cos $a = a$ , and $d = 1 / 2$ . Note that $[ a - d , a + d ] \subseteq ( 0 , 3 / 2 ) \subseteq ( 0 , \pi / 2 )$ since $a \in ( 1 / 2 , 1 )$ , and therefore $\cos ^ { \prime } ( x ) | = | \sin x | < c$ for some $c < 1$

The given sequence $\left( a _ { n } \right)$ satisfies $a _ { 1 } \in [ - 1 , 1 ]$ , hence $a _ { 2 } \in [ \cos ( 1 ) , 1 ] \subseteq [ 1 / 2 , 1 ] \subseteq ( a -$ $1 / 2 , a + 1 / 2 )$ . We conclude that $( a _ { 2 } , a _ { 3 } , \ldots )$ converges to a.
:::
