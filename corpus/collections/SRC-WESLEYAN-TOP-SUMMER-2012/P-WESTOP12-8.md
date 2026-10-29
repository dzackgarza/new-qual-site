---
schema: qual/card@1
id: P-WESTOP12-8
kind: problem
title: Mod-$2$ simplicial cohomology of the Klein bottle from a $\Delta$-complex
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $X$ be the Klein bottle.

1. Give a $\Delta$-complex structure on $X$.
2. Using that structure, compute the simplicial cohomology groups of $X$ with coefficients in $\ZZ/2\ZZ$.
:::

::: {.solution}

Write
\[
\mathbb F_2
\coloneqq
\ZZ/2\ZZ.
\]

::: pf

::: {.pf-step #s1-1}

Present the Klein bottle as a square with edge word
\[
aba^{-1}b.
\]
Triangulate the square by one diagonal, called
\[
c.
\]
Then the quotient has:

- one vertex
  \[
  v;
  \]
- three $1$-simplices
  \[
  a,b,c;
  \]
- two $2$-simplices
  \[
  \sigma_1,\sigma_2.
  \]


::: pf-proof

Take the square with vertices
\[
v_0,v_1,v_2,v_3
\]
in cyclic order and identify opposite sides in the standard Klein-bottle
pattern
\[
aba^{-1}b.
\]
All four vertices become one vertex in the quotient.

Add the diagonal from
\[
v_0
\]
to
\[
v_2.
\]
It becomes the third edge $c$.
The two triangles cut by this diagonal descend to two $2$-simplices
\[
\sigma_1,\sigma_2.
\]
This gives the desired
\[
\Delta\text{-complex}
\]
structure.

:::

:::

::: pf-step

With coefficients in
\[
\mathbb F_2,
\]
the simplicial chain groups are
\[
C_2
\cong
\mathbb F_2^2,
\qquad
C_1
\cong
\mathbb F_2^3,
\qquad
C_0
\cong
\mathbb F_2.
\]


::: pf-proof

There are exactly two $2$-simplices, three $1$-simplices, and one vertex.
The simplicial chain group over a field is the free vector space on the
simplices in that degree.

:::

:::

::: {.pf-step #s1-3}

The boundary
\[
\partial_1:
C_1\to C_0
\]
is zero.


::: pf-proof

Every edge begins and ends at the same quotient vertex $v$.
Thus for an oriented edge $e$,
\[
\partial_1 e
=
v-v
=
0.
\]
Over
\[
\mathbb F_2
\]
the same conclusion holds.

:::

:::

::: {.pf-step #s1-4}

Over
\[
\mathbb F_2,
\]
both $2$-simplices have the same boundary:
\[
\boxed{
\partial_2\sigma_1
=
a+b+c,
\qquad
\partial_2\sigma_2
=
a+b+c.
}
\]


::: pf-proof

Each triangle has three sides:
one copy of the diagonal $c$, one side identified with $a$, and one side
identified with $b$.

The two triangles differ only in orientation conventions on some boundary
edges.
Over
\[
\mathbb F_2,
\]
all signs disappear.
Thus each boundary is the sum
\[
a+b+c.
\]

:::

:::

::: pf-step

Therefore
\[
\operatorname{rank}_{\mathbb F_2}
\partial_2
=
1.
\]


::: pf-proof

The image of $\partial_2$ is the one-dimensional subspace of
\[
\mathbb F_2^3
\]
spanned by
\[
a+b+c.
\]
This vector is nonzero.

:::

:::

::: pf-step

The simplicial cochain groups are
\[
C^0
\cong
\mathbb F_2,
\qquad
C^1
\cong
\mathbb F_2^3,
\qquad
C^2
\cong
\mathbb F_2^2.
\]


::: pf-proof

Over a field,
\[
C^n
=
\operatorname{Hom}_{\mathbb F_2}
(C_n,\mathbb F_2),
\]
so the cochain groups have the same dimensions as the corresponding chain
groups.

:::

:::

::: pf-step

The coboundary
\[
\delta^0:
C^0\to C^1
\]
is zero.


::: pf-proof

The cochain differential is dual to the chain differential:
\[
\delta^0
=
\partial_1^*.
\]
Step [](#s1-3){.pf-ref} gives
\[
\partial_1=0.
\]

:::

:::

::: {.pf-step #s1-8}

In the dual bases,
\[
\delta^1:
\mathbb F_2^3
\to
\mathbb F_2^2
\]
is
\[
\boxed{
\delta^1(x,y,z)
=
(x+y+z, x+y+z).
}
\]


::: pf-proof

For a $1$-cochain
\[
\phi
\]
with values
\[
\phi(a)=x,
\qquad
\phi(b)=y,
\qquad
\phi(c)=z,
\]
one has
\[
(\delta^1\phi)(\sigma_j)
=
\phi(\partial_2\sigma_j).
\]
By step [](#s1-4){.pf-ref},
\[
\partial_2\sigma_j
=
a+b+c.
\]
Hence
\[
(\delta^1\phi)(\sigma_j)
=
x+y+z
\]
for both
\[
j=1,2.
\]

:::

:::

::: {.pf-step #s1-9}

The zeroth cohomology group is
\[
\boxed{
H^0(X;\mathbb F_2)
\cong
\mathbb F_2.
}
\]


::: pf-proof

Since
\[
\delta^0=0,
\]
\[
H^0
=
\ker\delta^0
\cong
C^0
\cong
\mathbb F_2.
\]

:::

:::

::: {.pf-step #s1-10}

The first cohomology group is
\[
\boxed{
H^1(X;\mathbb F_2)
\cong
\mathbb F_2^2.
}
\]


::: pf-proof

By step [](#s1-8){.pf-ref},
\[
\ker\delta^1
=
\{
(x,y,z):
x+y+z=0
\}.
\]
This is a two-dimensional subspace of
\[
\mathbb F_2^3.
\]

Since
\[
\operatorname{im}\delta^0=0,
\]
\[
H^1
=
\ker\delta^1/
\operatorname{im}\delta^0
\cong
\mathbb F_2^2.
\]

:::

:::

::: {.pf-step #s1-11}

The second cohomology group is
\[
\boxed{
H^2(X;\mathbb F_2)
\cong
\mathbb F_2.
}
\]


::: pf-proof

There are no $3$-simplices, so
\[
\delta^2=0.
\]
Hence
\[
H^2
=
C^2/
\operatorname{im}\delta^1.
\]

By step [](#s1-8){.pf-ref},
\[
\operatorname{im}\delta^1
=
\{
(t,t):t\in\mathbb F_2
\},
\]
which is one-dimensional.
Therefore
\[
\dim H^2
=
2-1
=
1.
\]
Thus
\[
H^2
\cong
\mathbb F_2.
\]

:::

:::

::: {.pf-step #s1-12}

All higher cohomology groups vanish.


::: pf-proof

The chosen
\[
\Delta\text{-complex}
\]
has no simplices in dimensions greater than $2$.
Therefore
\[
C^n=0
\]
for
\[
n>2.
\]

:::

:::

::: {.pf-step #s1-13}

The complete answer is
\[
\boxed{
H^n(X;\ZZ/2)
\cong
\begin{cases}
\ZZ/2,
&n=0,2,\\
(\ZZ/2)^2,
&n=1,\\
0,
&n>2.
\end{cases}
}
\]


::: pf-proof

Collect steps [](#s1-9){.pf-ref} through [](#s1-12){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the
\[
\Delta\text{-complex}
\]
structure, and step [](#s1-13){.pf-ref} gives its simplicial cohomology with
\[
\ZZ/2
\]
coefficients.

:::

:::

:::
