---
schema: qual/card@1
id: P-AGXMISCCALCULATIONS
kind: problem
title: Oral calculations on projective space, sections and divisors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Space
  - Picard Group
  - Line Bundles
relations:
- kind: related-to
  target: T-IJW1K
- kind: related-to
  target: PR-DIVLB
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read all ten parts against the retained oral-vault transcription
    imported in 364c1b499. Checked the projective-space cohomology and Euler
    sequence calculations, the affine and toric section formulas, the
    blowup/tautological-bundle identification, the Cartier-Picard-H1
    correspondences, and the non-Cartier divisor example. The collection
    records no provenance URL, and the repository/session trace inspected
    supplied no separate original source bytes.
---

::: {.problem}
a. Show that $\Pic(\PP^1_\CC) \cong \ZZ$.

b. Compute $H^0(X, \mcf)$ for $X = \PP^1$ and $\mcf = \OO_X$ or $\OO_X(m)$; for $X = \PP^n$ and $\mcf = \OO_X(m)$ or $\Omega_{X/k}$; for the same sheaves on $X = \AA^n$; and for $X$ a toric variety and $\mcf = \OO(D)$ with $D$ a torus-invariant divisor.

c. Describe the morphisms $\PP^n \to \AA^m$.

d. For each of the following, describe its consequences and give an example and a counterexample: separated varieties and morphisms, proper varieties and morphisms, complete varieties, flat morphisms, reduced schemes, normal varieties.

e. Show that $\Bl_0 \AA^{n+1}$ is the total space of $\OO_{\PP^n}(-1)$.

f. Show that $\omega_{\PP^1} = \OO_{\PP^1}(-2)$.

g. Define the tautological bundle on $\PP^n$, and find the degree of the canonical line bundle on $\PP^1$.

h. Show that $\CaCl(X) \cong H^1(X, \OO_X^*)$ for an integral scheme $X$.

i. Produce a Weil divisor that is not Cartier.

j. How are line bundles related to Cartier divisors?
:::

::: {.remark}
Part (g) is stated in the source for $\CC\PP^n$ with the answer $-2$, which is the degree only for $n = 1$.
Part (h) is stated in the source as $\operatorname{CaDiv}(X) \cong H^1(X, \OO_X^*)$; it is the group of Cartier divisor classes, not of Cartier divisors, that is isomorphic to $\Pic(X) \cong H^1(X, \OO_X^*)$, and the isomorphism with $\Pic$ uses integrality.
:::

::: {.solution}
<1>1. (a) The degree map gives
$$
\boxed{\Pic(\PP^1_{\CC})\cong\ZZ},
$$
with $1\in\ZZ$ corresponding to $\OO_{\PP^1}(1)$.

::: {.proof}
The curve $\PP^1_\CC$ is smooth, so Cartier divisors, Weil divisors, and
line bundles have the same divisor-class group. Fix the point
$\infty=[1:0]$ and the affine coordinate $t$ on
$$
\PP^1\sm\{\infty\}\cong\AA^1.
$$
Let
$$
D=\sum_{p\in\PP^1}n_p[p]
$$
be a divisor and put
$$
d=\deg D=\sum_p n_p.
$$
For each finite point $p=a\in\CC$, the rational function $t-a$ has
divisor
$$
\div(t-a)=[a]-[\infty].
$$
Therefore
$$
D-d[\infty]
=
\sum_{a\in\CC}n_a\bigl([a]-[\infty]\bigr)
$$
is principal. Hence every divisor class is represented by
$$
d[\infty].
$$
Degree vanishes on principal divisors, so two such representatives are
linearly equivalent only when their integers agree. Thus degree is an
isomorphism
$$
\CaCl(\PP^1_\CC)\xrightarrow{\sim}\ZZ.
$$
Under the divisor-line-bundle correspondence [[PR-DIVLB]],
$$
\OO_{\PP^1}([\infty])\cong\OO_{\PP^1}(1),
$$
which gives the claimed identification with $\Pic(\PP^1_\CC)$.
:::

<1>2. (b) On projective space,
$$
\boxed{
H^0(\PP_k^n,\OO(m))
=
\begin{cases}
k[x_0,\ldots,x_n]_m,&m\ge0,\\
0,&m<0,
\end{cases}}
$$
and, for $n\ge1$,
$$
\boxed{H^0(\PP_k^n,\Omega^1_{\PP^n/k})=0}.
$$

::: {.proof}
The twisting-sheaf calculation is [[T-IJW1K]]:
$$
H^0(\PP_k^n,\OO(m))=k[x_0,\ldots,x_n]_m
$$
for $m\ge0$ and is zero for $m<0$. In particular,
$$
H^0(\PP^1,\OO)=k,
$$
and
$$
\dim_k H^0(\PP^n,\OO(m))
=
\binom{n+m}{n}
$$
when $m\ge0$.

