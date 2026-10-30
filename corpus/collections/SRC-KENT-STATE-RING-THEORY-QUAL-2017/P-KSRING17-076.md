---
schema: qual/card@1
id: P-KSRING17-076
kind: problem
title: Transitivity of integral extensions
classification:
  areas: [algebra]
  topics:
  - Integral Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 76 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Recall that if $R \subseteq S$ is an inclusion of commutative rings (with the same identity) then S is an integral extension of R if every element of S satisfies some monic polynomial with coefficients in R. Prove that if $R \subseteq S \subseteq T$ are commutative rings with the same identity, then S is integral over R and T is integral over S if and only if T is integral over R.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume first that
$$
T
$$
is integral over
$$
R.
$$
Then
$$
S
$$
is integral over
$$
R.
$$


::: pf-proof

Every element
$$
s\in S
$$
is also an element of
$$
T.
$$
Since
$$
T
$$
is integral over
$$
R,
$$
the element $s$ satisfies a monic polynomial with coefficients in $R$.
Thus every element of $S$ is integral over $R$.

:::

:::

::: {.pf-step #s1-2}

Under the same hypothesis, $T$ is integral over $S$.


::: pf-proof

Let
$$
t\in T.
$$
Since $T$ is integral over $R$, there exists a monic polynomial
$$
f(X)
\in
R[X]
$$
such that
$$
f(t)=0.
$$
Because
$$
R\subseteq S,
$$
the same polynomial lies in
$$
S[X].
$$
Hence $t$ is integral over $S$.
Since $t$ was arbitrary, $T$ is integral over $S$.

:::

:::

::: {.pf-step #s1-3}

Now assume conversely that
$$
S
$$
is integral over
$$
R
$$
and
$$
T
$$
is integral over
$$
S.
$$
Fix
$$
t\in T.
$$


::: pf-proof

It suffices to prove that this arbitrary element $t$ is integral over $R$.

:::

:::

::: {.pf-step #s1-4}

Since $t$ is integral over $S$, there exist
$$
n\ge1
$$
and
$$
s_0,\ldots,s_{n-1}\in S
$$
such that
$$
t^n
+
s_{n-1}t^{n-1}
+
\cdots
+
s_1t
+
s_0
=
0.
$$


::: pf-proof

This is the definition of integrality of $t$ over $S$.

:::

:::

::: {.pf-step #s1-5}

Set
$$
A
\coloneqq
R[s_0,\ldots,s_{n-1}].
$$
Then $A$ is finitely generated as an $R$-module.


::: pf-proof

Each coefficient
$$
s_i\in S
$$
is integral over $R$, because $S$ is integral over $R$.

Adjoin these coefficients one at a time.
If an element
$$
u
$$
is integral over a ring
$$
B,
$$
say
$$
u^m+b_{m-1}u^{m-1}+\cdots+b_0=0,
$$
then
$$
B[u]
$$
is generated as a $B$-module by
$$
1,u,\ldots,u^{m-1}.
$$

Thus
$$
R[s_0]
$$
is finite as an $R$-module,
$$
R[s_0,s_1]
$$
is finite as an $R[s_0]$-module and therefore finite as an $R$-module, and continuing inductively gives that
$$
A
=
R[s_0,\ldots,s_{n-1}]
$$
is finitely generated as an $R$-module.

:::

:::

::: {.pf-step #s1-6}

The element $t$ is integral over $A$.


::: pf-proof

The monic relation in step [](#s1-4){.pf-ref} has all coefficients
$$
s_i
$$
in
$$
A.
$$
Therefore $t$ satisfies a monic polynomial in
$$
A[X].
$$

:::

:::

::: {.pf-step #s1-7}

The ring
$$
B
\coloneqq
A[t]
$$
is finitely generated as an $A$-module.


::: pf-proof

By step [](#s1-6){.pf-ref}, $t$ is integral over $A$.
Using the monic equation from step [](#s1-4){.pf-ref}, every power
$$
t^m
$$
with
$$
m\ge n
$$
reduces to an $A$-linear combination of
$$
1,t,\ldots,t^{n-1}.
$$
Hence
$$
B
=
A\cdot1
+
A\cdot t
+
\cdots
+
A\cdot t^{n-1}.
$$

:::

:::

::: {.pf-step #s1-8}

The ring $B$ is finitely generated as an $R$-module.


::: pf-proof

By step [](#s1-5){.pf-ref}, choose finitely many $R$-module generators
$$
a_1,\ldots,a_r
$$
of $A$.
By step [](#s1-7){.pf-ref}, choose finitely many $A$-module generators
$$
b_1,\ldots,b_m
$$
of $B$.
Then the finitely many products
$$
a_i b_j
$$
generate $B$ as an $R$-module.
Indeed, an arbitrary element of $B$ is an $A$-linear combination of the $b_j$, and each coefficient in $A$ is an $R$-linear combination of the $a_i$.

:::

:::

::: {.pf-step #s1-9}

Regard $B$ as an $R[t]$-module by multiplication.
Then $B$ is faithful as an $R[t]$-module.


::: pf-proof

One has
$$
R[t]\subseteq A[t]=B.
$$
Suppose
$$
f(t)\in R[t]
$$
annihilates all of $B$.
In particular it annihilates
$$
1\in B.
$$
Hence
$$
f(t)\cdot1
=
f(t)
=
0
$$
in $B$.
Therefore the annihilator of $B$ in $R[t]$ is zero, so the module is faithful.

:::

:::

::: {.pf-step #s1-10}

Choose $R$-module generators
$$
m_1,\ldots,m_N
$$
of $B.
For each $j$, write
$$
t m_j
=
\sum_{i=1}^{N}a_{ij}m_i
$$
with
$$
a_{ij}\in R.
$$


::: pf-proof

Finite generation of $B$ over $R$ was proved in step [](#s1-8){.pf-ref}.
Because
$$
t\in B
$$
and $B$ is a ring,
$$
t m_j\in B.
$$
Hence it can be expressed as an $R$-linear combination of the chosen generators.

:::

:::

::: {.pf-step #s1-11}

Let
$$
A_0
\coloneqq
(a_{ij})
\in
M_N(R).
$$
Then
$$
\det(tI_N-A_0)
$$
annihilates every generator $m_j$.


::: pf-proof

The relations from step [](#s1-10){.pf-ref} can be written as
$$
(tI_N-A_0)\mathbf m=0,
$$
where
$$
\mathbf m
\coloneqq
\begin{pmatrix}
m_1\\
\vdots\\
m_N
\end{pmatrix}.
$$
Multiply by the adjugate matrix:
$$
\operatorname{adj}(tI_N-A_0)(tI_N-A_0)\mathbf m
=
0.
$$
Using
$$
\operatorname{adj}(M)M
=
\det(M)I_N
$$
over the commutative ring $R[t]$, one obtains
$$
\det(tI_N-A_0)\mathbf m
=
0.
$$
Thus the determinant annihilates each generator.

:::

:::

::: {.pf-step #s1-12}

One has
$$
\det(tI_N-A_0)=0
$$
in $B$.


::: pf-proof

By step [](#s1-11){.pf-ref}, the element
$$
\det(tI_N-A_0)
\in
R[t]
$$
annihilates every $R$-module generator of $B$, hence annihilates all of $B$.
By faithfulness from step [](#s1-9){.pf-ref}, its annihilator in $R[t]$ is zero.
Therefore
$$
\det(tI_N-A_0)=0.
$$

:::

:::

::: {.pf-step #s1-13}

The polynomial
$$
\chi(X)
\coloneqq
\det(XI_N-A_0)
$$
is monic with coefficients in $R$, and
$$
\chi(t)=0.
$$


::: pf-proof

The determinant
$$
\det(XI_N-A_0)
$$
is a monic polynomial of degree $N$ in $X$: its highest-degree term is obtained by taking the $X$ entry from each diagonal position and equals
$$
X^N.
$$
All coefficients lie in $R$ because the entries of $A_0$ lie in $R$.

Step [](#s1-12){.pf-ref} gives
$$
\chi(t)
=
\det(tI_N-A_0)
=
0.
$$

:::

:::

::: {.pf-step #s1-14}

Therefore $t$ is integral over $R$.


::: pf-proof

Step [](#s1-13){.pf-ref} gives a monic polynomial
$$
\chi(X)\in R[X]
$$
with
$$
\chi(t)=0.
$$
This is exactly the definition of integrality of $t$ over $R$.

:::

:::

::: {.pf-step #s1-15}

Therefore $T$ is integral over $R$.


::: pf-proof

The element
$$
t\in T
$$
was arbitrary in step [](#s1-3){.pf-ref}.
Step [](#s1-14){.pf-ref} shows that every such $t$ is integral over $R$.
Hence
$$
T
$$
is integral over
$$
R.
$$

:::

:::

::: {.pf-step #s1-16}

Consequently,
$$
\boxed{
\bigl(S\text{ integral over }R
\text{ and }
T\text{ integral over }S\bigr)
\iff
T\text{ integral over }R.
}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} prove the reverse implication from
$$
T/R
$$
to
$$
S/R
\text{ and }
T/S.
$$
Steps [](#s1-3){.pf-ref} through [](#s1-15){.pf-ref} prove transitivity.

:::

:::

::: pf-qed

Step [](#s1-16){.pf-ref} is the required equivalence.

:::

:::

:::
