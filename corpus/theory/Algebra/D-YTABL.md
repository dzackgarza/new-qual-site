---
schema: qual/card@1
id: D-YTABL
kind: definition
title: Partitions, Young diagrams, and semistandard tableaux
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
  - Young Tableaux
relations: []
review: draft
---

::: {.definition}
A \dfn{partition} of $n$ is a finite nonincreasing sequence $\lambda=(\lambda_1\geq\lambda_2\geq\cdots\geq\lambda_\ell\geq1)$ of positive integers with $\sum_i\lambda_i=n$; its \dfn{length} is $\ell(\lambda)\coloneqq\ell$ and its \dfn{size} is $\abs\lambda\coloneqq n$.
The \dfn{Young diagram} of $\lambda$ is the set of cells $(i,j)$ with $1\leq i\leq\ell$ and $1\leq j\leq\lambda_i$, drawn with $i$ increasing downwards and $j$ increasing to the right.
For partitions $\mu\subseteq\lambda$, that is $\mu_i\leq\lambda_i$ for every $i$, the \dfn{skew shape} $\lambda/\mu$ is the set of cells of the diagram of $\lambda$ that are not cells of the diagram of $\mu$.
:::

::: {.definition}
A \dfn{filling} of a skew shape assigns a positive integer to each of its cells, and a filling is a \dfn{semistandard tableau} if its entries are weakly increasing along each row from left to right and strictly increasing down each column.
The \dfn{content} of a filling is the sequence $\nu=(\nu_1,\nu_2,\ldots)$ whose $i$th term is the number of cells whose entry is $i$.
The \dfn{word} of a filling is the sequence of its entries read from right to left in each row, beginning with the top row and working down.
A word $w_1w_2\cdots w_m$ is a \dfn{lattice word}, or Yamanouchi word, if for every $t\leq m$ and every $i$ the first $t$ letters contain at least as many $i$'s as $(i+1)$'s.
:::
