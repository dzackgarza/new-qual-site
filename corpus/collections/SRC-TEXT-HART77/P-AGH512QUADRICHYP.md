---
schema: qual/card@1
id: P-AGH512QUADRICHYP
kind: problem
title: Rank normal form, irreducibility, and singular locus of a quadric hypersurface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quadratic Forms
  - Singularities
  - Projective Varieties
  - Cones
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all four parts and the cone definition with the retained Hartshorne I.5.12 transcription. The source implicitly requires f to be nonzero: the zero quadratic has no displayed normal form with 0 <= r <= n. The proof diagonalizes the associated symmetric form, uses matrix rank to characterize factorization, and identifies the singular axis and cone directly.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Assume $\operatorname{char} k \neq 2$, and let $f$ be a nonzero homogeneous polynomial of degree $2$ in $x_0, \ldots, x_n$.

1. Show that after a suitable linear change of variables, $f$ can be brought into the form $f = x_0^2 + \cdots + x_r^2$ for some $0 \leq r \leq n$.

2. Show that $f$ is irreducible if and only if $r \geq 2$.

3. Assume $r \geq 2$, and let $Q$ be the quadric hypersurface in $\PP^n$ defined by $f$.
   Show that the singular locus $Z = \Sing Q$ of $Q$ is a linear variety of dimension $n - r - 1$.
   In particular, $Q$ is nonsingular if and only if $r = n$.

4. In case $r < n$, show that $Q$ is a cone with axis $Z$ over a nonsingular quadric hypersurface $Q' \subseteq \PP^r$.

Here, if $Y$ is a closed subset of $\PP^r$ and $Z$ is a linear subspace of dimension $n - r - 1$ in $\PP^n$, embed $\PP^r$ in $\PP^n$ so that $\PP^r \intersect Z = \emptyset$; the *cone over $Y$ with axis $Z$* is the union of all lines joining a point of $Y$ to a point of $Z$.
:::

::: {.solution}
Let $V=k^{n+1}$.
Because $\operatorname{char}k\ne2$, the quadratic polynomial $f$ has an associated symmetric bilinear form
$$
B(u,v)=\frac12\bigl(f(u+v)-f(u)-f(v)\bigr)
$$
with $f(v)=B(v,v)$.

::: pf

