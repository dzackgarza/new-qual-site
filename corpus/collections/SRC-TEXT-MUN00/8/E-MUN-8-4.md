---
schema: qual/card@1
id: E-MUN-8-4
kind: problem
title: Defining the Fibonacci numbers by recursive definition
classification:
  areas:
  - topology
  topics:
  - Recursive Definition
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §8 Exercise 4, printed p. 56; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.4,
    printed pp. 95-96 (tmp/sources/munkres-solutions-whitman.pdf). His rho is 1 at
    m = 1 and f(m) + f(m-1) for m > 1, with a_0 = 1; the range is Z_+ because the
    Fibonacci numbers are positive.
---

::: {.exercise}

The Fibonacci numbers of number theory are defined recursively by the formula
$$
\lambda_1 = \lambda_2 = 1,
\qquad
\lambda_n = \lambda_{n-1} + \lambda_{n-2} \quad \text{for } n > 2.
$$
Define them rigorously by use of Theorem 8.4.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.4, printed pp. 95--96** (`tmp/sources/munkres-solutions-whitman.pdf`); the function $\rho$ below is his.

Take $A=\ZZ_+$ and $a_0=1$, and for $f:\{1,\dots,m\}\to\ZZ_+$ set
$$
\rho(f)=
\begin{cases}
1,&m=1,\\
f(m)+f(m-1),&m>1.
\end{cases}
$$
Every value is again a positive integer, so $\rho$ is a function into $A$ defined on each nonempty section, and Theorem 8.4 gives a unique $F:\ZZ_+\to\ZZ_+$ with
$$
F(1)=1,
\qquad
F(n)=\rho(F\restrict\{1,\dots,n-1\})=\begin{cases}1,&n=2,\\ F(n-1)+F(n-2),&n>2.\end{cases}
$$
The numbers $\lambda_n=F(n)$ therefore satisfy $\lambda_1=1$, $\lambda_2=1$ and $\lambda_n=\lambda_{n-1}+\lambda_{n-2}$ for $n>2$, which is the Fibonacci recursion; and any two functions satisfying it agree, since the recursion determines each value from its predecessors and Theorem 8.4 gives uniqueness.
:::
