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

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.5.12,
    printed p. 38 (PDF p. 53 of tmp/sources/hartshorne-1977-algebraic-geometry.md).
    A. Shichijo, R.Hartshorne "Algebraic Geometry" 演習問題への解答 (2020/March),
    Chapter 1 section 5, Exercise 5.12, printed pp. 10--11, read in the MinerU
    extraction tmp/sources/shitijyou-ch1-section5.md. Its (a), printed p. 10, is
    the diagonalization of the symmetric form and the rescaling x_i -> a_i^{-1/2}
    x_i, which is this card's step s1. Its (b), same page, takes the route
    r < 2 gives x_0^2 or x_0^2+x_1^2, visibly reducible, and reducible with
    deg f = 2 gives two linear factors, a linear change to y_0 y_1 and then
    z_0^2+z_1^2 through y_0 = z_0+iz_1, y_1 = z_0-iz_1, so r < 2; it is not the
    card's rank count, and the earlier version of this note was wrong to say so.
    That proof is transcribed in step s2. Its (c) and (d), printed p. 11, compute
    Sing Q from the partials 2x_i and describe Q as the cone with axis Z over the
    quadric in the first r+1 variables. Checked against the book: char k != 2 is
    used where the source uses it, in the polarization of (a) and in the two
    distinct factors z_0 +- i z_1; the source asserts the irreducibility of
    x_0^2+...+x_r^2 for r >= 2 at the opening of (c) ("r >= 2 なので f は
    irreducible") rather than at the end of (b), where it proves only that a
    reducible form has r < 2.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Step s2 is now the transcription of Shichijo's Exercise 5.12(b), printed
    p. 10, with the citation on the step; the card's own route there (the rank of
    the symmetric matrix of a product of two linear forms) is replaced by the
    source's, and the one inference the source leaves implicit, that r+1 is the
    rank, is supplied from step s1. Steps s1, s3 and s4 keep the card's proofs,
    which agree with the source on pp. 10--11 and are not transcriptions of it.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    s2 repaired: the step to y_0 y_1 needs the two linear factors of f to be
    linearly independent, and the source takes that step without separating the
    case f = c l^2 of proportional factors, where no linear change produces
    y_0 y_1. The step now treats the proportional case separately: l -> x_0 by a
    linear change and x_0 -> c^{-1/2} x_0 give f = x_0^2, the normal form with
    r = 0, so r < 2 holds there too. Nothing else in s2 changed; the citation
    and printed page on the step are unaffected. The two inferences now recorded
    as supplied by this card are the rank statement from s1 and this case.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the quoted passage this pass. Printed exercise read: Hartshorne,
    Algebraic Geometry (1977), I.5.12, printed p. 38 (PDF p. 53 of the
    extraction), which does say "Assume char k != 2", so the card's hypothesis
    is the book's. Shichijo, Chapter 1 section 5, Exercise 5.12, printed p. 10
    for (a) and (b) and p. 11 for (c) and (d), read in
    tmp/sources/shitijyou-ch1-section5.md: for (b) he argues that the linear
    change preserves irreducibility, that r < 2 gives x_0^2 or x_0^2 + x_1^2,
    and that a reducible f is a product of two linear forms, hence y_0y_1 after a
    linear change and z_0^2 + z_1^2 after y_0 = z_0 + i z_1, y_1 = z_0 - i z_1,
    so r < 2. Confirmed on the printed text that his step to y_0y_1 assumes the
    two linear factors independent; the case f = c l^2 is the card's step s2,
    and his r+1 = rank is the card's step s1.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    The local reader's report: the mathematics accepted, and the one citation
    defect repaired. All three Shichijo citations on this card --- in the body
    before step s2, in step s2 itself, and in the remark --- now name the text
    version tmp/sources/shitijyou-ch1-section5.md, which is the MinerU extraction
    of tmp/sources/shitijyou-ch1-section5.pdf; before this they named only the
    URL and the printed page. Nothing in the card's argument changed.

---

::: {.problem}
Assume $\operatorname{char} k \neq 2$, and let $f$ be a nonzero homogeneous polynomial of degree $2$ in $x_0, \ldots, x_n$.

(a) Show that after a suitable linear change of variables, $f$ can be brought into the form $f = x_0^2 + \cdots + x_r^2$ for some $0 \leq r \leq n$.

(b) Show that $f$ is irreducible if and only if $r \geq 2$.

(c) Assume $r \geq 2$, and let $Q$ be the quadric hypersurface in $\PP^n$ defined by $f$.
Show that the singular locus $Z = \Sing Q$ of $Q$ is a linear variety ([[P-AGH211LINEAR]]) of dimension $n - r - 1$.
In particular, $Q$ is nonsingular if and only if $r = n$.

(d) In case $r < n$, show that $Q$ is a cone with axis $Z$ over a nonsingular quadric hypersurface $Q' \subseteq \PP^r$.

This notion of cone generalizes the one defined in [[P-AGH210CONE]].
If $Y$ is a closed subset of $\PP^r$, and if $Z$ is a linear subspace of dimension $n - r - 1$ in $\PP^n$, we embed $\PP^r$ in $\PP^n$ so that $\PP^r \intersect Z = \emptyset$, and define the \dfn{cone over $Y$ with axis $Z$} to be the union of all lines joining a point of $Y$ to a point of $Z$.
:::

