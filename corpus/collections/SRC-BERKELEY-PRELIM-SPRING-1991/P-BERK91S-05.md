---
schema: qual/card@1
id: P-BERK91S-05
kind: problem
title: Integer eigenvalues and row sums divide the determinant of an integer matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the integer matrix, integer eigenvalue, equal row sums, and both determinant-divisibility conclusions with Problem 5 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
---

::: {.problem}
Let $A=(a_{ij})_{i,j=1}^r$ be a square matrix with integer entries.

(a) Prove that if an integer $n$ is an eigenvalue of $A$, then $n$ divides $\det A$.

(b) Suppose that $n$ is an integer and every row of $A$ has sum $n$:
$$
\sum_{j=1}^r a_{ij}=n
\qquad(1\le i\le r).
$$
Prove that $n$ divides $\det A$.
:::

::: {.hint}
For part (a), write the characteristic polynomial as
$$
\chi_A(t)\coloneqq\det(tI_r-A)
=tq(t)+(-1)^r\det A,
\qquad q(t)\in\ZZ[t],
$$
and evaluate at the integer eigenvalue $n$. This expresses
$\det A$ as an integer multiple of $n$ without dividing by
$n$, so it also covers $n=0$.
For part (b), apply $A$ to the nonzero column vector
$(1,\ldots,1)^{\mathsf T}$ and use part (a).
:::

::: {.solution}
Let $I_r$ be the $r\times r$ identity matrix and let
$\chi_A(t)\coloneqq\det(tI_r-A)$ be the characteristic polynomial of $A$.

<1>1. There is a polynomial $q(t)\in\ZZ[t]$ such that
$$
\chi_A(t)=tq(t)+(-1)^r\det A.
$$

::: {.proof}
The determinant expansion expresses $\chi_A(t)$ as a sum of signed
products of polynomials with integer coefficients, so $\chi_A(t)\in\ZZ[t]$.
Its constant coefficient is $\chi_A(0)=\det(-A)=(-1)^r\det A$.
Subtracting this constant leaves an integer polynomial with zero constant
coefficient, which is $tq(t)$ for some $q(t)\in\ZZ[t]$.
:::

<1>2. Part (a): every integer eigenvalue $n$ of $A$ divides $\det A$.

::: {.proof}
Since $n$ is an eigenvalue, $nI_r-A$ has a nonzero vector in its kernel.
Consequently $\chi_A(n)=0$. Evaluating the identity in step <1>1 at $n$ gives
$$
\det A=(-1)^{r+1}nq(n).
$$
The number $(-1)^{r+1}q(n)$ is an integer, so this equality expresses
$\det A$ as an integer multiple of $n$. It also applies when $n=0$,
in which case $\det A=0$.
:::

<1>3. Part (b): if each row of $A$ has sum $n$, then $n$ divides $\det A$.

::: {.proof}
Let $e\coloneqq(1,\ldots,1)^{\mathsf T}\in\ZZ^r$. For each $1\le i\le r$,
$$
(Ae)_i=\sum_{j=1}^r a_{ij}=n=ne_i.
$$
Thus $Ae=ne$. Since $e\ne0$, the integer $n$ is an eigenvalue of $A$.
Step <1>2 therefore gives $n\mid\det A$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 prove parts (a) and (b), respectively.
:::
:::
