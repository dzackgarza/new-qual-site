---
schema: qual/card@1
id: P-AGH5112NUMAMPLE
kind: problem
title: Ampleness is a numerical property but very ampleness is not
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.12, the retained Egbert companion construction, the
    Nakai--Moishezon criterion, the curve very-ampleness criterion, and the
    Jacobian dimension statement. The companion invokes ruled-surface results
    from the following section. The proof below avoids that forward dependency:
    it first constructs two degree-2g line bundles on a genus-g curve, one very
    ample and one not, then external-products them with O(1) on P^1. Their
    difference has degree zero on the curve factor, so the resulting surface
    divisors are numerically equivalent.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.1,
    exercise 1.12, printed page 368 (PDF page 383 of the extraction). Checked
    every step against the book: ampleness by Nakai-Moishezon; the closed
    immersion criterion for a complete linear system in IV.3, printed pages
    307-308, which needs h^0(L(-Z)) = h^0(L)-2 for every length-two scheme Z,
    reduced or not, which is what step s3 checks; Riemann-Roch IV.1.3, printed
    page 295; numerical equivalence as equality of intersection numbers with
    every curve, V.1, printed page 357. Searched for a published solution
    outside the twelve retained sets and found two, both defective: Algebraic
    Geometry II, National Taiwan University, 2020 Spring, Chapter V homework,
    Exercise 12, PDF p. 5 (tmp/sources/ntu-ag2-chapter5.pdf), and Yang Pi-Yeh,
    Hartshorne Solutions, exercise 5.1.12, printed p. 102
    (tmp/sources/lfwin-hartshorne-solutions.pdf). Both take D x P^1 as the
    very ample member, and D x P^1 is p_1^*D, of degree 0 on every fibre, so it
    is not ample; the card's step s5 to s8 tensor the degree-one class of P^1
    on instead. Egbert, PDF p. 261, quotes Fuentes-Pedreira for the surface
    criterion and proves only the curve comparison. Not checked: whether
    Fuentes-Pedreira's criterion could have been used, since that paper is not
    in tmp/sources.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the printed exercise at Hartshorne (1977), V.1, exercise 1.12, printed
    p. 368 (PDF p. 383), and the two published surface examples on 2026-11-16: the
    National Taiwan University set's Exercise 12 (Pei-Hsuan Chang), text version
    tmp/sources/ntu-ag2-chapter5.md, printed p. 5 of that set, and Yang Pi-Yeh,
    exercise 5.1.12. Both take the external product D x P^1 as the very ample
    member, and that is the pullback p_1^*D, whose degree on every fibre is zero,
    so it is not ample and not very ample; a very ample divisor meets every curve
    positively, a positive multiple of it being a hyperplane section. The
    construction therefore fails at the one point the exercise asks for, and
    neither set is a complete published argument for the surface example. Their
    curve argument, that on a curve of genus g a degree-2g divisor is very ample
    exactly when it is not of the form K_C + P + Q, is correct and is the card's
    step s2 to s4. Steps s5 to s8 add the degree-one class of P^1 on both sides,
    which makes the fibre degree one and leaves the failure of very ampleness in
    the curve factor, where step s7 reads it off a fibre. The question this event
    left open, whether Fuentes and Pedreira, The Projective Theory of Ruled
    Surfaces, Theorem 3.9, could supply the surface criterion, is settled in the
    event below: their Theorem 3.9(3) does supply it for a decomposable ruled
    surface, and their Corollary 2.13 is proved, its converse following from
    Proposition 2.3 with Theorem 2.11.
---

::: {.problem}
If $D$ is an ample divisor on the surface $X$, and $D^{\prime} \equiv D$, then $D^{\prime}$ is also ample.
Give an example to show, however, that if $D$ is very ample, $D^{\prime}$ need not be very ample.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Ampleness of divisors on a smooth projective surface depends only on
numerical equivalence.

::: pf-proof

