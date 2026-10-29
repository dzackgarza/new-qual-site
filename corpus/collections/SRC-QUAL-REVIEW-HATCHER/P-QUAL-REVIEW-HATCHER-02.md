---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-02
kind: problem
title: Total Hom complexes preserve chain homotopies
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 2 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Suppose $C_*$ and $D_*$ are bounded-below chain complexes.
Form the double complex having $\operatorname{Hom}(C_i,D_j)$ in bidegree $(i,j)$, and write
\[
\underline{\operatorname{Hom}}(C_*,D_*)
\]
for its total complex.
The following facts are given:

1. If $C_*$ is free, then the functor
   \[
   D_*\longmapsto \underline{\operatorname{Hom}}(C_*,D_*)
   \]
   preserves all quasi-isomorphisms.

2. For any $D_*$, the functor
   \[
   C_*\longmapsto \underline{\operatorname{Hom}}(C_*,D_*)
   \]
   preserves chain homotopies.

Prove (2).

If
\[
H_0(C)=\ZZ,\qquad H_1(C)=\ZZ/3\oplus\ZZ,\qquad H_2(C)=\ZZ/4,\qquad H_3(C)=\ZZ/2,
\]
and
\[
H_0(D)=\ZZ/8,\qquad H_1(D)=\ZZ\oplus\ZZ/6,\qquad H_2(D)=\ZZ/2,
\]
with all other homology groups zero, determine the homology groups of $\underline{\operatorname{Hom}}(C_*,D_*)$.
Use the same circle of ideas used in proving the Künneth theorem.
:::

::: {.solution}

Use the standard homological grading on the internal Hom complex:
\[
\underline{\operatorname{Hom}}_n(C,D)
\coloneqq
\prod_i
\operatorname{Hom}(C_i,D_{i+n}),
\]
with differential
\[
\partial\phi
\coloneqq
d_D\phi-(-1)^n\phi d_C
\]
for homogeneous
\[
\phi
\in
\underline{\operatorname{Hom}}_n(C,D).
\]

The numerical part of the source requires the usual additional hypothesis
that $C_*$ is a bounded-below complex of free abelian groups, or equivalently
that the total Hom is being computed from a free model of $C_*$. Without
this hypothesis, the listed homology groups do not determine the answer.

::: pf

