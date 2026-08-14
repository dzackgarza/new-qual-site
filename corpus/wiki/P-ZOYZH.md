---
schema: qual/card@1
id: P-ZOYZH
kind: problem
title: "A ring \\( R \\) is called simple if its only two-sided ideals are $0$\u2026"
classification:
  areas:
  - algebra
  topics:
  - fields
  - ideals
  - semisimplicity
relations: []
review: draft
---

A ring \( R \) is called *simple* if its only two-sided ideals are $0$ and $R$.

a. Suppose $R$ is a commutative ring with 1. Prove $R$ is simple if and only if $R$ is a field.

b. Let $k$ be a field.
Show the ring $M_n (k)$, $n \times n$ matrices with entries in $k$, is a simple ring.

::: {.concept}
\envlist

- Nonzero proper ideals contain at least one nonzero element.

- $I=R$ when $1\in I$.

- Effects of special matrices: let $A_{ij}$ be a matrix with only a 1 in the $ij$ position.

  - Left-multiplying $A_{ij}M$ moves row $j$ to row $i$ and zeros out the rest of $M$.

  - Right-multiplying $MA_{ij}$ moves column $i$ to column $j$ and zeros out the rest.

  - So $A_{ij} M A_{kl}$ moves entry $j, k$ to $i, l$ and zeros out the rest.
:::

::: {.solution}
\envlist

::: {.proof title="of a"}
$\implies$:

- Suppose $\Id(R) = \ts{\gens{0}, \gens{1}}$.
  Then for any nonzero $r\in R$, the ideal $\gens{r} = \gens{1}$ is the entire ring.

- In particular, $1\in \gens{r}$, so we can write $a = tr$ for some $t\in R$.

- But then $r\in R\units$ with $t\da r\inv$.

$\impliedby$:

- Suppose $R$ is a field and $I\in \Id(R)$ is an ideal.

- If $I \neq \gens{0}$ is proper and nontrivial, then $I$ contains at least one nonzero element $a\in I$.

- Since $R$ is a field, $a\inv \in R$, and $aa\inv = 1\in I$ forces $I = \gens{1}$.
:::

::: {.proof title="of b"}

- Let $J\normal R$ be a nonzero two-sided ideal, noting that $R$ is noncommutative -- the claim is that $J$ contains $I_n$, the $n\times n$ identity matrix, and thus $J = R$.

- Pick a nonzero element $M\in I$, then $M$ has a nonzero entry $m{ij}$.

- Let $A_{ij}$ be the matrix with a 1 in the $i,j$ position and zeros elsewhere.

  - Left-multiplying $A_{ij}M$ moves row $j$ to row $i$ and zeros out the rest of $M$.

  - Right-multiplying $MA_{ij}$ moves column $i$ to column $j$ and zeros out the rest.

  - So $A_{ij} M A_{kl}$ moves entry $j, k$ to $i, l$ and zeros out the rest.

- So define $B \da A_{i, i}MA_{j, i}$, which movies $m_{ij}$ to the $i,i$ position on the diagonal and has zeros elsewhere.

- Then $m_{ij}\inv \eps_{ii} \da A_{ii}$ is a matrix with $1$ in the $i, i$ spot for any $i$.
  Since $I$ is an ideal, we have $\eps_{ii}\in I$ for every $i$.

- We can write the identity $I_n$ as $\sum_{i=1}^n \eps_{ii}$, so $I_n \in I$ and $I=R$.
:::
:::