::: {.solution}
Part (b) below is transcribed from A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 5, read in `tmp/sources/shitijyou-ch1-section5.md`, the MinerU extraction of `tmp/sources/shitijyou-ch1-section5.pdf`, where the citation is placed; parts (a), (c) and (d) are this card's own proofs, which the same pages reach by the same means.

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
This proves part (a).

:::

:::

::: {.pf-step #s2}

The polynomial $f=x_0^2+\cdots+x_r^2$ is irreducible exactly when
$$
\boxed{r\ge2.}
$$

::: pf-proof

This is A. Shichijo's argument, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 5, Exercise 5.12(b), read in `tmp/sources/shitijyou-ch1-section5.md`, the MinerU extraction of `tmp/sources/shitijyou-ch1-section5.pdf`, transcribed.

The linear change of variables of step [](#s1){.pf-ref} is invertible, so it does not change irreducibility, and it suffices to test the normal form $x_0^2+\cdots+x_r^2$.

If $r<2$, then $f$ is $x_0^2$ or $x_0^2+x_1^2$, and both are reducible: $x_0^2=x_0\cdot x_0$, and
$$
x_0^2+x_1^2=(x_0+ix_1)(x_0-ix_1)
$$
for an $i\in k$ with $i^2=-1$, the two factors being distinct because $\operatorname{char}k\ne2$.

Conversely suppose that $f$ is not irreducible. Since $\deg f=2$, it is a product of two linear homogeneous forms (the source refers to the footnote of its Exercise 5.9 for the factorization of a homogeneous polynomial into homogeneous factors); write $f=\ell_1\ell_2$.

If $\ell_1$ and $\ell_2$ are linearly independent, a linear change of variables, again invertible, brings them into the form $y_0y_1$, and the further change $y_0=z_0+iz_1$, $y_1=z_0-iz_1$, whose matrix has determinant $2i\ne0$, brings it into the form
$$
z_0^2+z_1^2=x_0^2+x_1^2,
$$
that is, into the normal form of step [](#s1){.pf-ref} with $r=1$.

If on the other hand $\ell_1$ and $\ell_2$ are linearly dependent, then $f=c\ell^2$ with $c\ne0$ and $\ell=\ell_2$; a linear change of variables sends $\ell$ to $x_0$, and rescaling $x_0$ by a square root of $c$, which exists because $k$ is algebraically closed, gives $f=x_0^2$, the normal form of step [](#s1){.pf-ref} with $r=0$. This is the case the source passes over when it goes from "a product of two linear forms" straight to $y_0y_1$, and it is not empty: $c\ell^2$ is a reducible quadratic of rank one. In it the conclusion $r<2$ is immediate.

In both cases the normal form has $r<2$. The source concludes $r<2$ at this point; the inference uses that $r+1$ is the rank of the symmetric matrix of $f$, which a linear change of variables preserves, and step [](#s1){.pf-ref} supplies it.

The two implications together prove part (b).

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
This proves part (c), with the usual convention that the empty singular locus corresponds to dimension $-1$ in the formula.

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
The two sets are equal, proving part (d).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the normal form, step [](#s2){.pf-ref} proves irreducibility, step [](#s3){.pf-ref} computes the singular locus, and step [](#s4){.pf-ref} proves the cone description.

:::

:::

:::

::: {.remark title="The zero quadratic"}
The source states part (a) for an arbitrary homogeneous quadratic while requiring $0\le r\le n$ in the displayed normal form.
The zero polynomial has rank zero and would correspond to an empty sum of squares, i.e. formally to $r=-1$.
Thus the stated range implicitly excludes $f=0$; the card makes that hypothesis explicit.
:::

::: {.remark title="Published solution"}
Part (b) is transcribed in step [](#s2){.pf-ref} from A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 5, Exercise 5.12, read in `tmp/sources/shitijyou-ch1-section5.md`, the MinerU extraction of `tmp/sources/shitijyou-ch1-section5.pdf`, which proves (a) and (b) there and (c) and (d). Parts (a), (c) and (d) here are the card's own proofs.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.5.12, text version `tmp/sources/hartshorne-solutions-egbert.md`, argues (a), (c) and (d) as here, and gives (b) as "for larger $r$, any factors must be linear, but then multiplying the two factors together will create terms of higher than degree $2$", which is false of a product of two linear forms. Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, Exercise I.5.12, text version `tmp/sources/hartshorne-solutions-cutrone-marshburn.md`, argue (b) by saying that in $k[x_0,\ldots,x_r]$ the form $x_0^2+\cdots+x_r^2$ "defines a nonsingular, hence irreducible, hypersurface", which is the assertion being proved.

The two inferences Shichijo's (b) leaves implicit are that $r+1$ is the rank of the symmetric matrix, which is what makes the normal form $z_0^2+z_1^2$ give $r=1<2$, and the case $f=c\ell^2$ of proportional factors, in which his step to $y_0y_1$ is not available; step [](#s1){.pf-ref} proves the first, and step [](#s2){.pf-ref} supplies the second. The source asserts the irreducibility of $x_0^2+\cdots+x_r^2$ for $r\ge2$ at the opening of its part (c).
:::
