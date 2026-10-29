---
schema: qual/card@1
id: P-TRIV-LA25
kind: problem
title: Diagonalization and invariant subspaces of a symmetric $3\times 3$ matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 25, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
A linear transformation A writes in some basis in $\RR ^ { n }$ as follows, $A = { \left[ \begin{array} { l l l } { 0 } & { 2 } & { 1 } \\ { 2 } & { 8 } & { 2 } \\ { 1 } & { 2 } & { 0 } \end{array} \right] }$

(a) Write the transition matrix to the basis composed of the eigenvectors of A.

(b) Write the transformation A in this basis.

(c) Determine the invariant subspaces of A.
:::

::: {.solution}

Let
$$
A=
\begin{pmatrix}
0&2&1\\
2&8&2\\
1&2&0
\end{pmatrix}.
$$

::: pf

::: pf-step

The vector
$$
v_{-1}=
\begin{pmatrix}
1\\0\\-1
\end{pmatrix}
$$
is an eigenvector with eigenvalue $-1$.


::: pf-proof

Direct multiplication gives
$$
Av_{-1}
=
\begin{pmatrix}
-1\\0\\1
\end{pmatrix}
=
-v_{-1}.
$$

:::

:::

::: {.pf-step #s1-2}

The plane
$$
S=\{(a,b,a):a,b\in\RR\}
$$
is invariant under $A$.


::: pf-proof

For
$$
v=(a,b,a)^T,
$$
one has
$$
Av
=
\begin{pmatrix}
a+2b\\
4a+8b\\
a+2b
\end{pmatrix},
$$
whose first and third coordinates are equal.

:::

:::

::: pf-step

In coordinates $(a,b)$ on $S$, the restriction of $A$ is represented by
$$
\begin{pmatrix}
1&2\\
4&8
\end{pmatrix},
$$
whose eigenvalues are $0$ and $9$.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
(a,b)\longmapsto(a+2b,4a+8b).
$$
The characteristic polynomial is
$$
\det
\begin{pmatrix}
1-\lambda&2\\
4&8-\lambda
\end{pmatrix}
=
(1-\lambda)(8-\lambda)-8
=
\lambda(\lambda-9).
$$

:::

:::

::: pf-step

Eigenvectors for the remaining eigenvalues may be chosen as
$$
v_0=
\begin{pmatrix}
-2\\1\\-2
\end{pmatrix}
$$
and
$$
v_9=
\begin{pmatrix}
1\\4\\1
\end{pmatrix}.
$$


::: pf-proof

For eigenvalue $0$, the equation
$$
a+2b=0
$$
gives $a=-2b$, so choose $(a,b)=(-2,1)$.

For eigenvalue $9$, the equation
$$
a+2b=9a
$$
gives $b=4a$, so choose $(a,b)=(1,4)$.

:::

:::

::: {.pf-step #s1-5}

The three eigenvectors are mutually orthogonal and therefore form a
basis of $\RR^3$.


::: pf-proof

Their pairwise inner products are
$$
v_{-1}\cdot v_0=-2+2=0,
$$
$$
v_{-1}\cdot v_9=1-1=0,
$$
and
$$
v_0\cdot v_9=-2+4-2=0.
$$
All three vectors are nonzero, so they are linearly independent.

:::

:::

::: {.pf-step #s1-6}

A transition matrix whose columns are eigenvectors is
$$
\boxed{
P=
\begin{pmatrix}
1&-2&1\\
0&1&4\\
-1&-2&1
\end{pmatrix}.
}
$$


::: pf-proof

The columns are respectively $v_{-1},v_0,v_9$. By step [](#s1-5){.pf-ref} they form a
basis, so $P$ is invertible.

:::

:::

::: {.pf-step #s1-7}

Part (a) follows.


::: pf-proof

Step [](#s1-6){.pf-ref} gives the requested change-of-basis matrix. If the convention is
that coordinates transform from the original basis to the eigenbasis, the
coordinate-change matrix is $P^{-1}$.

:::

:::

::: {.pf-step #s1-8}

In the eigenbasis,
$$
\boxed{
P^{-1}AP
=
\begin{pmatrix}
-1&0&0\\
0&0&0\\
0&0&9
\end{pmatrix}.
}
$$


::: pf-proof

Each column of $P$ is an eigenvector, so
$$
AP
=
P
\operatorname{diag}(-1,0,9).
$$
Multiply on the left by $P^{-1}$.

:::

:::

::: {.pf-step #s1-9}

Part (b) follows.


::: pf-proof

This is step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Each span of a subset of
$$
\{v_{-1},v_0,v_9\}
$$
is invariant under $A$.


::: pf-proof

Each $v_\lambda$ is an eigenvector. Therefore $A$ maps every selected
eigendirection to itself, and hence maps any sum of selected eigendirections
to itself.

:::

:::

::: {.pf-step #s1-11}

Conversely, every invariant subspace of $A$ is the span of a subset of
the three eigendirections.


::: pf-proof

Let $W\subseteq\RR^3$ be $A$-invariant. Since $W$ is invariant under
$A$, it is invariant under every polynomial in $A$.

Because the eigenvalues $-1,0,9$ are distinct, define the spectral projection
polynomials
$$
p_{-1}(t)
=
\frac{t(t-9)}{(-1)(-10)},
$$
$$
p_0(t)
=
\frac{(t+1)(t-9)}{(1)(-9)},
$$
and
$$
p_9(t)
=
\frac{(t+1)t}{(10)(9)}.
$$
Each $p_\lambda(A)$ is the projection onto the $\lambda$-eigenspace.

If
$$
w
=
c_{-1}v_{-1}+c_0v_0+c_9v_9
\in W,
$$
then invariance under these polynomial projections gives
$$
c_\lambda v_\lambda
=
p_\lambda(A)w
\in W
$$
for each eigenvalue $\lambda$. Thus $W$ is the direct sum of those
eigendirections that occur in it.

:::

:::

::: {.pf-step #s1-12}

Hence the invariant subspaces are exactly
$$
\boxed{
\begin{gathered}
\{0\},\\
\operatorname{span}(v_{-1}),\quad
\operatorname{span}(v_0),\quad
\operatorname{span}(v_9),\\
\operatorname{span}(v_{-1},v_0),\quad
\operatorname{span}(v_{-1},v_9),\quad
\operatorname{span}(v_0,v_9),\\
\RR^3.
\end{gathered}
}
$$


::: pf-proof

Step [](#s1-10){.pf-ref} shows that every displayed subspace is invariant, and step [](#s1-11){.pf-ref}
shows that no others occur.

:::

:::

::: {.pf-step #s1-13}

Part (c) follows.


::: pf-proof

This is step [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} and [](#s1-9){.pf-ref}, and [](#s1-13){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