The Euler sequence [[T-MODEULER]]
$$
0\longrightarrow\Omega^1_{\PP^n/k}
\longrightarrow
\OO(-1)^{\oplus(n+1)}
\longrightarrow
\OO
\longrightarrow0
$$
gives an injection
$$
H^0(\PP^n,\Omega^1_{\PP^n/k})
\injects
H^0(\PP^n,\OO(-1))^{\oplus(n+1)}
=0.
$$
Thus the differential sheaf has no nonzero global sections.
:::

<1>3. (b) On affine space,
$$
\boxed{H^0(\AA_k^n,\OO)=k[x_1,\ldots,x_n]}
$$
and
$$
\boxed{
H^0(\AA_k^n,\Omega^1_{\AA^n/k})
=
\bigoplus_{i=1}^n k[x_1,\ldots,x_n]\,dx_i.
}
$$
If $\OO(m)$ means the restriction of the projective twisting sheaf to the
standard affine chart $\AA^n\subseteq\PP^n$, then it is trivial there and
has the same global sections as $\OO$.

::: {.proof}
For
$$
A=k[x_1,\ldots,x_n],
$$
the affine scheme $\AA^n=\Spec A$ satisfies
$$
\Gamma(\AA^n,\OO)=A.
$$
Its module of Kähler differentials is the free $A$-module
$$
\Omega^1_{A/k}
=
\bigoplus_{i=1}^n A\,dx_i,
$$
and the associated quasicoherent sheaf has these same global sections.

There is no intrinsic affine twisting sheaf indexed by $m$. On the
standard chart $D_+(x_0)\cong\AA^n$, the projective sheaf $\OO(m)$ is
trivialized by $x_0^m$, so its restriction has global sections $A$.
:::

<1>4. (b) For a toric variety $X_\Sigma$ and a torus-invariant divisor
$$
D=\sum_{\rho\in\Sigma(1)}a_\rho D_\rho,
$$
one has
$$
\boxed{
H^0(X_\Sigma,\OO(D))
=
\bigoplus_{m\in P_D\cap M}k\chi^m,
}
$$
where
$$
P_D
=
\left\{
m\in M_\RR:
\langle m,u_\rho\rangle\ge-a_\rho
\text{ for every }\rho
\right\}.
$$

::: {.proof}
The character $\chi^m$ is a section of $\OO(D)$ exactly when
$$
\div(\chi^m)+D\ge0.
$$
Since the coefficient of $D_\rho$ in $\div(\chi^m)$ is
$$
\langle m,u_\rho\rangle,
$$
this is equivalent to the inequalities defining $P_D$. Distinct
characters are linearly independent on the dense torus, and every section
decomposes into torus weights. This is the standard toric section formula
[[D-TORQD]].
:::

<1>5. (c) Every morphism
$$
\PP_k^n\longrightarrow\AA_k^m
$$
is constant.

::: {.proof}
A morphism to
$$
\AA^m=\Spec k[t_1,\ldots,t_m]
$$
is determined by the pullbacks of the coordinate functions $t_i$, hence
by $m$ global regular functions on $\PP^n$. Step <1>2 with $m=0$ gives
$$
\Gamma(\PP^n,\OO)=k.
$$
Therefore every coordinate pullback is constant, so the morphism is
constant.
:::

<1>6. (d) The requested properties, consequences, examples, and
nonexamples are as follows.

<2>1. Separatedness is the closed-diagonal condition.

::: {.proof}
A morphism $f:X\to Y$ is separated if
$$
\Delta_f:X\longrightarrow X\times_YX
$$
is a closed immersion. Consequently, if $Y$ is separated over the base,
the graph of every morphism $X\to Y$ is closed. Every affine scheme over
a field is separated. The affine line with doubled origin is the standard
nonseparated prevariety: the two origins cannot be separated by the
diagonal.
:::

<2>2. Properness is finite type, separatedness, and universal closedness.

::: {.proof}
A proper morphism remains closed after every base change; properness is
also stable under composition and base change. Every projective morphism
is proper. The structure morphism
$$
\AA^1_k\longrightarrow\Spec k
$$
is not proper. Indeed, the morphism
$$
\Spec k((t))\longrightarrow\AA^1,
\qquad
x\longmapsto t^{-1},
$$
does not extend to $\Spec k[[t]]$, because $t^{-1}\notin k[[t]]$. This
violates the valuative criterion for properness.
:::

<2>3. A complete variety is a variety proper over its base field.

