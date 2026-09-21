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
<1>1. Put $T$ into Jordan canonical form over $\CC$.
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

::: {.proof}
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

<1>2. For the same block,
$$
\dim\ker(J_s(\lambda)-\lambda I_s)=1.
$$

::: {.proof}
The matrix
$$
J_s(\lambda)-\lambda I_s=N_s
$$
is the standard nilpotent Jordan block. Its kernel is spanned by the first
basis vector of the block and therefore has dimension $1$.
:::

<1>3. Under the hypothesis
$$
\ker(T-\lambda I)^n=\ker(T-\lambda I)
$$
for every $\lambda\in\CC$, every Jordan block of $T$ has size $1$.

::: {.proof}
Fix an eigenvalue $\lambda$. On the direct sum of the Jordan blocks with
eigenvalue $\lambda$, step <1>1 shows that
$$
\ker(T-\lambda I)^n
$$
contains the whole generalized $\lambda$-eigenspace. On a block of size
$s$, step <1>2 shows that
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

<1>4. Under the hypothesis of part (1),
$$
\boxed{
T\text{ is diagonalizable}.
}
$$

::: {.proof}
By step <1>3, the Jordan canonical form of $T$ consists entirely of
$1\times1$ blocks. Hence it is diagonal.
:::

<1>5. For part (2), suppose
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

::: {.proof}
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

<1>6. If $N$ is normal, then
$$
\ker N=\ker N^*.
$$

::: {.proof}
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

<1>7. If
$$
Tv=\lambda v,
$$
then
$$
T^*v=\bar\lambda v.
$$

::: {.proof}
Set
$$
N=T-\lambda I.
$$
Then $Nv=0$. By steps <1>5--<1>6,
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

<1>8. If $v$ is an eigenvector of the normal operator $T$, then its
orthogonal complement
$$
v^\perp
$$
is invariant under both $T$ and $T^*$.

::: {.proof}
Let $w\in v^\perp$. By step <1>7,
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

<1>9. The restriction
$$
T|_{v^\perp}
$$
is normal.

::: {.proof}
By step <1>8, both $T$ and $T^*$ preserve $v^\perp$. Hence the adjoint of
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

<1>10. Every normal operator on $\CC^n$ has an orthonormal basis of
eigenvectors.

::: {.proof}
Proceed by induction on $n$. The assertion is immediate for $n=0$ and
$n=1$. Suppose $n>1$.

The characteristic polynomial of $T$ has a complex root, so $T$ has a
unit eigenvector $v$. By step <1>8,
$$
\CC^n
=
\CC v\oplus v^\perp
$$
is an orthogonal decomposition into invariant subspaces. By step <1>9,
the restriction of $T$ to $v^\perp$ is normal. Its dimension is $n-1$, so
the induction hypothesis gives an orthonormal eigenbasis of $v^\perp$.
Adjoining $v$ produces an orthonormal eigenbasis of $\CC^n$.
:::

<1>11. If $T$ commutes with $T^*$, then
$$
\boxed{
T\text{ is diagonalizable}.
}
$$

::: {.proof}
The commutation hypothesis says that $T$ is normal. Step <1>10 gives an
orthonormal basis of eigenvectors, so the matrix of $T$ in that basis is
diagonal.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>4 proves part (1), and step <1>11 proves part (2).
:::
:::