::: {.pf-step #s1-1}

The numerical assertion is not determined by homology for arbitrary
bounded-below chain complexes.


::: pf-proof

Consider the bounded acyclic complex
\[
A:
0
\longrightarrow
\ZZ
\xrightarrow{\times2}
\ZZ
\xrightarrow{\bmod 2}
\ZZ/2
\longrightarrow
0,
\]
concentrated in degrees
\[
2,1,0.
\]
It is exact:
\[
\ker(\ZZ\to\ZZ/2)
=
2\ZZ
=
\operatorname{im}(\times2),
\]
the first map is injective, and the last map is surjective.
Thus
\[
H_*(A)=0.
\]

Let
\[
E
\]
be the chain complex
\[
\ZZ
\]
concentrated in degree $0$.
Then
\[
\underline{\operatorname{Hom}}(A,E)
\]
has nonzero terms
\[
\ZZ
\xrightarrow{\times2}
\ZZ
\]
in degrees
\[
-1\to-2.
\]
Therefore
\[
H_{-2}
\underline{\operatorname{Hom}}(A,E)
\cong
\ZZ/2.
\]

So adding the acyclic summand $A$ to a complex does not change its homology
but can change the homology of raw total Hom.
Hence the second half of the source needs a free/projective model
hypothesis.

:::

:::

::: {.pf-step #s1-2}

Let
\[
f,g:C_*\to C'_*
\]
be chain maps that are chain-homotopic.
Choose a chain homotopy
\[
h_i:C_i\to C'_{i+1}
\]
such that
\[
f-g
=
d_{C'}h+hd_C.
\]


::: pf-proof

This is the definition of a chain homotopy between the chain maps $f$ and
$g$.

:::

:::

::: {.pf-step #s1-3}

Precomposition gives chain maps
\[
f^*,g^*:
\underline{\operatorname{Hom}}(C'_*,D_*)
\longrightarrow
\underline{\operatorname{Hom}}(C_*,D_*),
\]
defined by
\[
f^*(\phi)=\phi f,
\qquad
g^*(\phi)=\phi g.
\]


::: pf-proof

If
\[
\phi:C'_i\to D_{i+n}
\]
has degree $n$, then
\[
\phi f:C_i\to D_{i+n}
\]
has the same degree.

Since $f$ and $g$ commute with the chain differentials, the internal-Hom
differential satisfies
\[
\partial(\phi f)
=
(\partial\phi)f,
\]
and similarly for $g$.
Thus both precomposition maps are chain maps.

:::

:::

::: {.pf-step #s1-4}

Define
\[
K:
\underline{\operatorname{Hom}}_n(C'_*,D_*)
\longrightarrow
\underline{\operatorname{Hom}}_{n+1}(C_*,D_*)
\]
by
\[
\boxed{
K(\phi)
=
(-1)^n\phi h.
}
\]


::: pf-proof

The homotopy
\[
h:C_i\to C'_{i+1}
\]
raises the $C'$-index by $1$.
Thus if
\[
\phi:C'_{i+1}\to D_{i+1+n},
\]
then
\[
\phi h:C_i\to D_{i+(n+1)},
\]
so $K$ has degree $+1$ as required for a chain homotopy.

:::

:::

::: {.pf-step #s1-5}

One has
\[
\boxed{
\partial K+K\partial
=
f^*-g^*.
}
\]


::: pf-proof

Let
\[
\phi
\]
have degree $n$.
Then
\[
K(\phi)=(-1)^n\phi h.
\]
Using the internal-Hom differential,
\[
\begin{aligned}
\partial K(\phi)
&=
(-1)^n d_D\phi h
-
(-1)^{n+1}(-1)^n\phi h d_C\\
&=
(-1)^n d_D\phi h
+
\phi h d_C.
\end{aligned}
\]

Also
\[
\partial\phi
=
d_D\phi-(-1)^n\phi d_{C'}
\]
has degree $n-1$, so
\[
\begin{aligned}
K\partial(\phi)
&=
(-1)^{n-1}
\left(
d_D\phi-(-1)^n\phi d_{C'}
\right)h\\
&=
-(-1)^n d_D\phi h
+
\phi d_{C'}h.
\end{aligned}
\]
Adding gives
\[
\begin{aligned}
(\partial K+K\partial)(\phi)
&=
\phi
\bigl(
h d_C+d_{C'}h
\bigr)\\
&=
\phi(f-g)\\
&=
f^*(\phi)-g^*(\phi).
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-6}

Therefore the functor
\[
C_*
\longmapsto
\underline{\operatorname{Hom}}(C_*,D_*)
\]
sends chain-homotopic maps to chain-homotopic maps.


::: pf-proof

Step [](#s1-5){.pf-ref} explicitly constructs the required chain homotopy.
This proves assertion (2) from the source.

:::

:::

::: {.pf-step #s1-7}

Assume henceforth that $C_*$ is degreewise free.
Then, noncanonically,
\[
H_n
\underline{\operatorname{Hom}}(C_*,D_*)
\cong
\bigoplus_{j-i=n}
\operatorname{Hom}
\bigl(
H_i(C),H_j(D)
\bigr)
\oplus
\bigoplus_{j-i-1=n}
\operatorname{Ext}^1
\bigl(
H_i(C),H_j(D)
\bigr).
\]


::: pf-proof

Over
\[
\ZZ,
\]
subgroups of free abelian groups are free.
Thus a bounded-below free chain complex decomposes, up to chain homotopy,
into elementary summands representing its homology:

- a free summand
  \[
  \ZZ[i]
  \]
  for each free homology generator in degree $i$;
- a two-term free resolution
  \[
  0\to\ZZ
  \xrightarrow{\times m}
  \ZZ\to0
  \]
  in degrees
  \[
  i+1\to i
  \]
  for each
  \[
  \ZZ/m
  \]
  homology summand in degree $i$.

Step [](#s1-6){.pf-ref} allows replacement of $C_*$ by this chain-homotopy equivalent
model.
Fact (1) from the source then allows replacement of $D_*$ by a convenient
quasi-isomorphic free model.

For a free homology generator in degree $i$, total Hom contributes
\[
\operatorname{Hom}(H_i(C),H_j(D))
\]
in degree
\[
j-i.
\]

For a torsion generator, its two-term resolution contributes
\[
\operatorname{Hom}(H_i(C),H_j(D))
\]
in degree
\[
j-i
\]
and
\[
\operatorname{Ext}^1(H_i(C),H_j(D))
\]
one degree lower, namely
\[
j-i-1.
\]

Taking the direct sum over all homological degrees gives the displayed
decomposition.
This is the Hom analogue of the elementary-complex proof of the Künneth
theorem.

:::

:::

::: {.pf-step #s1-8}

The required elementary abelian-group calculations are
\[
\operatorname{Hom}(\ZZ,B)
\cong
B,
\qquad
\operatorname{Ext}^1(\ZZ,B)=0,
\]
and
\[
\operatorname{Hom}(\ZZ/m,\ZZ)=0,
\qquad
\operatorname{Ext}^1(\ZZ/m,\ZZ)
\cong
\ZZ/m,
\]
while
\[
\operatorname{Hom}
(\ZZ/m,\ZZ/n)
\cong
\ZZ/\gcd(m,n)
\]
and
\[
\operatorname{Ext}^1
(\ZZ/m,\ZZ/n)
\cong
\ZZ/\gcd(m,n).
\]


::: pf-proof

The Hom formulas are immediate.

For Ext, resolve
\[
\ZZ/m
\]
by
\[
0
\to
\ZZ
\xrightarrow{\times m}
\ZZ
\to
\ZZ/m
\to
0.
\]
Applying
\[
\operatorname{Hom}(-,B)
\]
shows
\[
\operatorname{Ext}^1(\ZZ/m,B)
\cong
B/mB.
\]
For
\[
B=\ZZ
\]
this is
\[
\ZZ/m,
\]
and for
\[
B=\ZZ/n
\]
it is
\[
\ZZ/\gcd(m,n).
\]

:::

:::

::: {.pf-step #s1-9}

In degree
\[
n=2,
\]
\[
\boxed{
H_2
\underline{\operatorname{Hom}}(C,D)
\cong
\ZZ/2.
}
\]


::: pf-proof

The only pair with
\[
j-i=2
\]
is
\[
i=0,
\qquad
j=2.
\]
Thus the Hom term is
\[
\operatorname{Hom}
(\ZZ,\ZZ/2)
\cong
\ZZ/2.
\]
There is no Ext contribution with
\[
j-i-1=2.
\]

:::

:::

::: {.pf-step #s1-10}

In degree
\[
n=1,
\]
\[
\boxed{
H_1
\underline{\operatorname{Hom}}(C,D)
\cong
\ZZ
\oplus
\ZZ/6
\oplus
\ZZ/2.
}
\]


::: pf-proof

The Hom contributions with
\[
j-i=1
\]
are
\[
\operatorname{Hom}
(H_0(C),H_1(D))
\cong
\ZZ\oplus\ZZ/6
\]
and
\[
\operatorname{Hom}
(H_1(C),H_2(D)).
\]
Now
\[
H_1(C)
=
\ZZ/3\oplus\ZZ,
\]
so
\[
\operatorname{Hom}
(H_1(C),\ZZ/2)
\cong
0\oplus\ZZ/2.
\]
There is no Ext contribution.

:::

:::

::: {.pf-step #s1-11}

In degree
\[
n=0,
\]
\[
\boxed{
H_0
\underline{\operatorname{Hom}}(C,D)
\cong
\ZZ
\oplus
\ZZ/8
\oplus
\ZZ/6
\oplus
\ZZ/3
\oplus
\ZZ/2.
}
\]


::: pf-proof

The Hom terms with
\[
j=i
\]
are:
\[
\operatorname{Hom}
(\ZZ,\ZZ/8)
\cong
\ZZ/8,
\]
\[
\operatorname{Hom}
(\ZZ/3\oplus\ZZ,
\ZZ\oplus\ZZ/6)
\cong
\ZZ/3
\oplus
\ZZ
\oplus
\ZZ/6,
\]
and
\[
\operatorname{Hom}
(\ZZ/4,\ZZ/2)
\cong
\ZZ/2.
\]

The potential Ext terms require
\[
j=i+1.
\]
The only torsion source that could contribute is
\[
\ZZ/3
\subset H_1(C)
\]
against
\[
H_2(D)=\ZZ/2,
\]
but
\[
\operatorname{Ext}^1
(\ZZ/3,\ZZ/2)
=
0.
\]
Thus there is no Ext contribution.

:::

:::

::: {.pf-step #s1-12}

In degree
\[
n=-1,
\]
\[
\boxed{
H_{-1}
\underline{\operatorname{Hom}}(C,D)
\cong
\ZZ/8
\oplus
(\ZZ/2)^3
\oplus
(\ZZ/3)^2.
}
\]


::: pf-proof

The Hom terms with
\[
j-i=-1
\]
are
\[
\operatorname{Hom}
(H_1(C),H_0(D))
\cong
\ZZ/8,
\]
\[
\operatorname{Hom}
(H_2(C),H_1(D))
\cong
\ZZ/2,
\]
and
\[
\operatorname{Hom}
(H_3(C),H_2(D))
\cong
\ZZ/2.
\]

The Ext terms satisfy
\[
j=i.
\]
They are
\[
\operatorname{Ext}^1
(\ZZ/3,
\ZZ)
\cong
\ZZ/3,
\]
\[
\operatorname{Ext}^1
(\ZZ/3,
\ZZ/6)
\cong
\ZZ/3,
\]
and
\[
\operatorname{Ext}^1
(\ZZ/4,
\ZZ/2)
\cong
\ZZ/2.
\]
Adding these summands gives the displayed group.

:::

:::

::: {.pf-step #s1-13}

In degree
\[
n=-2,
\]
\[
\boxed{
H_{-2}
\underline{\operatorname{Hom}}(C,D)
\cong
(\ZZ/4)^2
\oplus
(\ZZ/2)^3.
}
\]


::: pf-proof

The Hom terms with
\[
j-i=-2
\]
are
\[
\operatorname{Hom}
(\ZZ/4,\ZZ/8)
\cong
\ZZ/4
\]
and
\[
\operatorname{Hom}
(\ZZ/2,\ZZ/6)
\cong
\ZZ/2.
\]

The Ext terms require
\[
j=i-1.
\]
They are
\[
\operatorname{Ext}^1
(\ZZ/4,\ZZ)
\cong
\ZZ/4,
\]
\[
\operatorname{Ext}^1
(\ZZ/4,\ZZ/6)
\cong
\ZZ/2,
\]
and
\[
\operatorname{Ext}^1
(\ZZ/2,\ZZ/2)
\cong
\ZZ/2.
\]

:::

:::

::: {.pf-step #s1-14}

In degree
\[
n=-3,
\]
\[
\boxed{
H_{-3}
\underline{\operatorname{Hom}}(C,D)
\cong
\ZZ/4
\oplus
(\ZZ/2)^3.
}
\]


::: pf-proof

The Hom contribution is
\[
\operatorname{Hom}
(\ZZ/2,\ZZ/8)
\cong
\ZZ/2.
\]

The Ext contributions are
\[
\operatorname{Ext}^1
(\ZZ/4,\ZZ/8)
\cong
\ZZ/4,
\]
\[
\operatorname{Ext}^1
(\ZZ/2,\ZZ)
\cong
\ZZ/2,
\]
and
\[
\operatorname{Ext}^1
(\ZZ/2,\ZZ/6)
\cong
\ZZ/2.
\]

:::

:::

::: {.pf-step #s1-15}

In degree
\[
n=-4,
\]
\[
\boxed{
H_{-4}
\underline{\operatorname{Hom}}(C,D)
\cong
\ZZ/2.
}
\]


::: pf-proof

There is no Hom contribution.
The only Ext contribution has
\[
i=3,
\qquad
j=0,
\]
and equals
\[
\operatorname{Ext}^1
(\ZZ/2,\ZZ/8)
\cong
\ZZ/2.
\]

:::

:::

::: {.pf-step #s1-16}

All remaining homology groups vanish.


::: pf-proof

The only nonzero homology degrees of $C$ are
\[
0,1,2,3,
\]
and those of $D$ are
\[
0,1,2.
\]
Hence the differences
\[
j-i
\]
range only from
\[
-3
\]
to
\[
2,
\]
while the Ext shift
\[
j-i-1
\]
ranges only from
\[
-4
\]
to
\[
1.
\]
Steps [](#s1-9){.pf-ref} through [](#s1-15){.pf-ref} have exhausted all nonzero Hom and Ext contributions.

:::

:::

::: {.pf-step #s1-17}

Under the intended free-source hypothesis, the complete answer is
\[
\boxed{
H_n
\underline{\operatorname{Hom}}(C,D)
\cong
\begin{cases}
\ZZ/2,
&n=2,\\
\ZZ\oplus\ZZ/6\oplus\ZZ/2,
&n=1,\\
\ZZ\oplus\ZZ/8\oplus\ZZ/6
\oplus\ZZ/3\oplus\ZZ/2,
&n=0,\\
\ZZ/8\oplus(\ZZ/2)^3\oplus(\ZZ/3)^2,
&n=-1,\\
(\ZZ/4)^2\oplus(\ZZ/2)^3,
&n=-2,\\
\ZZ/4\oplus(\ZZ/2)^3,
&n=-3,\\
\ZZ/2,
&n=-4,\\
0,
&\text{otherwise}.
\end{cases}
}
\]


::: pf-proof

Collect steps [](#s1-9){.pf-ref} through [](#s1-16){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-6){.pf-ref} prove the chain-homotopy preservation assertion.
Step [](#s1-1){.pf-ref} records why the numerical half needs the missing free/projective
hypothesis.
Under that intended hypothesis, steps [](#s1-7){.pf-ref} through [](#s1-17){.pf-ref} compute all homology
groups of the total Hom complex.

:::

:::

:::
