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
(a) Define the operator norm of a real $n\times n$ matrix, considered as a linear transformation from $\mathbb R^n$ to $\mathbb R^n$.

(b) Let $I$ be the $n\times n$ identity matrix. Show that
\[
\exp(A)=I+A+\frac{A^2}{2!}+\frac{A^3}{3!}+\cdots
\]
converges entrywise.

(c) Show that
\[
\ln(I+A)=A-\frac{A^2}{2}+\frac{A^3}{3}-\cdots+(-1)^{n+1}\frac{A^n}{n}+\cdots
\]
converges if the operator norm of $A$ is less than one.

(d) Show that $\exp(\ln(I+A))=I+A$ if the operator norm of $A$ is less than one.
:::

::: {.solution}
<1>1. The operator norm of a real $n\times n$ matrix $A$ is
\[
\boxed{
\|A\|_{\mathrm{op}}
=
\sup_{\|x\|_2=1}\|Ax\|_2.
}
\]

::: {.proof}
This is the norm induced by the Euclidean norm on $\mathbb R^n$.
Equivalently,
\[
\|A\|_{\mathrm{op}}
=
\sup_{x\ne0}
\frac{\|Ax\|_2}{\|x\|_2}.
\]
This answers part (a).
:::

<1>2. The operator norm is submultiplicative:
\[
\|AB\|_{\mathrm{op}}
\le
\|A\|_{\mathrm{op}}
\|B\|_{\mathrm{op}}.
\]

::: {.proof}
For every vector $x$,
\[
\|ABx\|_2
\le
\|A\|_{\mathrm{op}}\|Bx\|_2
\le
\|A\|_{\mathrm{op}}
\|B\|_{\mathrm{op}}
\|x\|_2.
\]
Take the supremum over unit vectors $x$.
:::

<1>3. For every positive integer $m$,
\[
\|A^m\|_{\mathrm{op}}
\le
\|A\|_{\mathrm{op}}^m.
\]

::: {.proof}
Apply step <1>2 inductively.
:::

<1>4. The exponential series
\[
\sum_{m=0}^{\infty}\frac{A^m}{m!}
\]
converges absolutely in operator norm.

::: {.proof}
By step <1>3,
\[
\left\|
\frac{A^m}{m!}
\right\|_{\mathrm{op}}
\le
\frac{\|A\|_{\mathrm{op}}^m}{m!}.
\]
The scalar series
\[
\sum_{m=0}^{\infty}
\frac{\|A\|_{\mathrm{op}}^m}{m!}
=
e^{\|A\|_{\mathrm{op}}}
\]
converges.
Therefore the matrix series converges absolutely in the finite-dimensional normed space
\[
M_n(\mathbb R).
\]
:::

<1>5. Operator-norm convergence implies entrywise convergence.

::: {.proof}
Let
\[
E_j
\]
be the $j$th standard basis vector.
For any matrix $B=(b_{ij})$,
\[
|b_{ij}|
=
|E_i^TBE_j|
\le
\|BE_j\|_2
\le
\|B\|_{\mathrm{op}}.
\]
Thus if
\[
\|B_m-B\|_{\mathrm{op}}\to0,
\]
then every entry of $B_m-B$ tends to zero.
:::

<1>6. Hence
\[
\boxed{
\exp(A)
=
I+A+\frac{A^2}{2!}+\cdots
}
\]
converges entrywise for every real matrix $A$.

::: {.proof}
Step <1>4 gives convergence in operator norm, and step <1>5 gives entrywise convergence.
This proves part (b).
:::

<1>7. Suppose
\[
\|A\|_{\mathrm{op}}<1.
\]
Then the logarithm series
\[
\sum_{m=1}^{\infty}
(-1)^{m+1}\frac{A^m}{m}
\]
converges absolutely in operator norm.

::: {.proof}
Let
\[
q=\|A\|_{\mathrm{op}}<1.
\]
By step <1>3,
\[
\left\|
\frac{A^m}{m}
\right\|_{\mathrm{op}}
\le
\frac{q^m}{m}.
\]
The scalar series
\[
\sum_{m=1}^{\infty}\frac{q^m}{m}
\]
converges for
\[
0\le q<1.
\]
Therefore the matrix series converges absolutely.
:::

<1>8. Consequently,
\[
\boxed{
\ln(I+A)
=
\sum_{m=1}^{\infty}
(-1)^{m+1}\frac{A^m}{m}
}
\]
is well-defined whenever
\[
\|A\|_{\mathrm{op}}<1.
\]

::: {.proof}
This is exactly the convergent series from step <1>7.
By step <1>5, it also converges entrywise.
This proves part (c).
:::

<1>9. In any complete normed algebra, absolutely convergent power series in one element may be multiplied and composed according to the corresponding scalar power-series identities, provided the scalar compositions converge absolutely.

::: {.proof}
Let
\[
P(A)=\sum_{m=0}^{\infty}p_mA^m
\]
and
\[
Q(A)=\sum_{m=0}^{\infty}q_mA^m
\]
converge absolutely.
Submultiplicativity gives
\[
\sum_{m,n}
|p_mq_n|\|A\|^{m+n}
<
\infty.
\]
Hence the double series for the product converges absolutely and may be regrouped by total degree:
\[
P(A)Q(A)
=
\sum_{k=0}^{\infty}
\left(
\sum_{m+n=k}p_mq_n
\right)A^k.
\]
Thus Cauchy products agree with scalar Cauchy products.
Repeated application gives the same conclusion for absolutely convergent compositions of scalar power series.
:::

<1>10. For scalar $z$ with
\[
|z|<1,
\]
one has the analytic identity
\[
\exp(\log(1+z))
=
1+z,
\]
where
\[
\log(1+z)
=
\sum_{m=1}^{\infty}
(-1)^{m+1}\frac{z^m}{m}.
\]

::: {.proof}
This is the ordinary scalar power-series identity for the exponential and logarithm in the disk
\[
|z|<1.
\]
Both series converge absolutely there, and their composition represents the analytic function $1+z$.
:::

<1>11. If
\[
\|A\|_{\mathrm{op}}<1,
\]
then substituting $A$ into the scalar identity in step <1>10 gives
\[
\boxed{
\exp(\ln(I+A))
=
I+A.
}
\]

::: {.proof}
By steps <1>4 and <1>7, the exponential and logarithm matrix series converge absolutely in operator norm.
Step <1>9 permits the same Cauchy-product and composition manipulations as for the scalar power series.
The scalar identity from step <1>10 has power-series expansion exactly
\[
1+z.
\]
Replacing $z$ by $A$ therefore gives
\[
\exp(\ln(I+A))
=
I+A.
\]
This proves part (d).
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>1 answers part (a), step <1>6 proves part (b), step <1>8 proves part (c), and step <1>11 proves part (d).
:::
:::