::: {.pf-step #s1}

There is a basis of $V$ in which
$$
\boxed{f=x_0^2+\cdots+x_r^2}
$$
for some $0\le r\le n$.

::: pf-proof

Since $f\ne0$, there is a vector $v$ with $f(v)\ne0$.
Indeed, if $f(v)=0$ for every $v$, then polarization would give
$$
2B(u,v)=f(u+v)-f(u)-f(v)=0
$$
for all $u,v$, hence $B=0$ and $f=0$, a contradiction.

The line $kv$ is nondegenerate for $B$, so
$$
V=kv\oplus v^\perp.
$$
Thus in a basis beginning with $v$, the quadratic form is
$$
a_0x_0^2+f_1(x_1,\ldots,x_n),
\qquad a_0\ne0.
$$
Repeat on the restriction to $v^\perp$ until the remaining restriction is zero.
This gives a diagonal form
$$
a_0x_0^2+\cdots+a_rx_r^2
$$
with every $a_i\ne0$.
Since $k$ is algebraically closed, choose square roots $b_i^2=a_i$ and rescale $x_i$ by $b_i$.
The resulting form is the displayed sum of squares.
The number $r+1$ is the rank of the symmetric matrix of $B$, so it is independent of the choices.
This proves part (1).

:::

:::

::: {.pf-step #s2}

The polynomial $f=x_0^2+\cdots+x_r^2$ is irreducible exactly when
$$
\boxed{r\ge2.}
$$

::: pf-proof

If $r=0$, then $f=x_0^2$ is reducible.
If $r=1$, algebraic closedness gives an element $i\in k$ with $i^2=-1$, and
$$
x_0^2+x_1^2=(x_0+i x_1)(x_0-i x_1).
$$
The two factors are distinct because $\operatorname{char}k\ne2$.

Conversely, suppose $r\ge2$ and $f$ were reducible.
As a homogeneous quadratic, it would factor as a product of two nonzero linear forms
$$
f=\ell m.
$$
Write their coefficient column vectors as $a,b\in k^{n+1}$.
The symmetric matrix of the quadratic form $\ell m$ is
$$
\frac12(ab^t+ba^t),
$$
whose image is contained in the span of $a$ and $b$ and therefore has rank at most two.
But the matrix of
$$
x_0^2+\cdots+x_r^2
$$
has rank $r+1\ge3$.
This contradiction proves irreducibility for $r\ge2$, establishing part (2).

:::

:::

::: {.pf-step #s3}

Assume $r\ge2$ and put
$$
Q=V_+(x_0^2+\cdots+x_r^2)\subseteq\PP^n.
$$
Its singular locus is
$$
\boxed{\Sing Q=V_+(x_0,\ldots,x_r).}
$$

::: pf-proof

The partial derivatives of the defining quadratic are
$$
2x_0,\ldots,2x_r,0,\ldots,0.
$$
Since $2$ is invertible, they vanish simultaneously exactly when
$$
x_0=\cdots=x_r=0.
$$
Every such projective point automatically lies on $Q$.
By the projective Jacobian criterion [[P-AGH58JACOBIANRANK]], this is precisely the singular locus.

If $r<n$, it is the projectivization of the coordinate vector subspace spanned by
$$
e_{r+1},\ldots,e_n,
$$
so it is a linear variety of dimension
$$
n-r-1
$$
by [[P-AGH211LINEAR]].
If $r=n$, the displayed simultaneous equations have no projective solution, so the singular locus is empty.
Consequently
$$
\boxed{Q\text{ is nonsingular }\Longleftrightarrow r=n.}
$$
This proves part (3), with the usual convention that the empty singular locus corresponds to dimension $-1$ in the formula.

:::

:::

::: {.pf-step #s4}

If $r<n$, let
$$
Q'=V_+(x_0^2+\cdots+x_r^2)\subseteq\PP^r
$$
and
$$
Z=V_+(x_0,\ldots,x_r)\subseteq\PP^n.
$$
Then $Q$ is exactly the cone over $Q'$ with axis $Z$.

::: pf-proof

Embed
$$
\PP^r=V_+(x_{r+1},\ldots,x_n)
$$
in $\PP^n$.
It is disjoint from $Z$.
The quadratic $Q'$ has full rank $r+1$ on this $\PP^r$, so step [](#s3){.pf-ref} applied there shows that $Q'$ is nonsingular.

Take a point
$$
q=[a_0:\cdots:a_r:0:\cdots:0]\in Q'
$$
and a point
$$
z=[0:\cdots:0:b_{r+1}:\cdots:b_n]\in Z.
$$
Every point on their joining line has coordinates
$$
[\lambda a_0:\cdots:\lambda a_r:
\mu b_{r+1}:\cdots:\mu b_n].
$$
Substitution into the equation of $Q$ gives
$$
\lambda^2(a_0^2+\cdots+a_r^2)=0,
$$
so the whole line lies in $Q$.
Thus the cone described in the statement is contained in $Q$.

Conversely, let
$$
p=[a_0:\cdots:a_r:b_{r+1}:\cdots:b_n]\in Q.
$$
If all $a_i$ vanish, then $p\in Z$.
Otherwise
$$
q=[a_0:\cdots:a_r]\in Q'
$$
because the equation of $Q$ only involves the $a_i$.
If all $b_j$ vanish, then $p=q\in Q'$.
Otherwise let
$$
z=[b_{r+1}:\cdots:b_n]\in Z.
$$
The point $p$ lies on the line joining $q$ and $z$.
Hence every point of $Q$ lies in the cone.
The two sets are equal, proving part (4).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the normal form, step [](#s2){.pf-ref} proves irreducibility, step [](#s3){.pf-ref} computes the singular locus, and step [](#s4){.pf-ref} proves the cone description.

:::

:::

:::

::: {.remark title="The zero quadratic"}
The source states part (1) for an arbitrary homogeneous quadratic while requiring $0\le r\le n$ in the displayed normal form.
The zero polynomial has rank zero and would correspond to an empty sum of squares, i.e. formally to $r=-1$.
Thus the stated range implicitly excludes $f=0$; the card makes that hypothesis explicit.
:::
