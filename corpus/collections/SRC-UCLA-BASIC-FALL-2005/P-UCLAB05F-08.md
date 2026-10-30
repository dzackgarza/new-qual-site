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
For a real $n\times n$ matrix $A$, let $T_A:\RR^n\to\RR^n$ be the associated linear map.
Use the operator norm
$$
\norm{A}=\sup_{\norm{x}_2=1}\norm{T_Ax}_2,
$$
where $\norm{\cdot}_2$ is the Euclidean norm.

(a) Prove that
$$
\norm{A+B}\leq\norm{A}+\norm{B}.
$$

(b) Use part (a) to check that the set $M$ of all real $n\times n$ matrices is a metric space for
$$
d(A,B)=\norm{B-A}.
$$

(c) Prove that $M$ is complete for this metric.

Suggestion: the $(i,j)$ entry of $A$ is $\langle T_Ae_j,e_i\rangle$, where $e_i$ is the $i$th standard basis vector.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every matrix $A$ and every $x\in\RR^n$,
$$
\norm{T_Ax}_2\le \norm{A}\,\norm{x}_2.
$$


::: pf-proof

If $x=0$, the inequality is immediate. If $x\ne0$, write
$$
u=\frac{x}{\norm{x}_2}.
$$
Then $\norm{u}_2=1$, so by the definition of the operator norm,
$$
\norm{T_Au}_2\le\norm{A}.
$$
Therefore
$$
\norm{T_Ax}_2
=
\norm{x}_2\norm{T_Au}_2
\le
\norm{A}\,\norm{x}_2.
$$

:::

:::

::: {.pf-step #s1-2}

For all real $n\times n$ matrices $A,B$,
$$
\boxed{\norm{A+B}\le\norm{A}+\norm{B}}.
$$


::: pf-proof

If $\norm{x}_2=1$, then
$$
\begin{aligned}
\norm{T_{A+B}x}_2
&=
\norm{T_Ax+T_Bx}_2\\
&\le
\norm{T_Ax}_2+\norm{T_Bx}_2\\
&\le
\norm{A}+\norm{B}
\end{aligned}
$$
by step [](#s1-1){.pf-ref}. Taking the supremum over all unit vectors $x$ proves the inequality.

:::

:::

::: {.pf-step #s1-3}

The operator norm satisfies
$$
\norm{A}\ge0,\qquad
\norm{-A}=\norm{A},
$$
and
$$
\norm{A}=0\Longleftrightarrow A=0.
$$


::: pf-proof

Nonnegativity is immediate from the definition. Also
$$
\norm{-A}
=
\sup_{\norm{x}_2=1}\norm{-T_Ax}_2
=
\norm{A}.
$$
If $A=0$, then $\norm{A}=0$. Conversely, if $\norm{A}=0$, then step [](#s1-1){.pf-ref} gives
$$
\norm{T_Ax}_2=0
$$
for every $x$, so $T_A=0$ and hence $A=0$.

:::

:::

::: {.pf-step #s1-4}

The function
$$
d(A,B)=\norm{B-A}
$$
is a metric on the vector space $M$ of real $n\times n$ matrices.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
d(A,B)\ge0,
$$
and
$$
d(A,B)=0
\Longleftrightarrow
B-A=0
\Longleftrightarrow
A=B.
$$
Also
$$
d(A,B)
=
\norm{B-A}
=
\norm{A-B}
=
d(B,A)
$$
by step [](#s1-3){.pf-ref}. Finally, step [](#s1-2){.pf-ref} gives
$$
\begin{aligned}
d(A,C)
&=
\norm{C-A}\\
&=
\norm{(C-B)+(B-A)}\\
&\le
\norm{C-B}+\norm{B-A}\\
&=
d(B,C)+d(A,B).
\end{aligned}
$$
Thus all metric axioms hold.

:::

:::

::: {.pf-step #s1-5}

If $(A_k)$ is Cauchy in the operator norm and
$$
A_k=(a_{ij}^{(k)}),
$$
then every scalar sequence
$$
(a_{ij}^{(k)})_{k\ge1}
$$
is Cauchy in $\RR$.


::: pf-proof

For the standard basis vectors $e_i,e_j$,
$$
a_{ij}^{(k)}-a_{ij}^{(\ell)}
=
\langle T_{A_k-A_\ell}e_j,e_i\rangle.
$$
By Cauchy--Schwarz and step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\abs{a_{ij}^{(k)}-a_{ij}^{(\ell)}}
&\le
\norm{T_{A_k-A_\ell}e_j}_2\norm{e_i}_2\\
&\le
\norm{A_k-A_\ell}.
\end{aligned}
$$
The right side tends to zero as $k,\ell\to\infty$, because $(A_k)$ is Cauchy.

:::

:::

::: {.pf-step #s1-6}

There is a real matrix
$$
A=(a_{ij})
$$
such that
$$
a_{ij}^{(k)}\to a_{ij}
$$
for every $i,j$.


::: pf-proof

By step [](#s1-5){.pf-ref}, each entry sequence is Cauchy in the complete space $\RR$. Define $a_{ij}$ to be its limit. Since there are finitely many entries, these limits assemble into a real $n\times n$ matrix $A$.

:::

:::

::: {.pf-step #s1-7}

One has
$$
\norm{A_k-A}\longrightarrow0.
$$


::: pf-proof

Let
$$
C_k=A_k-A=(c_{ij}^{(k)}).
$$
For a unit vector $x=(x_1,\ldots,x_n)^t$,
$$
(C_kx)_i=\sum_{j=1}^n c_{ij}^{(k)}x_j.
$$
By Cauchy--Schwarz,
$$
\abs{(C_kx)_i}^2
\le
\left(\sum_{j=1}^n\abs{c_{ij}^{(k)}}^2\right)
\left(\sum_{j=1}^n\abs{x_j}^2\right)
=
\sum_{j=1}^n\abs{c_{ij}^{(k)}}^2.
$$
Summing over $i$ gives
$$
\norm{C_kx}_2^2
\le
\sum_{i,j=1}^n\abs{c_{ij}^{(k)}}^2.
$$
Hence
$$
\norm{C_k}
\le
\left(\sum_{i,j=1}^n\abs{c_{ij}^{(k)}}^2\right)^{1/2}.
$$
By step [](#s1-6){.pf-ref}, every entry $c_{ij}^{(k)}$ tends to zero. Since the sum has only finitely many terms, its square root tends to zero. Therefore $\norm{A_k-A}\to0$.

:::

:::

::: {.pf-step #s1-8}

The metric space $(M,d)$ is complete.


::: pf-proof

Let $(A_k)$ be any Cauchy sequence in $M$. Step [](#s1-6){.pf-ref} constructs a matrix $A\in M$, and step [](#s1-7){.pf-ref} proves
$$
d(A_k,A)=\norm{A-A_k}\to0.
$$
Thus every Cauchy sequence converges in $M$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), step [](#s1-4){.pf-ref} proves part (b), and step [](#s1-8){.pf-ref} proves part (c).

:::

:::

:::
