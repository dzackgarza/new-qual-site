---
schema: qual/card@1
id: P-AGH457AUTOMORPHISMSGENUSTHREE
kind: problem
title: Automorphisms of genus $3$ curves and the Klein quartic with $168$ automorphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Canonical Divisor
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.5.7, the retained companion material, and the adjacent
    canonical-model and Hurwitz exercises. Two source corrections are
    necessary. Part (a) requires the curve to be nonhyperelliptic: a
    hyperelliptic genus-three curve has canonical map of degree two onto a
    conic, not a canonical embedding. In part (b), the displayed quartic is
    singular in characteristic seven (at [1:2:4]), so the hypothesis must also
    exclude characteristic seven. Characteristic two still gives the simple
    group GL_3(F_2) of order 168, but its maximality is a separate wild
    characteristic-two input. For every characteristic p>4 other than seven,
    the positive-characteristic extension recorded in IV.2.5 gives the same
    Hurwitz bound. Part (c) is interpreted over C, as in Hartshorne's following
    note.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
  note: >-
    Rechecked the banked proof against IV.5.7, the retained companion, IV.2.5,
    and the canonical-model calculations. Extended the maximality argument to
    all characteristics p>4 allowed by the corrected statement, isolated the
    characteristic-two classification input (cross-checked against Tuffery,
    Deformations de courbes avec action de groupe II, Forum Math. 8 (1996),
    205--218), and replaced the unsupported three-eigenvalue count in part (c)
    by an explicit monomial-weight bound.
---

::: {.problem}
a. Any automorphism of a curve of genus 3 is induced by an automorphism of $\PP^2$ via the canonical embedding.

b. \* Assume $\characteristic k \neq 3$. If $X$ is the curve given by
$$
x^3 y+y^3 z+z^3 x=0
$$
the group $\Aut X$ is the simple group of order 168, whose order is the maximum $84(g-1)$ allowed by (Ex. 2.5). See Burnside ($\S$ 232) or Klein.

c. \* Most curves of genus 3 have no automorphisms except the identity.

    Hint: For each $n$, count the dimension of the family of curves with an automorphism $T$ of order $n$. For example, if $n=2$, then for suitable choice of coordinates, $T$ can be written as $x \mapsto -x$, $y \mapsto y$, $z \mapsto z$. Then there is an 8-dimensional family of curves fixed by $T$; changing coordinates there is a 4-dimensional family of such $T$, so the curves having an automorphism of degree 2 form a family of dimension 12 inside the 14-dimensional family of all plane curves of degree 4.

    More generally it is true (at least over $\CC$) that for any $g \geq 3$, a "sufficiently general" curve of genus $g$ has no automorphisms except the identity; see Baily.
:::

::: {.remark title="Errata to parts (a) and (b)"}
Part (a) is correct for a nonhyperelliptic curve of genus $3$.  For a
hyperelliptic genus-$3$ curve the canonical morphism has degree $2$ onto a
conic, so there is no canonical embedding in $\PP^2$ through which to induce
the automorphism.

Part (b) must also exclude characteristic $7$.  Indeed, for
$$
F=x^3y+y^3z+z^3x
$$
one has, in characteristic $7$,
$$
F(1,2,4)=F_x(1,2,4)=F_y(1,2,4)=F_z(1,2,4)=0,
$$
so the displayed plane quartic is singular at $[1:2:4]$ and is not the
nonsingular genus-$3$ curve asserted in the exercise.  Thus the corrected
hypothesis in (b) is $\characteristic k\neq3,7$.
:::

::: {.solution}
For part (a), let $X$ be nonhyperelliptic.  For part (c) we work over
$\CC$, as in the note following the exercise.

::: pf

