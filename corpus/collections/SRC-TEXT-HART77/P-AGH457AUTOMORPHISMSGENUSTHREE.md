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
    group GL_3(F_2) of order 168, but the characteristic-zero Hurwitz bound
    cited in the exercise cannot be used to prove maximality there. Part (c)
    is interpreted over C, as in Hartshorne's following note.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
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

<1>1. Every automorphism $\sigma$ of a nonhyperelliptic genus-$3$ curve
$X$ is induced by a unique element of $\PGL_3$ on its canonical plane
quartic.

::: {.proof}
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

<1>2. If $\characteristic k=7$, the equation in part (b) does not define a
nonsingular genus-$3$ curve.

::: {.proof}
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

<1>3. Assume $\characteristic k\neq2,3,7$.  The Klein quartic
$$
X=V(x^3y+y^3z+z^3x)
$$
has a subgroup of automorphisms isomorphic to $\PSL_2(\FF_7)$ and therefore
of order $168$.

::: {.proof}
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

<1>4. If $\characteristic k=0$, then
$$
\Aut X\cong\PSL_2(\FF_7)
$$
and $\abs{\Aut X}=168$.

::: {.proof}
The quartic is nonsingular, so it has genus $3$.  By step <1>3 its
automorphism group contains $168$ elements.  Hurwitz's theorem from
[[P-AGH425HURWITZAUTOMORPHISMBOUND|Exercise IV.2.5]] gives
$$
\abs{\Aut X}\leq84(g-1)=168.
$$
Consequently equality holds and the subgroup in step <1>3 is the full
automorphism group.
:::

<1>5. The conclusion of part (b) also holds in characteristic $2$; the
Hurwitz-bound argument in step <1>4 is not the proof in this characteristic.

::: {.proof}
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
Thus no common zero of the partial derivatives lies on $X$.  The
characteristic-$2$ classification
of the Klein curve gives
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

<1>6. Over $\CC$, the locus of smooth plane quartics with a nontrivial
automorphism is a proper subset of the $14$-dimensional parameter space of
plane quartics.

::: {.proof}
Let
$$
V=H^0(\PP^2,\OO_{\PP^2}(4)),\qquad \PP(V)\cong\PP^{14},
$$
and let $U\subseteq\PP(V)$ be the nonempty open subset parametrizing smooth
quartics.  By step <1>1, automorphisms of the corresponding curves are
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
For every other root of unity the largest eigenspace is no larger.  Thus
these quartics sweep a locus of dimension at most
$$
4+(9-1)=12<14.
$$

If the three eigenvalues are distinct, the conjugacy class has dimension
$6$.  After dividing by one eigenvalue, sort the fifteen degree-$4$
monomials by their character under the resulting finite cyclic group.  If
three eigenvalues are distinct, no character occurs more than five times:
for order $3$ the monomials split as $5+5+5$, and identifying any further
weights would force two of the three eigenvalues to coincide.  Hence these
quartics sweep a locus of dimension at most
$$
6+(5-1)=10<14.
$$
There are only finitely many conjugacy types under consideration, so their
union has dimension at most $12$.  Its intersection with $U$ is therefore a
proper subset of $U$.
:::

<1>7. A sufficiently general genus-$3$ curve over $\CC$ has no
automorphisms except the identity.

::: {.proof}
The hyperelliptic locus in the $6$-dimensional moduli space $\mathcal M_3$
has dimension $2g-1=5$, hence is proper.  Every nonhyperelliptic genus-$3$
curve is a smooth plane quartic by its canonical embedding.  Step <1>6 shows
that the nontrivial-stabilizer locus among those plane quartics is also
proper.  Therefore outside these proper loci the automorphism group is
trivial.  This is the assertion of part (c).
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>1 proves the corrected part (a).  Steps <1>2--<1>5 prove part (b)
with the necessary characteristic-$7$ correction.  Steps <1>6--<1>7 prove
part (c) over $\CC$.
:::
:::
