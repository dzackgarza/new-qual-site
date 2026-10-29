---
schema: qual/card@1
id: P-UCLAB11F-10
kind: problem
title: Real matrices satisfying the cube identity
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 10. Let $A$ be a $3\times3$ real matrix satisfying $A^3=I$.
Show that $A$ is similar over $\RR$ to a matrix of the form
\[
\begin{pmatrix}
1&0&0\\
0&\cos\theta&-\sin\theta\\
0&\sin\theta&\cos\theta
\end{pmatrix}
\]
for some real $\theta$.
What values of $\theta$ are possible?
:::

::: {.solution}

::: pf

::: pf-step

The minimal polynomial of $A$ divides
\[
t^3-1=(t-1)(t^2+t+1).
\]


::: pf-proof

The relation
\[
A^3=I
\]
is exactly
\[
(A^3-I)=0.
\]
Hence the polynomial $t^3-1$ annihilates $A$, so the minimal polynomial of $A$ divides it.

:::

:::

::: {.pf-step #s1-2}

The matrix $A$ is diagonalizable over $\CC$.


::: pf-proof

The polynomial
\[
t^3-1
\]
has the three distinct roots
\[
1,\qquad
\omega=e^{2\pi i/3},\qquad
\overline{\omega}=e^{-2\pi i/3}.
\]
Since the minimal polynomial of $A$ divides this squarefree polynomial, the minimal polynomial also has no repeated root. Therefore $A$ is diagonalizable over $\CC$.

:::

:::

::: pf-step

The complex spectrum of $A$ is contained in
\[
\{1,\omega,\overline\omega\}.
\]


::: pf-proof

If
\[
Av=\lambda v
\]
with $v\ne0$, then
\[
v=A^3v=\lambda^3v.
\]
Thus
\[
\lambda^3=1,
\]
so $\lambda$ is one of the three cube roots of unity.

:::

:::

::: {.pf-step #s1-4}

The eigenvalue $1$ occurs with odd multiplicity, and the multiplicities of $\omega$ and $\overline\omega$ are equal.


::: pf-proof

Because $A$ is real, its characteristic polynomial has real coefficients. Therefore nonreal eigenvalues occur with their complex conjugates and with the same algebraic multiplicity.

The total dimension is $3$. Thus the combined multiplicity of the pair
\[
\omega,\overline\omega
\]
is even. The remaining multiplicity, belonging to the only real cube root $1$, is therefore odd.

:::

:::

::: {.pf-step #s1-5}

There are only two spectral possibilities:
\[
\{1,1,1\}
\qquad\text{or}\qquad
\{1,\omega,\overline\omega\}.
\]


::: pf-proof

By step [](#s1-4){.pf-ref}, the multiplicity of $1$ is either $1$ or $3$. If it is $3$, there are no other eigenvalues. If it is $1$, the remaining two eigenvalues must be the conjugate pair $\omega,\overline\omega$.

:::

:::

::: pf-step

In the first case of step [](#s1-5){.pf-ref},
\[
A=I.
\]


::: pf-proof

By step [](#s1-2){.pf-ref}, $A$ is diagonalizable over $\CC$. If all three eigenvalues are $1$, then in an eigenbasis its matrix is the identity. Hence the operator itself is the identity.

:::

:::

::: {.pf-step #s1-7}

In the second case of step [](#s1-5){.pf-ref}, there is a real basis
\[
u_1,u_2,u_3
\]
in which
\[
[A]
=
\begin{pmatrix}
1&0&0\\
0&-\frac12&-\frac{\sqrt3}{2}\\
0&\frac{\sqrt3}{2}&-\frac12
\end{pmatrix}.
\]


::: pf-proof

Choose a nonzero real eigenvector $u_1$ for eigenvalue $1$.
Choose a complex eigenvector
\[
z=u+iv
\]
for
\[
\omega=-\frac12+\frac{\sqrt3}{2}i.
\]
The real vectors $u,v$ are linearly independent: otherwise $z$ would be a complex scalar multiple of a real vector, which would make the corresponding eigenvalue real.

Since $A$ is real,
\[
A(u+iv)
=
\omega(u+iv).
\]
Equating real and imaginary parts gives
\[
Au
=
-\frac12u-\frac{\sqrt3}{2}v,
\]
\[
Av
=
\frac{\sqrt3}{2}u-\frac12v.
\]
Replacing $v$ by $-v$ if necessary gives the displayed $2\times2$ rotation block on the real span of $u,v$. Together with $u_1$, these vectors form a real basis of $\RR^3$.

:::

:::

::: {.pf-step #s1-8}

Thus $A$ is similar over $\RR$ to
\[
\boxed{
\begin{pmatrix}
1&0&0\\
0&\cos\theta&-\sin\theta\\
0&\sin\theta&\cos\theta
\end{pmatrix}
}
\]
with
\[
\boxed{\theta\equiv0,\ \frac{2\pi}{3},\ \frac{4\pi}{3}\pmod{2\pi}}.
\]


::: pf-proof

If $A=I$, take $\theta=0$.
In the second case, step [](#s1-7){.pf-ref} gives the rotation block with
\[
\cos\theta=-\frac12,
\qquad
\sin\theta=\frac{\sqrt3}{2},
\]
so one may take
\[
\theta=\frac{2\pi}{3}.
\]
Changing the orientation of the real basis of the invariant plane replaces $\theta$ by
\[
-\frac{2\pi}{3}\equiv\frac{4\pi}{3}\pmod{2\pi}.
\]
Conversely, for any of the three displayed congruence classes,
\[
3\theta\in2\pi\ZZ,
\]
so the corresponding rotation block has cube equal to the identity.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} gives both the required real similarity form and all possible values of $\theta$.

:::

:::

:::
