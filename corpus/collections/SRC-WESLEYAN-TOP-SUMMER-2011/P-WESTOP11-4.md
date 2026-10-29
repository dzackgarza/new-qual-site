---
schema: qual/card@1
id: P-WESTOP11-4
kind: problem
title: Maximal ideals of rings of continuous functions on compact Hausdorff spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
For a topological space $X$, let $C(X)$ be the ring of continuous real-valued functions on $X$. For $f\in C(X)$ and $S\subseteq X$, define
\[
Z(f)=\{p\in X:f(p)=0\},
\qquad
I(S)=\{f\in C(X):S\subseteq Z(f)\}.
\]

1. Show that $I(S)$ is an ideal of $C(X)$, that
   \[
   I(S)=I(\overline S),
   \]
   and that $S_1\subseteq S_2$ implies $I(S_2)\subseteq I(S_1)$.
2. If $X$ is completely regular and $p\in X$, show that $I(\{p\})$ is a maximal ideal of $C(X)$.
3. If $X$ is compact Hausdorff and $I$ is a maximal ideal of $C(X)$, show that
   \[
   I=I(\{p\})
   \]
   for some $p\in X$.
:::

::: {.solution}

For
\[
S\subseteq X,
\]
write
\[
I(S)
=
\{f\in C(X):f|_S=0\}.
\]

::: pf

