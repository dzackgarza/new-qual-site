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
\[
bc^{-1}a,
\quad abc,
\quad ded^{-1}ef,
\quad fgh,
\quad g^{-1}hik,
\quad ji^{-1}jk^{-1}.
\]

1. List the compact connected surfaces up to homeomorphism.
2. Identify $X$, with justification, in terms of that classification.
:::

::: {.solution}
<1>1. The classification theorem for compact connected surfaces says that every compact connected surface is homeomorphic to exactly one of:

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
\#^k\mathbb{RP}^2,
\qquad
k\ge1.}
$$

::: {.proof}
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

<1>2. The quotient
$$
X
$$
has two connected components.

::: {.proof}
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

<1>3. Let
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

::: {.proof}
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

<1>4. The Euler characteristic of
$$
X_1
$$
is
$$
\boxed{\chi(X_1)=1}.
$$

::: {.proof}
By step <1>3,
$$
\chi(X_1)
=
V_1-E_1+F_1
=
2-3+2
=1.
$$
:::

<1>5. The component
$$
X_1
$$
is nonorientable.

::: {.proof}
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

<1>6. Therefore
$$
\boxed{
X_1\cong\mathbb{RP}^2}.
$$

::: {.proof}
By steps <1>4--<1>5,
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
X_1\cong N_1=\mathbb{RP}^2.
$$
:::

<1>7. Let
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

::: {.proof}
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

<1>8. The Euler characteristic of
$$
X_2
$$
is
$$
\boxed{\chi(X_2)=-3}.
$$

::: {.proof}
By step <1>7,
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

<1>9. The component
$$
X_2
$$
is nonorientable.

::: {.proof}
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

<1>10. Therefore
$$
\boxed{
X_2
\cong
N_5
=
\#^5\mathbb{RP}^2}.
$$

::: {.proof}
By steps <1>8--<1>9,
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

<1>11. The complete quotient is
$$
\boxed{
X
\cong
\mathbb{RP}^2
\sqcup
\left(
\#^5\mathbb{RP}^2
\right)}.
$$

::: {.proof}
Step <1>2 gives exactly two components. Steps <1>6 and <1>10 identify them.
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>1 lists the compact connected surfaces, and step <1>11 identifies the quotient in that classification.
:::
:::
