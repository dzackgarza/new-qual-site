---
schema: qual/card@1
id: P-UCLAB08S-11
kind: problem
title: A finite-order complex matrix is diagonalizable
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $A\in M_n(\CC)$ and suppose that $A^m=I_n$ for some positive integer $m$.
Prove that $A$ is diagonalizable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The matrix $A$ is annihilated by the polynomial
$$
p(t)=t^m-1.
$$


::: pf-proof

The hypothesis
$$
A^m=I_n
$$
is equivalent to
$$
A^m-I_n=0.
$$
Thus
$$
p(A)=0.
$$

:::

:::

::: {.pf-step #s1-2}

The polynomial
$$
p(t)=t^m-1
$$
has no repeated root over $\CC$.


::: pf-proof

Its derivative is
$$
p'(t)=mt^{m-1}.
$$
If $\lambda$ were a repeated root of $p$, then
$$
p(\lambda)=0
\qquad\text{and}\qquad
p'(\lambda)=0.
$$
The second equality gives
$$
\lambda=0,
$$
while
$$
p(0)=-1\ne0.
$$
This is impossible.
Hence all roots are simple.

:::

:::

::: {.pf-step #s1-3}

The minimal polynomial
$$
\mu_A(t)
$$
divides
$$
t^m-1.
$$


::: pf-proof

The minimal polynomial is the monic polynomial of least positive degree annihilating $A$.
If a polynomial $q$ annihilates $A$, divide $q$ by $\mu_A$:
$$
q=s\mu_A+r,
\qquad
\deg r<\deg\mu_A.
$$
Evaluating at $A$ gives
$$
0=q(A)=s(A)\mu_A(A)+r(A)=r(A).
$$
Minimality forces
$$
r=0.
$$
Thus $\mu_A$ divides every annihilating polynomial, in particular the polynomial from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The minimal polynomial $\mu_A$ splits into distinct linear factors.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\mu_A
\mid
t^m-1.
$$
By step [](#s1-2){.pf-ref}, the polynomial $t^m-1$ is a product of distinct linear factors over $\CC$.
Any divisor of such a polynomial also has no repeated factor.
Thus
$$
\mu_A(t)
=
\prod_{j=1}^r(t-\lambda_j)
$$
with pairwise distinct complex numbers $\lambda_j$.

:::

:::

::: {.pf-step #s1-5}

A complex matrix whose minimal polynomial splits into distinct linear factors is diagonalizable.


::: pf-proof

Let
$$
\mu_A(t)
=
\prod_{j=1}^r(t-\lambda_j)
$$
with distinct $\lambda_j$.
For each $j$, define
$$
q_j(t)
=
\prod_{i\ne j}
\frac{t-\lambda_i}{\lambda_j-\lambda_i}.
$$
Then
$$
q_j(\lambda_i)=\delta_{ij}.
$$
Set
$$
P_j=q_j(A).
$$
The polynomial
$$
1-\sum_{j=1}^rq_j(t)
$$
has degree at most $r-1$ and vanishes at the $r$ distinct numbers $\lambda_i$, so it is zero; equivalently Lagrange interpolation gives
$$
\sum_{j=1}^rq_j(t)=1.
$$
Thus
$$
\sum_{j=1}^rP_j=I.
$$

Moreover,
$$
(A-\lambda_jI)P_j
$$
is obtained by evaluating at $A$ a polynomial divisible by $\mu_A$, so it is zero.
Hence
$$
\operatorname{im}P_j
\subseteq
\ker(A-\lambda_jI).
$$
For any vector $v$,
$$
v=\sum_{j=1}^rP_jv
$$
is therefore a sum of eigenvectors belonging to the eigenspaces of $A$.
Thus the eigenspaces span $\CC^n$.
Choosing a basis in each eigenspace gives a basis of eigenvectors for $A$.
Therefore $A$ is diagonalizable.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{A\text{ is diagonalizable over }\CC}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} shows that the minimal polynomial of $A$ splits into distinct linear factors.
Step [](#s1-5){.pf-ref} then gives diagonalizability.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
