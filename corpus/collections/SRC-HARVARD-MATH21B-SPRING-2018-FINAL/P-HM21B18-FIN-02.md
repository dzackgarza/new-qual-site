---
schema: qual/card@1
id: P-HM21B18-FIN-02
kind: problem
title: Matrix properties and differential-equation graph matching
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The four candidate graphs in part (c) are image-only in the retained extraction; their labels A--D are preserved without reconstructing the drawings.
---

::: {.problem}
(a) For
$$
A=\begin{pmatrix}
0&1&1&1\\
1&0&1&1\\
1&1&0&1\\
1&1&1&0
\end{pmatrix},
$$
decide which of the following properties hold: projection, reflection, orthogonal, invertible, symmetric, diagonalizable over $\RR$.

(b) Decide which of the following hold for every noninvertible $2\times2$ real matrix $A$: $\operatorname{tr}A=0$; $\det A=0$; $\operatorname{tr}A$ is an eigenvalue; $\det A$ is an eigenvalue; the columns are parallel; the rows are parallel.

(c) Match the equations
$$
f''=1,\qquad f'=1,\qquad f'=-f+1,\qquad f'''=-f'
$$
to the source graphs A--D. Graph A is a decreasing convex curve approaching
a positive horizontal asymptote; graph B is a nonconstant periodic sinusoidal
curve; graph C is an increasing straight line; graph D is an increasing,
upward-convex parabolic arc.
:::

::: {.solution}

Let $\mathbf 1=(1,1,1,1)^T$.

::: pf

::: {.pf-step #s1-1}

In part (a), $A$ is invertible, symmetric, and diagonalizable over
$\RR$, and it is not a projection, reflection, or orthogonal matrix.


::: pf-proof

Write $A=J-I$, where $J$ is the $4\times4$ all-ones matrix. Since
$J\mathbf 1=4\mathbf 1$,
$$
A\mathbf 1=3\mathbf 1.
$$
If $v\perp\mathbf 1$, then the sum of the coordinates of $v$ is zero, so
$Jv=0$ and therefore $Av=-v$. Thus $A$ has eigenvalue $3$ on
$\operatorname{span}\{\mathbf 1\}$ and eigenvalue $-1$ on the
three-dimensional space $\mathbf 1^\perp$. Hence $A$ is invertible and
diagonalizable over $\RR$. It is symmetric because $A^T=A$.

A projection can have only eigenvalues $0$ and $1$, while $A$ has
eigenvalue $3$, so $A$ is not a projection. A reflection satisfies
$R^2=I$, whereas $A^2\mathbf 1=9\mathbf 1\neq\mathbf 1$, so $A$ is
not a reflection. Finally,
$$
Ae_1=(0,1,1,1)^T
$$
has norm $\sqrt3\neq1=\norm{e_1}$, so $A$ is not orthogonal.

:::

:::

::: {.pf-step #s1-2}

In part (b), every listed assertion is true except
$\operatorname{tr}A=0$.


::: pf-proof

For a noninvertible $2\times2$ matrix, $\det A=0$. Its characteristic
polynomial is therefore
$$
p_A(\lambda)
=\lambda^2-(\operatorname{tr}A)\lambda
=\lambda(\lambda-\operatorname{tr}A).
$$
Consequently both $0=\det A$ and $\operatorname{tr}A$ are eigenvalues.
Also $\operatorname{rank}A\leq1$, so its two columns are linearly
dependent, hence parallel; applying the same argument to $A^T$ shows that
its two rows are parallel. The trace need not vanish: for
$$
A=\begin{pmatrix}1&0\\0&0\end{pmatrix}
$$
one has $\det A=0$ but $\operatorname{tr}A=1$.

:::

:::

::: {.pf-step #s1-3}

In part (c), $f''=1$ matches graph D.


::: pf-proof

Integrating twice gives
$$
f(t)=\frac12t^2+ct+d.
$$
Every such solution is a parabola opening upward, which is the qualitative
shape of graph D.

:::

:::

::: pf-step

In part (c), $f'=1$ matches graph C.


::: pf-proof

Integrating gives $f(t)=t+c$, an increasing straight line of slope $1$.
This is graph C.

:::

:::

::: pf-step

In part (c), $f'=-f+1$ matches graph A.


::: pf-proof

The equation is $f'+f=1$, whose general solution is
$$
f(t)=1+Ce^{-t}.
$$
For $C>0$ this is decreasing and convex while approaching the horizontal
asymptote $f=1$, exactly as graph A does.

:::

:::

::: {.pf-step #s1-6}

In part (c), $f'''=-f'$ matches graph B.


::: pf-proof

The equation is
$$
(f''+f)'=0,
$$
so $f''+f=C$ for some constant $C$. Hence
$$
f(t)=C+a\cos t+b\sin t.
$$
Nonconstant solutions are periodic sinusoidal curves about the level $C$,
which is the qualitative shape of graph B.

:::

:::

::: {.pf-step #s1-7}

The complete answers are
$$
\boxed{
\begin{aligned}
\text{(a)}&\quad
\text{invertible, symmetric, diagonalizable},\\
\text{(b)}&\quad
\det A=0,\quad
\operatorname{tr}A\text{ is an eigenvalue},\quad
\det A\text{ is an eigenvalue},\\
&\qquad
\text{the columns are parallel, and the rows are parallel},\\
\text{(c)}&\quad
f''=1\mapsto D,\quad
f'=1\mapsto C,\quad
f'=-f+1\mapsto A,\quad
f'''=-f'\mapsto B.
\end{aligned}}
$$


::: pf-proof

Part (a) is established by step [](#s1-1){.pf-ref}, part (b) by step [](#s1-2){.pf-ref}, and the four
matches in part (c) by steps [](#s1-3){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} records all requested selections and matches.

:::

:::

:::
