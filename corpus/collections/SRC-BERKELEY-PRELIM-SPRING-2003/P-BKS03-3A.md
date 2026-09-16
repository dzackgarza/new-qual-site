---
schema: qual/card@1
id: P-BKS03-3A
kind: problem
title: Centralizer of a Jordan block over $\mathbb Q$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $R$ be the subring of $M_2(\mathbb Q)$ consisting of matrices commuting with
\[
\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

(a) Prove that $R$ is a subring of $M_2(\mathbb Q)$.

(b) Prove that $R\cong\mathbb Q[x]/(x^2)$.
:::

::: {.solution}
(a) Let $N = { \binom { 1 } { 0 } } \ 1 )$ . If $A , B \in R ,$ , then $( A + B ) N = A N + B N = N A + N B = N ( A + B )$ , so $A + B \in R$ . If ${ \dot { A } } , B \in R$ , then $( A B ) N = A ( B N ) = A ( N B ) = ( A N ) B = ( N A ) B = N ( A B )$ so $A B \in R$ . If I is the identity matrix, then clearly $- I \in R$ . These three facts imply that R is a subring.

(b) Calculating shows that the matrix $A = { \binom { a b } { c d } }$ belongs to R if and only if $a = a + c ,$ $a + b = b + d ,$ , and $c + d = d ,$ that is, if and only if A has the form ${ \binom { a } { 0 } } \ b \ \qquad$ . We define a Q-algebra homomorphism $h : \mathbb { Q } [ x ] \to R$ by mapping x to $\left( { \begin{array} { c c } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} } \right)$ . Clearly $h ( x ^ { 2 } ) =$ ${ \left( \begin{array} { l l } { 0 } & { 1 } \\ { 0 } & { 0 } \end{array} \right) } ^ { 2 } = 0$ , so h induces a homomorphism $\mathbb { Q } [ x ] / ( x ^ { 2 } ) \to R$ . Since $h ( a + b x ) = { \binom { a b } { 0 } }$ this homomorphism $\mathbb { Q } [ x ] / ( x ^ { 2 } ) \to R$ is an isomorphism.
:::
