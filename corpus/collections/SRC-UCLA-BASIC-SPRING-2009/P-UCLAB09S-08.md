---
schema: qual/card@1
id: P-UCLAB09S-08
kind: problem
title: Frobenius inner product and the adjoint of a commutator map
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
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Spring 2009.
---

::: {.problem}
Let $M_{n\times n}(\RR)$ be the vector space of real $n\times n$ matrices.

(a) Prove that
$$
\langle A,B\rangle=\operatorname{tr}(AB^T)
$$
defines an inner product.

(b) For fixed $C\in M_{n\times n}(\RR)$, define
$$
\Phi_C(A)=CA-AC.
$$
Compute the adjoint of $\Phi_C$.
Check that if $C$ is symmetric, then $\Phi_C$ is self-adjoint.

(c) Prove that for every $C$, the map $\Phi_C$ is not onto.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For matrices
$$
A=(a_{ij}),
\qquad
B=(b_{ij}),
$$
one has
$$
\operatorname{tr}(AB^T)
=
\sum_{i,j=1}^n a_{ij}b_{ij}.
$$


::: pf-proof

The $i$th diagonal entry of
$$
AB^T
$$
is
$$
(AB^T)_{ii}
=
\sum_{j=1}^n
a_{ij}(B^T)_{ji}
=
\sum_{j=1}^n
a_{ij}b_{ij}.
$$
Summing over $i$ gives the formula.

:::

:::

::: {.pf-step #s1-2}

The map
$$
\langle A,B\rangle
=
\operatorname{tr}(AB^T)
$$
is bilinear and symmetric.


::: pf-proof

Bilinearity follows from bilinearity of matrix multiplication and linearity of trace and transpose.
By step [](#s1-1){.pf-ref},
$$
\langle A,B\rangle
=
\sum_{i,j}a_{ij}b_{ij}
=
\sum_{i,j}b_{ij}a_{ij}
=
\langle B,A\rangle.
$$

:::

:::

::: {.pf-step #s1-3}

For every matrix $A$,
$$
\langle A,A\rangle
=
\sum_{i,j=1}^n a_{ij}^2
\ge0,
$$
with equality if and only if
$$
A=0.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} with $B=A$.
The sum of squares is nonnegative and vanishes exactly when every entry $a_{ij}$ is zero.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\langle A,B\rangle
=
\operatorname{tr}(AB^T)
}
$$
defines an inner product on
$$
M_{n\times n}(\RR).
$$


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} verify bilinearity, symmetry, and positive definiteness.

:::

:::

::: {.pf-step #s1-5}

For all matrices $A,B$,
$$
\langle \Phi_C(A),B\rangle
=
\operatorname{tr}
\bigl(
A(B^TC-CB^T)
\bigr).
$$


::: pf-proof

By definition,
$$
\Phi_C(A)=CA-AC.
$$
Hence
$$
\begin{aligned}
\langle\Phi_C(A),B\rangle
&=
\operatorname{tr}
\bigl(
(CA-AC)B^T
\bigr)\\
&=
\operatorname{tr}(CAB^T)
-
\operatorname{tr}(ACB^T).
\end{aligned}
$$
Using cyclicity of trace,
$$
\operatorname{tr}(CAB^T)
=
\operatorname{tr}(AB^TC).
$$
Thus
$$
\langle\Phi_C(A),B\rangle
=
\operatorname{tr}
\bigl(
A(B^TC-CB^T)
\bigr).
$$

:::

:::

::: {.pf-step #s1-6}

The adjoint of $\Phi_C$ is
$$
\boxed{
\Phi_C^*(B)
=
C^TB-BC^T
=
\Phi_{C^T}(B).
}
$$


::: pf-proof

The adjoint is characterized by
$$
\langle\Phi_C(A),B\rangle
=
\langle A,\Phi_C^*(B)\rangle
=
\operatorname{tr}
\bigl(
A(\Phi_C^*(B))^T
\bigr)
$$
for every $A$.
By step [](#s1-5){.pf-ref}, it is enough to require
$$
(\Phi_C^*(B))^T
=
B^TC-CB^T.
$$
Transposing gives
$$
\Phi_C^*(B)
=
C^TB-BC^T.
$$

:::

:::

::: {.pf-step #s1-7}

If $C$ is symmetric, then $\Phi_C$ is self-adjoint.


::: pf-proof

If
$$
C^T=C,
$$
step [](#s1-6){.pf-ref} gives
$$
\Phi_C^*
=
\Phi_{C^T}
=
\Phi_C.
$$
Thus
$$
\boxed{\Phi_C\text{ is self-adjoint}.}
$$

:::

:::

::: {.pf-step #s1-8}

For every $A$,
$$
\operatorname{tr}\Phi_C(A)=0.
$$


::: pf-proof

Using cyclicity of trace,
$$
\begin{aligned}
\operatorname{tr}\Phi_C(A)
&=
\operatorname{tr}(CA-AC)\\
&=
\operatorname{tr}(CA)
-
\operatorname{tr}(AC)\\
&=
0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-9}

The map $\Phi_C$ is not onto.


::: pf-proof

By step [](#s1-8){.pf-ref},
$$
\operatorname{im}\Phi_C
\subseteq
\{X:\operatorname{tr}X=0\}.
$$
The trace-zero matrices form a proper subspace of
$$
M_{n\times n}(\RR),
$$
because, for example,
$$
\operatorname{tr}(I_n)=n\ne0.
$$
Hence $I_n$ does not lie in the image of $\Phi_C$.
Therefore
$$
\boxed{\Phi_C\text{ is not surjective}.}
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} prove part (b), and step [](#s1-9){.pf-ref} proves part (c).

:::

:::

:::
