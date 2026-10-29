---
schema: qual/card@1
id: P-UCLAB08F-11
kind: problem
title: Periodic finite-difference Poisson matrix solvability
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
  note: Checked against Problem 11 of the retained UCLA Basic Examination, Fall 2008.
---
::: {.problem}
Consider the periodic Poisson problem on $[0,1]$
\[
u''=f,\qquad u(0)=u(1),
\]
and its second-order finite-difference system
\[
A\mathbf u=\Delta x^2\mathbf f,
\]
where $\Delta x=1/n$ and
\[
A=\begin{pmatrix}
-2&1&0&\cdots&0&1\\
1&-2&1&0&\cdots&0\\
0&1&-2&1&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&1&-2&1\\
1&0&\cdots&0&1&-2
\end{pmatrix}.
\]

::: pf

::: pf-step

Show that $A$ is singular.

:::

::: pf-step

Determine the condition on $\mathbf f$ necessary and sufficient for a solution to exist.

:::

:::

:::

::: {.solution}
Let
\[
\mathbf 1=(1,\ldots,1)^t\in\RR^n.
\]

::: pf

::: {.pf-step #p2-s1}

One has
\[
A\mathbf 1=0.
\]

::: pf-proof

Every row of $A$ has exactly two entries equal to $1$ and one diagonal entry equal to $-2$, so every row sum is
\[
-2+1+1=0.
\]
Thus multiplying $A$ by the all-ones vector gives the zero vector.

:::

:::

::: {.pf-step #p2-s2}

The matrix $A$ is singular.

::: pf-proof

By step [](#p2-s1){.pf-ref},
\[
\mathbf1\ne0
\]
lies in $\ker A$. Hence $A$ has a nontrivial kernel and is singular.

:::

:::

::: {.pf-step #p2-s3}

For every $\mathbf v=(v_0,\ldots,v_{n-1})^t$,
\[
\mathbf v^tA\mathbf v
=
-\sum_{j=0}^{n-1}(v_{j+1}-v_j)^2,
\]
where indices are read modulo $n$, so $v_n=v_0$.

::: pf-proof

Expanding the quadratic form gives
\[
\mathbf v^tA\mathbf v
=
-2\sum_{j=0}^{n-1}v_j^2
+
2\sum_{j=0}^{n-1}v_jv_{j+1}.
\]
On the other hand,
\[
\begin{aligned}
\sum_{j=0}^{n-1}(v_{j+1}-v_j)^2
&=
\sum_{j=0}^{n-1}
\left(v_{j+1}^2-2v_jv_{j+1}+v_j^2\right)\\
&=
2\sum_{j=0}^{n-1}v_j^2
-
2\sum_{j=0}^{n-1}v_jv_{j+1}.
\end{aligned}
\]
Negating this identity gives the formula.

:::

:::

::: {.pf-step #p2-s4}

The nullspace of $A$ is exactly
\[
\ker A=\operatorname{span}\{\mathbf1\}.
\]

::: pf-proof

Step [](#p2-s1){.pf-ref} gives
\[
\operatorname{span}\{\mathbf1\}\subseteq\ker A.
\]
Conversely, let
\[
A\mathbf v=0.
\]
Then
\[
0
=
\mathbf v^tA\mathbf v
=
-\sum_{j=0}^{n-1}(v_{j+1}-v_j)^2
\]
by step [](#p2-s3){.pf-ref}. Every summand is nonnegative, so each difference vanishes:
\[
v_{j+1}=v_j
\]
for all $j$. Hence all coordinates of $\mathbf v$ are equal, so $\mathbf v$ is a scalar multiple of $\mathbf1$.

:::

:::

::: {.pf-step #p2-s5}

The range of $A$ is
\[
\operatorname{Range}A
=
\mathbf1^\perp
=
\left\{
\mathbf y\in\RR^n:
\sum_{j=0}^{n-1}y_j=0
\right\}.
\]

::: pf-proof

The matrix $A$ is symmetric. Hence
\[
\operatorname{Range}A
=
(\ker A)^\perp.
\]
By step [](#p2-s4){.pf-ref},
\[
\ker A=\operatorname{span}\{\mathbf1\}.
\]
Therefore
\[
\operatorname{Range}A
=
\mathbf1^\perp.
\]
The orthogonality condition
\[
\mathbf1^t\mathbf y=0
\]
is exactly
\[
\sum_{j=0}^{n-1}y_j=0.
\]

:::

:::

::: {.pf-step #p2-s6}

The finite-difference system
\[
A\mathbf u=\Delta x^2\mathbf f
\]
has a solution if and only if
\[
\boxed{
\sum_{j=0}^{n-1}f_j=0
}.
\]

::: pf-proof

Since
\[
\Delta x=\frac1n\ne0,
\]
the scalar factor $\Delta x^2$ does not affect membership in the subspace $\operatorname{Range}A$. Thus the system is solvable exactly when
\[
\mathbf f\in\operatorname{Range}A.
\]
By step [](#p2-s5){.pf-ref}, this is equivalent to
\[
\sum_{j=0}^{n-1}f_j=0.
\]

:::

:::

::: pf-qed

Step [](#p2-s2){.pf-ref} proves part step [](#p2-s1){.pf-ref}, and step [](#p2-s6){.pf-ref} gives the necessary and sufficient solvability condition in part step [](#p2-s2){.pf-ref}.

:::

:::

:::
