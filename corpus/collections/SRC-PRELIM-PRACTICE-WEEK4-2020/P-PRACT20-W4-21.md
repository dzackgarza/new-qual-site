---
schema: qual/card@1
id: P-PRACT20-W4-21
kind: problem
title: Eigenvectors for distinct eigenvalues are linearly independent
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Eigenvalues and Eigenvectors
relations: []
review: draft
---

::: {.problem}
Suppose that A has distinct eigenvalues $\lambda _ { 1 } , \ldots , \lambda _ { k }$ with corresponding eigenvectors $v _ { 1 } , \dots v _ { k }$ . Show that $\{ v _ { 1 } \ldots , v _ { k } \}$ is a linearly independent set.
:::

::: {.solution}
We use induction on $k . { \mathrm { ~ H ~ } } k = 1$ , the claim is trivial since $\{ v _ { 1 } \}$ is always a linearly independent set when $v _ { 1 } \neq 0$ . Suppose that any set of k eigenvectors corresponding to distinct eigenvalues is linearly independent and suppose that $\{ v _ { 1 } , \ldots , v _ { k } , v _ { k + 1 } \}$ is a set of $k + 1$ eigenvectors corresponding to distinct eigenvalues $\lambda _ { 1 } , \dots , \lambda _ { k } , \lambda _ { k + 1 }$ . Let $\alpha _ { 1 } , \ldots , \alpha _ { k } , \alpha _ { k + 1 } \in \mathbb { C }$ be such that

$$
\alpha _ { 1 } v _ { 1 } + \cdot \cdot \cdot + \alpha _ { k } v _ { k } + \alpha _ { k + 1 } v _ { k + 1 } = 0 .
$$

Apply the operator $A - \lambda _ { k + 1 } I$ to this equation and use that $( A - \lambda _ { k + 1 } I ) v _ { k + 1 } = 0$ and $( A - \lambda _ { k + 1 } I ) v _ { \ell } =$ $\lambda _ { \ell } v _ { \ell } - \lambda _ { k + 1 } v _ { \ell } = ( \lambda _ { \ell } - \lambda _ { k + 1 } ) v _ { \ell }$ for $\ell = 1 , \ldots , k$ . Then we see

$$
\alpha _ { 1 } ( \lambda _ { 1 } - \lambda _ { k + 1 } ) v _ { 1 } + \cdot \cdot \cdot + \alpha _ { k } ( \lambda _ { k } - \lambda _ { k + 1 } ) v _ { k } = 0 .
$$

However, these vectors are linearly independent by our inductive hypothesis.
Thus

$$
\alpha _ { 1 } ( \lambda _ { 1 } - \lambda _ { k + 1 } ) = \cdots = \alpha _ { k } ( \lambda _ { k } - \lambda _ { k + 1 } ) = 0 .
$$

Since the eigenvalues are assumed to be distinct, we can divide by $\lambda _ { \ell } - \lambda _ { k + 1 }$ to see that $\alpha _ { \ell } = 0$ for all $\ell = 1 , \ldots , k$ . But then we have $\alpha _ { k + 1 } v _ { k + 1 } = 0$ which gives $\alpha _ { k + 1 } = 0$ as well, and we conclude that $\{ v _ { 1 } , \ldots , v _ { k } , v _ { k + 1 } \}$ is a linearly independent set.
:::
