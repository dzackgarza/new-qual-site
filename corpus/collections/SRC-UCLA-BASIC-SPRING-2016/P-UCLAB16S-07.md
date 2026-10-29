---
schema: qual/card@1
id: P-UCLAB16S-07
kind: problem
title: Every orthogonal matrix is a product of at most $n-1$ elementary orthogonal matrices
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
An orthogonal $n\times n$ matrix $A$ is called elementary if the corresponding linear transformation $L_A:\RR^n\to\RR^n$ fixes an $(n-2)$-dimensional subspace.

Prove that every orthogonal matrix $M$ is a product of at most $n-1$ elementary orthogonal matrices.
:::

::: {.solution}

Assume
\[
n\ge2.
\]

::: pf

::: {.pf-step #s1-1}

Let $u,v\in\RR^n$ be unit vectors.
There exists an orthogonal transformation $E$ such that
\[
Eu=v
\]
and $E$ fixes pointwise an $(n-2)$-dimensional subspace.


::: pf-proof

If
\[
u=v,
\]
take
\[
E=I.
\]
Then $E$ fixes every vector.

Suppose
\[
u\ne\pm v.
\]
The plane
\[
P=\operatorname{span}\{u,v\}
\]
has dimension $2$.
Choose an orthogonal transformation of $P$ sending $u$ to $v$, and extend it by the identity on
\[
P^\perp.
\]
The resulting transformation of $\RR^n$ is orthogonal and fixes
\[
P^\perp,
\]
which has dimension $n-2$.

Finally, suppose
\[
u=-v.
\]
Choose a unit vector
\[
w\perp u.
\]
On
\[
\operatorname{span}\{u,w\},
\]
define $E$ by
\[
Eu=-u=v,
\qquad
Ew=w,
\]
and extend by the identity on the orthogonal complement.
Again $E$ is orthogonal and fixes at least an $(n-2)$-dimensional subspace.

:::

:::

::: pf-step

We prove the theorem by induction on $n$.


::: pf-proof

The base case and induction step are established in the following steps.

:::

:::

::: {.pf-step #s1-3}

For
\[
n=2,
\]
every orthogonal matrix is elementary.


::: pf-proof

The required fixed subspace has dimension
\[
n-2=0.
\]
Every linear transformation fixes the zero subspace pointwise.
Thus every orthogonal $2\times2$ matrix is elementary, so one factor suffices:
\[
1=n-1.
\]

:::

:::

::: pf-step

Assume the result holds in dimension
\[
n-1,
\]
and let
\[
M\in O(n).
\]
Set
\[
u=Me_n.
\]
Then $u$ is a unit vector.


::: pf-proof

Since $M$ is orthogonal,
\[
\|Me_n\|
=
\|e_n\|
=1.
\]

:::

:::

::: {.pf-step #s1-5}

Choose an elementary orthogonal transformation $E$ such that
\[
Eu=e_n.
\]
Then
\[
(EM)e_n=e_n.
\]


::: pf-proof

Apply step [](#s1-1){.pf-ref} to the unit vectors $u$ and $e_n$.
Then
\[
(EM)e_n
=
E(Me_n)
=
Eu
=
e_n.
\]

:::

:::

::: {.pf-step #s1-6}

The subspace
\[
H=e_n^\perp
\]
is invariant under
\[
EM.
\]


::: pf-proof

Let
\[
F=EM.
\]
The matrix $F$ is orthogonal and satisfies
\[
Fe_n=e_n
\]
by step [](#s1-5){.pf-ref}.
Hence
\[
F^{-1}e_n=e_n.
\]
For
\[
x\in H,
\]
\[
\langle Fx,e_n\rangle
=
\langle x,F^{-1}e_n\rangle
=
\langle x,e_n\rangle
=0.
\]
Thus
\[
Fx\in H.
\]

:::

:::

::: pf-step

The restriction
\[
F|_H:H\to H
\]
is an orthogonal transformation of the $(n-1)$-dimensional space $H$.


::: pf-proof

By step [](#s1-6){.pf-ref}, the restriction is well-defined.
Since $F$ preserves the Euclidean inner product on all of $\RR^n$, its restriction preserves the inner product on $H$.

:::

:::

::: {.pf-step #s1-8}

By the induction hypothesis,
\[
F|_H
\]
is a product of at most
\[
n-2
\]
elementary orthogonal transformations of $H$.


::: pf-proof

The space $H$ has dimension
\[
n-1.
\]
Apply the induction hypothesis in that dimension.

:::

:::

::: {.pf-step #s1-9}

Extend each factor from step [](#s1-8){.pf-ref} to $\RR^n$ by fixing $e_n$.
Each extension is elementary in $\RR^n$.


::: pf-proof

An elementary orthogonal transformation of $H$ fixes pointwise a subspace of $H$ of dimension
\[
(n-1)-2=n-3.
\]
After extending by the identity on
\[
\operatorname{span}\{e_n\},
\]
the extended map fixes pointwise the direct sum of that fixed subspace with
\[
\operatorname{span}\{e_n\},
\]
whose dimension is
\[
(n-3)+1=n-2.
\]
Thus the extension is elementary in $\RR^n$.

:::

:::

::: {.pf-step #s1-10}

The matrix $F=EM$ is a product of at most
\[
n-2
\]
elementary orthogonal matrices.


::: pf-proof

The extensions from step [](#s1-9){.pf-ref} agree with $F$ on $H$ by step [](#s1-8){.pf-ref}.
They also fix $e_n$, as does $F$.
Since
\[
\RR^n
=
H\oplus\operatorname{span}\{e_n\},
\]
the product of those extensions equals $F$ on all of $\RR^n$.

:::

:::

::: {.pf-step #s1-11}

The inverse
\[
E^{-1}
\]
is elementary.


::: pf-proof

The transformation $E$ fixes pointwise some $(n-2)$-dimensional subspace $W$.
For
\[
w\in W,
\]
\[
Ew=w.
\]
Applying $E^{-1}$ gives
\[
E^{-1}w=w.
\]
Thus $E^{-1}$ fixes the same subspace pointwise.
It is orthogonal because the inverse of an orthogonal matrix is orthogonal.

:::

:::

::: {.pf-step #s1-12}

Therefore $M$ is a product of at most
\[
\boxed{n-1}
\]
elementary orthogonal matrices.


::: pf-proof

By step [](#s1-10){.pf-ref}, write
\[
EM
=
F_1\cdots F_r
\]
with
\[
r\le n-2.
\]
Then
\[
M
=
E^{-1}F_1\cdots F_r.
\]
By step [](#s1-11){.pf-ref}, $E^{-1}$ is elementary, and each $F_j$ is elementary by step [](#s1-9){.pf-ref}.
Thus the number of factors is at most
\[
1+(n-2)
=
n-1.
\]

:::

:::

::: pf-qed

The base case is step [](#s1-3){.pf-ref} and the induction step is completed in step [](#s1-12){.pf-ref}.

:::

:::

:::
