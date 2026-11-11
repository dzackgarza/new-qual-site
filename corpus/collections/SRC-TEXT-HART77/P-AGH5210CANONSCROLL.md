---
schema: qual/card@1
id: P-AGH5210CANONSCROLL
kind: problem
title: Canonical curves on a rational scroll and nonhyperelliptic curves with a $g^1_3$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Canonical Divisor
relations: []
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter V, section 2,
    exercise 2.10, printed page 385 (PDF page 400 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise reads: "For any n > e >= 0, let X be the
    rational scroll of degree d = 2n - e in P^{d+1} given by (2.19). If
    n >= 2e - 2, show that X contains a nonsingular curve Y of genus g = d + 2
    which is a canonical curve in this embedding. Conclude that for every
    g >= 4, there exists a nonhyperelliptic curve of genus g which has a g_3^1."
    The card states exactly this. The proof was read and checked, and the two
    numerical claims were recomputed: with H = C_0 + nf, H^2 = 2n - e = d and
    K.H = e - 2n - 2, so a member of |H - K_X| has degree
    H.(H - K_X) = 4n - 2e + 2 = 2g - 2 and genus g = d + 2; adjunction gives
    K_Y = (K_X + Y)|_Y = H|_Y, so Y is canonical in the embedding. Base-point
    freeness comes from pi_*O(aC_0 + bf) = sum_{i=0}^{a} O(b - ie) with a = 3
    and b - 3e = n - 2e + 2 >= 0, which is exactly the hypothesis
    n >= 2e - 2; the q = 0 case uses D.C_0 = 3(C_0 + ef).C_0 = 0 and Bertini off
    the contracted section. No retained solution set in the repository covers
    this exercise (Egbert's set, the only one that mentions scrolls, does not
    treat it), so the proof is derived and says so; the hyperplane class and
    K_X are taken from [[FE-TORHIRZ]].
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Rechecked against the printed exercise, printed page 385, and against two
    published treatments outside the twelve retained sets. Algebraic Geometry
    II, National Taiwan University, 2020 Spring, Chapter V homework, Exercise 10
    of section 2, PDF p. 8 (tmp/sources/ntu-ag2-chapter5.pdf), carries the same
    construction and cites Corollary 2.18, printed page 380, for the nonsingular
    member; it does not prove that the embedding of Y is complete, which is step
    s6 here and needs H^0(O_X(H)) = H^0(Y,K_Y) together with
    h^0(O_X(H)) = 2n-e+2. Yang Pi-Yeh, Hartshorne Solutions, exercise 5.2.10,
    printed p. 104 (tmp/sources/lfwin-hartshorne-solutions.pdf), computes the
    genus and the g_3^1 and never shows the member nonsingular or K_Y the
    restricted hyperplane class. All eight steps were re-read: the pushforward
    pi_*O(aC_0+bf) as the sum of O(b-ie) with b-3e = n-2e+2 >= 0 for
    base-point freeness, D.C_0 = 0 in the q = 0 branch, H^i(X,O(-D)) = 0 from
    H^i(X,O(H)) with R^1 pi_*O(H) = 0, H.D = 4n-2e+2, and
    h^0(O_X(H)) = 2n-e+2 = d+2. Not checked: whether Corollary 2.18's criterion
    covers the e = 0 case of the q = 0 branch exactly as used; the card proves
    that branch separately.
---

::: {.problem}
For any $n>e \geqslant 0$, let $X$ be the rational scroll of degree $d=2 n-e$ in $\PP^{d+1}$ given by (2.19). If $n \geqslant 2 e-2$, show that $X$ contains a nonsingular curve $Y$ of genus $g=d+2$ which is a canonical curve in this embedding.

Conclude that for every $g \geqslant 4$, there exists a nonhyperelliptic curve of genus $g$ which has a $g_3^1$.
Cf.
(IV, §5).
:::

::: {.solution}
Write $X=\FF_e$, let $C_0$ be its negative section, and let $f$ be a
fibre of the ruling
$$
\pi:X\longrightarrow\PP^1.
$$
Thus
$$
C_0^2=-e,
\qquad
C_0\cdot f=1,
\qquad
f^2=0,
$$
and
$$
K_X\sim-2C_0-(e+2)f
$$
[[FE-TORHIRZ]].  In the embedding of (2.19), the hyperplane class is
$$
H\sim C_0+nf,
$$
so $H^2=2n-e=d$.

::: pf

::: {.pf-step #s1}

The divisor
$$
D\coloneqq H-K_X
\sim
3C_0+(n+e+2)f
$$
has a base-point-free complete linear system.

::: pf-proof

Put
$$
b=n+e+2.
$$
For a divisor $aC_0+bf$ with $a\ge0$, the ruled-surface projection gives
$$
\pi_*\OO_X(aC_0+bf)
\cong
\bigoplus_{i=0}^{a}\OO_{\PP^1}(b-ie).
$$
Hence $\OO_X(aC_0+bf)$ is globally generated whenever $b\ge ae$: every
summand on the right is then globally generated, and the relative
$\OO_X(a)$ evaluation map is surjective.

For $D$ one has $a=3$, and the hypothesis $n\ge2e-2$ gives
$$
b-3e
=
n-2e+2
\ge0.
$$
Thus $\linearsystem{D}$ is base-point-free.

:::

:::

::: {.pf-step #s2}

The system $\linearsystem{D}$ contains a nonsingular member $Y$.

::: pf-proof

Set
$$
q=n-2e+2\ge0.
$$
Then
$$
D
\sim
3(C_0+ef)+qf.
$$
If $q>0$, then
$$
D
\sim
\bigl(C_0+(e+q)f\bigr)+2(C_0+ef).
$$
The first summand is very ample by the rational-scroll construction (2.19),
because $e+q>e$, while step [](#s1){.pf-ref} with $a=1$ shows that $C_0+ef$ is
base-point-free.  The tensor product of a very ample invertible sheaf with
globally generated invertible sheaves is very ample.  Hence $D$ is very
ample, so a general member of $\linearsystem{D}$ is nonsingular by Bertini's theorem.

Suppose $q=0$.  The base-point-free system $\linearsystem{C_0+ef}$ defines the usual
morphism from $\FF_e$ to the rational normal scroll cone: it contracts
exactly $C_0$ and is an immersion on $X\setminus C_0$.  The system

$$
\linearsystem{D}=\linearsystem{3(C_0+ef)}
$$

has the same property away from $C_0$.  Moreover,
$$
D\cdot C_0=0.
$$
Since $\linearsystem{D}$ is base-point-free, a general member does not contain the
contracted section $C_0$, and hence is disjoint from it.  Bertini applied
on $X\setminus C_0$, where the associated morphism is an immersion, then
shows that a general member is nonsingular.  Choose such a member and call
it $Y$.

:::

:::

::: {.pf-step #s3}

The curve $Y$ is connected, hence irreducible.

::: pf-proof

From
$$
0\longrightarrow\OO_X(-D)
\longrightarrow\OO_X
\longrightarrow\OO_Y
\longrightarrow0
$$
it is enough to prove
$$
H^0(X,\OO_X(-D))=0,
\qquad
H^1(X,\OO_X(-D))=0.
$$
For the first vanishing, choose a fibre that is not a component of an
effective divisor.  Its intersection with that divisor is nonnegative, while
$$
(-D)\cdot f=-3,
$$
so $-D$ cannot be effective.

For the second, Serre duality and $D=H-K_X$ give
$$
H^1(X,\OO_X(-D))^\vee
\cong
H^1(X,\OO_X(K_X+D))
=
H^1(X,\OO_X(H)).
$$
Since
$$
\pi_*\OO_X(H)
\cong
\OO_{\PP^1}(n)\oplus\OO_{\PP^1}(n-e)
$$
and $R^1\pi_*\OO_X(H)=0$, while $n>e\ge0$, one obtains
$$
H^1(X,\OO_X(H))=0.
$$
Therefore $H^0(Y,\OO_Y)=k$, so $Y$ is connected.  By step [](#s2){.pf-ref} it is
nonsingular; a connected nonsingular curve is irreducible.

:::

:::

::: {.pf-step #s4}

The canonical bundle of $Y$ is the restriction of the hyperplane
bundle:
$$
\boxed{K_Y\cong\OO_Y(H)}.
$$

::: pf-proof

Adjunction and the definition $D=H-K_X$ give
$$
K_Y
\cong
(K_X+Y)\restrict_Y
\cong
(K_X+D)\restrict_Y
\cong
\OO_Y(H).
$$

:::

:::

::: {.pf-step #s5}

The genus of $Y$ is
$$
\boxed{g(Y)=d+2}.
$$

::: pf-proof

By step [](#s4){.pf-ref},
$$
2g(Y)-2
=
\deg K_Y
=
H\cdot D.
$$
Using $H=C_0+nf$ and
$D=3C_0+(n+e+2)f$,
$$
\begin{aligned}
H\cdot D
&=(C_0+nf)\cdot\bigl(3C_0+(n+e+2)f\bigr)\\
&=-3e+(n+e+2)+3n\\
&=4n-2e+2\\
&=2(2n-e)+2\\
&=2d+2.
\end{aligned}
$$
Thus $2g(Y)-2=2d+2$, whence $g(Y)=d+2$.

:::

:::

::: {.pf-step #s6}

The restriction map
$$
H^0(X,\OO_X(H))
\longrightarrow
H^0(Y,K_Y)
$$
is an isomorphism.  Consequently the given embedding of $Y$ is its
complete canonical embedding.

::: pf-proof

Since $Y\sim D=H-K_X$, restriction gives
$$
0
\longrightarrow
\OO_X(K_X)
\longrightarrow
\OO_X(H)
\longrightarrow
\OO_Y(H)
\longrightarrow0.
$$
Now $H^0(X,\OO_X(K_X))=0$: an effective canonical divisor would have
nonnegative intersection with a general fibre, whereas $K_X\cdot f=-2$.
Also
$$
H^1(X,\OO_X(K_X))
\cong
H^1(X,\OO_X)^\vee
=0
$$
by Serre duality, because $X$ is ruled over $\PP^1$ and
$H^1(X,\OO_X)=0$.  The cohomology sequence therefore makes the restriction
map an isomorphism.  By step [](#s4){.pf-ref} its target is $H^0(Y,K_Y)$.

Moreover,
$$
h^0(X,\OO_X(H))
=
h^0(\PP^1,\OO(n))+h^0(\PP^1,\OO(n-e))
=
2n-e+2
=
d+2.
$$
Thus the given embedding $X\hookrightarrow\PP^{d+1}$ uses all sections of
$H$.  Its restriction to $Y$ is therefore defined by the complete canonical
system $\linearsystem{K_Y}$, as claimed.

:::

:::

::: {.pf-step #s7}

For every integer $g\ge4$, parameters $n>e\ge0$ satisfying the
hypotheses can be chosen with
$$
2n-e=g-2.
$$

::: pf-proof

Put $d=g-2\ge2$.  If $d$ is even, take
$$
e=0,
\qquad
n=\frac d2.
$$
Then $n>e$, $2n-e=d$, and $n\ge2e-2$.

If $d$ is odd, then $d\ge3$; take
$$
e=1,
\qquad
n=\frac{d+1}{2}.
$$
Then $n>1=e$, $2n-e=d$, and $n\ge0=2e-2$.
Thus steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} produce a canonical curve of genus $g=d+2$ in every
genus $g\ge4$.

:::

:::

::: {.pf-step #s8}

Every curve $Y$ produced above carries a $g^1_3$ and is
nonhyperelliptic.

::: pf-proof

The ruling restricts to a morphism
$$
\pi\restrict_Y:Y\longrightarrow\PP^1
$$
of degree
$$
Y\cdot f
=
D\cdot f
=3.
$$
Therefore the pullback of $\linearsystem{\OO_{\PP^1}(1)}$ is a base-point-free
$g^1_3$ on $Y$.

By step [](#s6){.pf-ref} the complete canonical map of $Y$ is an embedding.  A
hyperelliptic curve of genus at least $2$ has canonical map of degree $2$
onto a rational normal curve, so $Y$ is not hyperelliptic.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} construct the required nonsingular canonical curve of genus
$d+2$.  Steps [](#s7){.pf-ref} and [](#s8){.pf-ref} give, for every $g\ge4$, a nonhyperelliptic
genus-$g$ curve carrying a $g^1_3$.

:::

:::

:::

::: {.remark title="Published solution"}
Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 10 of §2 (solution by Chi-Kang), PDF p. 8, runs the same construction: with $D=C_0+nf$ the very ample class of the embedding, it takes $Y\in\abs{D-K_X}=\abs{3C_0+(n+e+2)f}$, which by Corollary 2.18 (printed page 380) has a nonsingular member under $e\ge0$ and $n+e+2\ge3e$, the hypothesis $n\ge2e-2$; adjunction gives $K_Y=D\restriction_Y$, then $\deg K_Y=D\cdot Y=4n-2e+2=2d+2$, so $g(Y)=d+2$, and $f\cdot Y=3$ gives a $g^1_3$. That is steps [](#s1){.pf-ref} to [](#s5){.pf-ref} and step [](#s8){.pf-ref}. It does not check that the embedding of $Y$ is the complete canonical one, which needs $H^0(\OO_X(H))\cong H^0(Y,K_Y)$; step [](#s6){.pf-ref} supplies that, and it is what makes the conclusion a canonical curve rather than a curve whose canonical class happens to be the restriction.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.2.10, printed p. 104, argues that "$3C_0+af$ can be written as a curve iff $C\cdot C_0\ge0$, i.e. $a\ge3e$", computes $2g-2=C\cdot(C+K)=4n-2e+2$ and reads off $g=2n-e+2$ and $C\cdot f=3$; it does not show the member nonsingular, and it never identifies $K_Y$ with the restricted hyperplane class.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.2.10, PDF p. 267: the whole of his solution is "See example 2.10 in Kollar's Complex Algebraic Geometry", and Kollár's book is not in `tmp/sources`, so there is no argument to read.
:::