Let $D$ be ample and suppose
$$
D'\equiv D.
$$
Numerical equivalence preserves all intersection numbers, so
$$
(D')^2=D^2>0
$$
and, for every irreducible curve $C\subseteq X$,
$$
D'\cdot C=D\cdot C>0.
$$
The two inequalities on the right are exactly the Nakai--Moishezon criterion
[[T-SRFNAKAI]]. Hence
$$
\boxed{D'\text{ is ample}.}
$$

:::

:::

::: {.pf-step #s2}

Let $C$ be any nonsingular projective curve of genus $g\geq3$. There is
a degree-$2g$ line bundle $L$ on $C$ such that
$$
L\not\cong K_C(P+Q)
$$
for every pair of points $P,Q\in C$, allowing $P=Q$.

::: pf-proof

The variety $\Pic^{2g}(C)$ is a translate of the Jacobian, hence is
irreducible of dimension $g$ by [[T-CRVJACFUN]]. Consider the morphism
$$
\Sym^2C\longrightarrow\Pic^{2g}(C),
\qquad
P+Q\longmapsto K_C(P+Q).
$$
Its source is projective of dimension two, so its image is closed and has
dimension at most two. Since $g\geq3$, this image is a proper subset of the
$g$-dimensional variety $\Pic^{2g}(C)$. Choose $L$ outside that image.

:::

:::

::: {.pf-step #s3}

The line bundle $L$ chosen in step [](#s2){.pf-ref} is very ample.

::: pf-proof

Since
$$
\deg L=2g>2g-2,
$$
Riemann--Roch gives
$$
h^0(C,L)=2g+1-g=g+1.
$$
Let $Z=P+Q$ be any effective divisor of degree two, including the case
$P=Q$. Riemann--Roch for $L(-Z)$ gives
$$
h^0(C,L(-Z))
=
g-1+h^0\qty(C,K_C\tensor L^{-1}(Z)).
$$
The line bundle
$$
K_C\tensor L^{-1}(Z)
$$
has degree zero. A degree-zero line bundle on an integral projective curve has
a nonzero global section only when it is trivial. By the choice of $L$ in
step [](#s2){.pf-ref}, it is never trivial. Therefore
$$
h^0(C,L(-Z))=g-1=h^0(C,L)-2
$$
for every length-two effective divisor $Z$.

Thus the complete linear system of $L$ separates every pair of points and
every tangent direction. The closed-immersion criterion for a complete linear
system, [[T-DIVMAPPN]], gives
$$
\boxed{L\text{ is very ample}.}
$$

:::

:::

::: {.pf-step #s4}

For any points $P,Q\in C$, the degree-$2g$ line bundle
$$
L'=K_C(P+Q)
$$
is not very ample.

::: pf-proof

Again $\deg L'=2g$, so Riemann--Roch gives
$$
h^0(C,L')=g+1.
$$
But
$$
L'(-P-Q)\cong K_C,
$$
and therefore
$$
h^0(C,L'(-P-Q))=h^0(C,K_C)=g.
$$
For a very ample line bundle, imposing the length-two subscheme $P+Q$ would
lower $h^0$ by two, giving $g-1$. Here it lowers $h^0$ by only one. Hence the
complete linear system fails to separate the corresponding two points or
tangent direction, and
$$
\boxed{L'\text{ is not very ample}.}
$$

:::

:::

::: {.pf-step #s5}

Put
$$
X=C\times\PP^1
$$
with projections $p_1,p_2$, and define
$$
M=p_1^*L\tensor p_2^*\OO_{\PP^1}(1),
\qquad
M'=p_1^*L'\tensor p_2^*\OO_{\PP^1}(1).
$$
Then
$$
M\equiv M'
$$
numerically on $X$.

::: pf-proof

Their quotient is
$$
M\tensor(M')^{-1}
=
p_1^*(L\tensor(L')^{-1}).
$$
The line bundle $L\tensor(L')^{-1}$ has degree zero on $C$.

Let $\Gamma\subseteq X$ be any irreducible curve and let
$\widetilde\Gamma\to\Gamma$ be its normalization. If the induced map
$$
\widetilde\Gamma\longrightarrow C
$$
is constant, the pullback of $L\tensor(L')^{-1}$ has degree zero. If it is
nonconstant of degree $e$, then its pullback has degree
$$
e\deg\qty(L\tensor(L')^{-1})=0.
$$
Thus
$$
c_1\qty(M\tensor(M')^{-1})\cdot\Gamma=0
$$
for every irreducible curve $\Gamma$. Hence $M$ and $M'$ are numerically
equivalent.

:::

:::

::: {.pf-step #s6}

The line bundle
$$
M=p_1^*L\tensor p_2^*\OO_{\PP^1}(1)=X_0+Lf
$$
is very ample on $X=C\times\PP^1$.

::: pf-proof

Read $X$ as the ruled surface $\pi=p_1:X\to C$ with normalized bundle
$\mathcal E=\OO_C\oplus\OO_C$, so that the invariant is $e=0$ and the divisor
$\mfe$ representing $\det\mathcal E$ is zero. The section
$$
X_0=C\times\{t\}=p_2^*\OO_{\PP^1}(1)\sim p_2^*[t]
$$
has $X_0^2=0=-e$, and the ruling fibres are
$$
f=\{c\}\times\PP^1=p_1^*[c].
$$
Since
$$
p_1^*L=p_1^*D_L=Lf
$$
for a divisor $D_L$ of $L$, and $p_2^*\OO_{\PP^1}(1)=\OO_X(X_0)$, the line
bundle $M$ is
$$
\OO_X(X_0+Lf).
$$

Fuentes and Pedreira, *The Projective Theory of Ruled Surfaces*
(arXiv:math/0006204v3), text version
`tmp/sources/projective-theory-ruled-surfaces.md`, Theorem 3.9(3), printed
p. 18, states that on a decomposable ruled surface the complete system
$\linearsystem{X_0+\mfb f}$ is very ample if and only if $\mfb$ and
$\mfb+\mfe$ are very ample on the base curve. Here $\mfb=L$ and $\mfe=0$, so
the criterion asks that $L$ be very ample, which is step [](#s3){.pf-ref}.
Hence $M$ is very ample.

Independently of that criterion, step [](#s3){.pf-ref} also gives a closed
immersion $C\hookrightarrow\PP^r$ defined by $L$, and $\OO_{\PP^1}(1)$ defines
the standard closed immersion of $\PP^1$; the product of the two followed by
the Segre closed immersion embeds $C\times\PP^1$ with hyperplane bundle
$p_1^*L\tensor p_2^*\OO_{\PP^1}(1)=M$.
$$
\boxed{M\text{ is very ample}.}
$$

:::

:::

::: {.pf-step #s7}

The numerically equivalent line bundle
$$
M'=p_1^*L'\tensor p_2^*\OO_{\PP^1}(1)=X_0+L'f
$$
is not very ample.

::: pf-proof

With $\mfb=L'$ and $\mfe=0$, the criterion of Fuentes--Pedreira Theorem 3.9(3)
makes $M'$ very ample exactly when $L'=K_C(P+Q)$ is very ample, and step
[](#s4){.pf-ref} shows that it is not.

Independently of the criterion: restriction to the closed fibre
$$
C\times\{t\}\cong C
$$
of $p_2$ gives
$$
M'\restrict_{C\times\{t\}}\cong L',
$$
because $p_2^*\OO_{\PP^1}(1)$ is trivial there. If $M'$ were very ample on
$X$, an embedding defined by $M'$ would restrict to a closed immersion of this
fibre, so $L'$ would be very ample. This contradicts step [](#s4){.pf-ref}.
Hence
$$
\boxed{M'\text{ is not very ample}.}
$$

:::

:::

::: {.pf-step #s8}

There are numerically equivalent divisors $D,D'$ on the surface $X$ with
$D$ very ample and $D'$ not very ample.

::: pf-proof

Because $X$ is smooth and integral, choose Cartier divisors $D,D'$ with
$$
\OO_X(D)\cong M,
\qquad
\OO_X(D')\cong M'.
$$
Step [](#s5){.pf-ref} gives
$$
D\equiv D'.
$$
Steps [](#s6){.pf-ref} and [](#s7){.pf-ref} give respectively that $D$ is very ample and $D'$ is not.
This is the required counterexample.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves numerical invariance of ampleness, and steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} give
the required failure of numerical invariance for very ampleness.

:::

:::

:::

::: {.remark title="Published solution"}
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.1.12, PDF p. 261: for a curve of genus $g$, a divisor $D$ of degree $2g$ is very ample if and only if $h^0(D-P-Q)=h^0(D)-2$ by IV.3.4, and Riemann--Roch gives this exactly when $K_C-D+P+Q$ has nonpositive degree, so the very ample classes of degree $2g$ are those outside a two-dimensional family; he then takes $H=\abs{C_0+\mfb f}$ on a decomposable ruled surface and quotes "Fuentes-Pedreira thm 3.9" for the very-ampleness criterion on it, a source now retained as `tmp/sources/projective-theory-ruled-surfaces.pdf` with text version `tmp/sources/projective-theory-ruled-surfaces.md`. What he leaves undone is the specialization: he fixes no value of $e$ and never checks the second hypothesis of that theorem, that $\mfb+\mfe$ be very ample, so his surface example is a citation rather than an exhibit. Step [](#s3){.pf-ref} proves the curve statement as a separation statement, and steps [](#s5){.pf-ref} to [](#s8){.pf-ref} replace his surface example by $C\times\PP^1$ with $M=p_1^*L\otimes p_2^*\OO(1)$ and $M'=p_1^*L'\otimes p_2^*\OO(1)$, resting only on Riemann--Roch and a degree-zero pullback.

Two published sets give a surface example by the external product $D\times\PP^1$, and the construction fails there. Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework, text version `tmp/sources/ntu-ag2-chapter5.md`, Exercise 12, printed p. 5 of that set, ends "let $X=C\times\PP^1$, $\widetilde D=D\times\PP^1$ and $\widetilde D{}'=D'\times\PP^1$; then $\widetilde D\equiv\widetilde D{}'$ but $\widetilde D{}'$ is very ample, and $\widetilde D$ is not". Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, exercise 5.1.12, printed p. 102, ends "the divisor $D\times\PP^1$ and $D'\times\PP^1$ are numerically equivalent, and the first is very ample but second is just ample". Both print $D'$ and $\widetilde D{}'$, not $D_0$.

An external product $D\times\PP^1$ is the pullback $p_1^*D$, and a fibre of $p_1$ is $\{c\}\times\PP^1$, on which $p_1^*D$ has degree zero; a very ample divisor meets every curve positively, a positive multiple of it being a hyperplane section, so $p_1^*D$ is not even ample. On the other fibre, $C\times\{t\}$, its degree is $\deg D=2g$, so the defect is not a vanishing degree on every curve: it is that the fibre the divisor must meet positively is the one of $p_1$. Adding the degree-one class of $\PP^1$ to both sides, as in $M$ and $M'$ of step [](#s5){.pf-ref}, makes the $p_1$-fibre degree one and leaves the failure of very ampleness in the curve factor, where step [](#s7){.pf-ref} reads it off a $p_2$-fibre.

Read as a decomposable ruled surface of invariant $e=0$, the same example is settled by Fuentes and Pedreira, *The Projective Theory of Ruled Surfaces* (arXiv:math/0006204v3), text version `tmp/sources/projective-theory-ruled-surfaces.md`, Theorem 3.9(3), printed p. 18: $\linearsystem{X_0+\mfb f}$ is very ample exactly when $\mfb$ and $\mfb+\mfe$ are, which at $e=0$ is very ampleness of $\mfb$ alone, and $M=X_0+Lf$ and $M'=X_0+L'f$ carry $\mfb=L$ and $\mfb=L'=K_C(P+Q)$, very ample by step [](#s3){.pf-ref} and not by step [](#s4){.pf-ref}. Steps [](#s6){.pf-ref} and [](#s7){.pf-ref} use that criterion and keep the card's direct arguments beside it.

The criterion rests on the paper's Corollary 2.13, printed p. 14, and that corollary is proved. Its forward direction is Theorem 2.11; its converse is Proposition 2.3, printed p. 8, applied to the system $|H-Pf|$: if the map defined by $|H|$ is not an isomorphism at a point, Theorem 2.11, printed pp. 12--13, makes that point a base point of some $|H-Pf|$, and Proposition 2.3 then produces $Q$ with $h^0(H-(P+Q)f)\ge h^0(H-Pf)-1$, which is $h^0(H)-3$ once $|H|$ is base-point-free. The case $Q=P$ is the one Theorem 2.11 covers through tangent directions, so the two-fibre condition does test a tangent direction transverse to a fibre. Proposition 2.15, printed p. 15, rests on the same corollary and is sound for the same reason.
:::
