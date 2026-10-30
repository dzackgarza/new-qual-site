---
schema: qual/card@1
id: P-KSRING17-049
kind: problem
title: Ideals maximal among non-finitely generated ideals are prime
classification:
  areas: [algebra]
  topics:
  - Prime Ideals
  - Zorn's Lemma
  - Finitely Generated Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 49 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with identity and let U be maximal among non-finitely generated ideals of R. Prove U is a prime ideal.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The ideal $U$ is proper.


::: pf-proof

The whole ring is the principal ideal
$$
R=(1),
$$
so it is finitely generated. Since $U$ is assumed not finitely generated,
$$
U\ne R.
$$

:::

:::

::: {.pf-step #s1-2}

Suppose
$$
ab\in U
$$
and
$$
a\notin U.
$$
Then
$$
U+(a)
$$
properly contains $U$ and is finitely generated.


::: pf-proof

Because
$$
a\notin U,
$$
one has
$$
U\subsetneq U+(a).
$$
By maximality of $U$ among non-finitely generated ideals, every ideal properly containing $U$ is finitely generated. Hence
$$
U+(a)
$$
is finitely generated.

:::

:::

::: {.pf-step #s1-3}

There exist
$$
u_1,\ldots,u_r\in U
$$
such that
$$
U+(a)
=
(u_1,\ldots,u_r,a).
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, choose generators
$$
y_1,\ldots,y_r
$$
for
$$
U+(a).
$$
Each generator can be written
$$
y_i=u_i+c_i a
$$
with
$$
u_i\in U,
\qquad
c_i\in R.
$$
Then each $y_i$ lies in
$$
(u_1,\ldots,u_r,a),
$$
so
$$
U+(a)
\subseteq
(u_1,\ldots,u_r,a).
$$
Conversely,
$$
u_i=y_i-c_i a
\in
U+(a),
$$
and of course
$$
a\in U+(a).
$$
Thus equality holds.

:::

:::

::: {.pf-step #s1-4}

Define the colon ideal
$$
(U:a)
\coloneqq
\{r\in R:ra\in U\}.
$$
Then
$$
U\subseteq(U:a).
$$


::: pf-proof

If
$$
u\in U,
$$
then
$$
ua\in U
$$
because $U$ is an ideal. Hence
$$
u\in(U:a).
$$

:::

:::

::: {.pf-step #s1-5}

If, in addition,
$$
b\notin U,
$$
then
$$
U\subsetneq(U:a).
$$


::: pf-proof

The hypothesis
$$
ab\in U
$$
means exactly that
$$
b\in(U:a).
$$
If
$$
b\notin U,
$$
then the containment from step [](#s1-4){.pf-ref} is strict.

:::

:::

::: pf-step

Under the hypotheses
$$
ab\in U,
\qquad
a\notin U,
\qquad
b\notin U,
$$
the ideal
$$
(U:a)
$$
is finitely generated.


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
(U:a)
$$
properly contains $U$. Maximality of $U$ among non-finitely generated ideals therefore forces
$$
(U:a)
$$
to be finitely generated.

:::

:::

::: {.pf-step #s1-7}

Choose generators
$$
c_1,\ldots,c_s
$$
of
$$
(U:a).
$$
Then
$$
U
=
(u_1,\ldots,u_r,c_1a,\ldots,c_sa).
$$


::: pf-proof

Each displayed generator lies in $U$: the $u_i$ do by construction, and
$$
c_j\in(U:a)
$$
implies
$$
c_ja\in U.
$$
Thus
$$
(u_1,\ldots,u_r,c_1a,\ldots,c_sa)
\subseteq
U.
$$

Conversely, let
$$
x\in U.
$$
By step [](#s1-3){.pf-ref}, write
$$
x
=
\sum_{i=1}^r r_i u_i
+
ra
$$
for some
$$
r_i,r\in R.
$$
Since both
$$
x
$$
and
$$
\sum_i r_i u_i
$$
belong to $U$, their difference
$$
ra
$$
also lies in $U$. Hence
$$
r\in(U:a).
$$
Write
$$
r
=
\sum_{j=1}^s t_jc_j.
$$
Then
$$
x
=
\sum_{i=1}^r r_i u_i
+
\sum_{j=1}^s t_j(c_ja),
$$
so $x$ lies in the displayed finitely generated ideal.

:::

:::

::: {.pf-step #s1-8}

The hypotheses
$$
ab\in U,
\qquad
a\notin U,
\qquad
b\notin U
$$
are impossible.


::: pf-proof

Under those hypotheses, step [](#s1-7){.pf-ref} expresses $U$ as a finitely generated ideal, contradicting the assumption that $U$ is not finitely generated.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{U\text{ is prime}.}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} shows $U$ is proper. If
$$
ab\in U,
$$
then step [](#s1-8){.pf-ref} says it is impossible for both
$$
a\notin U
$$
and
$$
b\notin U.
$$
Hence
$$
a\in U
\quad\text{or}\quad
b\in U.
$$
This is exactly the definition of a prime ideal.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required conclusion.

:::

:::

:::
