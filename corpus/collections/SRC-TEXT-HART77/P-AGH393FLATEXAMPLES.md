---
schema: qual/card@1
id: P-AGH393FLATEXAMPLES
kind: problem
title: Examples of flatness and nonflatness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Finite Morphisms
  - Embedded Points
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise III.9.3 and the flatness criteria preceding it in Hartshorne III.9. Part (a) is proved locally by regular parameters and the Koszul criterion for a finite module over a regular local ring. In (b) the union ring is A plus the maximal ideal as an A-module; in (c) the square-zero nilradical is the same torsion-free maximal-ideal module, so the scheme has no embedded associated primes although the morphism is not flat.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Some examples of flatness and nonflatness.

(a) If $f: X \to Y$ is a finite surjective morphism of nonsingular varieties over an algebraically closed field $k$, then $f$ is flat.

(b) Let $X$ be a union of two planes meeting at a point, each of which maps isomorphically to a plane $Y$. Show that $f$ is not flat. For example, let $Y = \Spec k[x,y]$ and
\[
X = \Spec k[x,y,z,w] / (z,w) \intersect (x+z, y+w)
.\]

(c) Again let $Y = \Spec k[x,y]$, but take $X = \Spec k[x,y,z,w] / (z^2, zw, w^2, xz - yw)$. Show that $X_{\mathrm{red}} \cong Y$ and $X$ has no embedded points, but that $f$ is not flat.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A finite surjective morphism of nonsingular varieties is flat.

::: pf-proof

Let $x\in X$, put $y=f(x)$, and write
$$
A=\OO_{Y,y},\qquad B=\OO_{X,x}.
$$
Because $f$ is finite, the local homomorphism $A\to B$ is finite.
Both rings are regular local rings because $X$ and $Y$ are nonsingular.

The finite surjective morphism is dominant, so $A\to B$ is an injective integral extension of domains.
The regular local ring $A$ is normal.
Going-up for integral extensions and going-down over the integrally closed domain $A$ show that chains of primes ending at the maximal ideal of $B$ correspond in length to chains ending at the maximal ideal of $A$.
Hence
$$
\dim A=\dim B=d.
$$
Choose a regular system of parameters
$$
t_1,\ldots,t_d
$$
for $A$.
Since $B$ is finite over $A$, the ideal
$$
(t_1,\ldots,t_d)B=\mathfrak m_AB
$$
is $\mathfrak m_B$-primary, so the images of the $t_i$ form a system of parameters of $B$.
The regular local ring $B$ is Cohen--Macaulay, hence every system of parameters is a regular sequence.
Thus
$$
t_1,\ldots,t_d
$$
is a $B$-regular sequence.

The Koszul complex on the $t_i$ is a free resolution of the residue field $k(y)$ over the regular local ring $A$.
Tensoring it with $B$ remains exact in positive degrees because the $t_i$ form a $B$-regular sequence.
Therefore
$$
\operatorname{Tor}_1^A(k(y),B)=0.
$$

Choose a minimal set of generators of the finite $A$-module $B$, giving an exact sequence
$$
0\longrightarrow K\longrightarrow A^m\longrightarrow B\longrightarrow0.
$$
The ring $A$ is noetherian, so $K$ is finite.
Tensoring with $k(y)$, minimality makes
$$
k(y)^m\longrightarrow B/\mathfrak m_AB
$$
an isomorphism, while the Tor vanishing shows that
$$
K/\mathfrak m_AK=0.
$$
Nakayama's lemma gives $K=0$.
Hence $B\cong A^m$ is free, in particular flat, over $A$.

This holds for every $x\in X$, so $f$ is flat.
This proves part (a).

:::

:::