::: {.pf-step #s1-1}

The set $I(S)$ is an ideal of $C(X)$.


::: pf-proof

The zero function belongs to $I(S)$.

If
\[
f,g\in I(S),
\]
then for every
\[
x\in S,
\]
one has
\[
f(x)=g(x)=0.
\]
Hence
\[
(f-g)(x)=0,
\]
so
\[
f-g\in I(S).
\]

If
\[
h\in C(X)
\]
and
\[
f\in I(S),
\]
then for
\[
x\in S,
\]
\[
(hf)(x)
=
h(x)f(x)
=
0.
\]
Thus
\[
hf\in I(S).
\]
Therefore $I(S)$ is an ideal.

:::

:::

::: {.pf-step #s1-2}

One has
\[
\boxed{
I(S)=I(\overline S).
}
\]


::: pf-proof

Because
\[
S\subseteq\overline S,
\]
every function vanishing on $\overline S$ vanishes on $S$, so
\[
I(\overline S)
\subseteq
I(S).
\]

Conversely, let
\[
f\in I(S).
\]
Its zero set
\[
Z(f)
=
f^{-1}(\{0\})
\]
is closed because $f$ is continuous and
\[
\{0\}\subseteq\RR
\]
is closed. Since
\[
S\subseteq Z(f),
\]
closedness gives
\[
\overline S
\subseteq
Z(f).
\]
Thus $f$ vanishes on $\overline S$, so
\[
f\in I(\overline S).
\]

:::

:::

::: {.pf-step #s1-3}

If
\[
S_1\subseteq S_2,
\]
then
\[
\boxed{
I(S_2)\subseteq I(S_1).
}
\]


::: pf-proof

If
\[
f\in I(S_2),
\]
then $f$ vanishes on every point of $S_2$, and hence on every point of the
subset $S_1$. Thus
\[
f\in I(S_1).
\]

:::

:::

::: {.pf-step #s1-4}

Fix
\[
p\in X.
\]
The evaluation map
\[
\operatorname{ev}_p:C(X)\to\RR,
\qquad
\operatorname{ev}_p(f)=f(p),
\]
is a surjective ring homomorphism.


::: pf-proof

For
\[
f,g\in C(X),
\]
evaluation satisfies
\[
\operatorname{ev}_p(f+g)
=
f(p)+g(p),
\]
and
\[
\operatorname{ev}_p(fg)
=
f(p)g(p).
\]
Also,
\[
\operatorname{ev}_p(1)=1.
\]
Thus it is a unital ring homomorphism.

For any
\[
r\in\RR,
\]
the constant function
\[
c_r(x)=r
\]
lies in $C(X)$ and satisfies
\[
\operatorname{ev}_p(c_r)=r.
\]
Hence evaluation is surjective.

:::

:::

::: {.pf-step #s1-5}

The kernel of $\operatorname{ev}_p$ is
\[
I(\{p\}).
\]


::: pf-proof

By definition,
\[
f\in\ker\operatorname{ev}_p
\quad\Longleftrightarrow\quad
f(p)=0.
\]
This is exactly the condition
\[
f\in I(\{p\}).
\]

:::

:::

::: {.pf-step #s1-6}

For every topological space $X$ and every $p\in X$,
\[
\boxed{
I(\{p\})
\text{ is a maximal ideal of }C(X).
}
\]


::: pf-proof

By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} and the first isomorphism theorem,
\[
C(X)/I(\{p\})
\cong
\RR.
\]
The quotient is a field. Therefore
\[
I(\{p\})
\]
is maximal.

In particular this proves the requested assertion when $X$ is completely
regular. The complete-regularity hypothesis is stronger than needed for this
part.

:::

:::

::: {.pf-step #s1-7}

Now assume $X$ is compact Hausdorff, and let
\[
I\subset C(X)
\]
be a maximal ideal. Suppose, toward a contradiction, that the functions in
$I$ have no common zero:
\[
\bigcap_{f\in I}Z(f)
=
\varnothing.
\]
Then the open sets
\[
X\setminus Z(f),
\qquad
f\in I,
\]
cover $X$.


::: pf-proof

The displayed empty intersection means that for every
\[
x\in X
\]
there exists
\[
f\in I
\]
with
\[
f(x)\ne0.
\]
Equivalently,
\[
x\in X\setminus Z(f).
\]
Since each zero set $Z(f)$ is closed, its complement is open.

:::

:::

::: {.pf-step #s1-8}

There exist finitely many functions
\[
f_1,\dots,f_m\in I
\]
such that
\[
\bigcap_{j=1}^mZ(f_j)
=
\varnothing.
\]


::: pf-proof

By step [](#s1-7){.pf-ref}, the open family
\[
\{X\setminus Z(f):f\in I\}
\]
covers the compact space $X$. Choose a finite subcover
\[
X
=
\bigcup_{j=1}^m
\bigl(
X\setminus Z(f_j)
\bigr).
\]
Taking complements gives
\[
\bigcap_{j=1}^mZ(f_j)
=
\varnothing.
\]

:::

:::

::: {.pf-step #s1-9}

Define
\[
g
\coloneqq
\sum_{j=1}^m f_j^2.
\]
Then
\[
g\in I
\]
and
\[
g(x)>0
\qquad
(x\in X).
\]


::: pf-proof

Since
\[
f_j\in I
\]
and $I$ is an ideal,
\[
f_j^2\in I.
\]
Since ideals are closed under finite sums,
\[
g\in I.
\]

For every
\[
x\in X,
\]
step [](#s1-8){.pf-ref} says that not all
\[
f_j(x)
\]
are zero. Hence at least one square is strictly positive, so
\[
g(x)
=
\sum_{j=1}^m f_j(x)^2
>
0.
\]

:::

:::

::: {.pf-step #s1-10}

The function $g$ from step [](#s1-9){.pf-ref} is a unit in $C(X)$.


::: pf-proof

Since
\[
g(x)>0
\]
for every $x$, the reciprocal
\[
h(x)
=
\frac1{g(x)}
\]
is a well-defined continuous real-valued function on $X$.
Therefore
\[
h\in C(X)
\]
and
\[
gh=1.
\]
Thus $g$ is invertible.

:::

:::

::: {.pf-step #s1-11}

The assumption in step [](#s1-7){.pf-ref} is impossible.


::: pf-proof

By step [](#s1-9){.pf-ref},
\[
g\in I.
\]
By step [](#s1-10){.pf-ref}, there is
\[
h\in C(X)
\]
with
\[
gh=1.
\]
Since $I$ is an ideal,
\[
1=gh\in I.
\]
Then
\[
I=C(X),
\]
contradicting that a maximal ideal is proper.

:::

:::

::: {.pf-step #s1-12}

Therefore there exists
\[
p\in X
\]
such that
\[
f(p)=0
\qquad
(f\in I).
\]
Equivalently,
\[
I\subseteq I(\{p\}).
\]


::: pf-proof

Step [](#s1-11){.pf-ref} shows
\[
\bigcap_{f\in I}Z(f)
\ne
\varnothing.
\]
Choose
\[
p
\]
in this intersection. Then every $f\in I$ vanishes at $p$.

:::

:::

::: {.pf-step #s1-13}

One has
\[
\boxed{
I=I(\{p\}).
}
\]


::: pf-proof

By step [](#s1-12){.pf-ref},
\[
I\subseteq I(\{p\}).
\]
Step [](#s1-6){.pf-ref} says
\[
I(\{p\})
\]
is a maximal ideal. Since $I$ is also maximal and both are proper ideals,
the inclusion forces equality.

:::

:::

::: {.pf-step #s1-14}

Thus, for compact Hausdorff $X$, the maximal ideals of $C(X)$ are
exactly the point-evaluation ideals
\[
\boxed{
I(\{p\})
=
\{f\in C(X):f(p)=0\},
\qquad
p\in X.
}
\]


::: pf-proof

Step [](#s1-6){.pf-ref} shows every point-evaluation ideal is maximal, and step [](#s1-13){.pf-ref}
shows every maximal ideal is of this form.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} prove part (1), steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} prove part (2), and
steps [](#s1-7){.pf-ref} through [](#s1-14){.pf-ref} prove part (3).

:::

:::

:::
