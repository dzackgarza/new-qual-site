---
schema: qual/card@1
id: P-AGXVARIDEALRADMAX
kind: problem
title: The ideal of a subset of $\AA^n$ is radical, and maximal exactly at points
classification:
  areas:
  - algebraic-geometry
  topics:
  - Radical Ideals
  - Maximal Ideals
  - Nullstellensatz
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Example 1.4 together with Definitions 1.1 and Notation 1.2
    in the recorded source. It states that for a subset Y of A^n, I(Y) is
    radical and is maximal exactly when Y is a singleton; the source gives no
    proof.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's standing base field explicit on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked radicality directly from pointwise vanishing. For maximality,
    checked both directions using evaluation at a point and the coordinate
    differences x_i-a_i; no Nullstellensatz is required.
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic zero and let
$X\subseteq\AA^n_k$. Show that $I(X)$ is radical in
$\mco(\AA^n_k)=k[x_1,\ldots,x_n]$, and maximal if and only if $X$ is a
point.
:::

::: {.solution}
Put
$$
A=k[x_1,\ldots,x_n]
$$
and
$$
I(X)
=
\{f\in A:f(a)=0\text{ for every }a\in X\}.
$$

<1>1. The ideal $I(X)$ is radical.

::: {.proof}
Let
$$
f^m\in I(X)
$$
for some integer $m\geq1$. Then for every
$$
a\in X
$$
one has
$$
0=f^m(a)=f(a)^m.
$$
Since $k$ is a field, it has no nonzero nilpotents, so
$$
f(a)=0
$$
for every $a\in X$. Hence
$$
f\in I(X).
$$
Thus
$$
\sqrt{I(X)}=I(X),
$$
so $I(X)$ is radical.
:::

<1>2. If
$$
X=\{a\},
\qquad
a=(a_1,\ldots,a_n),
$$
then
$$
I(X)
=
(x_1-a_1,\ldots,x_n-a_n)
$$
is maximal.

::: {.proof}
Evaluation at $a$ defines a surjective homomorphism
$$
\operatorname{ev}_a:A\longrightarrow k,
\qquad
f\longmapsto f(a).
$$
Its kernel is $I(\{a\})$. Hence the first isomorphism theorem gives
$$
A/I(\{a\})\cong k.
$$
Because the quotient is a field, $I(\{a\})$ is maximal.

The kernel is explicitly
$$
(x_1-a_1,\ldots,x_n-a_n),
$$
because quotienting by these generators sends every polynomial to its
constant value at $a$.
:::

<1>3. If $I(X)$ is maximal, then $X$ is a singleton.

::: {.proof}
Since a maximal ideal is proper,
$$
I(X)\ne A.
$$
But
$$
I(\varnothing)=A,
$$
so $X$ is nonempty. Choose
$$
a=(a_1,\ldots,a_n)\in X.
$$
Every polynomial vanishing on all of $X$ vanishes at $a$, hence
$$
I(X)\subseteq I(\{a\}).
$$
By step <1>2, $I(\{a\})$ is a proper ideal. Since $I(X)$ is maximal, the
inclusion forces
$$
I(X)=I(\{a\}).
$$

For each $i$,
$$
x_i-a_i\in I(\{a\})=I(X).
$$
Thus every
$$
b=(b_1,\ldots,b_n)\in X
$$
satisfies
$$
b_i-a_i=0
$$
for every $i$. Therefore $b=a$, and hence
$$
X=\{a\}.
$$
:::

<1>4. Therefore
$$
\boxed{
I(X)\text{ is maximal}
\quad\Longleftrightarrow\quad
X\text{ is a point}.
}
$$

::: {.proof}
Step <1>2 proves that a singleton has maximal vanishing ideal, and step
<1>3 proves that a maximal vanishing ideal comes from a singleton.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves radicality, and step <1>4 proves the maximality
characterization.
:::
:::