::: {.pf-step #s2}

In part (b), with $A=k[x,y]$, the coordinate ring of $X$ is naturally
$$
R\cong A\times_k A
=\{(u,v)\in A\oplus A:u(0,0)=v(0,0)\}.
$$

::: pf-proof

Let
$$
I_1=(z,w),\qquad I_2=(x+z,y+w)
$$
in $k[x,y,z,w]$.
The two components are the planes
$$
V(I_1)\cong\AA^2_{x,y},
\qquad
V(I_2)\cong\AA^2_{x,y},
$$
and their intersection is the origin.
For a union of two closed affine subschemes, the coordinate ring is the fibre product of their coordinate rings over the coordinate ring of the intersection.
Thus
$$
k[x,y,z,w]/(I_1\cap I_2)
\cong A\times_k A,
$$
where both maps $A\to k$ evaluate at $(0,0)$.
The morphism to $Y=\Spec A$ acts diagonally on this fibre product.

:::

:::

::: {.pf-step #s3}

As an $A$-module,
$$
R\cong A\oplus\mathfrak m,
\qquad
\mathfrak m=(x,y),
$$
so the morphism in part (b) is not flat.

::: pf-proof

The isomorphism is
$$
A\times_k A\longrightarrow A\oplus\mathfrak m,
\qquad
(u,v)\longmapsto(v,u-v).
$$
The condition $u(0)=v(0)$ says exactly that $u-v\in\mathfrak m$.

If $R$ were flat over $A$, its direct summand $\mathfrak m$ would be flat.
Localize at the maximal ideal $\mathfrak m$.
The finite module $\mathfrak mA_{\mathfrak m}$ would then be finite flat over the local ring $A_{\mathfrak m}$, hence free.
It has rank one, since
$$
\mathfrak m\otimes_A k(x,y)\cong k(x,y),
$$
so it would have to be free of rank one.
But
$$
\dim_k\mathfrak m/\mathfrak m^2=2,
$$
so Nakayama's lemma says that $\mathfrak mA_{\mathfrak m}$ requires two generators and cannot be free of rank one.
This contradiction proves nonflatness in part (b).

:::

:::

::: {.pf-step #s4}

In part (c), put
$$
A=k[x,y],
\qquad
R=A[z,w]/(z^2,zw,w^2,xz-yw),
\qquad
N=(z,w)\subseteq R.
$$
Then
$$
\boxed{X_{\mathrm{red}}\cong Y}.
$$

::: pf-proof

The relations $z^2=zw=w^2=0$ give
$$
N^2=0,
$$
so $N$ is nilpotent and is contained in the nilradical.
The quotient is
$$
R/N\cong A,
$$
which is reduced.
Hence the nilradical is exactly $N$, and
$$
R_{\mathrm{red}}=R/N\cong A.
$$
Therefore $X_{\mathrm{red}}\cong\Spec A=Y$.

:::

:::

::: {.pf-step #s5}

As an $A$-module, the square-zero ideal $N$ is naturally isomorphic to the ideal $(x,y)\subseteq A$.

::: pf-proof

The elements $z,w$ generate $N$, and the only $A$-linear relation imposed by the defining ideal is
$$
xz-yw=0.
$$
Thus
$$
N\cong A^2/A(x,-y),
$$
where the standard basis maps to $z,w$.

Define
$$
A^2\longrightarrow(x,y),
\qquad
(a,b)\longmapsto ay+bx.
$$
This is surjective, and $(x,-y)$ lies in its kernel.
Conversely, if
$$
ay+bx=0,
$$
coprimality of $x$ and $y$ in the UFD $A$ gives
$$
a=xc,\qquad b=-yc
$$
for some $c\in A$.
Hence the kernel is exactly $A(x,-y)$, and
$$
N\cong(x,y).
$$
In particular $N$ is torsion-free as an $A$-module.

:::

:::

::: {.pf-step #s6}

The scheme $X$ in part (c) has no embedded points.

::: pf-proof

As an $A$-module,
$$
R\cong A\oplus N
\cong A\oplus(x,y).
$$
Both summands are torsion-free over the domain $A$, so $R$ is torsion-free as an $A$-module.
Let $\mathfrak q=\operatorname{Ann}_R(r)$ be an associated prime of $R$, with $0\ne r\in R$.
Then
$$
\mathfrak q\cap A=\operatorname{Ann}_A(r)=0,
$$
because $R$ is torsion-free over $A$.

The finite extension $A\to R$ induces the homeomorphism
$$
\Spec R\xrightarrow{\sim}\Spec A
$$
because the nilpotent ideal $N$ is the kernel of $R\to A$.
Thus the only prime of $R$ contracting to $(0)$ is the minimal prime
$$
N=(z,w).
$$
It follows that
$$
\operatorname{Ass}_R(R)=\{N\}.
$$
Hence every associated point is minimal, so $X$ has no embedded points.

:::

:::

::: {.pf-step #s7}

The morphism in part (c) is nevertheless not flat.

::: pf-proof

Step [](#s5){.pf-ref} gives
$$
R\cong A\oplus(x,y)
$$
as an $A$-module.
If $R$ were flat, the direct summand $(x,y)$ would be flat.
Step [](#s3){.pf-ref} already proves that $(x,y)$ is not flat over $A$.
Therefore $R$ is not flat over $A$, and the morphism $X\to Y$ is not flat.
This proves part (c).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (b), and steps [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (c).

:::

:::

:::
