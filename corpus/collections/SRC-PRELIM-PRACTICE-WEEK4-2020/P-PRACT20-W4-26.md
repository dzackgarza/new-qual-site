---
schema: qual/card@1
id: P-PRACT20-W4-26
kind: problem
title: Invertibility and inverse of $I_n+\sigma J_n$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Matrices
  - Invertibility
relations: []
review: draft
---

::: {.problem}
Let $I _ { n }$ by the $n \times n$ identity matrix and let $J _ { n }$ be the $n \times n$ matrix with all entries equal to 1. Determine the values of $\sigma \in \mathbb { R }$ so that $I _ { n } + \sigma J _ { n }$ is invertible.
Find $( I _ { n } + \sigma J _ { n } ) ^ { - 1 }$ for such σ.
:::

::: {.solution}
Note that regardless of σ 1 is an eigenvalue of $I _ { n } + \sigma J _ { n }$ of multiplicity at least $n - 1$ since $\left( I _ { n } + \sigma J _ { n } \right) - 1 \cdot I _ { n } = \sigma J _ { n }$ has rank 1. Next, note that $\vec { \bf 1 } = ( 1 , 1 , \dots , 1 ) ^ { t }$ satisfies

$$
( I _ { n } + \sigma J _ { n } ) \vec { \bf 1 } = ( 1 + \sigma n ) \vec { \bf 1 } ,
$$

so the other eigenvalue is $1 + \sigma n$ . Thus the matrix is invertible unless $\sigma = - 1 / n$ . To find the inverse, consider

$$
( I _ { n } + \sigma J _ { n } ) ( I _ { n } + \tau J _ { n } ) = I _ { n } + ( \sigma + \tau + n \sigma \tau ) J _ { n } .
$$

If $\sigma \neq - 1 / n _ { \colon }$ , we can take $\textstyle \tau = - { \frac { \sigma } { 1 + n \sigma } }$ to see that

$$
\boxed { ( I _ { n } + \sigma J _ { n } ) ^ { - 1 } = I _ { n } - \frac { \sigma } { 1 + n \sigma } J _ { n } . }
$$
:::
