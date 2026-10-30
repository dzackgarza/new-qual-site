---
schema: qual/card@1
id: P-KSRING17-075
kind: problem
title: Equivalent characterizations of integral elements
classification:
  areas: [algebra]
  topics:
  - Integral Elements
  - Finitely Generated Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 75 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Recall that if $R \subseteq S$ is an inclusion of commutative rings (with the same identity) then an element $s \in S$ is integral over R if s satisfies some monic polynomial with coefficients in R. Prove the equivalence of the following statements.

(i) s is integral over R.

(ii) $R [ s ]$ is finitely generated as an R-module.

(iii) There exists a faithful $R [ s ]$ module which is finitely generated as an R-module.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume $s$ is integral over $R$.
Then there exist
$$
n\ge1
$$
and coefficients
$$
a_0,\ldots,a_{n-1}\in R
$$
such that
$$
s^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0=0.
$$


::: pf-proof

This is exactly the definition of integrality over $R$.

:::

:::

::: {.pf-step #s1-2}

Under the hypothesis of step [](#s1-1){.pf-ref}, every power
$$
s^m
$$
with
$$
m\ge n
$$
is an $R$-linear combination of
$$
1,s,\ldots,s^{n-1}.
$$


::: pf-proof

The relation from step [](#s1-1){.pf-ref} gives
$$
s^n
=
-a_{n-1}s^{n-1}
-\cdots
-a_1s
-a_0.
$$
Thus the claim holds for
$$
m=n.
$$

Assume it holds for all powers from $n$ through $m$.
Multiplying an $R$-linear expression for
$$
s^m
$$
by $s$ expresses
$$
s^{m+1}
$$
as an $R$-linear combination of
$$
s,s^2,\ldots,s^n.
$$
Replace the $s^n$ term using the monic relation from step [](#s1-1){.pf-ref}.
This yields an $R$-linear combination of
$$
1,s,\ldots,s^{n-1}.
$$
Induction proves the assertion.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
R[s]
\text{ is finitely generated as an }R\text{-module}.
}
$$


::: pf-proof

Every element of
$$
R[s]
$$
is a polynomial in $s$ with coefficients in $R$.
By step [](#s1-2){.pf-ref}, all powers
$$
s^m
$$
with
$$
m\ge n
$$
reduce to $R$-linear combinations of
$$
1,s,\ldots,s^{n-1}.
$$
Hence
$$
R[s]
=
R\cdot1
+R\cdot s
+\cdots
+R\cdot s^{n-1}.
$$
Thus (i) implies (ii).

:::

:::

::: {.pf-step #s1-4}

Assume
$$
R[s]
$$
is finitely generated as an $R$-module.
Then there exists a faithful $R[s]$-module finitely generated over $R$.


::: pf-proof

Take
$$
M
\coloneqq
R[s]
$$
with its regular left $R[s]$-module structure.
By hypothesis, $M$ is finitely generated as an $R$-module.

It is faithful as an $R[s]$-module:
if
$$
t\in R[s]
$$
annihilates $M$, then in particular
$$
t\cdot1=0,
$$
so
$$
t=0.
$$
Therefore (ii) implies (iii).

:::

:::

::: pf-step

Assume now that there exists a faithful $R[s]$-module
$$
M
$$
that is finitely generated as an $R$-module.
Choose $R$-module generators
$$
m_1,\ldots,m_n
$$
of $M$.


::: pf-proof

This is exactly the finite-generation hypothesis in (iii).

:::

:::

::: {.pf-step #s1-6}

For each
$$
j=1,\ldots,n,
$$
there exist coefficients
$$
a_{1j},\ldots,a_{nj}\in R
$$
such that
$$
s m_j
=
\sum_{i=1}^{n}a_{ij}m_i.
$$


::: pf-proof

Because $M$ is an $R[s]$-module,
$$
sm_j\in M.
$$
Because
$$
m_1,\ldots,m_n
$$
generate $M$ as an $R$-module, $sm_j$ has an $R$-linear expression in these generators.

:::

:::

::: {.pf-step #s1-7}

Let
$$
A
\coloneqq
(a_{ij})
\in
M_n(R)
$$
and let
$$
\mathbf m
\coloneqq
\begin{pmatrix}
m_1\\
\vdots\\
m_n
\end{pmatrix}.
$$
Then
$$
(sI_n-A)\mathbf m=0.
$$


::: pf-proof

The $j$th relation from step [](#s1-6){.pf-ref} is exactly the corresponding coordinate of the matrix equation
$$
(sI_n-A)\mathbf m=0,
$$
after choosing the convention that the $j$th column of $A$ records the coefficients of $sm_j$.
Equivalently, one may transpose the coefficient matrix; the determinant below is unchanged.

:::

:::

::: {.pf-step #s1-8}

Multiplying the equation in step [](#s1-7){.pf-ref} by the adjugate matrix gives
$$
\det(sI_n-A)\,m_j
=
0
$$
for every
$$
j=1,\ldots,n.
$$


::: pf-proof

Over the commutative ring
$$
R[s],
$$
the adjugate identity gives
$$
\operatorname{adj}(sI_n-A)(sI_n-A)
=
\det(sI_n-A)I_n.
$$
Apply this matrix to $\mathbf m$ and use step [](#s1-7){.pf-ref}:
$$
\det(sI_n-A)\mathbf m
=
0.
$$
Thus each coordinate satisfies the displayed annihilation relation.

:::

:::

::: {.pf-step #s1-9}

The element
$$
\det(sI_n-A)
\in
R[s]
$$
annihilates all of $M$.


::: pf-proof

By step [](#s1-8){.pf-ref}, it annihilates each $R$-module generator
$$
m_j.
$$
Since multiplication by an element of $R[s]$ is $R$-linear, it therefore annihilates every $R$-linear combination of the generators, hence all of $M$.

:::

:::

::: {.pf-step #s1-10}

Because $M$ is faithful as an $R[s]$-module,
$$
\det(sI_n-A)=0
$$
in $R[s]$.


::: pf-proof

Faithfulness means that the annihilator of $M$ in $R[s]$ is zero.
Step [](#s1-9){.pf-ref} shows
$$
\det(sI_n-A)
$$
lies in that annihilator.
Hence it is zero.

:::

:::

::: {.pf-step #s1-11}

The expression
$$
\det(TI_n-A)
$$
is a monic polynomial in
$$
R[T]
$$
of degree $n$.


::: pf-proof

In the determinant expansion, the unique degree-$n$ term is obtained by taking the diagonal term
$$
T
$$
from each row and column.
Its coefficient is $1$.
Every other term has smaller degree.
Therefore
$$
\chi_A(T)
\coloneqq
\det(TI_n-A)
$$
is monic of degree $n$ with coefficients in $R$.

:::

:::

::: {.pf-step #s1-12}

The element $s$ satisfies the monic polynomial
$$
\chi_A(T)
\in
R[T].
$$


::: pf-proof

By step [](#s1-10){.pf-ref},
$$
\det(sI_n-A)=0.
$$
By step [](#s1-11){.pf-ref},
$$
\chi_A(T)
=
\det(TI_n-A)
$$
is a monic polynomial over $R$.
Thus
$$
\chi_A(s)=0.
$$
Hence $s$ is integral over $R$.
Therefore (iii) implies (i).

:::

:::

::: {.pf-step #s1-13}

Consequently,
$$
\boxed{
\text{(i)}
\iff
\text{(ii)}
\iff
\text{(iii)}.
}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} proves
$$
\text{(i)}\implies\text{(ii)}.
$$
Step [](#s1-4){.pf-ref} proves
$$
\text{(ii)}\implies\text{(iii)}.
$$
Step [](#s1-12){.pf-ref} proves
$$
\text{(iii)}\implies\text{(i)}.
$$

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} establishes the equivalence of all three statements.

:::

:::

:::