::: {.proof}
If $X$ is complete and $Y$ is a separated variety, every morphism
$f:X\to Y$ is proper: its graph is a closed immersion into $X\times Y$,
and the projection $X\times Y\to Y$ is the base change of the proper
structure morphism $X\to\Spec k$. Hence $f$ has closed image. Projective
varieties are complete; in particular $\PP^n$ is complete. The affine
line $\AA^1$ is not complete, as in step <2>2.
:::

<2>4. Flatness is flatness of the local rings over the base.

::: {.proof}
A morphism $f:X\to Y$ is flat at $x$ when
$$
\OO_{X,x}
$$
is a flat $\OO_{Y,f(x)}$-module [[D-MORFLAT]]. Thus tensoring with the
structure sheaf preserves exact sequences; for flat projective families
over a connected Noetherian base, the Hilbert polynomial of the fibres is
constant. A projection
$$
Y\times\AA^r\longrightarrow Y
$$
is flat. The blowup
$$
\Bl_0\AA^2\longrightarrow\AA^2
$$
is not flat: its fibres away from the origin are points while the fibre
over the origin is $\PP^1$ [[FE-MORNOTFLAT]].
:::

<2>5. Reducedness means that no local ring has a nonzero nilpotent.

::: {.proof}
Equivalently, an affine scheme $\Spec A$ is reduced exactly when the
nilradical of $A$ is zero. Affine space is reduced because its polynomial
ring is a domain. The scheme
$$
\Spec k[\varepsilon]/(\varepsilon^2)
$$
is not reduced because the nonzero class of $\varepsilon$ is nilpotent.
Passing from any scheme to its reduced subscheme removes precisely these
nilpotents without changing the underlying topological space.
:::

<2>6. Normality means that the local rings are integrally closed domains.

::: {.proof}
A normal scheme is integral and every local ring is integrally closed in
its fraction field [[D-QJ5M9]]. Regular schemes are normal. Thus
$\AA^n$ is normal. The cuspidal cubic
$$
\Spec k[t^2,t^3]
$$
is not normal because $t$ is integral over $k[t^2,t^3]$ but does not
belong to it; its normalization is $\Spec k[t]$. In dimension one,
normality forces the local rings to be DVRs, hence regularity.
:::

<2>7. Q.E.D.

::: {.proof}
Steps <2>1--<2>6 give a definition, a standard consequence, an example,
and a nonexample for each property requested in part (d).
:::

<1>7. (e) There is an isomorphism over $\AA^{n+1}$
$$
\boxed{
\Bl_0\AA^{n+1}
\cong
\operatorname{Tot}\bigl(\OO_{\PP^n}(-1)\bigr).
}
$$

::: {.proof}
The blowup of the origin is the incidence variety
$$
B
=
\left\{
(x,[u])\in\AA^{n+1}\times\PP^n:
x_i u_j=x_j u_i
\text{ for all }i,j
\right\}.
$$
For a point $[u]\in\PP^n$, these equations say exactly that the vector
$x\in k^{n+1}$ lies on the line represented by $[u]$.

But the tautological line bundle $\OO_{\PP^n}(-1)$ has fibre over $[u]$
equal to that very line:
$$
\operatorname{Tot}(\OO(-1))
=
\{([u],x):x\in k u\}
\subseteq
\PP^n\times\AA^{n+1}.
$$
Thus the two incidence subschemes have the same defining equations.
On the chart $u_i\ne0$, normalize $u_i=1$ and put
$$
v_j=u_j/u_i
$$
and $\lambda=x_i$; then the equations become
$$
x_j=\lambda v_j,
$$
which identifies both schemes with
$$
\Spec k[v_0,\ldots,\widehat{v_i},\ldots,v_n,\lambda].
$$
These chart identifications have the transition functions of
$\OO(-1)$, so they glue to the asserted isomorphism. Projection to $x$
is the blowdown map.
:::

<1>8. (f) The canonical line bundle of the projective line is
$$
\boxed{\omega_{\PP^1}\cong\OO_{\PP^1}(-2)}.
$$

::: {.proof}
The Euler sequence on $\PP^1$ is
$$
0
\longrightarrow
\Omega^1_{\PP^1/k}
\longrightarrow
\OO(-1)^{\oplus2}
\longrightarrow
\OO
\longrightarrow0.
$$
Taking determinants gives
$$
\det\Omega^1_{\PP^1/k}
\cong
\det(\OO(-1)^{\oplus2})
\cong
\OO(-2).
$$
Since $\PP^1$ has dimension one,
$$
\omega_{\PP^1}=\Omega^1_{\PP^1/k}.
$$
This is also the $n=1$ case of [[T-MODEULER]].
:::

