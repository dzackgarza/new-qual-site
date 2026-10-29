---
schema: qual/card@1
id: P-WESTOP07-04
kind: problem
title: Classify a surface assembled from six labeled polygons
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $X$ be the quotient of six disjoint polygonal regions whose boundary-label words are
$$
bc^{-1}a,
\quad abc,
\quad ded^{-1}ef,
\quad fgh,
\quad g^{-1}hik,
\quad ji^{-1}jk^{-1}.
$$

1. List the compact connected surfaces up to homeomorphism.
2. Identify $X$, with justification, in terms of that classification.
:::

::: {.solution}

::: pf

::: {.pf-step #p1-s1-1}

The closed connected surfaces are classified as follows:

$$
\boxed{
S^2,
\quad
\#^g(S^1\times S^1)\ (g\ge1),
\quad
\#^k\RP^2\ (k\ge1).}
$$


::: pf-proof

The classification theorem for closed connected surfaces states that every such surface is homeomorphic to exactly one of:

1. the sphere;
2. an orientable surface of genus
$$
g\ge1,
$$
i.e. the connected sum of
$$
g
$$
tori;
3. a nonorientable surface of genus
$$
k\ge1,
$$
i.e. the connected sum of
$$
k
$$
real projective planes.

For these surfaces,
$$
\chi(\#^g T^2)=2-2g
$$
and
$$
\chi(\#^k\RP^2)=2-k.
$$

:::

:::

::: {.pf-step #p1-s1-2}

The edge labels determine
$$
\boxed{11}
$$
edge classes in the quotient.


::: pf-proof

The distinct labels are
$$
a,b,c,d,e,f,g,h,i,j,k.
$$
Each label occurs exactly twice among the six boundary words, so each pair becomes one edge in the quotient. Thus
$$
E=11.
$$

:::

:::

::: {.pf-step #p1-s1-3}

The first two triangular faces contribute exactly two vertex classes to the quotient.


::: pf-proof

Let the vertices of the first triangle
$$
bc^{-1}a
$$
be
$$
u_0,u_1,u_2
$$
in boundary order, and the vertices of the second triangle
$$
abc
$$
be
$$
v_0,v_1,v_2.
$$

Matching the two
$$
b
$$
edges identifies
$$
u_0\sim v_1,
\qquad
u_1\sim v_2.
$$
Matching the two
$$
c
$$
edges, taking the inverse orientation on the occurrence
$$
c^{-1},
$$
identifies
$$
u_2\sim v_2,
\qquad
u_1\sim v_0.
$$
Matching the two
$$
a
$$
edges identifies
$$
u_2\sim v_0,
\qquad
u_0\sim v_1.
$$
Hence
$$
u_1\sim u_2\sim v_0\sim v_2,
$$
while
$$
u_0\sim v_1
$$
forms the second class.

:::

:::

::: {.pf-step #p1-s1-4}

All vertices in the remaining four polygonal faces lie in one vertex class.


::: pf-proof

Write the third face as
$$
ded^{-1}ef.
$$
The identifications coming from the repeated
$$
d
$$
and
$$
e
$$
edges identify all five vertices of this pentagon.

Its
$$
f
$$
edge is glued to the
$$
f
$$
edge of the triangle
$$
fgh,
$$
so all vertices of that triangle join the same class after the
$$
g
$$
and
$$
h
$$
gluings with the quadrilateral
$$
g^{-1}hik.
$$
The
$$
i
$$
and
$$
k
$$
edges then glue this class to the vertices of
$$
ji^{-1}jk^{-1},
$$
and the two
$$
j
$$
edges identify the remaining vertices there.

Thus every vertex occurring in faces three through six belongs to one quotient vertex class.

:::

:::

::: {.pf-step #p1-s1-5}

Therefore the quotient has
$$
\boxed{V=3}
$$
vertices.


::: pf-proof

Steps [](#p1-s1-3){.pf-ref} through [](#p1-s1-4){.pf-ref} produce two vertex classes from the first two faces and one vertex class from the remaining four faces. No label occurs in both groups except through no edge at all, so these three classes remain distinct.

:::

:::

::: {.pf-step #p1-s1-6}

The quotient has Euler characteristic
$$
\boxed{\chi(X)=-2}.
$$


::: pf-proof

There are
$$
F=6
$$
polygonal faces, step [](#p1-s1-2){.pf-ref} gives
$$
E=11,
$$
and step [](#p1-s1-5){.pf-ref} gives
$$
V=3.
$$
Hence
$$
\chi(X)
=
V-E+F
=
3-11+6
=
-2.
$$

:::

:::

::: {.pf-step #p1-s1-7}

The surface $X$ is nonorientable.


::: pf-proof

For an orientable polygonal presentation, after orienting all faces consistently, each paired edge must occur once in each direction: the two boundary orientations induced on the glued edge are opposite.

Here the label
$$
a
$$
appears with exponent
$$
+1
$$
in both of the first two boundary words:
$$
bc^{-1}a
$$
and
$$
abc.
$$
Thus these two boundary edges are glued with the same induced boundary orientation. This creates an orientation-reversing identification, so no orientation on the quotient surface can be globally consistent.

Hence
$$
X
$$
is nonorientable.

:::

:::

::: {.pf-step #p1-s1-8}

The nonorientable genus of $X$ is
$$
\boxed{4}.
$$


::: pf-proof

By the classification theorem, a closed connected nonorientable surface of genus
$$
k
$$
has Euler characteristic
$$
2-k.
$$
Step [](#p1-s1-6){.pf-ref} gives
$$
2-k=-2,
$$
so
$$
k=4.
$$

:::

:::

::: {.pf-step #p1-s1-9}

Therefore
$$
\boxed{
X
\cong
\RP^2
\#\RP^2
\#\RP^2
\#\RP^2.}
$$


::: pf-proof

Step [](#p1-s1-7){.pf-ref} shows that $X$ is nonorientable, and step [](#p1-s1-8){.pf-ref} determines its nonorientable genus to be $4$. The classification theorem then gives the displayed homeomorphism type.

:::

:::

::: pf-qed

Step [](#p1-s1-1){.pf-ref} gives the classification list, and steps [](#p1-s1-2){.pf-ref} through [](#p1-s1-9){.pf-ref} identify the given quotient within that classification.

:::

:::

::: pf

::: {.pf-step #p2-s1-1}

The classification theorem for compact connected surfaces says that every compact connected surface is homeomorphic to exactly one of:

$$
\boxed{
\Sigma_g
=
\#^g(S^1\times S^1),
\qquad
g\ge0,}
$$
where
$$
\Sigma_0=S^2,
$$
or
$$
\boxed{
N_k
=
\#^k\RP^2,
\qquad
k\ge1.}
$$


::: pf-proof

The surfaces
$$
\Sigma_g
$$
are the compact connected orientable surfaces of genus
$$
g
$$
and satisfy
$$
\chi(\Sigma_g)=2-2g.
$$
The surfaces
$$
N_k
$$
are the compact connected nonorientable surfaces of nonorientable genus
$$
k
$$
and satisfy
$$
\chi(N_k)=2-k.
$$
The classification theorem states that orientability and Euler characteristic determine the homeomorphism type within this list.

:::

:::

::: {.pf-step #p2-s1-2}

The quotient
$$
X
$$
has two connected components.


::: pf-proof

The first two polygons have boundary words
$$
bc^{-1}a
\qquad\text{and}\qquad
abc.
$$
They involve only the labels
$$
a,b,c,
$$
so all of their edge identifications occur with each other.

The remaining four polygons have boundary words
$$
ded^{-1}ef,
\quad
fgh,
\quad
g^{-1}hik,
\quad
ji^{-1}jk^{-1},
$$
and involve only the labels
$$
d,e,f,g,h,i,j,k.
$$
Thus no edge of either of the first two polygons is identified with an edge of any of the last four.

The first two polygons are connected to each other through the paired
$$
a,b,c
$$
edges. The last four are connected successively through
$$
f,
$$
then
$$
g,h,
$$
then
$$
i,k.
$$
Hence there are exactly two connected components.

:::

:::

::: {.pf-step #p2-s1-3}

Let
$$
X_1
$$
be the component obtained from the first two triangles. It has
$$
F_1=2,
\qquad
E_1=3,
\qquad
V_1=2.
$$


::: pf-proof

There are two polygonal faces.

The labels
$$
a,b,c
$$
each occur exactly twice, so after pairwise gluing there are three edges.

For the vertices, label the vertices of the first triangle
$$
u_0,u_1,u_2
$$
in boundary order for
$$
bc^{-1}a,
$$
and those of the second
$$
v_0,v_1,v_2
$$
in boundary order for
$$
abc.
$$
Matching the directed copies of
$$
a,b,c
$$
gives two equivalence classes:
$$
\{u_0,v_1\}
$$
and
$$
\{u_1,u_2,v_0,v_2\}.
$$
Thus
$$
V_1=2.
$$

:::

:::

::: {.pf-step #p2-s1-4}

The Euler characteristic of
$$
X_1
$$
is
$$
\boxed{\chi(X_1)=1}.
$$


::: pf-proof

By step [](#p2-s1-3){.pf-ref},
$$
\chi(X_1)
=
V_1-E_1+F_1
=
2-3+2
=1.
$$

:::

:::

::: {.pf-step #p2-s1-5}

The component
$$
X_1
$$
is nonorientable.


::: pf-proof

Suppose the two triangular faces could be oriented compatibly.

For the
$$
a
$$
edge, the two occurrences have the same direction in the displayed words. To make the induced boundary orientations opposite after gluing, the two faces would therefore have to be assigned opposite orientations.

The same conclusion follows from the
$$
b
$$
edge.

But the two
$$
c
$$
occurrences have opposite signs:
$$
c^{-1}
$$
in the first face and
$$
c
$$
in the second. Compatibility along this edge would require the two faces to have the same orientation.

These requirements contradict each other. Hence
$$
X_1
$$
is nonorientable.

:::

:::

::: {.pf-step #p2-s1-6}

Therefore
$$
\boxed{
X_1\cong\RP^2}.
$$


::: pf-proof

By steps [](#p2-s1-4){.pf-ref} through [](#p2-s1-5){.pf-ref},
$$
X_1
$$
is a compact connected nonorientable surface with
$$
\chi(X_1)=1.
$$
For
$$
N_k,
$$
$$
\chi(N_k)=2-k.
$$
Thus
$$
2-k=1,
$$
so
$$
k=1.
$$
Hence
$$
X_1\cong N_1=\RP^2.
$$

:::

:::

::: {.pf-step #p2-s1-7}

Let
$$
X_2
$$
be the component obtained from the last four polygons. It has
$$
F_2=4,
\qquad
E_2=8,
\qquad
V_2=1.
$$


::: pf-proof

There are four polygonal faces.

The labels
$$
d,e,f,g,h,i,j,k
$$
each occur exactly twice, giving eight quotient edges.

Tracing the endpoint identifications from the paired directed edges shows that all sixteen polygon vertices lie in a single equivalence class. Concretely, the self-pairings of
$$
d,e
$$
identify all vertices of the first of these four polygons; the
$$
f
$$
pairing brings in the vertices of the next polygon; the
$$
g,h
$$
pairings bring in the third; and the
$$
i,k
$$
pairings bring in the fourth. Hence
$$
V_2=1.
$$

:::

:::

::: {.pf-step #p2-s1-8}

The Euler characteristic of
$$
X_2
$$
is
$$
\boxed{\chi(X_2)=-3}.
$$


::: pf-proof

By step [](#p2-s1-7){.pf-ref},
$$
\chi(X_2)
=
V_2-E_2+F_2
=
1-8+4
=
-3.
$$

:::

:::

::: {.pf-step #p2-s1-9}

The component
$$
X_2
$$
is nonorientable.


::: pf-proof

In the polygon with boundary word
$$
ded^{-1}ef,
$$
the two occurrences of
$$
e
$$
have the same direction.

They are edges of the same face. Reversing the orientation of that face reverses both induced edge orientations simultaneously, so the two copies of
$$
e
$$
still have the same induced direction. But an orientation on the quotient surface would require the two boundary orientations to be opposite along an identified edge.

Thus no global orientation is possible. Hence
$$
X_2
$$
is nonorientable.

:::

:::

::: {.pf-step #p2-s1-10}

Therefore
$$
\boxed{
X_2
\cong
N_5
=
\#^5\RP^2}.
$$


::: pf-proof

By steps [](#p2-s1-8){.pf-ref} through [](#p2-s1-9){.pf-ref},
$$
X_2
$$
is compact, connected, nonorientable, and has Euler characteristic
$$
-3.
$$
For
$$
N_k,
$$
$$
\chi(N_k)=2-k.
$$
Thus
$$
2-k=-3,
$$
so
$$
k=5.
$$

:::

:::

::: {.pf-step #p2-s1-11}

The complete quotient is
$$
\boxed{
X
\cong
\RP^2
\sqcup
\left(
\#^5\RP^2
\right)}.
$$


::: pf-proof

Step [](#p2-s1-2){.pf-ref} gives exactly two components. Steps [](#p2-s1-6){.pf-ref} and [](#p2-s1-10){.pf-ref} identify them.

:::

:::

::: pf-qed

Step [](#p2-s1-1){.pf-ref} lists the compact connected surfaces, and step [](#p2-s1-11){.pf-ref} identifies the quotient in that classification.

:::

:::

:::
