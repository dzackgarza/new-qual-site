---
schema: qual/card@1
id: P-UCLARA13S-08
kind: problem
title: Three-lines interpolation for positive definite matrices
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $A$ and $B$ be positive-definite real symmetric $n\times n$ matrices such that
$$
\norm{BA^{-1}x}\le \norm{x}\qquad\text{for every }x\in\RR^n.
$$

(a) For $x,y\in\RR^n$, show that
$$
z\longmapsto \langle y,B^zA^{-z}x\rangle
$$
admits an analytic continuation from $0<z<1$ to the whole complex plane.

(b) Show that
$$
\norm{B^\theta A^{-\theta}x}\le \norm{x}
$$
for every $0\le\theta\le1$ and every $x\in\RR^n$.
:::

::: {.solution}

For a positive-definite real symmetric matrix $C$, choose an orthogonal diagonalization
$$
C=Q\operatorname{diag}(\lambda_1,\dots,\lambda_n)Q^T,
\qquad
\lambda_j>0,
$$
and for $z\in\CC$ define
$$
C^z
\coloneqq
Q\operatorname{diag}(e^{z\log\lambda_1},\dots,e^{z\log\lambda_n})Q^T.
$$

::: pf

::: {.pf-step #s1-1}

For every positive-definite real symmetric $C$, the matrix-valued map
$$
z\longmapsto C^z
$$
is entire on $\CC$.


::: pf-proof

Each entry of $C^z$ is a finite linear combination of the entire functions
$$
z\longmapsto e^{z\log\lambda_j}.
$$
Therefore every matrix entry is entire.

:::

:::

::: {.pf-step #s1-2}

For fixed $x,y\in\RR^n$, the function
$$
F_{x,y}(z)
\coloneqq
y^T B^zA^{-z}x
$$
is entire on $\CC$ and agrees with
$$
\langle y,B^zA^{-z}x\rangle
$$
for real $z$.


::: pf-proof

By step [](#s1-1){.pf-ref}, every entry of $B^z$ and $A^{-z}$ is entire. Matrix multiplication involves only finite sums and products, so every entry of $B^zA^{-z}$ is entire. Multiplication on the left by the fixed row vector $y^T$ and on the right by the fixed column vector $x$ preserves holomorphy.

For real $z$, all matrices are real, so $y^T B^zA^{-z}x$ is the usual Euclidean inner product.

:::

:::

::: {.pf-step #s1-3}

This proves part (a).


::: pf-proof

Step [](#s1-2){.pf-ref} gives an entire function whose restriction to $0<z<1$ is the function in the problem.

:::

:::

::: {.pf-step #s1-4}

The hypothesis
$$
\norm{BA^{-1}x}\le\norm{x}
\qquad
(x\in\RR^n)
$$
also holds for every $x\in\CC^n$ with the standard Hermitian norm.


::: pf-proof

Write
$$
x=u+iv,
\qquad
u,v\in\RR^n.
$$
Since $BA^{-1}$ is a real matrix,
$$
BA^{-1}x
=
BA^{-1}u+iBA^{-1}v.
$$
Hence
$$
\begin{aligned}
\norm{BA^{-1}x}^2
&=
\norm{BA^{-1}u}^2
+
\norm{BA^{-1}v}^2\\
&\le
\norm{u}^2+\norm{v}^2\\
&=
\norm{x}^2.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

For every real $t$,
$$
\norm{B^{it}}_{\mathrm{op}}
=
\norm{A^{-it}}_{\mathrm{op}}
=1
$$
on $\CC^n$.


::: pf-proof

In the spectral representation of $B^{it}$, the eigenvalues are
$$
e^{it\log\lambda_j},
$$
all of modulus $1$. Since the diagonalizing matrix is real orthogonal and hence unitary on $\CC^n$, $B^{it}$ is unitary. The same argument applies to $A^{-it}$.

:::

:::

::: {.pf-step #s1-6}

If
$$
\operatorname{Re}z=0,
$$
then
$$
\abs{F_{x,y}(z)}
\le
\norm{x}\,\norm{y}.
$$


::: pf-proof

Write $z=it$. By Cauchy--Schwarz and step [](#s1-5){.pf-ref},
$$
\begin{aligned}
\abs{F_{x,y}(it)}
&=
\abs{y^T B^{it}A^{-it}x}\\
&\le
\norm{y}\,\norm{B^{it}A^{-it}x}\\
&\le
\norm{y}\,\norm{x}.
\end{aligned}
$$
Here $y$ is real, so $y^T$ agrees with its Hermitian transpose.

:::

:::

::: {.pf-step #s1-7}

If
$$
\operatorname{Re}z=1,
$$
then
$$
\abs{F_{x,y}(z)}
\le
\norm{x}\,\norm{y}.
$$


::: pf-proof

Write $z=1+it$. Since powers of the same matrix commute,
$$
B^{1+it}A^{-1-it}
=
B^{it}(BA^{-1})A^{-it}.
$$
By steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref},
$$
\norm{B^{it}(BA^{-1})A^{-it}}_{\mathrm{op}}
\le1.
$$
Therefore Cauchy--Schwarz gives
$$
\abs{F_{x,y}(1+it)}
\le
\norm{x}\,\norm{y}.
$$

:::

:::

::: {.pf-step #s1-8}

The function $F_{x,y}$ is bounded on the closed strip
$$
S
\coloneqq
\{z\in\CC:0\le\operatorname{Re}z\le1\}.
$$


::: pf-proof

After diagonalizing $A$ and $B$, each entry of $B^zA^{-z}$ is a finite sum of terms of the form
$$
c\,\lambda^z\mu^{-z}
$$
with $\lambda,\mu>0$. On the strip,
$$
\abs{\lambda^z\mu^{-z}}
=
\lambda^{\operatorname{Re}z}
\mu^{-\operatorname{Re}z},
$$
which is bounded because $0\le\operatorname{Re}z\le1$. Hence every matrix entry, and therefore $F_{x,y}$, is bounded on $S$.

:::

:::

::: {.pf-step #s1-9}

For every $0\le\theta\le1$,
$$
\abs{F_{x,y}(\theta)}
\le
\norm{x}\,\norm{y}.
$$


::: pf-proof

Steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref} give the bound on both boundary lines of the strip, and step [](#s1-8){.pf-ref} supplies the boundedness hypothesis. Hadamard's three-lines theorem therefore gives the same bound throughout the strip, in particular on the real segment $0\le\theta\le1$.

:::

:::

::: {.pf-step #s1-10}

For every $0\le\theta\le1$ and $x\in\RR^n$,
$$
\boxed{
\norm{B^\theta A^{-\theta}x}
\le
\norm{x}
}.
$$


::: pf-proof

The vector
$$
v=B^\theta A^{-\theta}x
$$
is real. Hence
$$
\norm{v}
=
\sup_{\substack{y\in\RR^n\\\norm{y}=1}}
\abs{\langle y,v\rangle}.
$$
By step [](#s1-9){.pf-ref}, every term in this supremum is at most $\norm{x}$. Thus $\norm{v}\le\norm{x}$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-10){.pf-ref} proves part (b).

:::

:::

:::
