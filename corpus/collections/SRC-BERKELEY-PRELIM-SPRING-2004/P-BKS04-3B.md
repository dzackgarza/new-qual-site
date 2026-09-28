---
schema: qual/card@1
id: P-BKS04-3B
kind: problem
title: UC Berkeley Spring 2004 prelim 3B
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
Let A be ${ \mathrm { ~ a ~ } } d \times d$ matrix with complex entries.
Assume that every eigenvalue of A has absolute value 1. Prove that there exists a constant $c \in \mathbb { R }$ independent of n such that

$$
\| A ^ { n } x \| \leq c n ^ { d - 1 } \| x \|
$$

for all $n \geq 1$ and $\boldsymbol { x } \in \mathbb { C } ^ { d }$ . Here $\| x \| : = ( | x _ { 1 } | ^ { 2 } + \cdot \cdot \cdot + | x _ { d } | ^ { 2 } ) ^ { 1 / 2 }$ for all $( x _ { 1 } , \ldots , x _ { d } ) \in \mathbb { C } ^ { d } .$
:::

::: {.solution}
We may use $| x | _ { \infty } : = \operatorname* { m a x } \{ | x _ { 1 } | , \ldots , | x _ { n } | \}$ instead of $\lVert x \rVert$ , since different norms on a finite-dimensional vector space are bounded by positive constants times each other.
Then it suffices to show that the entries of $A ^ { n }$ are $O ( n ^ { d - 1 } )$ as $n \to \infty$ . This property is unchanged if we conjugate all the $A ^ { n }$ by a fixed invertible matrix.
Thus we may assume that A is in Jordan canonical form.
Thus $A = D + N$ where D is diagonal, N is nilpotent, and $D$ and $N$ commute.
By the Cayley-Hamilton theorem, $N ^ { d } = 0$ . Thus the binomial theorem gives

$$
A ^ { n } = D ^ { n } + { \binom { n } { 1 } } D ^ { n - 1 } N + { \binom { n } { 2 } } D ^ { n - 2 } N ^ { 2 } + \cdots + { \binom { n } { d - 1 } } D ^ { n - d + 1 } N ^ { d - 1 } .
$$

The diagonal entries of $D$ are the eigenvalues of A, which have absolute value 1, so the entries of $D ^ { m }$ are $O ( 1 )$ for any m. The entries of $N , \dot { N } ^ { 2 } , \dots , N ^ { d - 1 }$ do not depend on n. The binomial coefficients are $O ( n ^ { \dot { d } - 1 } )$ . Thus the entries of $A ^ { n }$ are $O ( n ^ { d - 1 } )$ , as desired.
:::
