---
schema: qual/card@1
id: P-UCLAB13S-09
kind: problem
title: Canonical real form of an orthogonal matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 9 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
Suppose $A$ is a real $n\times n$ orthogonal matrix.

(a) Show that $A$ is similar to a block-diagonal matrix whose blocks are $2\times2$ rotation matrices
$$
\begin{pmatrix}
\cos\theta&\sin\theta\\
-\sin\theta&\cos\theta
\end{pmatrix}
$$
together with some diagonal entries equal to $1$ or $-1$.

(b) Use part (a) to show that if $n$ is odd, then there is a nonzero vector $v$ such that $A^2v=v$.
:::

::: {.solution}

Regard the real matrix $A$ as a complex matrix acting on $\CC^n$.

::: pf

::: {.pf-step #s1-1}

Every complex eigenvalue $\lambda$ of $A$ satisfies
$$
\abs{\lambda}=1.
$$


::: pf-proof

Let
$$
Az=\lambda z
$$
with
$$
z\ne0.
$$
Since $A$ is real orthogonal,
$$
A^*A=A^TA=I.
$$
Thus $A$ preserves the Hermitian norm on $\CC^n$:
$$
\norm{Az}=\norm{z}.
$$
But
$$
\norm{Az}
=
\norm{\lambda z}
=
\abs{\lambda}\,\norm{z}.
$$
Since
$$
\norm{z}>0,
$$
one gets
$$
\abs{\lambda}=1.
$$

:::

:::

::: {.pf-step #s1-2}

The complex operator $A$ is normal and therefore has an orthonormal basis of complex eigenvectors.


::: pf-proof

From
$$
A^*A=I
$$
one also has
$$
AA^*=I.
$$
Hence
$$
A^*A=AA^*,
$$
so $A$ is normal.
The complex spectral theorem then gives an orthonormal eigenbasis.

:::

:::

::: pf-step

Every real eigenvalue of $A$ is either
$$
\boxed{1}
\qquad\text{or}\qquad
\boxed{-1}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, every eigenvalue has absolute value $1$.
The only real numbers of absolute value $1$ are $\pm1$.

:::

:::

::: pf-step

If
$$
\lambda=e^{i\theta}
$$
is a nonreal eigenvalue, then
$$
\overline{\lambda}=e^{-i\theta}
$$
is also an eigenvalue.


::: pf-proof

Because $A$ has real entries, complex conjugation commutes with $A$.
If
$$
Az=\lambda z,
$$
then
$$
A\overline z
=
\overline{Az}
=
\overline{\lambda}\,\overline z.
$$
Thus conjugate eigenvalues occur in pairs.

:::

:::

::: {.pf-step #s1-5}

Let
$$
z=u+iv
$$
be an eigenvector for a nonreal eigenvalue
$$
\lambda=e^{i\theta}
=
\cos\theta+i\sin\theta.
$$
Then the real plane
$$
P=\operatorname{span}_{\RR}\{u,v\}
$$
is $A$-invariant.


::: pf-proof

The eigenvalue equation
$$
A(u+iv)
=
(\cos\theta+i\sin\theta)(u+iv)
$$
gives, by comparing real and imaginary parts,
$$
Au
=
\cos\theta\,u
-
\sin\theta\,v,
$$
and
$$
Av
=
\sin\theta\,u
+
\cos\theta\,v.
$$
Thus both $Au$ and $Av$ lie in the real span of $u,v$.
Since $\lambda$ is nonreal,
$$
\sin\theta\ne0,
$$
and $u,v$ are linearly independent; otherwise $z$ would be a complex scalar multiple of a real vector and would yield a real eigenvector with nonreal eigenvalue.
Hence $P$ is a two-dimensional invariant plane.

:::

:::

::: {.pf-step #s1-6}

The restriction
$$
A\restrict_P
$$
is an orthogonal transformation of the real inner-product plane $P$ with determinant $1$.


::: pf-proof

Since $A$ is orthogonal on $\RR^n$, its restriction to any invariant real subspace preserves the inner product.
Thus
$$
A\restrict_P
$$
is orthogonal.

Its complex eigenvalues are
$$
e^{i\theta}
\quad\text{and}\quad
e^{-i\theta},
$$
so its determinant is their product:
$$
e^{i\theta}e^{-i\theta}=1.
$$

:::

:::

::: {.pf-step #s1-7}

There is an orthonormal basis of $P$ in which the matrix of $A\restrict_P$ is
$$
\boxed{
\begin{pmatrix}
\cos\theta&\sin\theta\\
-\sin\theta&\cos\theta
\end{pmatrix}.
}
$$


::: pf-proof

Choose any unit vector
$$
e_1\in P.
$$
Because $A\restrict_P$ is orientation-preserving and orthogonal by step [](#s1-6){.pf-ref}, it is a rotation of the Euclidean plane.
Choose the unit vector $e_2$ so that $(e_1,e_2)$ is positively oriented.
Then for some angle $\theta$,
$$
Ae_1
=
\cos\theta\,e_1
-
\sin\theta\,e_2,
$$
and orientation preservation forces
$$
Ae_2
=
\sin\theta\,e_1
+
\cos\theta\,e_2.
$$
The corresponding matrix has the displayed form.
The eigenvalues determine the same angle modulo sign and $2\pi$.

:::

:::

::: {.pf-step #s1-8}

The real space $\RR^n$ decomposes orthogonally into real eigenspaces for $\pm1$ and two-dimensional invariant planes associated to nonreal conjugate pairs.


::: pf-proof

By step [](#s1-2){.pf-ref}, $\CC^n$ is an orthogonal direct sum of eigenspaces of $A$.
The eigenspaces for the real eigenvalues $\pm1$ are invariant under conjugation and have real orthonormal bases.

For every nonreal eigenvalue $\lambda$, pair its eigenspace with the conjugate eigenspace for $\overline\lambda$.
Taking real and imaginary parts of paired complex eigenvectors produces real two-dimensional invariant planes as in step [](#s1-5){.pf-ref}.
Different spectral subspaces are orthogonal because $A$ is normal.
Collecting these real pieces gives an orthogonal direct-sum decomposition of $\RR^n$.

:::

:::

::: {.pf-step #s1-9}

Therefore $A$ is orthogonally similar to a block-diagonal matrix whose blocks are
$$
\boxed{
\begin{pmatrix}
\cos\theta&\sin\theta\\
-\sin\theta&\cos\theta
\end{pmatrix}
}
$$
together with $1\times1$ blocks
$$
\boxed{[1]}
\qquad\text{and}\qquad
\boxed{[-1]}.
$$


::: pf-proof

Choose orthonormal bases in each summand of the decomposition from step [](#s1-8){.pf-ref}.
On each two-dimensional plane, use the basis from step [](#s1-7){.pf-ref}.
On the real eigenspaces, use orthonormal eigenvectors.
The union is an orthonormal basis of $\RR^n$, and the matrix of $A$ in this basis is block diagonal with exactly the stated blocks.
This proves part (a).

:::

:::

::: {.pf-step #s1-10}

Suppose now that
$$
n
$$
is odd.
Then the block decomposition in step [](#s1-9){.pf-ref} contains at least one $1\times1$ block.


::: pf-proof

Every rotation block has dimension $2$.
If all blocks had size $2$, their total dimension would be even.
Since
$$
n
$$
is odd, at least one block must have size $1$.
Such a block is either $[1]$ or $[-1]$.

:::

:::

::: {.pf-step #s1-11}

There exists a nonzero real vector
$$
v
$$
such that
$$
Av=\pm v.
$$


::: pf-proof

Take a basis vector belonging to one of the $1\times1$ blocks from step [](#s1-10){.pf-ref}.
If that block is $[1]$, then
$$
Av=v.
$$
If it is $[-1]$, then
$$
Av=-v.
$$

:::

:::

::: {.pf-step #s1-12}

Hence
$$
\boxed{A^2v=v}.
$$


::: pf-proof

From step [](#s1-11){.pf-ref},
$$
Av=\pm v.
$$
Applying $A$ once more gives
$$
A^2v
=
A(\pm v)
=
\pm Av
=
\pm(\pm v)
=
v.
$$
Since $v$ is a basis vector, it is nonzero.
This proves part (b).

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} proves part (a), and step [](#s1-12){.pf-ref} proves part (b).

:::

:::

:::
