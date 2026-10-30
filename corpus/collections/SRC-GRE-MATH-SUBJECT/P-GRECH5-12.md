---
schema: qual/card@1
id: P-GRECH5-12
kind: problem
title: Dimension of symmetric matrices
classification:
  areas:
  - applied-algebra
  topics:
  - Dimension
  - Symmetric Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 5 review Question 12 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch5-review/, replacing the earlier chapter-5.pdf transcription.
---

::: {.problem}
A square matrix $A$ is said to be symmetric if it equals its own transpose: $A = A^T$. What is the dimension of the subspace $S_{n \times n}(\RR)$ of real symmetric $n \times n$ matrices in the space of all real $n \times n$ matrices, $M_{n \times n}(\RR)$?

(A) $\frac{1}{2}n$
(B) $\frac{1}{2}n(n - 1)$
(C) $\frac{1}{2}n^2$
(D) $\frac{1}{2}n(n + 1)$
(E) $\frac{1}{2}n!$
:::

::: {.solution}

For $1\le i,j\le n$, let $E_{ij}$ denote the matrix with a $1$ in position $(i,j)$ and zeros elsewhere.

::: pf

::: {.pf-step #s1-1}

The set
$$
\mathcal B=
\{E_{ii}:1\le i\le n\}
\cup
\{E_{ij}+E_{ji}:1\le i<j\le n\}
$$
is a basis of $S_{n\times n}(\RR)$.


::: pf-proof

Every matrix in $\mathcal B$ is symmetric. If $A=(a_{ij})$ is symmetric, then
$$
A=\sum_{i=1}^n a_{ii}E_{ii}
+\sum_{1\le i<j\le n} a_{ij}(E_{ij}+E_{ji}),
$$
so $\mathcal B$ spans the symmetric matrices. In a linear combination of elements of $\mathcal B$, the coefficient of $E_{ii}$ is read from the $(i,i)$ entry and the coefficient of $E_{ij}+E_{ji}$ is read from the $(i,j)$ entry for $i<j$. Hence a zero linear combination has all coefficients zero, so $\mathcal B$ is linearly independent.

:::

:::

::: {.pf-step #s1-2}

The set $\mathcal B$ has
$$
n+\binom n2=\frac{n(n+1)}2
$$
elements.


::: pf-proof

There are $n$ diagonal matrices $E_{ii}$ and one matrix $E_{ij}+E_{ji}$ for each unordered pair of distinct indices, of which there are $\binom n2=n(n-1)/2$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\dim S_{n\times n}(\RR)=\frac12 n(n+1)},
$$
so the answer is (D).


::: pf-proof

By step [](#s1-1){.pf-ref}, $\mathcal B$ is a basis, and by step [](#s1-2){.pf-ref} it has $n(n+1)/2$ elements. The dimension equals the cardinality of a basis.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested dimension.

:::

:::

:::
