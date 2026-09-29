---
schema: qual/card@1
id: P-BKF12-9B
kind: problem
title: The product of the nonzero eigenvalues of a matrix lies in its field of entries
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 9B in the retained Fall 2012 Berkeley prelim exam.
    The retained solution packet incorrectly identifies the algebraic
    multiplicity of the zero eigenvalue with the nullity of M.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the characteristic-polynomial factorization over K and the
    coefficient that equals the signed product of the nonzero eigenvalues.
---

::: {.problem}
Let $M$ be a (possibly singular) square matrix over a field $F$. Let $p$ be the product of the nonzero eigenvalues of $M$ (counted with multiplicities) in some algebraically closed extension $K$ of $F$. Prove that $p\in F$.
:::

::: {.solution}
Let $M$ be $n\times n$, and let
$$
\chi_M(t)\coloneqq\det(tI-M)\in F[t].
$$

::: pf

::: {.pf-step #s1}

Over $K$, the characteristic polynomial has a factorization
$$
\chi_M(t)
=t^m\prod_{i=1}^{n-m}(t-\lambda_i),
$$
where $m$ is the algebraic multiplicity of the eigenvalue $0$ and the
$\lambda_i$ are exactly the nonzero eigenvalues of $M$, counted with
algebraic multiplicity.

::: pf-proof

The field $K$ is algebraically closed, so the monic polynomial
$\chi_M$ splits completely in $K[t]$. Separate the factors whose root
is $0$ from those whose roots are nonzero. The exponent $m$ is by
definition the multiplicity of $0$ as a root of $\chi_M$.

:::

:::

::: {.pf-step #s2}

If
$$
\chi_M(t)=c_0+c_1t+\cdots+c_nt^n,
\qquad
c_j\in F,
$$
then
$$
c_m=(-1)^{n-m}p.
$$

::: pf-proof

By step [](#s1){.pf-ref}, write
$$
\chi_M(t)=t^m q(t),
\qquad
q(t)=\prod_{i=1}^{n-m}(t-\lambda_i).
$$
The coefficient of $t^m$ in $t^m q(t)$ is the constant term of $q$.
Therefore
$$
c_m=q(0)
=\prod_{i=1}^{n-m}(-\lambda_i)
=(-1)^{n-m}p.
$$
This also covers the case in which there are no nonzero eigenvalues:
then the product is empty and equals $1$.

:::

:::

::: {.pf-step #s3}

The product of the nonzero eigenvalues satisfies
$$
\boxed{p\in F}.
$$

::: pf-proof

All coefficients $c_j$ of $\chi_M(t)\in F[t]$ lie in $F$. By step
[](#s2){.pf-ref},
$$
p=(-1)^{n-m}c_m,
$$
and the right-hand side belongs to $F$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
