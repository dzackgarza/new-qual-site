---
schema: qual/card@1
id: P-APAS04C
kind: problem
title: Pseudo-inverse gives the minimal $2$-norm least-squares solution
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Linear Algebra
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $\hat{x}$ be a least squares solution to $Ax=b$, where $A\in M_{m,n}$ and $m\ge n$.
Let $A^\dagger$ be the pseudo-inverse of $A$.
Use the Singular Value Decomposition to show that $\tilde{x}=A^\dagger b$ is the min $2$-norm least squares solution to $Ax=b$, i.e., show

(a) $\tilde{x}$ is a least squares solution,

(b) if $\hat{x}$ is a least square solution then $\|\hat{x}\|_2\ge\|\tilde{x}\|_2$, and

(c) $\tilde{x}$ is unique.

(Notation: $M_{m,n}$ denotes the set of $m\times n$ complex matrices.)
:::

::: {.solution}
Let
\[
A=U\Sigma V^*
\]
be a singular value decomposition, where $U\in U(m)$, $V\in U(n)$, and, if $r=\operatorname{rank}A$,
\[
\Sigma=
\begin{pmatrix}
\operatorname{diag}(\sigma_1,\ldots,\sigma_r)&0\\
0&0
\end{pmatrix},
\qquad \sigma_i>0.
\]
Put
\[
c=U^*b,
\qquad
y=V^*x.
\]
Then $\|x\|_2=\|y\|_2$ and
\[
\|Ax-b\|_2=\|\Sigma y-c\|_2.
\]

<1>1. A vector $x=Vy$ is a least-squares solution if and only if
\[
y_i=\frac{c_i}{\sigma_i}\qquad(1\le i\le r),
\]
with $y_{r+1},\ldots,y_n$ arbitrary.
::: {.proof}
Since $U$ is unitary,
\[
\|Ax-b\|_2^2
=\|\Sigma y-c\|_2^2
=\sum_{i=1}^r|\sigma_i y_i-c_i|^2
+\sum_{i=r+1}^m|c_i|^2.
\]
The second sum is independent of $y$. Each term in the first sum is nonnegative and can be made zero uniquely by taking
\[
y_i=c_i/\sigma_i.
\]
The coordinates $y_{r+1},\ldots,y_n$ do not occur in the residual at all. Hence the displayed condition is exactly the set of least-squares solutions.
:::

<1>2. The pseudoinverse is
\[
A^\dagger=V\Sigma^\dagger U^*,
\]
where
\[
\Sigma^\dagger c
=
\left(\frac{c_1}{\sigma_1},\ldots,\frac{c_r}{\sigma_r},0,\ldots,0\right)^T.
\]
Thus
\[
\widetilde x=A^\dagger b
\]
is a least-squares solution.
::: {.proof}
By definition of the Moore--Penrose pseudoinverse of an SVD,
\[
\Sigma^\dagger
\]
is obtained by replacing each nonzero singular value $\sigma_i$ by $1/\sigma_i$ and transposing the rectangular diagonal matrix. Therefore
\[
V^*\widetilde x
=V^*V\Sigma^\dagger U^*b
=\Sigma^\dagger c.
\]
Its first $r$ coordinates are exactly $c_i/\sigma_i$, so <1>1 shows that $\widetilde x$ is a least-squares solution. This proves part (a).
:::

<1>3. If $\widehat x$ is any least-squares solution, then
\[
\|\widehat x\|_2^2
=\|\widetilde x\|_2^2
+\sum_{i=r+1}^n |\widehat y_i|^2,
\qquad
\widehat y=V^*\widehat x.
\]
In particular,
\[
\|\widehat x\|_2\ge \|\widetilde x\|_2.
\]
::: {.proof}
By <1>1, every least-squares solution has
\[
\widehat y_i=c_i/\sigma_i\qquad(1\le i\le r).
\]
By <1>2, the SVD coordinates of $\widetilde x$ have these same first $r$ entries and zero entries afterward. Since $V$ is unitary,
\[
\|\widehat x\|_2^2
=\|\widehat y\|_2^2
=\sum_{i=1}^r\left|\frac{c_i}{\sigma_i}\right|^2
 +\sum_{i=r+1}^n|\widehat y_i|^2,
\]
whereas
\[
\|\widetilde x\|_2^2
=\sum_{i=1}^r\left|\frac{c_i}{\sigma_i}\right|^2.
\]
This proves part (b).
:::

<1>4. The minimum-$2$-norm least-squares solution is unique and equals $A^\dagger b$.
::: {.proof}
Equality in <1>3 holds if and only if
\[
\widehat y_{r+1}=\cdots=\widehat y_n=0.
\]
Together with the forced first $r$ coordinates from <1>1, this determines $\widehat y$ uniquely as $\Sigma^\dagger c$. Therefore
\[
\widehat x=V\widehat y=V\Sigma^\dagger U^*b=A^\dagger b=\widetilde x.
\]
Hence $\widetilde x$ is the unique least-squares solution of minimum Euclidean norm. This proves part (c).
:::
:::
