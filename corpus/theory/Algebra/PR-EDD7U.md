---
schema: qual/card@1
id: PR-EDD7U
kind: proposition
title: Characteristic polynomials via traces of exterior powers
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Determinants
  - Trace
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field, $A \in \Mat_{n\times n}(k)$, and $\chi_A(t) \coloneqq \det(tI - A)$.
Then
$$
\begin{aligned}
\chi_A(t) &= \sum_{k=0}^n (-1)^k \trace\qty{\Extpower^k A}\, t^{n-k} \\
&= t^n - \trace\qty{A} t^{n-1} + \trace\qty{\Extpower^2 A}\, t^{n-2} - \cdots + (-1)^{n-1} \trace\qty{\Extpower^{n-1} A}\, t + (-1)^n \det(A),
\end{aligned}
$$
where $\trace\qty{\Extpower^0 A} = 1$, $\Extpower^1 A = A$, and $\trace\qty{\Extpower^n A} = \det(A)$.
Moreover, for $0 \leq \ell \leq n$,
$$
\trace\qty{\Extpower^\ell A} = \sum_{\substack{S \subseteq \theset{1, \ldots, n} \\ \abs{S} = \ell}} \det\qty{A_{S,S}},
$$
the sum of the $\binom{n}{\ell}$ principal $\ell\times\ell$ minors of $A$, where $A_{S,S}$ is the submatrix of $A$ with rows and columns indexed by $S$, obtained by deleting the rows and columns indexed by the complement of $S$.
:::

::: {.example}
Let $M = (4i + j)_{0 \leq i, j \leq 3} \in \Mat_{4\times 4}(\QQ)$.
Its principal submatrices of each size $\ell$ are listed below; there are none of size $5$.

![](../../assets/figures/2021-07-24_19-48-11.png)

The $1\times 1$ minors sum to $\trace M = 0 + 5 + 10 + 15 = 30$, and the $2\times 2$ minors are $-4, -16, -36, -4, -16, -4$, with sum $-80$.
Every row of $M$ is a linear combination of $(1,1,1,1)$ and $(0,1,2,3)$, so $\rank M = 2$ and every $3\times 3$ and $4\times 4$ minor vanishes.
Therefore $\chi_M(t) = t^4 - 30t^3 - 80t^2$.
:::

::: {.proposition}
Let $f(t) = a_n t^n + \cdots + a_1 t + a_0 \in \ZZ[t]$ with $a_n \neq 0$.
If $p/q \in \QQ$ is a root of $f$ with $p, q \in \ZZ$ coprime, then $p \divides a_0$ and $q \divides a_n$.
In particular, if $f$ is monic, every rational root of $f$ is an integer dividing $a_0$.
:::

::: {.remark}
If $r$ is a root of $f$, polynomial long division gives $f(t) = (t - r)\,g(t)$ with $\deg g = \deg f - 1$, and the remaining roots of $f$ are the roots of $g$.
:::
