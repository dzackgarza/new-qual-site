---
schema: qual/card@1
id: P-BERK78S-15
kind: problem
title: Complete reducibility is equivalent to diagonalizability over an algebraically closed field
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
    For a diagonalizable operator, polynomial spectral projections show
    that every invariant subspace splits as the direct sum of its
    intersections with the eigenspaces; choosing complements inside each
    eigenspace gives an invariant complement. Conversely, complete
    reducibility splits off an eigenline, and the property passes to the
    invariant complement, so induction on dimension produces an
    eigenbasis.
---

::: {.problem}
Let $V$ be a finite-dimensional vector space over an algebraically closed field. Call a linear operator $T:V\to V$ **completely reducible** if, whenever $E\subset V$ is $T$-invariant, there is a $T$-invariant subspace $F\subset V$ such that
\[
V=E\oplus F.
\]
Prove that $T$ is completely reducible if and only if $V$ has a basis of eigenvectors of $T$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose $V$ has a basis of eigenvectors of $T$. Let
$$
\lambda_1,\ldots,\lambda_r
$$
be the distinct eigenvalues and set
$$
V_i=\ker(T-\lambda_iI).
$$
Then
$$
V=V_1\oplus\cdots\oplus V_r.
$$

::: pf-proof

An eigenbasis is the disjoint union of bases of the eigenspaces
$V_i$. Therefore the eigenspaces span $V$, and eigenspaces belonging to
distinct eigenvalues have zero intersection. This gives the displayed
direct sum.

:::

:::

::: {.pf-step #s2}

For each $i$, define the polynomial
$$
q_i(t)
=
\prod_{j\neq i}
\frac{t-\lambda_j}{\lambda_i-\lambda_j}.
$$
Then
$$
q_i(T)
$$
is the projection of $V$ onto $V_i$ along the sum of the other
eigenspaces.

::: pf-proof

For an eigenvector $v\in V_k$,
$$
q_i(T)v
=
q_i(\lambda_k)v.
$$
By construction,
$$
q_i(\lambda_i)=1
$$
and
$$
q_i(\lambda_k)=0
$$
for $k\neq i$. Thus $q_i(T)$ is the identity on $V_i$ and zero on every
$V_k$ with $k\neq i$. Step [](#s1){.pf-ref} then gives the stated projection.

:::

:::

::: {.pf-step #s3}

If $E\subseteq V$ is $T$-invariant, then
$$
E
=
\bigoplus_{i=1}^r(E\cap V_i).
$$

::: pf-proof

Because $E$ is $T$-invariant, it is invariant under every polynomial in
$T$. In particular,
$$
q_i(T)(E)\subseteq E
$$
for every $i$.

Take $e\in E$. By step [](#s1){.pf-ref}, write
$$
e=e_1+\cdots+e_r,
\qquad
e_i\in V_i.
$$
Step [](#s2){.pf-ref} gives
$$
e_i=q_i(T)e.
$$
Hence each $e_i$ lies in $E$ as well as in $V_i$. Therefore
$$
E
\subseteq
\sum_{i=1}^r(E\cap V_i).
$$
The reverse inclusion is immediate, and the sum is direct because the
$V_i$ form a direct sum.

:::

:::

::: {.pf-step #s4}

Under the hypothesis of step [](#s1){.pf-ref}, every $T$-invariant subspace has
a $T$-invariant complement.

::: pf-proof

Let $E\subseteq V$ be $T$-invariant. For each $i$, choose a vector-space
complement
$$
F_i\subseteq V_i
$$
such that
$$
V_i
=
(E\cap V_i)\oplus F_i.
$$
Every subspace of $V_i$ is $T$-invariant because $T$ acts on $V_i$ as
scalar multiplication by $\lambda_i$. Thus each $F_i$ is $T$-invariant.

Set
$$
F=F_1\oplus\cdots\oplus F_r.
$$
Then $F$ is $T$-invariant. Using steps [](#s1){.pf-ref} and [](#s3){.pf-ref},
$$
\begin{aligned}
V
&=
\bigoplus_{i=1}^r V_i\\
&=
\bigoplus_{i=1}^r
\bigl((E\cap V_i)\oplus F_i\bigr)\\
&=
E\oplus F.
\end{aligned}
$$

:::

:::

::: {.pf-step #s5}

If $V$ has a basis of eigenvectors, then $T$ is completely
reducible.

::: pf-proof

Step [](#s4){.pf-ref} gives the required invariant complement for every invariant
subspace.

:::

:::

::: {.pf-step #s6}

Conversely, suppose $T$ is completely reducible. If
$$
\dim V>0,
$$
then $T$ has an eigenvector.

::: pf-proof

The characteristic polynomial of $T$ has positive degree and has a root
because the ground field is algebraically closed. If $\lambda$ is such a
root, then
$$
\ker(T-\lambda I)\neq0.
$$
Any nonzero vector in this kernel is an eigenvector.

:::

:::

::: {.pf-step #s7}

Let $v$ be an eigenvector from step [](#s6){.pf-ref} and let
$$
E=\operatorname{span}\{v\}
$$
be the line it spans. There is a $T$-invariant subspace $W$ such
that
$$
V=E\oplus W.
$$

::: pf-proof

The eigenline $E$ is $T$-invariant. Complete reducibility of $T$ therefore
provides a $T$-invariant complement $W$.

:::

:::

::: {.pf-step #s8}

The restriction
$$
T|_W:W\to W
$$
is completely reducible.

::: pf-proof

Let
$$
L\subseteq W
$$
be invariant under $T|_W$. Then $L$ is also $T$-invariant as a subspace
of $V$. Since $T$ is completely reducible, there is a $T$-invariant
subspace $C\subseteq V$ such that
$$
V=L\oplus C.
$$

We claim
$$
W=L\oplus(W\cap C).
$$
Indeed, take $w\in W$. Write uniquely
$$
w=\ell+c,
\qquad
\ell\in L,\quad c\in C.
$$
Since both $w$ and $\ell$ lie in $W$, one has
$$
c=w-\ell\in W.
$$
Thus $c\in W\cap C$, so the displayed sum spans $W$. It is direct because
$L\cap C=0$. Finally, $W\cap C$ is $T$-invariant because both $W$ and $C$
are. Hence every invariant subspace of $W$ has an invariant complement in
$W$.

:::

:::

::: {.pf-step #s9}

If $T$ is completely reducible, then $V$ has a basis of
eigenvectors.

::: pf-proof

Proceed by induction on
$$
\dim V.
$$
The assertion is trivial for $\dim V=0$. Suppose $\dim V>0$. By steps
[](#s6){.pf-ref} and [](#s7){.pf-ref},
$$
V=\operatorname{span}\{v\}\oplus W
$$
with $v$ an eigenvector and $W$ invariant. By step [](#s8){.pf-ref}, the restriction
$T|_W$ is completely reducible. Since
$$
\dim W=\dim V-1,
$$
the induction hypothesis gives a basis of $W$ consisting of eigenvectors
of $T|_W$, hence of $T$. Adjoining $v$ gives an eigenbasis of $V$.

:::

:::

::: {.pf-step #s10}

The equivalence holds:
$$
\boxed{
T\text{ is completely reducible}
\iff
V\text{ has a basis of eigenvectors of }T.
}
$$

::: pf-proof

Step [](#s5){.pf-ref} proves that an eigenbasis implies complete reducibility, and
step [](#s9){.pf-ref} proves the reverse implication.

:::

:::

::: pf-qed

Step [](#s10){.pf-ref} is the required equivalence.

:::

:::

:::
