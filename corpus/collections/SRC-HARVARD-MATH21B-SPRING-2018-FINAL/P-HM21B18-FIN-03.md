---
schema: qual/card@1
id: P-HM21B18-FIN-03
kind: problem
title: Diagonalizability, linearity, and Fourier-coefficient diagnostics
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
(a) Decide which of
\[
A=\begin{pmatrix}0&1&0&0&0\\0&0&1&0&0\\0&0&0&1&0\\0&0&0&0&1\\1&0&0&0&0\end{pmatrix},
\quad
B=\begin{pmatrix}0&1&0&0&1\\1&0&1&0&0\\0&1&0&1&0\\0&0&1&0&1\\1&0&0&1&0\end{pmatrix},
\]
\[
C=\begin{pmatrix}0&1&1&0&0\\0&0&1&1&0\\0&0&0&1&1\\0&0&0&0&1\\0&0&0&0&0\end{pmatrix}
\]
are diagonalizable over $\RR$.

(b) Decide which of the two displayed Game-of-Life matrices “Loaf” and “Boat” has a nonreal eigenvalue:
\[
L=\begin{pmatrix}
0&0&0&0&0&0\\0&0&1&1&0&0\\0&1&0&0&1&0\\0&0&1&0&1&0\\0&0&0&1&0&0\\0&0&0&0&0&0
\end{pmatrix},
\]
\[
B_0=\begin{pmatrix}
0&0&0&0&0\\0&1&1&0&0\\0&1&0&1&0\\0&0&1&0&0\\0&0&0&0&0
\end{pmatrix}.
\]

(c) On $X=C^\infty_{\mathrm{per}}([ -\pi,\pi])$, decide which of the sets
\[
\{f\in X:f(1)=b_1(f)\},\qquad \{f\in X:f'(1)=0\}
\]
are linear subspaces, and which of the maps
\[
T(f)=a_1(f)f,
\qquad
T(f)=\|f\|\sin x
\]
are linear.

(d) For a continuous Fourier series
\[
f(x)=\frac{a_0}{\sqrt2}+\sum_{n\ge1}a_n\cos(nx)+b_n\sin(nx),
\]
decide which of the assertions $a_0=0$, all $a_n=0$ for $n>0$, and all $b_n=0$ hold for every even $f$, every odd $f$, and every $f$ with no real zeros.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In part (a), only $B$ is diagonalizable over $\RR$.


::: pf-proof

Let $\omega=e^{2\pi i/5}$. For
\[
v=(1,\omega,\omega^2,\omega^3,\omega^4)^T
\]
one has $Av=\omega v$. Thus $A$ has a nonreal eigenvalue and cannot be
diagonalizable over $\RR$.

The matrix $B$ is real symmetric, since $B^T=B$. By the spectral theorem,
$B$ is diagonalizable over $\RR$.

The matrix $C$ is strictly upper triangular, hence nilpotent, and it is
nonzero. Therefore its only eigenvalue is $0$. If it were diagonalizable,
it would be similar to the zero diagonal matrix and hence would itself be
zero, a contradiction.

:::

:::

::: pf-step

In part (b), Loaf has a nonreal eigenvalue, while Boat has only real
eigenvalues.


::: pf-proof

The first and sixth coordinates of the Loaf matrix are zero direct
summands. On the remaining four coordinates its matrix is
\[
M=
\begin{pmatrix}
0&1&1&0\\
1&0&0&1\\
0&1&0&1\\
0&0&1&0
\end{pmatrix}.
\]
A determinant expansion gives
\[
\det(\lambda I-M)
=\lambda^4-2\lambda^2-2\lambda+1=:q(\lambda).
\]
For $s\geq0$,
\[
q(-s)=(s^2-1)^2+2s>0,
\]
so $q$ has no nonpositive real root. Moreover
$q(0)=1$, $q(1)=-2$, and $q(2)=5$, so it has at least two positive real
roots. Descartes' rule of signs gives at most two positive roots. Hence
exactly two of the four roots of $q$ are real, and the other two form a
nonreal conjugate pair. Thus Loaf has nonreal eigenvalues.

The Boat matrix is real symmetric, so all of its eigenvalues are real by
the spectral theorem.

:::

:::

::: pf-step

Both sets in part (c) are linear subspaces of $X$.


::: pf-proof

Evaluation $f\mapsto f(1)$, differentiation followed by evaluation
$f\mapsto f'(1)$, and the Fourier coefficient functional
$f\mapsto b_1(f)$ are linear. Therefore
\[
\{f:f(1)=b_1(f)\}
=\ker\bigl(f\mapsto f(1)-b_1(f)\bigr)
\]
and
\[
\{f:f'(1)=0\}
=\ker\bigl(f\mapsto f'(1)\bigr)
\]
are kernels of linear maps, hence linear subspaces.

:::

:::

::: pf-step

Neither map in part (c) is linear.


::: pf-proof

For $S(f)=a_1(f)f$, take $f(x)=\cos x$. Then $a_1(f)\neq0$, and
\[
S(2f)=a_1(2f)(2f)=4a_1(f)f=4S(f)\neq2S(f),
\]
so $S$ is not linear.

For $R(f)=\|f\|\sin x$, any nonzero $f$ gives
\[
R(-f)=\|-f\|\sin x=\|f\|\sin x=R(f)\neq-R(f).
\]
Thus $R$ is not linear.

:::

:::

::: pf-step

For every even $f$, all sine coefficients $b_n$ vanish, and neither
of the two assertions about the cosine coefficients is forced.


::: pf-proof

If $f$ is even, then $f(x)\sin(nx)$ is odd, so its integral over
$[-\pi,\pi]$ is zero and hence $b_n=0$ for every $n\geq1$.
The constant function $1$ is even and has $a_0\neq0$, while $\cos x$ is
even and has $a_1\neq0$. Therefore neither $a_0=0$ nor
$a_n=0$ for all $n>0$ holds for every even function.

:::

:::

::: pf-step

For every odd $f$, one has $a_0=0$ and $a_n=0$ for all $n>0$, while
the sine coefficients need not all vanish.


::: pf-proof

If $f$ is odd, then both $f(x)$ and $f(x)\cos(nx)$ are odd. Their
integrals over $[-\pi,\pi]$ vanish, giving $a_0=0$ and $a_n=0$ for every
$n>0$. The odd function $\sin x$ has $b_1\neq0$, so the sine coefficients
are not forced to vanish.

:::

:::

::: {.pf-step #s1-7}

For a continuous periodic function having no real zeros, none of
the three Fourier-vanishing assertions is forced.


::: pf-proof

The function
\[
f(x)=3+\cos x+\sin x
\]
satisfies
\[
f(x)\geq3-\sqrt2>0
\]
for every real $x$, so it has no real zeros. Its constant coefficient,
its first cosine coefficient, and its first sine coefficient are all
nonzero. Hence none of the three proposed vanishing conditions holds for
every nowhere-zero function.

:::

:::

::: {.pf-step #s1-8}

The complete answers are
\[
\boxed{
\begin{gathered}
\text{(a) only }B;\qquad
\text{(b) Loaf};\\
\text{(c) both sets are subspaces; both displayed maps are nonlinear};\\
\text{(d) even: only all }b_n=0;\quad
\text{odd: }a_0=0\text{ and all }a_n=0\ (n>0);\\
\text{no real zeros: none of the three conditions is forced.}
\end{gathered}}
\]


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref} establish the corresponding assertions in parts
(a)--(d).

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} records all requested decisions.

:::

:::

:::
