---
schema: qual/card@1
id: P-UCLAB15S-11
kind: problem
title: Ten commuting real matrices of the same finite order
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Two matrices $A,B$ are called commuting if $AB=BA$.
The order of a matrix $A$ is the smallest integer $k>0$ such that $A^k=I$; if no such $k$ exists, its order is infinite.

Prove that there exist ten distinct real $2\times2$ matrices which are pairwise commuting and all have the same finite order.
:::

::: {.solution}
For
\[
k=1,\ldots,10,
\]
define
\[
\theta_k=\frac{2\pi k}{11}
\]
and let
\[
\boxed{
R_k
=
\begin{pmatrix}
\cos\theta_k&-\sin\theta_k\\
\sin\theta_k&\cos\theta_k
\end{pmatrix}.
}
\]

<1>1. Each $R_k$ is a real $2\times2$ rotation matrix.

::: {.proof}
Its entries are real, and it is the standard matrix for rotation through angle
\[
\theta_k.
\]
:::

<1>2. For any real angles $\alpha,\beta$,
\[
R(\alpha)R(\beta)
=
R(\alpha+\beta).
\]

::: {.proof}
Multiply the standard rotation matrices and use the angle-addition formulas
\[
\cos(\alpha+\beta)
=
\cos\alpha\cos\beta-\sin\alpha\sin\beta,
\]
\[
\sin(\alpha+\beta)
=
\sin\alpha\cos\beta+\cos\alpha\sin\beta.
\]
:::

<1>3. The matrices
\[
R_1,\ldots,R_{10}
\]
are pairwise commuting.

::: {.proof}
By step <1>2,
\[
R_jR_k
=
R(\theta_j+\theta_k)
=
R_kR_j.
\]
:::

<1>4. The matrices
\[
R_1,\ldots,R_{10}
\]
are pairwise distinct.

::: {.proof}
If
\[
R_j=R_k,
\]
then the two rotations have the same angle modulo $2\pi$:
\[
\theta_j\equiv\theta_k\pmod{2\pi}.
\]
Thus
\[
\frac{2\pi(j-k)}{11}
\]
is an integer multiple of $2\pi$, so
\[
11\mid(j-k).
\]
Since
\[
1\le j,k\le10,
\]
this forces
\[
j=k.
\]
:::

<1>5. For every positive integer $m$,
\[
R_k^m
=
R\left(\frac{2\pi km}{11}\right).
\]

::: {.proof}
Apply step <1>2 repeatedly.
:::

<1>6. One has
\[
R_k^{11}=I
\]
for every
\[
k=1,\ldots,10.
\]

::: {.proof}
By step <1>5,
\[
R_k^{11}
=
R(2\pi k)
=
I.
\]
:::

<1>7. If
\[
1\le m<11,
\]
then
\[
R_k^m\ne I.
\]

::: {.proof}
If
\[
R_k^m=I,
\]
then by step <1>5,
\[
\frac{2\pi km}{11}
\]
must be an integer multiple of $2\pi$.
Thus
\[
11\mid km.
\]
Because $11$ is prime and
\[
1\le k\le10,
\]
one has
\[
11\nmid k.
\]
Hence
\[
11\mid m,
\]
contradicting
\[
1\le m<11.
\]
:::

<1>8. Therefore every $R_k$ has order exactly
\[
\boxed{11}.
\]

::: {.proof}
Step <1>6 shows the order divides $11$, while step <1>7 shows no smaller positive exponent gives the identity.
:::

<1>9. Thus
\[
\boxed{
R_1,\ldots,R_{10}
}
\]
are ten distinct pairwise commuting real $2\times2$ matrices, all of the same finite order.

::: {.proof}
Distinctness is step <1>4, pairwise commutativity is step <1>3, and common order $11$ is step <1>8.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required construction.
:::
:::
