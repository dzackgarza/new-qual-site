---
schema: qual/card@1
id: P-UCLAB13S-07
kind: problem
title: Matrix exponential and logarithm from operator-norm series
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
(a) Define the operator norm of a real $n\times n$ matrix, considered as a linear transformation from $\RR^n$ to $\RR^n$.

(b) Let $I$ be the $n\times n$ identity matrix. Show that
$$
\exp(A)=I+A+\frac{A^2}{2!}+\frac{A^3}{3!}+\cdots
$$
converges entrywise.

(c) Show that
$$
\ln(I+A)=A-\frac{A^2}{2}+\frac{A^3}{3}-\cdots+(-1)^{n+1}\frac{A^n}{n}+\cdots
$$
converges if the operator norm of $A$ is less than one.

(d) Show that $\exp(\ln(I+A))=I+A$ if the operator norm of $A$ is less than one.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The operator norm of a real $n\times n$ matrix $A$ is
$$
\boxed{
\norm{A}_{\mathrm{op}}
=
\sup_{\norm{x}_2=1}\norm{Ax}_2.
}
$$


::: pf-proof

This is the norm induced by the Euclidean norm on $\RR^n$.
Equivalently,
$$
\norm{A}_{\mathrm{op}}
=
\sup_{x\ne0}
\frac{\norm{Ax}_2}{\norm{x}_2}.
$$
This answers part (a).

:::

:::

::: {.pf-step #s1-2}

The operator norm is submultiplicative:
$$
\norm{AB}_{\mathrm{op}}
\le
\norm{A}_{\mathrm{op}}
\norm{B}_{\mathrm{op}}.
$$


::: pf-proof

For every vector $x$,
$$
\norm{ABx}_2
\le
\norm{A}_{\mathrm{op}}\norm{Bx}_2
\le
\norm{A}_{\mathrm{op}}
\norm{B}_{\mathrm{op}}
\norm{x}_2.
$$
Take the supremum over unit vectors $x$.

:::

:::

::: {.pf-step #s1-3}

For every positive integer $m$,
$$
\norm{A^m}_{\mathrm{op}}
\le
\norm{A}_{\mathrm{op}}^m.
$$


::: pf-proof

Apply step [](#s1-2){.pf-ref} inductively.

:::

:::

::: {.pf-step #s1-4}

The exponential series
$$
\sum_{m=0}^{\infty}\frac{A^m}{m!}
$$
converges absolutely in operator norm.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\norm{
\frac{A^m}{m!}
}_{\mathrm{op}}
\le
\frac{\norm{A}_{\mathrm{op}}^m}{m!}.
$$
The scalar series
$$
\sum_{m=0}^{\infty}
\frac{\norm{A}_{\mathrm{op}}^m}{m!}
=
e^{\norm{A}_{\mathrm{op}}}
$$
converges.
Therefore the matrix series converges absolutely in the finite-dimensional normed space
$$
M_n(\RR).
$$

:::

:::

::: {.pf-step #s1-5}

Operator-norm convergence implies entrywise convergence.


::: pf-proof

Let
$$
E_j
$$
be the $j$th standard basis vector.
For any matrix $B=(b_{ij})$,
$$
\abs{b_{ij}}
=
\abs{E_i^TBE_j}
\le
\norm{BE_j}_2
\le
\norm{B}_{\mathrm{op}}.
$$
Thus if
$$
\norm{B_m-B}_{\mathrm{op}}\to0,
$$
then every entry of $B_m-B$ tends to zero.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
\exp(A)
=
I+A+\frac{A^2}{2!}+\cdots
}
$$
converges entrywise for every real matrix $A$.


::: pf-proof

Step [](#s1-4){.pf-ref} gives convergence in operator norm, and step [](#s1-5){.pf-ref} gives entrywise convergence.
This proves part (b).

:::

:::

::: {.pf-step #s1-7}

Suppose
$$
\norm{A}_{\mathrm{op}}<1.
$$
Then the logarithm series
$$
\sum_{m=1}^{\infty}
(-1)^{m+1}\frac{A^m}{m}
$$
converges absolutely in operator norm.


::: pf-proof

Let
$$
q=\norm{A}_{\mathrm{op}}<1.
$$
By step [](#s1-3){.pf-ref},
$$
\norm{
\frac{A^m}{m}
}_{\mathrm{op}}
\le
\frac{q^m}{m}.
$$
The scalar series
$$
\sum_{m=1}^{\infty}\frac{q^m}{m}
$$
converges for
$$
0\le q<1.
$$
Therefore the matrix series converges absolutely.

:::

:::

::: {.pf-step #s1-8}

Consequently,
$$
\boxed{
\ln(I+A)
=
\sum_{m=1}^{\infty}
(-1)^{m+1}\frac{A^m}{m}
}
$$
is well-defined whenever
$$
\norm{A}_{\mathrm{op}}<1.
$$


::: pf-proof

This is exactly the convergent series from step [](#s1-7){.pf-ref}.
By step [](#s1-5){.pf-ref}, it also converges entrywise.
This proves part (c).

:::

:::

::: {.pf-step #s1-9}

In any complete normed algebra, absolutely convergent power series in one element may be multiplied and composed according to the corresponding scalar power-series identities, provided the scalar compositions converge absolutely.


::: pf-proof

Let
$$
P(A)=\sum_{m=0}^{\infty}p_mA^m
$$
and
$$
Q(A)=\sum_{m=0}^{\infty}q_mA^m
$$
converge absolutely.
Submultiplicativity gives
$$
\sum_{m,n}
\abs{p_mq_n}\norm{A}^{m+n}
<
\infty.
$$
Hence the double series for the product converges absolutely and may be regrouped by total degree:
$$
P(A)Q(A)
=
\sum_{k=0}^{\infty}
\left(
\sum_{m+n=k}p_mq_n
\right)A^k.
$$
Thus Cauchy products agree with scalar Cauchy products.
Repeated application gives the same conclusion for absolutely convergent compositions of scalar power series.

:::

:::

::: {.pf-step #s1-10}

For scalar $z$ with
$$
\abs{z}<1,
$$
one has the analytic identity
$$
\exp(\log(1+z))
=
1+z,
$$
where
$$
\log(1+z)
=
\sum_{m=1}^{\infty}
(-1)^{m+1}\frac{z^m}{m}.
$$


::: pf-proof

This is the ordinary scalar power-series identity for the exponential and logarithm in the disk
$$
\abs{z}<1.
$$
Both series converge absolutely there, and their composition represents the analytic function $1+z$.

:::

:::

::: {.pf-step #s1-11}

If
$$
\norm{A}_{\mathrm{op}}<1,
$$
then substituting $A$ into the scalar identity in step [](#s1-10){.pf-ref} gives
$$
\boxed{
\exp(\ln(I+A))
=
I+A.
}
$$


::: pf-proof

By steps [](#s1-4){.pf-ref} and [](#s1-7){.pf-ref}, the exponential and logarithm matrix series converge absolutely in operator norm.
Step [](#s1-9){.pf-ref} permits the same Cauchy-product and composition manipulations as for the scalar power series.
The scalar identity from step [](#s1-10){.pf-ref} has power-series expansion exactly
$$
1+z.
$$
Replacing $z$ by $A$ therefore gives
$$
\exp(\ln(I+A))
=
I+A.
$$
This proves part (d).

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), step [](#s1-6){.pf-ref} proves part (b), step [](#s1-8){.pf-ref} proves part (c), and step [](#s1-11){.pf-ref} proves part (d).

:::

:::

:::