<1>9. (g) The tautological line bundle on $\PP^n$ is $\OO_{\PP^n}(-1)$,
whose fibre at a point $[\ell]\in\PP^n$ is the line
$$
\ell\subseteq k^{n+1}.
$$
Moreover,
$$
\boxed{\deg\omega_{\PP^1}=-2}.
$$

::: {.proof}
The fibre description is the definition of the tautological bundle
[[D-CB9XS]]. By step <1>8,
$$
\omega_{\PP^1}\cong\OO_{\PP^1}(-2).
$$
Since
$$
\deg\OO_{\PP^1}(d)=d,
$$
its degree is $-2$.
:::

<1>10. (h) For an integral scheme $X$,
$$
\boxed{
\CaCl(X)
\cong
\Pic(X)
\cong
H^1(X,\OO_X^\times).
}
$$

::: {.proof}
Let $\mck$ be the constant sheaf of the function field $K(X)$. A Cartier
divisor is represented by local rational functions $f_i\in K(X)^\times$
whose ratios
$$
f_i/f_j
$$
are units on overlaps. These ratios are transition functions for the
invertible sheaf $\OO_X(D)$. A principal divisor gives a trivial line
bundle, so
$$
[D]\longmapsto[\OO_X(D)]
$$
defines an injection
$$
\CaCl(X)\injects\Pic(X).
$$

Conversely, if $\mcl$ is an invertible sheaf, its generic fibre is a
one-dimensional $K(X)$-vector space. Choose a nonzero rational section
$s$. On a trivializing cover, write
$$
s=f_i e_i
$$
with $f_i\in K(X)^\times$. On overlaps $f_i/f_j$ is a unit, so the
$f_i$ define a Cartier divisor whose associated line bundle is $\mcl$.
Thus $\CaCl(X)\cong\Pic(X)$; this is [[PR-DIVLB]].

Finally, a line bundle trivialized on an open cover has transition
functions
$$
g_{ij}\in\OO_X^\times(U_i\cap U_j)
$$
satisfying the cocycle identity. Changing trivializations changes the
cocycle by a coboundary, and every such cocycle glues trivial line
bundles to an invertible sheaf. Hence
$$
\Pic(X)\cong H^1(X,\OO_X^\times),
$$
as proved in [[P-AGH345PICH1]].
:::

<1>11. (i) The ruling on the quadric cone gives a Weil divisor that is
not Cartier.

::: {.proof}
Let
$$
A=k[x,y,z]/(xy-z^2),
\qquad
X=\Spec A,
$$
and let
$$
D=V(x,z).
$$
The ring $A$ is a normal two-dimensional domain [[D-5PQ5W]]. The quotient
$$
A/(x,z)\cong k[y]
$$
is a domain of dimension one, so $(x,z)$ is a height-one prime. Hence
$D$ is a prime Weil divisor.

At the vertex
$$
\mfm=(x,y,z),
$$
the ideal of $D$ is
$$
I=(x,z)A_\mfm.
$$
The relation $xy-z^2$ has degree two, so the classes of $x,y,z$ are
linearly independent in
$$
\mfm A_\mfm/\mfm^2A_\mfm.
$$
The image of $I$ in this vector space therefore has dimension two,
spanned by the classes of $x$ and $z$. A principal ideal contained in
$\mfm A_\mfm$ has image of dimension at most one. Hence $I$ is not
principal, so $D$ is not Cartier at the vertex. This is the example in
[[D-5PQ5W]].
:::

<1>12. (j) On an integral scheme, Cartier divisors modulo principal
divisors are exactly line bundles up to isomorphism; more precisely a
Cartier divisor is equivalent to a line bundle equipped with a nonzero
rational section.

::: {.proof}
For a Cartier divisor represented by rational functions $f_i$, the
transition functions
$$
f_i/f_j\in\OO_X^\times
$$
glue the local trivial bundles to $\OO_X(D)$. The rational functions
$f_i$ simultaneously determine a distinguished nonzero rational section.

Conversely, if $\mcl$ is a line bundle with nonzero rational section
$s$, choose local frames $e_i$ and write
$$
s=f_i e_i.
$$
The ratios $f_i/f_j$ are units, so the $f_i$ define a Cartier divisor.
Tensor product of line bundles corresponds to addition of divisors,
duals correspond to negatives, and changing $s$ by a global rational
function changes the divisor by a principal divisor. This is precisely
the correspondence [[PR-DIVLB]].
:::

<1>13. Q.E.D.

::: {.proof}
Steps <1>1--<1>12 answer parts (a)--(j), with part (b) divided into the
projective, affine, and toric cases and part (d) expanded into its six
requested properties.
:::
:::
