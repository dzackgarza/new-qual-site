---
schema: qual/card@1
id: P-BKS00-6
kind: problem
title: Resolvents as low-degree polynomials in a matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Part 1 factors mu(t)-mu(lambda) and uses minimality to show
    mu(lambda) is nonzero. For part 2, the k resolvents lie in the
    k-dimensional algebra spanned by I,A,...,A^{k-1}; multiplying a
    putative dependence by the product of the resolvent denominators
    reduces it to an annihilating polynomial of degree below k.
---

::: {.problem}
Let $A$ be an $n\times n$ complex matrix whose minimal polynomial $\mu$ has degree $k$.

1. If $\lambda\in\mathbb C$ is not an eigenvalue of $A$, prove that there is a polynomial $p_\lambda$ of degree at most $k-1$ such that
   \[
   p_\lambda(A)=(A-\lambda I)^{-1}.
   \]
2. Let $\lambda_1,\ldots,\lambda_k$ be distinct complex numbers, none of them an eigenvalue of $A$. Prove that there exist $c_1,\ldots,c_k\in\mathbb C$ such that
   \[
   \sum_{j=1}^k c_j(A-\lambda_jI)^{-1}=I.
   \]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For part 1, if $\lambda$ is not an eigenvalue of $A$, then
$$
\mu(\lambda)\ne0.
$$

::: pf-proof

Since $\lambda$ is not an eigenvalue, $A-\lambda I$ is invertible. If
$\mu(\lambda)=0$, then
$$
\mu(t)=(t-\lambda)\nu(t)
$$
for some polynomial $\nu$ of degree $k-1$. Evaluating at $A$ gives
$$
0
=
\mu(A)
=
(A-\lambda I)\nu(A).
$$
Multiplying by $(A-\lambda I)^{-1}$ would give $\nu(A)=0$, contradicting
the minimality of $\mu$, since $\deg\nu<\deg\mu$.

:::

:::

::: {.pf-step #s2}

There is a polynomial $p_\lambda$ of degree at most $k-1$ such
that
$$
p_\lambda(A)=(A-\lambda I)^{-1}.
$$

::: pf-proof

The polynomial
$$
q_\lambda(t)
=
\frac{\mu(t)-\mu(\lambda)}{t-\lambda}
$$
has degree at most $k-1$. Evaluating the identity
$$
\mu(t)-\mu(\lambda)
=(t-\lambda)q_\lambda(t)
$$
at $A$ gives
$$
-\mu(\lambda)I
=
(A-\lambda I)q_\lambda(A).
$$
By step [](#s1){.pf-ref}, $\mu(\lambda)\ne0$. Hence the polynomial
$$
p_\lambda(t)
=
-\frac{q_\lambda(t)}{\mu(\lambda)}
$$
has degree at most $k-1$ and satisfies
$$
(A-\lambda I)p_\lambda(A)=I.
$$
Since $p_\lambda(A)$ is a polynomial in $A$, it commutes with
$A-\lambda I$, so it is the two-sided inverse:
$$
p_\lambda(A)=(A-\lambda I)^{-1}.
$$

:::

:::

::: {.pf-step #s3}

The vector space
$$
V
=
\operatorname{span}_{\CC}\{I,A,\ldots,A^{k-1}\}
$$
has dimension $k$.

::: pf-proof

If
$$
c_0I+c_1A+\cdots+c_{k-1}A^{k-1}=0
$$
with coefficients not all zero, then the nonzero polynomial
$$
r(t)=c_0+c_1t+\cdots+c_{k-1}t^{k-1}
$$
would satisfy $r(A)=0$ and have degree at most $k-1$. This contradicts
the definition of the minimal polynomial $\mu$ of degree $k$. Thus the
displayed spanning family is linearly independent, hence is a basis of
$V$.

:::

:::

::: {.pf-step #s4}

For part 2, the $k$ matrices
$$
R_j=(A-\lambda_jI)^{-1},
\qquad
1\leq j\leq k,
$$
are linearly independent elements of $V$.

::: pf-proof

Step [](#s2){.pf-ref} shows that each $R_j$ is a polynomial in $A$ of degree at most
$k-1$, so $R_j\in V$.

Suppose
$$
\sum_{j=1}^k d_jR_j=0.
$$
Set
$$
Q(t)=\prod_{i=1}^k(t-\lambda_i).
$$
Every factor $A-\lambda_iI$ is invertible and all these factors commute.
Multiplying the assumed relation by $Q(A)$ gives
$$
0
=
\sum_{j=1}^k
d_j\prod_{i\ne j}(A-\lambda_iI).
$$
Thus the polynomial
$$
r(t)
=
\sum_{j=1}^k
d_j\prod_{i\ne j}(t-\lambda_i)
$$
has degree at most $k-1$ and satisfies $r(A)=0$. By the minimality of
$\mu$, this forces $r=0$.

For each $j$, evaluation at $t=\lambda_j$ gives
$$
0
=
r(\lambda_j)
=
d_j\prod_{i\ne j}(\lambda_j-\lambda_i).
$$
The $\lambda_i$ are distinct, so the product is nonzero and hence
$d_j=0$. Therefore $R_1,\ldots,R_k$ are linearly independent.

:::

:::

::: {.pf-step #s5}

There exist $c_1,\ldots,c_k\in\CC$ such that
$$
\sum_{j=1}^k c_j(A-\lambda_jI)^{-1}=I.
$$

::: pf-proof

By step [](#s3){.pf-ref}, $V$ has dimension $k$, and by step [](#s4){.pf-ref} the $k$ matrices
$R_1,\ldots,R_k$ are linearly independent elements of $V$. They
therefore form a basis of $V$. Since $I\in V$, there exist
$c_1,\ldots,c_k\in\CC$ such that
$$
I
=
\sum_{j=1}^k c_jR_j
=
\sum_{j=1}^k c_j(A-\lambda_jI)^{-1}.
$$

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part 1, and step [](#s5){.pf-ref} proves part 2.

:::

:::

:::
