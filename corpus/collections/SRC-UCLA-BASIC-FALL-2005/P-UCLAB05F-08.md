---
schema: qual/card@1
id: P-UCLAB05F-08
kind: problem
title: Operator norm and completeness of the matrix space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Examination, September 2005 PDF. The source's displayed definition of `\|A\|` is typographically incomplete; the associated map $T_A$ and all three requested parts determine the standard operator norm used here.
---

::: {.problem}
For a real $n\times n$ matrix $A$, let $T_A:\mathbb R^n\to\mathbb R^n$ be the associated linear map.
Use the operator norm
\[
\|A\|=\sup_{\|x\|_2=1}\|T_Ax\|_2,
\]
where $\|\cdot\|_2$ is the Euclidean norm.

(a) Prove that
\[
\|A+B\|\leq\|A\|+\|B\|.
\]

(b) Use part (a) to check that the set $M$ of all real $n\times n$ matrices is a metric space for
\[
d(A,B)=\|B-A\|.
\]

(c) Prove that $M$ is complete for this metric.

Suggestion: the $(i,j)$ entry of $A$ is $\langle T_Ae_j,e_i\rangle$, where $e_i$ is the $i$th standard basis vector.
:::

::: {.solution}
<1>1. For every matrix $A$ and every $x\in\mathbb R^n$,
\[
\|T_Ax\|_2\le \|A\|\,\|x\|_2.
\]

::: {.proof}
If $x=0$, the inequality is immediate. If $x\ne0$, write
\[
u=\frac{x}{\|x\|_2}.
\]
Then $\|u\|_2=1$, so by the definition of the operator norm,
\[
\|T_Au\|_2\le\|A\|.
\]
Therefore
\[
\|T_Ax\|_2
=
\|x\|_2\|T_Au\|_2
\le
\|A\|\,\|x\|_2.
\]
:::

<1>2. For all real $n\times n$ matrices $A,B$,
\[
\boxed{\|A+B\|\le\|A\|+\|B\|}.
\]

::: {.proof}
If $\|x\|_2=1$, then
\[
\begin{aligned}
\|T_{A+B}x\|_2
&=
\|T_Ax+T_Bx\|_2\\
&\le
\|T_Ax\|_2+\|T_Bx\|_2\\
&\le
\|A\|+\|B\|
\end{aligned}
\]
by step <1>1. Taking the supremum over all unit vectors $x$ proves the inequality.
:::

<1>3. The operator norm satisfies
\[
\|A\|\ge0,\qquad
\|-A\|=\|A\|,
\]
and
\[
\|A\|=0\Longleftrightarrow A=0.
\]

::: {.proof}
Nonnegativity is immediate from the definition. Also
\[
\|-A\|
=
\sup_{\|x\|_2=1}\|-T_Ax\|_2
=
\|A\|.
\]
If $A=0$, then $\|A\|=0$. Conversely, if $\|A\|=0$, then step <1>1 gives
\[
\|T_Ax\|_2=0
\]
for every $x$, so $T_A=0$ and hence $A=0$.
:::

<1>4. The function
\[
d(A,B)=\|B-A\|
\]
is a metric on the vector space $M$ of real $n\times n$ matrices.

::: {.proof}
By step <1>3,
\[
d(A,B)\ge0,
\]
and
\[
d(A,B)=0
\Longleftrightarrow
B-A=0
\Longleftrightarrow
A=B.
\]
Also
\[
d(A,B)
=
\|B-A\|
=
\|A-B\|
=
d(B,A)
\]
by step <1>3. Finally, step <1>2 gives
\[
\begin{aligned}
d(A,C)
&=
\|C-A\|\\
&=
\|(C-B)+(B-A)\|\\
&\le
\|C-B\|+\|B-A\|\\
&=
d(B,C)+d(A,B).
\end{aligned}
\]
Thus all metric axioms hold.
:::

<1>5. If $(A_k)$ is Cauchy in the operator norm and
\[
A_k=(a_{ij}^{(k)}),
\]
then every scalar sequence
\[
(a_{ij}^{(k)})_{k\ge1}
\]
is Cauchy in $\mathbb R$.

::: {.proof}
For the standard basis vectors $e_i,e_j$,
\[
a_{ij}^{(k)}-a_{ij}^{(\ell)}
=
\langle T_{A_k-A_\ell}e_j,e_i\rangle.
\]
By Cauchy--Schwarz and step <1>1,
\[
\begin{aligned}
|a_{ij}^{(k)}-a_{ij}^{(\ell)}|
&\le
\|T_{A_k-A_\ell}e_j\|_2\|e_i\|_2\\
&\le
\|A_k-A_\ell\|.
\end{aligned}
\]
The right side tends to zero as $k,\ell\to\infty$, because $(A_k)$ is Cauchy.
:::

<1>6. There is a real matrix
\[
A=(a_{ij})
\]
such that
\[
a_{ij}^{(k)}\to a_{ij}
\]
for every $i,j$.

::: {.proof}
By step <1>5, each entry sequence is Cauchy in the complete space $\mathbb R$. Define $a_{ij}$ to be its limit. Since there are finitely many entries, these limits assemble into a real $n\times n$ matrix $A$.
:::

<1>7. One has
\[
\|A_k-A\|\longrightarrow0.
\]

::: {.proof}
Let
\[
C_k=A_k-A=(c_{ij}^{(k)}).
\]
For a unit vector $x=(x_1,\ldots,x_n)^t$,
\[
(C_kx)_i=\sum_{j=1}^n c_{ij}^{(k)}x_j.
\]
By Cauchy--Schwarz,
\[
|(C_kx)_i|^2
\le
\left(\sum_{j=1}^n|c_{ij}^{(k)}|^2\right)
\left(\sum_{j=1}^n|x_j|^2\right)
=
\sum_{j=1}^n|c_{ij}^{(k)}|^2.
\]
Summing over $i$ gives
\[
\|C_kx\|_2^2
\le
\sum_{i,j=1}^n|c_{ij}^{(k)}|^2.
\]
Hence
\[
\|C_k\|
\le
\left(\sum_{i,j=1}^n|c_{ij}^{(k)}|^2\right)^{1/2}.
\]
By step <1>6, every entry $c_{ij}^{(k)}$ tends to zero. Since the sum has only finitely many terms, its square root tends to zero. Therefore $\|A_k-A\|\to0$.
:::

<1>8. The metric space $(M,d)$ is complete.

::: {.proof}
Let $(A_k)$ be any Cauchy sequence in $M$. Step <1>6 constructs a matrix $A\in M$, and step <1>7 proves
\[
d(A_k,A)=\|A-A_k\|\to0.
\]
Thus every Cauchy sequence converges in $M$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), step <1>4 proves part (b), and step <1>8 proves part (c).
:::
:::