::: {.pf-step #s1}

Every automorphism $\sigma$ of a nonhyperelliptic genus-$3$ curve
$X$ is induced by a unique element of $\PGL_3$ on its canonical plane
quartic.

::: pf-proof

Pullback of differentials gives an invertible linear map
$$
\sigma^*:H^0(X,K_X)\longrightarrow H^0(X,K_X).
$$
The canonical morphism is functorial for this action: if
$$
\phi_K:X\longrightarrow\PP\bigl(H^0(X,K_X)^\vee\bigr),
$$
then projectivizing the dual of $\sigma^*$ gives
$$
\phi_K\circ\sigma=\PP((\sigma^*)^\vee)\circ\phi_K.
$$
Since $X$ is nonhyperelliptic and $g=3$, $\phi_K$ is an embedding into
$\PP^2$; its image has degree $\deg K_X=4$.  Hence $\sigma$ is the
restriction of the displayed projective transformation.  Uniqueness follows
because a projective transformation of $\PP^2$ fixing the plane quartic
pointwise fixes more than four points in general position and is therefore
the identity.

:::

:::

::: {.pf-step #s2}

If $\characteristic k=7$, the equation in part (b) does not define a
nonsingular genus-$3$ curve.

::: pf-proof

For
$$
F=x^3y+y^3z+z^3x
$$
the partial derivatives are
$$
F_x=3x^2y+z^3,\qquad
F_y=x^3+3y^2z,\qquad
F_z=y^3+3z^2x.
$$
At $P=[1:2:4]$ in characteristic $7$ these four polynomials have values
$$
F(P)=2+32+64=98=0,
$$
$$
F_x(P)=6+64=70=0,\qquad
F_y(P)=1+48=49=0,\qquad
F_z(P)=8+48=56=0.
$$
Thus $P$ is singular.  This proves the characteristic-$7$ correction stated
in the erratum.

:::

:::

::: {.pf-step #s3}

Assume $\characteristic k\neq2,3,7$.  The Klein quartic
$$
X=V(x^3y+y^3z+z^3x)
$$
has a subgroup of automorphisms isomorphic to $\PSL_2(\FF_7)$ and therefore
of order $168$.

::: pf-proof

Let $\zeta$ be a primitive seventh root of unity and put
$$
S=\begin{pmatrix}
\zeta&0&0\\0&\zeta^4&0\\0&0&\zeta^2
\end{pmatrix},
\qquad
T=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.
$$
Both preserve $F$: the three monomials have $S$-weight $\zeta^7=1$, and
$T$ cyclically permutes them.  The classical Klein calculation cited in the
exercise supplies the third projective transformation
$$
U=\frac1{\sqrt{-7}}
\begin{pmatrix}
a&b&c\\b&c&a\\c&a&b
\end{pmatrix},
$$
where
$$
a=\zeta-\zeta^6,\qquad
b=\zeta^2-\zeta^5,\qquad
c=\zeta^4-\zeta^3.
$$
Direct substitution gives $F\circ U=F$, and the projective transformations
$S,T,U$ satisfy the standard presentation of the simple group
$\PSL_2(\FF_7)$; in particular the group they generate has order
$$
\abs{\PSL_2(\FF_7)}
=\frac{7(7^2-1)}2
=168.
$$
Thus $\PSL_2(\FF_7)\subseteq\Aut X$.

:::

:::

::: {.pf-step #s4}

If $\characteristic k=0$, or if $\characteristic k=p>4$ with
$p\neq7$, then
$$
\Aut X\cong\PSL_2(\FF_7)
$$
and $\abs{\Aut X}=168$.

::: pf-proof

The quartic is nonsingular in these characteristics.  Indeed, a common zero
of the three partial derivatives has no zero coordinate, and multiplying
$$
z^3=-3x^2y,\qquad x^3=-3y^2z,\qquad y^3=-3z^2x
$$
would give
$$
1=-27,
$$
which is impossible unless the characteristic is $2$ or $7$.  Thus $X$ has
genus $3$.

By step [](#s3){.pf-ref} its automorphism group contains $168$ elements.  In
characteristic $0$, Hurwitz's theorem from
[[P-AGH425HURWITZAUTOMORPHISMBOUND|Exercise IV.2.5]] gives
$$
\abs{\Aut X}\leq84(g-1)=168.
$$
For $p>4$, the positive-characteristic extension stated in the same exercise
gives the identical bound, with its sole exceptional genus-$3$ characteristic
being $p=7$; that characteristic has already been excluded in step [](#s2){.pf-ref}.
Consequently equality holds in every case covered by this step, and the
subgroup in step [](#s3){.pf-ref} is the full automorphism group.

:::

:::

::: {.pf-step #s5}

The conclusion of part (b) also holds in characteristic $2$; the
Hurwitz-bound argument in step [](#s4){.pf-ref} is not the proof in this characteristic.

::: pf-proof

In characteristic $2$ the curve is nonsingular: the equations
$$
x^2y+z^3=x^3+y^2z=y^3+z^2x=0
$$
have no common zero on $X$.  Indeed, a common zero with $x=0$ would force
$z=0$ and then $y=0$.  If $x\neq0$, scale to $x=1$.  The first two equations
give $y=z^3$ and $z^7=1$, while on such a point
$$
F(1,z^3,z)=z^3+z^{10}+z^3=z^{10}\neq0.
$$
Thus no common zero of the partial derivatives lies on $X$.

The remaining full-group assertion is genuinely a wild-characteristic
classification input rather than a consequence of Hurwitz's bound.  The
classification invoked by the starred source exercise identifies the full
automorphism group of this characteristic-$2$ Klein curve as
$$
\Aut X\cong\GL_3(\FF_2)
\cong\PSL_2(\FF_7).
$$
Its order is
$$
(2^3-1)(2^3-2)(2^3-2^2)=7\cdot6\cdot4=168,
$$
and $\GL_3(\FF_2)$ is the simple group of order $168$.  This is a wild
automorphism case, so the characteristic-zero Hurwitz bound is not being
invoked.

:::

:::

::: {.pf-step #s6}

Over $\CC$, the locus of smooth plane quartics with a nontrivial
automorphism is a proper subset of the $14$-dimensional parameter space of
plane quartics.

::: pf-proof

Let
$$
V=H^0(\PP^2,\OO_{\PP^2}(4)),\qquad \PP(V)\cong\PP^{14},
$$
and let $U\subseteq\PP(V)$ be the nonempty open subset parametrizing smooth
quartics.  By step [](#s1){.pf-ref}, automorphisms of the corresponding curves are
exactly their projective stabilizers.

Every nontrivial automorphism has finite order, bounded by $168$ by
[[P-AGH425HURWITZAUTOMORPHISMBOUND|Exercise IV.2.5]].  Hence it suffices to
consider the finitely many projective conjugacy types of elements of orders
$2,\ldots,168$.  Such an element is semisimple.  If it has eigenvalue
multiplicities $2+1$, its conjugacy class in $\PGL_3$ has dimension $4$.
After scaling it has the form
$$
\operatorname{diag}(\lambda,1,1),\qquad\lambda\neq1.
$$
A quartic fixed as a zero locus must lie in one eigenspace of its action on
$V$.  For $\lambda=-1$ the largest eigenspace consists of the monomials in
which the exponent of the first variable is even and has vector-space
dimension
$$
5+3+1=9.
$$
If $m$ is the order of $\lambda$, the eigenspaces group together the
monomials whose first-variable exponents are congruent modulo $m$.  The five
possible exponents $0,1,2,3,4$ occur with multiplicities $5,4,3,2,1$.
Hence the largest eigenspace has dimension $9$ for $m=2$, $7$ for $m=3$,
$6$ for $m=4$, and $5$ for $m\geq5$.  Thus
these quartics sweep a locus of dimension at most
$$
4+(9-1)=12<14.
$$

If the three eigenvalues are distinct, the conjugacy class has dimension
$6$.  Write the eigenvalues as $\alpha,\beta,\gamma$.  Two degree-$4$
monomials whose exponent triples differ by a permutation of $(1,-1,0)$
cannot have the same weight, since their weight ratio is one of
$$
\frac\alpha\beta,\qquad
\frac\alpha\gamma,\qquad
\frac\beta\gamma,
$$
none of which is $1$.  Thus monomials of one weight form an independent set
in the triangular array of exponent triples
$$
\{(i,j,k)\in\ZZ_{\geq0}^3:i+j+k=4\},
$$
where adjacent triples differ by a permutation of $(1,-1,0)$.  A row-by-row
check of this five-row triangle shows that an independent set has at most six
vertices, and that the unique six-vertex independent set is
$$
\begin{gathered}
(4,0,0),(0,4,0),(0,0,4),\\
(2,2,0),(2,0,2),(0,2,2).
\end{gathered}
$$
These six monomials cannot all have the same weight: equality of the weights
of $x^4$, $y^4$, and $x^2y^2$ gives $\alpha^2=\beta^2$, and similarly one
gets $\alpha^2=\gamma^2$.  After scaling by $\alpha$, both remaining
eigenvalues would therefore lie in $\{1,-1\}$, contradicting the assumption
that all three eigenvalues are distinct.  Hence every eigenspace has
dimension at most $5$, and these quartics sweep a locus of dimension at most
$$
6+(5-1)=10<14.
$$
There are only finitely many conjugacy types under consideration, so their
union has dimension at most $12$.  Its intersection with $U$ is therefore a
proper subset of $U$.

:::

:::

::: {.pf-step #s7}

A sufficiently general genus-$3$ curve over $\CC$ has no
automorphisms except the identity.

::: pf-proof

The smooth plane quartics form a $14$-dimensional open subset of
$\PP(V)$.  Their stabilizers in $\PGL_3$ are finite by
[[P-AGH452AUTOMORPHISMGROUPFINITE|Exercise IV.5.2]], so the family of
isomorphism classes of nonhyperelliptic genus-$3$ curves has dimension
$$
14-\dim\PGL_3=14-8=6.
$$
Thus $\mathcal M_3$ has dimension $6$.

The hyperelliptic locus has dimension $2g-1=5$: such a curve is determined
by its unordered set of $2g+2=8$ branch points on $\PP^1$, a family of
dimension $8-\dim\PGL_2=5$.  Hence it is proper.  Every nonhyperelliptic
genus-$3$ curve is a smooth plane quartic by its canonical embedding, and
step [](#s6){.pf-ref} shows that the nontrivial-stabilizer locus among those plane
quartics is also proper.  Therefore outside these proper loci the
automorphism group is trivial.  This is the assertion of part (c).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the corrected part (a).  Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (b)
with the necessary characteristic-$7$ correction.  Steps [](#s6){.pf-ref} and [](#s7){.pf-ref} prove
part (c) over $\CC$.

:::

:::

:::
