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
\[
\|BA^{-1}x\|\le \|x\|\qquad\text{for every }x\in\mathbb R^n.
\]

(a) For $x,y\in\mathbb R^n$, show that
\[
z\longmapsto \langle y,B^zA^{-z}x\rangle
\]
admits an analytic continuation from $0<z<1$ to the whole complex plane.

(b) Show that
\[
\|B^\theta A^{-\theta}x\|\le \|x\|
\]
for every $0\le\theta\le1$ and every $x\in\mathbb R^n$.
:::

::: {.solution}
For a positive-definite real symmetric matrix $C$, choose an orthogonal diagonalization
\[
C=Q\operatorname{diag}(\lambda_1,\dots,\lambda_n)Q^T,
\qquad
\lambda_j>0,
\]
and for $z\in\mathbb C$ define
\[
C^z
\coloneqq
Q\operatorname{diag}(e^{z\log\lambda_1},\dots,e^{z\log\lambda_n})Q^T.
\]

<1>1. For every positive-definite real symmetric $C$, the matrix-valued map
\[
z\longmapsto C^z
\]
is entire on $\mathbb C$.

::: {.proof}
Each entry of $C^z$ is a finite linear combination of the entire functions
\[
z\longmapsto e^{z\log\lambda_j}.
\]
Therefore every matrix entry is entire.
:::

<1>2. For fixed $x,y\in\mathbb R^n$, the function
\[
F_{x,y}(z)
\coloneqq
y^T B^zA^{-z}x
\]
is entire on $\mathbb C$ and agrees with
\[
\langle y,B^zA^{-z}x\rangle
\]
for real $z$.

::: {.proof}
By step <1>1, every entry of $B^z$ and $A^{-z}$ is entire. Matrix multiplication involves only finite sums and products, so every entry of $B^zA^{-z}$ is entire. Multiplication on the left by the fixed row vector $y^T$ and on the right by the fixed column vector $x$ preserves holomorphy.

For real $z$, all matrices are real, so $y^T B^zA^{-z}x$ is the usual Euclidean inner product.
:::

<1>3. This proves part (a).

::: {.proof}
Step <1>2 gives an entire function whose restriction to $0<z<1$ is the function in the problem.
:::

<1>4. The hypothesis
\[
\|BA^{-1}x\|\le\|x\|
\qquad
(x\in\mathbb R^n)
\]
also holds for every $x\in\mathbb C^n$ with the standard Hermitian norm.

::: {.proof}
Write
\[
x=u+iv,
\qquad
u,v\in\mathbb R^n.
\]
Since $BA^{-1}$ is a real matrix,
\[
BA^{-1}x
=
BA^{-1}u+iBA^{-1}v.
\]
Hence
\[
\begin{aligned}
\|BA^{-1}x\|^2
&=
\|BA^{-1}u\|^2
+
\|BA^{-1}v\|^2\\
&\le
\|u\|^2+\|v\|^2\\
&=
\|x\|^2.
\end{aligned}
\]
:::

<1>5. For every real $t$,
\[
\|B^{it}\|_{\mathrm{op}}
=
\|A^{-it}\|_{\mathrm{op}}
=1
\]
on $\mathbb C^n$.

::: {.proof}
In the spectral representation of $B^{it}$, the eigenvalues are
\[
e^{it\log\lambda_j},
\]
all of modulus $1$. Since the diagonalizing matrix is real orthogonal and hence unitary on $\mathbb C^n$, $B^{it}$ is unitary. The same argument applies to $A^{-it}$.
:::

<1>6. If
\[
\operatorname{Re}z=0,
\]
then
\[
|F_{x,y}(z)|
\le
\|x\|\,\|y\|.
\]

::: {.proof}
Write $z=it$. By Cauchy--Schwarz and step <1>5,
\[
\begin{aligned}
|F_{x,y}(it)|
&=
|y^T B^{it}A^{-it}x|\\
&\le
\|y\|\,\|B^{it}A^{-it}x\|\\
&\le
\|y\|\,\|x\|.
\end{aligned}
\]
Here $y$ is real, so $y^T$ agrees with its Hermitian transpose.
:::

<1>7. If
\[
\operatorname{Re}z=1,
\]
then
\[
|F_{x,y}(z)|
\le
\|x\|\,\|y\|.
\]

::: {.proof}
Write $z=1+it$. Since powers of the same matrix commute,
\[
B^{1+it}A^{-1-it}
=
B^{it}(BA^{-1})A^{-it}.
\]
By steps <1>4 and <1>5,
\[
\|B^{it}(BA^{-1})A^{-it}\|_{\mathrm{op}}
\le1.
\]
Therefore Cauchy--Schwarz gives
\[
|F_{x,y}(1+it)|
\le
\|x\|\,\|y\|.
\]
:::

<1>8. The function $F_{x,y}$ is bounded on the closed strip
\[
S
\coloneqq
\{z\in\mathbb C:0\le\operatorname{Re}z\le1\}.
\]

::: {.proof}
After diagonalizing $A$ and $B$, each entry of $B^zA^{-z}$ is a finite sum of terms of the form
\[
c\,\lambda^z\mu^{-z}
\]
with $\lambda,\mu>0$. On the strip,
\[
|\lambda^z\mu^{-z}|
=
\lambda^{\operatorname{Re}z}
\mu^{-\operatorname{Re}z},
\]
which is bounded because $0\le\operatorname{Re}z\le1$. Hence every matrix entry, and therefore $F_{x,y}$, is bounded on $S$.
:::

<1>9. For every $0\le\theta\le1$,
\[
|F_{x,y}(\theta)|
\le
\|x\|\,\|y\|.
\]

::: {.proof}
Steps <1>6 and <1>7 give the bound on both boundary lines of the strip, and step <1>8 supplies the boundedness hypothesis. Hadamard's three-lines theorem therefore gives the same bound throughout the strip, in particular on the real segment $0\le\theta\le1$.
:::

<1>10. For every $0\le\theta\le1$ and $x\in\mathbb R^n$,
\[
\boxed{
\|B^\theta A^{-\theta}x\|
\le
\|x\|
}.
\]

::: {.proof}
The vector
\[
v=B^\theta A^{-\theta}x
\]
is real. Hence
\[
\|v\|
=
\sup_{\substack{y\in\mathbb R^n\\\|y\|=1}}
|\langle y,v\rangle|.
\]
By step <1>9, every term in this supremum is at most $\|x\|$. Thus $\|v\|\le\|x\|$.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), and step <1>10 proves part (b).
:::
:::
