---
schema: qual/card@1
id: P-BKF08-5B
kind: problem
title: $\operatorname{PGL}_2(\mathbb F_3)$ is isomorphic to $S_4$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 5B of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the action on the four projective lines, the scalar kernel,
    the description of the center, and the group-order argument proving
    surjectivity onto S_4.
---

::: {.problem}
Prove that the quotient of $\operatorname{GL}_2(\ZZ/3\ZZ)$ by its center is isomorphic to the symmetric group $S_4$.
:::

::: {.solution}
Put
$$
V\coloneqq\FF_3^2,
\qquad
G\coloneqq\operatorname{GL}_2(\FF_3).
$$

::: pf

::: {.pf-step #s1}

The set of one-dimensional subspaces of $V$ has exactly four
elements.

::: pf-proof

There are $3^2-1=8$ nonzero vectors in $V$. Each one-dimensional
subspace contains exactly $3-1=2$ nonzero vectors, and distinct
one-dimensional subspaces have no nonzero vector in common. Hence the
number of such subspaces is
$$
\frac{8}{2}=4.
$$

:::

:::

::: pf-step

The natural action of $G$ on the one-dimensional subspaces of $V$
defines a homomorphism
$$
\rho\colon G\longrightarrow S_4.
$$

::: pf-proof

An invertible linear transformation sends a one-dimensional subspace to
a one-dimensional subspace and preserves distinctness. Thus every element
of $G$ permutes the four subspaces from step [](#s1){.pf-ref}. Compatibility of the
action with composition gives a group homomorphism to their permutation
group, which is $S_4$.

:::

:::

::: {.pf-step #s3}

The kernel of $\rho$ is exactly the group of nonzero scalar
matrices
$$
\{I,-I\}.
$$

::: pf-proof

Every nonzero scalar matrix fixes each one-dimensional subspace, so it
lies in the kernel.

Conversely, let $A\in\ker\rho$. For the standard basis $e_1,e_2$, the
lines $\langle e_1\rangle$ and $\langle e_2\rangle$ are fixed, so
$$
Ae_1=\lambda e_1,
\qquad
Ae_2=\mu e_2
$$
for some $\lambda,\mu\in\FF_3^\times$. The line
$\langle e_1+e_2\rangle$ is also fixed, so
$$
\lambda e_1+\mu e_2=A(e_1+e_2)
$$
must be a scalar multiple of $e_1+e_2$. Therefore $\lambda=\mu$, and
$A=\lambda I$. Since $\FF_3^\times=\{1,-1\}$, the kernel is exactly
$\{I,-I\}$.

:::

:::

::: {.pf-step #s4}

The center of $G$ is exactly $\{I,-I\}$.

::: pf-proof

Every scalar matrix is central. Conversely, let
$$
A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}
$$
be central. Commuting with
$$
D=\begin{pmatrix}-1&0\\0&1\end{pmatrix}
$$
gives $b=c=0$, since $1\ne-1$ in $\FF_3$. Thus
$A=\operatorname{diag}(a,d)$. Commuting with
$$
U=\begin{pmatrix}1&1\\0&1\end{pmatrix}
$$
then gives $a=d$. Hence $A=aI$, and invertibility forces
$a\in\FF_3^\times=\{1,-1\}$.

:::

:::

::: {.pf-step #s5}

The homomorphism $\rho$ induces an injective homomorphism
$$
\overline\rho\colon G/Z(G)\longrightarrow S_4.
$$

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref},
$$
\ker\rho=Z(G).
$$
The first isomorphism theorem therefore factors $\rho$ through the
quotient by the center, with injective induced map $\overline\rho$.

:::

:::

::: {.pf-step #s6}

The quotient $G/Z(G)$ has order $24$.

::: pf-proof

To choose an invertible $2\times2$ matrix over $\FF_3$, choose its first
column to be any nonzero vector, giving $3^2-1=8$ choices. The second
column can be any vector outside the three-element span of the first,
giving $3^2-3=6$ choices. Hence
$$
\abs{G}=8\cdot6=48.
$$
By step [](#s4){.pf-ref}, $\abs{Z(G)}=2$, so
$$
\abs{G/Z(G)}=\frac{48}{2}=24.
$$

:::

:::

::: {.pf-step #s7}

Therefore
$$
\boxed{
G/Z(G)\cong S_4
}.
$$

::: pf-proof

By step [](#s5){.pf-ref}, $G/Z(G)$ embeds in $S_4$. Step [](#s6){.pf-ref} gives
$\abs{G/Z(G)}=24=\abs{S_4}$. An injective map between finite groups of
the same order is surjective, hence an isomorphism.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is exactly the required isomorphism.

:::

:::

:::
