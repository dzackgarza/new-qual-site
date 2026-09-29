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

The line bundle $M$ is very ample on $X$.

::: pf-proof

By step [](#s3){.pf-ref}, $L$ defines a closed immersion
$$
C\hookrightarrow\PP^r.
$$
The line bundle $\OO_{\PP^1}(1)$ defines the standard closed immersion of
$\PP^1$. Their product is a closed immersion
$$
C\times\PP^1\hookrightarrow\PP^r\times\PP^1.
$$
Composing with the Segre closed immersion gives an embedding into projective
space whose hyperplane bundle pulls back to
$$
p_1^*L\tensor p_2^*\OO_{\PP^1}(1)=M.
$$
Therefore
$$
\boxed{M\text{ is very ample}.}
$$

:::

:::

::: {.pf-step #s7}

The numerically equivalent line bundle $M'$ is not very ample.

::: pf-proof

Fix a point $t\in\PP^1$. Restriction to the closed fibre
$$
C\times\{t\}\cong C
$$
gives
$$
M'|_{C\times\{t\}}\cong L'.
$$
If $M'$ were very ample on $X$, an embedding defined by $M'$ would restrict to
a closed immersion of this fibre, so its restriction $L'$ would be very ample.
This contradicts step [](#s4){.pf-ref}. Hence
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
