---
schema: qual/card@1
id: P-BERK78S-16
kind: problem
title: Two criteria for diagonalizability of a complex operator
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For part 1, inspected the Jordan blocks: on a lambda-block of size s,
    the nth power of T-lambda I kills the whole block, while its first
    power has one-dimensional kernel; the stated kernel equality therefore
    forces every block to have size one. For part 2, normality gives
    ker(T-lambda I)=ker(T^*-bar(lambda)I). An eigenline therefore has an
    invariant orthogonal complement on which the restriction remains
    normal, so induction yields an orthonormal eigenbasis.
---

::: {.problem}
Let $T:\mathbb C^n\to\mathbb C^n$ be linear.

1. Prove that $T$ is diagonalizable if, for every $\lambda\in\mathbb C$,
   \[
   \ker(T-\lambda I)^n=\ker(T-\lambda I).
   \]
2. Show that $T$ is diagonalizable if $T$ commutes with its conjugate transpose $T^*$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Put $T$ into Jordan canonical form over $\CC$.
For a Jordan block
$$
J_s(\lambda)
=
\lambda I_s+N_s
$$
of size $s$, one has
$$
\ker(J_s(\lambda)-\lambda I_s)^n=\CC^s.
$$

::: pf-proof

The nilpotent Jordan matrix $N_s$ satisfies
$$
N_s^s=0.
$$
Since $s\leq n$,
$$
N_s^n=0.
$$
Therefore
$$
(J_s(\lambda)-\lambda I_s)^n
=
N_s^n
=
0,
$$
so its kernel is the whole block space.

:::

:::

::: {.pf-step #s2}

For the same block,
$$
\dim\ker(J_s(\lambda)-\lambda I_s)=1.
$$

::: pf-proof

The matrix
$$
J_s(\lambda)-\lambda I_s=N_s
$$
is the standard nilpotent Jordan block. Its kernel is spanned by the first
basis vector of the block and therefore has dimension $1$.

:::

:::

::: {.pf-step #s3}

Under the hypothesis
$$
\ker(T-\lambda I)^n=\ker(T-\lambda I)
$$
for every $\lambda\in\CC$, every Jordan block of $T$ has size $1$.

::: pf-proof

Fix an eigenvalue $\lambda$. On the direct sum of the Jordan blocks with
eigenvalue $\lambda$, step [](#s1){.pf-ref} shows that
$$
\ker(T-\lambda I)^n
$$
contains the whole generalized $\lambda$-eigenspace. On a block of size
$s$, step [](#s2){.pf-ref} shows that
$$
\ker(T-\lambda I)
$$
contributes only one dimension.

If any $\lambda$-block had size $s>1$, the generalized
$\lambda$-eigenspace would contain vectors in
$$
\ker(T-\lambda I)^n
$$
which are not in
$$
\ker(T-\lambda I),
$$
contradicting the assumed equality. Hence every block has size $1$.

:::

:::

::: {.pf-step #s4}

Under the hypothesis of part (1),
$$
\boxed{
T\text{ is diagonalizable}.
}
$$

::: pf-proof

By step [](#s3){.pf-ref}, the Jordan canonical form of $T$ consists entirely of
$1\times1$ blocks. Hence it is diagonal.

:::

:::

::: {.pf-step #s5}

For part (2), suppose
$$
TT^*=T^*T.
$$
For every $\lambda\in\CC$, the operator
$$
N=T-\lambda I
$$
is normal:
$$
NN^*=N^*N.
$$

::: pf-proof

One has
$$
N^*=T^*-\bar\lambda I.
$$
Expanding both products,
$$
\begin{aligned}
NN^*
&=
TT^*-\bar\lambda T-\lambda T^*
+\abs{\lambda}^2I,\\
N^*N
&=
T^*T-\bar\lambda T-\lambda T^*
+\abs{\lambda}^2I.
\end{aligned}
$$
These are equal because $TT^*=T^*T$.

:::

:::

::: {.pf-step #s6}

If $N$ is normal, then
$$
\ker N=\ker N^*.
$$

::: pf-proof

For every vector $v$,
$$
\begin{aligned}
\norm{Nv}^2
&=
v^*N^*Nv\\
&=
v^*NN^*v\\
&=
\norm{N^*v}^2.
\end{aligned}
$$
Thus
$$
Nv=0
\iff
N^*v=0.
$$

:::

:::

::: {.pf-step #s7}

If
$$
Tv=\lambda v,
$$
then
$$
T^*v=\bar\lambda v.
$$

::: pf-proof

Set
$$
N=T-\lambda I.
$$
Then $Nv=0$. By steps [](#s5){.pf-ref} and [](#s6){.pf-ref},
$$
N^*v=0.
$$
Since
$$
N^*=T^*-\bar\lambda I,
$$
this says exactly that
$$
T^*v=\bar\lambda v.
$$

:::

:::

::: {.pf-step #s8}

If $v$ is an eigenvector of the normal operator $T$, then its
orthogonal complement
$$
v^\perp
$$
is invariant under both $T$ and $T^*$.

::: pf-proof

Let $w\in v^\perp$. By step [](#s7){.pf-ref},
$$
T^*v=\bar\lambda v.
$$
Therefore
$$
\langle Tw,v\rangle
=
\langle w,T^*v\rangle
=
0,
$$
so
$$
Tw\in v^\perp.
$$

Since $T^*$ is also normal and
$$
T^*v=\bar\lambda v,
$$
the same argument with $T$ and $T^*$ interchanged gives
$$
T^*w\in v^\perp.
$$

:::

:::

::: {.pf-step #s9}

The restriction
$$
T|_{v^\perp}
$$
is normal.

::: pf-proof

By step [](#s8){.pf-ref}, both $T$ and $T^*$ preserve $v^\perp$. Hence the adjoint of
the restriction is
$$
(T|_{v^\perp})^*
=
T^*|_{v^\perp}.
$$
Restricting the identity
$$
TT^*=T^*T
$$
to $v^\perp$ gives normality of $T|_{v^\perp}$.

:::

:::

::: {.pf-step #s10}

Every normal operator on $\CC^n$ has an orthonormal basis of
eigenvectors.

::: pf-proof

Proceed by induction on $n$. The assertion is immediate for $n=0$ and
$n=1$. Suppose $n>1$.

The characteristic polynomial of $T$ has a complex root, so $T$ has a
unit eigenvector $v$. By step [](#s8){.pf-ref},
$$
\CC^n
=
\CC v\oplus v^\perp
$$
is an orthogonal decomposition into invariant subspaces. By step [](#s9){.pf-ref},
the restriction of $T$ to $v^\perp$ is normal. Its dimension is $n-1$, so
the induction hypothesis gives an orthonormal eigenbasis of $v^\perp$.
Adjoining $v$ produces an orthonormal eigenbasis of $\CC^n$.

:::

:::

::: {.pf-step #s11}

If $T$ commutes with $T^*$, then
$$
\boxed{
T\text{ is diagonalizable}.
}
$$

::: pf-proof

The commutation hypothesis says that $T$ is normal. Step [](#s10){.pf-ref} gives an
orthonormal basis of eigenvectors, so the matrix of $T$ in that basis is
diagonal.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves part (1), and step [](#s11){.pf-ref} proves part (2).

:::

:::

:::
