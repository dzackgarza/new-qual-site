---
schema: qual/card@1
id: P-UCLAB11S-01
kind: problem
title: Jordan forms from three power traces
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Spring 2011.
---

::: {.problem}
Let $A$ be a $3\times3$ matrix with complex entries satisfying
$$
\operatorname{Tr}(A)=4,\qquad \operatorname{Tr}(A^2)=6,\qquad \operatorname{Tr}(A^3)=10.
$$
For each similarity class of such matrices, give one representative in Jordan normal form.

You may use the identity: if
$$
b_1=a_1+a_2+a_3,\quad b_2=a_1^2+a_2^2+a_3^2,\quad b_3=a_1^3+a_2^3+a_3^3,
$$
then
$$
6a_1a_2a_3=b_1^3+2b_3-3b_1b_2.
$$
:::

::: {.solution}

Let
$$
\lambda_1,\lambda_2,\lambda_3
$$
be the eigenvalues of $A$, counted with algebraic multiplicity.

::: pf

::: {.pf-step #s1-1}

The trace identities give
$$
\lambda_1+\lambda_2+\lambda_3=4,
$$
$$
\lambda_1^2+\lambda_2^2+\lambda_3^2=6,
$$
and
$$
\lambda_1^3+\lambda_2^3+\lambda_3^3=10.
$$


::: pf-proof

Over $\CC$, $A$ is similar to an upper triangular matrix whose diagonal entries are its eigenvalues counted with algebraic multiplicity.
The diagonal entries of the $m$th power are then
$$
\lambda_1^m,\lambda_2^m,\lambda_3^m.
$$
Trace is similarity-invariant, so
$$
\operatorname{Tr}(A^m)
=
\lambda_1^m+\lambda_2^m+\lambda_3^m
$$
for
$$
m=1,2,3.
$$
Substitute the given traces.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\lambda_1\lambda_2+\lambda_1\lambda_3+\lambda_2\lambda_3
=
5.
$$


::: pf-proof

Square the first identity from step [](#s1-1){.pf-ref}:
$$
16
=
\lambda_1^2+\lambda_2^2+\lambda_3^2
+
2(\lambda_1\lambda_2+\lambda_1\lambda_3+\lambda_2\lambda_3).
$$
Using
$$
\lambda_1^2+\lambda_2^2+\lambda_3^2=6,
$$
one gets
$$
16=6+2e_2,
$$
so
$$
e_2=5.
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\lambda_1\lambda_2\lambda_3=2.
$$


::: pf-proof

Apply the identity supplied in the problem with
$$
b_1=4,
\qquad
b_2=6,
\qquad
b_3=10.
$$
Then
$$
\begin{aligned}
6\lambda_1\lambda_2\lambda_3
&=
4^3+2\cdot10-3\cdot4\cdot6\\
&=
64+20-72\\
&=
12.
\end{aligned}
$$
Thus
$$
\lambda_1\lambda_2\lambda_3=2.
$$

:::

:::

::: {.pf-step #s1-4}

The characteristic polynomial of $A$ is
$$
\boxed{
\chi_A(t)
=
t^3-4t^2+5t-2
=
(t-1)^2(t-2).
}
$$


::: pf-proof

For three eigenvalues, the characteristic polynomial is
$$
\chi_A(t)
=
t^3
-
(\lambda_1+\lambda_2+\lambda_3)t^2
+
(\lambda_1\lambda_2+\lambda_1\lambda_3+\lambda_2\lambda_3)t
-
\lambda_1\lambda_2\lambda_3.
$$
Use steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} to obtain
$$
t^3-4t^2+5t-2.
$$
Factoring gives
$$
(t-1)^2(t-2).
$$

:::

:::

::: {.pf-step #s1-5}

Hence the eigenvalue $1$ has algebraic multiplicity $2$, and the eigenvalue $2$ has algebraic multiplicity $1$.


::: pf-proof

This follows directly from the factorization in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

For the eigenvalue $2$, the only possible Jordan block is
$$
[2].
$$


::: pf-proof

Its algebraic multiplicity is $1$ by step [](#s1-5){.pf-ref}.
Therefore the total size of all Jordan blocks carrying eigenvalue $2$ is $1$, so there is exactly one $1\times1$ block.

:::

:::

::: {.pf-step #s1-7}

For the eigenvalue $1$, there are exactly two possible Jordan block patterns:
$$
[1]\oplus[1]
$$
or
$$
J_2(1)
=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
$$


::: pf-proof

The algebraic multiplicity of $1$ is $2$.
The Jordan block sizes for eigenvalue $1$ therefore form a partition of $2$.
The only partitions are
$$
1+1
$$
and
$$
2.
$$

:::

:::

::: {.pf-step #s1-8}

Consequently there are exactly two similarity classes, represented by
$$
\boxed{
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&2
\end{pmatrix}
}
$$
and
$$
\boxed{
\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&2
\end{pmatrix}.
}
$$


::: pf-proof

Combine the unique block for eigenvalue $2$ from step [](#s1-6){.pf-ref} with each of the two possibilities for eigenvalue $1$ from step [](#s1-7){.pf-ref}.
Jordan normal form classifies complex matrices up to similarity, so these two block patterns give exactly the two similarity classes.

:::

:::

::: {.pf-step #s1-9}

Both representatives satisfy the three trace conditions.


::: pf-proof

For either Jordan form, the eigenvalues counted with algebraic multiplicity are
$$
1,1,2.
$$
Therefore
$$
\operatorname{Tr}(A)=1+1+2=4,
$$
$$
\operatorname{Tr}(A^2)=1+1+4=6,
$$
and
$$
\operatorname{Tr}(A^3)=1+1+8=10.
$$
Thus both listed classes actually occur.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} gives all similarity classes, and step [](#s1-9){.pf-ref} verifies that both satisfy the hypotheses.

:::

:::

:::
