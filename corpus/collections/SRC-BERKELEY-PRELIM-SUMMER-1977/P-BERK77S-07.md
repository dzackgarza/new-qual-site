---
schema: qual/card@1
id: P-BERK77S-07
kind: problem
title: A finite-order real operator on $\mathbb R^6$ splits into invariant planes
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
    Complexified A and used that its minimal polynomial divides the
    square-free polynomial x^26-1, hence the complexification is
    diagonalizable. Nonreal conjugate eigenvalues give real invariant
    two-planes from real and imaginary parts of eigenvectors. The remaining
    real eigenspaces for eigenvalues ±1 have even total dimension and split
    into invariant lines that can be paired into invariant two-planes.
---

::: {.problem}
Let $A:\mathbb R^6\to\mathbb R^6$ be linear and suppose
\[
A^{26}=I.
\]
Show that
\[
\mathbb R^6=V_1\oplus V_2\oplus V_3,
\]
where $V_1,V_2,V_3$ are two-dimensional $A$-invariant subspaces.
:::

::: {.solution}
Let
$$
A_{\CC}:\CC^6\longrightarrow\CC^6
$$
be the complexification of $A$.

<1>1. The operator $A_{\CC}$ is diagonalizable over $\CC$.

::: {.proof}
Since
$$
A_{\CC}^{26}=I,
$$
the minimal polynomial $m_A(x)$ of $A_{\CC}$ divides
$$
x^{26}-1.
$$
Over $\CC$, the polynomial $x^{26}-1$ has no repeated root because its
derivative is
$$
26x^{25},
$$
which has no common root with $x^{26}-1$. Hence $m_A(x)$ is a product of
distinct linear factors. Therefore $A_{\CC}$ is diagonalizable.
:::

<1>2. Every eigenvalue of $A_{\CC}$ is a $26$th root of unity, and
nonreal eigenvalues occur in conjugate pairs with equal multiplicity.

::: {.proof}
If
$$
A_{\CC}v=\lambda v
$$
with $v\neq0$, then
$$
v=A_{\CC}^{26}v=\lambda^{26}v,
$$
so $\lambda^{26}=1$.

Because $A$ has real coefficients, complex conjugation commutes with
$A_{\CC}$. Thus
$$
A_{\CC}\bar v
=
\overline{A_{\CC}v}
=
\bar\lambda\,\bar v.
$$
Conjugation therefore gives an antilinear bijection between the
$\lambda$- and $\bar\lambda$-eigenspaces, so they have equal complex
dimension.
:::

<1>3. For every nonreal eigenvalue $\lambda$ and every nonzero
$\lambda$-eigenvector
$$
v=u+iw
\qquad
(u,w\in\RR^6),
$$
the real plane
$$
P_v=\operatorname{span}_{\RR}\{u,w\}
$$
is two-dimensional and $A$-invariant.

::: {.proof}
Write
$$
\lambda=\alpha+i\beta
$$
with $\beta\neq0$. From
$$
A_{\CC}(u+iw)
=(\alpha+i\beta)(u+iw)
$$
and comparison of real and imaginary parts,
$$
Au=\alpha u-\beta w,
\qquad
Aw=\beta u+\alpha w.
$$
Hence $P_v$ is $A$-invariant.

If $u$ and $w$ were linearly dependent over $\RR$, then
$v$ would be a nonzero complex scalar multiple of a real vector $r$.
The equation $A_{\CC}v=\lambda v$ would then imply
$$
Ar=\lambda r.
$$
The left side is real while $\lambda$ is nonreal, impossible for
$r\neq0$. Thus $u,w$ are linearly independent and $\dim_{\RR}P_v=2$.
:::

<1>4. The real subspace corresponding to every conjugate pair of nonreal
eigenspaces is a direct sum of $A$-invariant two-planes.

::: {.proof}
Fix a nonreal eigenvalue $\lambda$ and choose a complex basis
$$
v_1,\ldots,v_m
$$
of its eigenspace. Write
$$
v_j=u_j+iw_j.
$$
By step <1>3, each
$$
P_j=\operatorname{span}_{\RR}\{u_j,w_j\}
$$
is an invariant two-plane.

Suppose
$$
\sum_{j=1}^m(a_ju_j+b_jw_j)=0
$$
with $a_j,b_j\in\RR$. Since
$$
u_j=\frac{v_j+\bar v_j}{2},
\qquad
w_j=\frac{v_j-\bar v_j}{2i},
$$
the displayed real relation becomes
$$
\sum_{j=1}^m\frac{a_j-ib_j}{2}v_j
+
\sum_{j=1}^m\frac{a_j+ib_j}{2}\bar v_j
=
0.
$$
The vectors $v_1,\ldots,v_m$ form a basis of the $\lambda$-eigenspace,
while $\bar v_1,\ldots,\bar v_m$ form a basis of the distinct
$\bar\lambda$-eigenspace. Their union is therefore complex-linearly
independent. All coefficients in the last relation vanish, so
$a_j=b_j=0$ for every $j$. Hence
$$
P_1\oplus\cdots\oplus P_m
$$
is direct. Its real dimension is $2m$, equal to the real dimension of the
real form of the direct sum of the $\lambda$- and
$\bar\lambda$-eigenspaces, so it is exactly that real form.
:::

<1>5. The only real eigenvalues of $A_{\CC}$ are $1$ and $-1$, and their
real eigenspaces split into $A$-invariant lines.

::: {.proof}
A real $26$th root of unity is necessarily $1$ or $-1$. Since
$A_{\CC}$ is diagonalizable by step <1>1, the real eigenspaces
$$
E_+=\ker(A-I),
\qquad
E_-=\ker(A+I)
$$
admit real bases. Every basis line in $E_+$ is fixed by $A$, and every
basis line in $E_-$ is multiplied by $-1$. Hence each basis line is
$A$-invariant.
:::

<1>6. The direct sum of all one-dimensional real eigenspaces has even
dimension.

::: {.proof}
By steps <1>2--<1>4, every contribution from a nonreal conjugate pair has
even real dimension. Since
$$
\dim_{\RR}\RR^6=6
$$
is even, the remaining real-eigenvalue contribution
$$
\dim E_+ + \dim E_-
$$
must also be even.
:::

<1>7. The real eigenlines can be paired to form $A$-invariant
two-dimensional subspaces.

::: {.proof}
By step <1>6 there are an even number of basis lines in the direct sum
$E_+\oplus E_-$. Pair them arbitrarily. The direct sum of any two invariant
lines is two-dimensional and $A$-invariant.
:::

<1>8. There exist two-dimensional $A$-invariant subspaces
$V_1,V_2,V_3$ such that
$$
\boxed{
\RR^6=V_1\oplus V_2\oplus V_3.
}
$$

::: {.proof}
Step <1>4 decomposes all nonreal spectral contributions into invariant
two-planes. Step <1>7 decomposes the remaining real spectral contribution
into invariant two-planes. Together these planes form a direct sum equal to
$\RR^6$ because the complex eigenspace decomposition in step <1>1 is
complete. Their dimensions sum to $6$, so exactly three planes occur.
Label them $V_1,V_2,V_3$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required decomposition.
:::
:::
