---
schema: qual/card@1
id: P-WESTOP05-02
kind: problem
title: Second countability under subspaces, quotients, and products
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Prove or disprove each statement:

1. If $X$ is second countable and $Y\subseteq X$, then $Y$ is second countable.
2. If $f:X\to Y$ is continuous and onto and $X$ is second countable, then $Y$ is second countable.
3. The product of an arbitrary family of second-countable spaces is second countable.
:::

::: {.solution}

## Statement 1

::: pf

::: pf-step

Let
\[
\mathcal B=\{B_1,B_2,\dots\}
\]
be a countable basis for \(X\).


::: pf-proof

Such a basis exists because \(X\) is second countable.

:::

:::

::: {.pf-step #s1-2}

Define
\[
\boxed{
\mathcal B_Y
=
\{B_n\cap Y:n\in\NN\}}.
\]


::: pf-proof

This is a countable family because it is indexed by \(\NN\).

:::

:::

::: {.pf-step #s1-3}

The family \(\mathcal B_Y\) is a basis for the subspace topology on
\(Y\).


::: pf-proof

Let \(U\subseteq Y\) be open in the subspace topology and let \(y\in U\).
Then
\[
U=V\cap Y
\]
for some open \(V\subseteq X\). Since \(\mathcal B\) is a basis for \(X\),
there exists \(B_n\in\mathcal B\) such that
\[
y\in B_n\subseteq V.
\]
Hence
\[
y\in B_n\cap Y\subseteq V\cap Y=U.
\]

:::

:::

::: {.pf-step #s1-4}

Therefore statement \(1\) is
\[
\boxed{\text{true}}.
\]


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} give a countable basis for \(Y\).

:::

:::

::: pf-step

This defines a topology on \(Y\).


::: pf-proof

The empty set is open, and \(Y\) satisfies the neighborhood condition.

Arbitrary unions of open sets are open. If the union contains \(\infty\),
one member of the union contains \(\infty\), and its rowwise cofinite tails
already verify the condition for the union.

For finite intersections, if \(U,V\) both contain \(\infty\), then for each
row \(m\), choose tail bounds \(N_m^U,N_m^V\). The intersection contains the
tail beginning at
\[
\max(N_m^U,N_m^V).
\]
All points away from \(\infty\) are isolated.

:::

:::

::: {.pf-step #s1-6}

The space \(Y\) is not first countable at \(\infty\).


::: pf-proof

Suppose
\[
U_1,U_2,\dots
\]
were a countable local base at \(\infty\).

For each \(k\), since \(U_k\) is a neighborhood of \(\infty\), its \(k\)-th
row contains all but finitely many points. Choose
\[
x_k=(k,n_k)\in U_k.
\]
Set
\[
V
=
Y-\{x_1,x_2,\dots\}.
\]
In each row \(k\), the set \(V\) omits only the one point \(x_k\), so \(V\)
is still a neighborhood of \(\infty\).

But
\[
x_k\in U_k-V,
\]
so
\[
U_k\nsubseteq V
\]
for every \(k\). This contradicts the assumption that the \(U_k\) form a
local base at \(\infty\).

:::

:::

::: {.pf-step #s1-7}

Consequently, \(Y\) is not second countable.


::: pf-proof

Every second-countable space is first countable: at a point \(y\), the basis
elements containing \(y\) form a countable local base. Step [](#s1-6){.pf-ref} shows that
this fails at \(\infty\).

:::

:::

::: pf-step

Let
\[
X
\]
be the same underlying set as \(Y\), but with the discrete topology.


::: pf-proof

The set \(Y\) is countable, so its discrete topology has the countable basis
of all singletons.

:::

:::

::: {.pf-step #s1-9}

Thus \(X\) is second countable.


::: pf-proof

The family
\[
\{\{x\}:x\in X\}
\]
is a countable basis.

:::

:::

::: {.pf-step #s1-10}

The identity map
\[
f:X\to Y
\]
is continuous and onto.


::: pf-proof

It is onto because it is the identity on the underlying set. For every open
set \(U\subseteq Y\),
\[
f^{-1}(U)=U,
\]
which is open in the discrete space \(X\).

:::

:::

::: {.pf-step #s1-11}

Therefore statement \(2\) is
\[
\boxed{\text{false}}.
\]


::: pf-proof

Steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref} give a continuous surjection from a second-countable space
onto \(Y\), while step [](#s1-7){.pf-ref} says \(Y\) is not second countable.

:::

:::

::: {.pf-step #s1-12}

Each factor \(X_i\) is second countable.


::: pf-proof

The two singletons
\[
\{0\},
\qquad
\{1\}
\]
form a finite basis.

:::

:::

::: {.pf-step #s1-13}

Fix a point
\[
x=(x_i)_{i\in I}\in X.
\]
Suppose
\[
B_1,B_2,\dots
\]
were a countable local base at \(x\).


::: pf-proof

We will derive a contradiction.

:::

:::

::: {.pf-step #s1-14}

For each \(n\), choose a basic product neighborhood
\[
C_n
\]
such that
\[
x\in C_n\subseteq B_n.
\]


::: pf-proof

Basic product neighborhoods form a basis for the product topology.

:::

:::

::: {.pf-step #s1-15}

Each \(C_n\) restricts only finitely many coordinates; let
\[
F_n\subseteq I
\]
be that finite set.


::: pf-proof

By definition of the product topology, a basic open set differs from the
whole factor in only finitely many coordinates.

:::

:::

::: {.pf-step #s1-16}

The set
\[
F=\bigcup_{n=1}^{\infty}F_n
\]
is countable.


::: pf-proof

It is a countable union of finite sets.

:::

:::

::: {.pf-step #s1-17}

Choose
\[
j\in I-F.
\]


::: pf-proof

The index set \(I\) is uncountable, while \(F\) is countable.

:::

:::

::: {.pf-step #s1-18}

Define the open neighborhood
\[
\boxed{
U
=
\{y\in X:y_j=x_j\}}
\]
of \(x\).


::: pf-proof

This is the inverse image of the open singleton \(\{x_j\}\subseteq X_j\)
under the coordinate projection
\[
\pi_j:X\to X_j.
\]

:::

:::

::: {.pf-step #s1-19}

No \(C_n\) is contained in \(U\).


::: pf-proof

Since
\[
j\notin F_n,
\]
the basic neighborhood \(C_n\) places no restriction on the \(j\)-th
coordinate. Thus it contains a point \(y\) agreeing with \(x\) on all
coordinates restricted by \(C_n\) but satisfying
\[
y_j\ne x_j.
\]
Such a point lies in \(C_n-U\).

:::

:::

::: {.pf-step #s1-20}

No \(B_n\) is contained in \(U\).


::: pf-proof

If
\[
B_n\subseteq U,
\]
then
\[
C_n\subseteq B_n\subseteq U,
\]
contradicting step [](#s1-19){.pf-ref}.

:::

:::

::: {.pf-step #s1-21}

This contradicts the assumption that \((B_n)\) is a local base at
\(x\).


::: pf-proof

Since \(U\) is a neighborhood of \(x\), some local-base element \(B_n\)
would have to satisfy
\[
x\in B_n\subseteq U.
\]
Step [](#s1-20){.pf-ref} says none does.

:::

:::

::: {.pf-step #s1-22}

Hence \(X\) is not first countable, and therefore is not second
countable.


::: pf-proof

Steps [](#s1-13){.pf-ref} through [](#s1-21){.pf-ref} show there is no countable local base at \(x\). A
second-countable space is first countable.

:::

:::

::: {.pf-step #s1-23}

Therefore statement \(3\) is
\[
\boxed{\text{false}}.
\]


::: pf-proof

The family \((X_i)_{i\in I}\) consists entirely of second-countable spaces
by step [](#s1-12){.pf-ref}, but their product is not second countable by step [](#s1-22){.pf-ref}.

:::

:::

::: pf-qed

Statement \(1\) is proved true in step [](#s1-4){.pf-ref}, while statements \(2\) and
\(3\) are disproved in steps [](#s1-11){.pf-ref} and [](#s1-23){.pf-ref}.

:::

:::

:::
