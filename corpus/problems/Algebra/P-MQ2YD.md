---
schema: qual/card@1
id: P-MQ2YD
kind: problem
title: Matrices satisfying a given polynomial over algebraically closed and finite
  fields
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Matrices
  - Finite Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
(1) What can you say about $n \times n$ matrices $A$ that satisfy a given polynomial $P(x) = 0$ over an algebraically closed field $k = \bar{k}$? How many similarity classes and how many such matrices are there?
(2) What about over a finite field $\mathbb{F}_q$? How many similarity classes and how many individual matrices satisfy $P(A) = 0$?
:::

::: {.solution}
For any field $K$,
\[
P(A)=0\iff \mu_A\mid P,
\]
where $\mu_A$ is the minimal polynomial of $A$.

Over an algebraically closed field, write
\[
P(x)=c\prod_{i=1}^r(x-\lambda_i)^{e_i}.
\]
Then a matrix $A\in M_n(K)$ satisfies $P(A)=0$ exactly when every Jordan block with eigenvalue $\lambda_i$ has size at most $e_i$, and no other eigenvalue occurs. Hence the similarity classes are parametrized by tuples of partitions
\[
\nu_i\vdash n_i,\qquad \sum_i n_i=n,
\]
with largest part of $\nu_i$ at most $e_i$. In particular, there are finitely many similarity classes.

The individual matrices form the finite union of their conjugacy orbits
\[
\mathcal O_A=\{SAS^{-1}:S\in\operatorname{GL}_n(K)\}.
\]
Thus there is no universal answer “infinitely many”: if all admissible matrices are scalar, the set may be finite (for example, $P=x-a$ gives only $aI$). If a non-scalar admissible similarity class occurs and $K$ is infinite, that orbit is positive-dimensional and has $|K|$ points; over $K=\mathbb C$ it therefore has continuum cardinality.

Over $\mathbb F_q$, factor
\[
P(x)=\prod_j f_j(x)^{e_j}
\]
into distinct monic irreducibles. Similarity classes are described by the corresponding rational-canonical/primary data: for each $f_j$, choose a partition whose largest part is at most $e_j$, subject to total dimension
\[
\sum_j (\deg f_j)|\nu_j|=n.
\]
Again only finitely many classes occur. The exact number of individual matrices is
\[
\sum_{[A]}\frac{|\operatorname{GL}_n(\mathbb F_q)|}
{|C_{\operatorname{GL}_n(\mathbb F_q)}(A)|},
\]
where the sum runs over the admissible similarity classes. This is a finite computable integer.
:::
