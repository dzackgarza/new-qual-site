---
schema: qual/card@1
id: P-BERK77S-12
kind: problem
title: Trace and eigenvectors of differentiation and its exponential on degree-ten polynomials
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    In the monomial basis, differentiation is strictly triangular, so its
    trace is zero. Its only eigenvectors are nonzero constants, with
    eigenvalue zero. Since D^11=0, e^D is the finite Taylor operator
    p(x)↦p(x+1); comparison of leading terms forces any eigenvalue to be
    one, and a polynomial satisfying p(x+1)=p(x) is constant.
---

::: {.problem}
Let $V$ be the vector space of polynomials of degree at most $10$, and let $D:V\to V$ be differentiation, $Dp=p'$.

1. Show that $\operatorname{tr}D=0$.
2. Find all eigenvectors of $D$ and of $e^D$.
:::

::: {.solution}
Use the ordered basis
$$
1,x,x^2,\ldots,x^{10}
$$
of $V$.

::: pf

::: {.pf-step #s1}

In this basis, the matrix of $D$ has zero diagonal.

::: pf-proof

For $j\geq1$,
$$
D(x^j)=jx^{j-1},
$$
while
$$
D(1)=0.
$$
Thus every basis vector is sent into the span of basis vectors preceding
it. Hence the matrix of $D$ is strictly triangular and in particular has
all diagonal entries equal to zero.

:::

:::

::: {.pf-step #s2}

One has
$$
\boxed{
\operatorname{tr}D=0.
}
$$

::: pf-proof

The trace is the sum of the diagonal entries of any matrix representing the
operator. Step [](#s1){.pf-ref} shows that all of them are zero.

:::

:::

::: {.pf-step #s3}

Every eigenvector of $D$ is a nonzero constant polynomial, and its
eigenvalue is $0$.

::: pf-proof

Suppose
$$
Dp=\lambda p
$$
for a nonzero polynomial $p\in V$. If $\deg p=m\geq1$ and $\lambda\neq0$,
then
$$
\deg(Dp)=m-1
$$
while
$$
\deg(\lambda p)=m,
$$
a contradiction. Hence $\lambda=0$, so
$$
p'=0.
$$
Therefore $p$ is constant. Conversely, every nonzero constant polynomial
is killed by $D$, so it is an eigenvector with eigenvalue $0$.

:::

:::

::: {.pf-step #s4}

The exponential operator is
$$
e^D
=
\sum_{k=0}^{10}\frac{D^k}{k!}
$$
and satisfies
$$
(e^Dp)(x)=p(x+1)
$$
for every $p\in V$.

::: pf-proof

Since every polynomial in $V$ has degree at most $10$,
$$
D^{11}=0.
$$
Thus the exponential series for the operator terminates after the
$D^{10}$ term. For each polynomial $p$, Taylor's formula is exact:
$$
p(x+1)
=
\sum_{k=0}^{10}\frac{p^{(k)}(x)}{k!}
=
\sum_{k=0}^{10}\frac{D^kp(x)}{k!}
=
(e^Dp)(x).
$$

:::

:::

::: {.pf-step #s5}

If $p$ is an eigenvector of $e^D$ with eigenvalue $\mu$, then
$$
\mu=1.
$$

::: pf-proof

By step [](#s4){.pf-ref}, the eigenvector equation is
$$
p(x+1)=\mu p(x).
$$
If $p$ has degree $m$ and leading coefficient $a_m\neq0$, then both
$p(x+1)$ and $p(x)$ have leading term
$$
a_mx^m.
$$
Comparison of the coefficients of $x^m$ gives
$$
a_m=\mu a_m,
$$
so $\mu=1$.

:::

:::

::: {.pf-step #s6}

Every eigenvector of $e^D$ is a nonzero constant polynomial.

::: pf-proof

By step [](#s5){.pf-ref}, an eigenvector satisfies
$$
p(x+1)=p(x).
$$
If $\deg p=m\geq1$ with leading coefficient $a_m$, then
$$
p(x+1)-p(x)
$$
has leading term
$$
ma_mx^{m-1},
$$
which is nonzero. Thus a nonconstant polynomial cannot satisfy the
displayed periodicity relation. Hence every eigenvector is constant.
Conversely, every nonzero constant polynomial is fixed by $e^D$, so it is
an eigenvector with eigenvalue $1$.

:::

:::

::: {.pf-step #s7}

The complete eigenvector classifications are
$$
\boxed{
\begin{aligned}
D &: \text{all nonzero constants, with eigenvalue }0,\\
e^D &: \text{all nonzero constants, with eigenvalue }1.
\end{aligned}
}
$$

::: pf-proof

This is exactly the content of steps [](#s3){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part (1), and step [](#s7){.pf-ref} proves part (2).

:::

:::

:::
