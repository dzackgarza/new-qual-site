---
schema: qual/card@1
id: P-AGH353ARITHGENUS
kind: problem
title: Arithmetic genus and nonsingular projective curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Arithmetic Genus
  - Euler Characteristic
  - Birational Invariants
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts and the constant-function hint with the retained Hartshorne Chapter III section 5 transcription. The proof distinguishes the dimension of X from its ambient projective dimension, compares the two genus definitions at polynomial value zero, and uses extension of rational maps on nonsingular curves for birational invariance.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a nonempty projective scheme of dimension $r$ over a field $k$.
We define the arithmetic genus $p_a$ of $X$ by
$$
p_a(X)=(-1)^r(\chi(\mco_X)-1).
$$
Note that it depends only on $X$, not on any projective embedding.

(a) If $X$ is integral, and $k$ algebraically closed, show that $H^0(X, \mco_X) \cong k$, so that
$$
p_a(X)=\sum_{i=0}^{r-1}(-1)^i \dim_k H^{r-i}(X, \mco_X).
$$
In particular, if $X$ is a curve, we have
$$
p_a(X)=\dim_k H^1(X, \mco_X).
$$

(b) If $X$ is a closed subvariety of $\PP_k^N$, show that this $p_a(X)$ coincides with the one defined in (I, Ex. 7.2), which apparently depended on the projective embedding.

(c) If $X$ is a nonsingular projective integral curve over an algebraically closed field $k$, show that $p_a(X)$ is in fact a birational invariant among such curves.
Conclude that a nonsingular plane curve of degree $d \geq 3$ is not rational.
:::

::: {.hint}
For (a), use Theorem I.3.4.
:::

::: {.solution}
Write $h^i(X,F)=\dim_k H^i(X,F)$.
The [[D-COHEULER|Euler characteristic]] is finite by coherent cohomology finiteness and vanishing.

::: pf

::: {.pf-step #s1}

If $X$ is integral and $k$ is algebraically closed, the constants map $k\to\Gamma(X,\OO_X)$ is an isomorphism.

::: pf-proof

The ring $B=\Gamma(X,\OO_X)$ is a domain, since regular functions on the integral scheme inject into its function field.
It is finite-dimensional over $k$ by [@Har10a, Theorem III.5.2].
For every nonzero $b\in B$, multiplication by $b$ is an injective endomorphism of this finite-dimensional vector space and hence is surjective.
In particular it takes some element to $1$, so $b$ is invertible.
Thus $B$ is a finite field extension of $k$.
Algebraic closedness of $k$ forces $B=k$, through its given constants inclusion.
This is the constant-function conclusion used in the hint.

:::

:::

::: {.pf-step #s2}

The formulas in (a) follow.

::: pf-proof

The groups $H^j(X,\OO_X)$ vanish for $j>r$ [@Har10a, Theorem III.2.7], and step [](#s1){.pf-ref} gives $h^0=1$.
Therefore
$$
\begin{aligned}
p_a(X)
&=(-1)^r\sum_{j=1}^r(-1)^j h^j(X,\OO_X)\\
&=\sum_{i=0}^{r-1}(-1)^i h^{r-i}(X,\OO_X),
\end{aligned}
$$
where the second line uses $i=r-j$.
For $r=0$ both sums are empty and the value is zero.
For a curve, $r=1$, and the formula is $p_a(X)=h^1(X,\OO_X)$.

:::

:::

::: {.pf-step #s3}

For any projective embedding in (b), the constant term of its Hilbert polynomial is $\chi(X,\OO_X)$, so the two definitions of arithmetic genus agree.

::: pf-proof

Let $S(X)$ be the homogeneous coordinate ring for $X\hookrightarrow\PP_k^N$ and let $P_X$ be its Hilbert polynomial.
The high-degree comparison in [[P-AGH259GAMMASTAR]] identifies
$$
S(X)_n\cong H^0(X,\OO_X(n))
$$
for every sufficiently large $n$.
Serre vanishing identifies the dimension of the latter space with $\chi(X,\OO_X(n))$ for every sufficiently large $n$ [@Har10a, Theorem III.5.2].
By [[P-AGH352HILBPOLY]], this Euler characteristic is given by one rational polynomial for every integer $n$.
That polynomial and $P_X$ agree at all sufficiently large integers and hence are the same polynomial.
At $n=0$ this gives $P_X(0)=\chi(X,\OO_X)$.

The genus defined from the projective embedding in [@Har10a, Exercise I.7.2] is $(-1)^{\dim X}(P_X(0)-1)$.
It is therefore $(-1)^r(\chi(X,\OO_X)-1)$, exactly the definition in the statement.
Since the latter uses only cohomology of the abstract scheme, it is independent of the embedding.
No equality of the coordinate ring with the section ring in small degrees is assumed.

:::

:::

::: {.pf-step #s4}

Birational nonsingular projective integral curves are isomorphic, and their arithmetic genera agree.

::: pf-proof

Let $C\dashrightarrow C'$ be a birational map between such curves.
At every closed point $x\in C$, the local ring $\OO_{C,x}$ is a DVR because $C$ is nonsingular and one-dimensional [@Har10a, Theorem I.6.2A].
Embed $C'$ in projective space and write the rational map in homogeneous coordinates in $K(C)$.
Multiply these coordinates by a common power of a uniformizer so that they all lie in $\OO_{C,x}$ and at least one is a unit.
They are regular on a neighborhood of $x$ and define a morphism there after shrinking so that the unit remains invertible.
The equations of $C'$ hold generically and therefore hold on that neighborhood, since $C$ is integral.
Thus the map extends near every closed point.
These extensions agree on overlaps by separatedness of $C'$ and equality on a dense open, as in [[P-AGH242AGREEDENSE]].
They glue with the original rational-map domain to a morphism $C\to C'$.

The rational inverse extends in the same way.
Their composites agree with the identity on dense opens and hence everywhere, again by separatedness and reducedness.
Thus the morphisms are inverse isomorphisms.
An isomorphism identifies the cohomology of the structure sheaves, and step [](#s2){.pf-ref} gives $p_a(C)=p_a(C')$.
This proves the birational-invariance assertion in (c).

:::

:::

::: {.pf-step #s5}

A nonsingular plane curve of degree $d\ge3$ is not rational.

::: pf-proof

Over the algebraically closed field, choose a point outside the plane curve and make it $[1:0:0]$ by a projective coordinate change.
The computation in [[P-AGH347PLANECURVEGENUS]] then gives
$$
h^0(C,\OO_C)=1,\qquad
h^1(C,\OO_C)=\frac{(d-1)(d-2)}2>0.
$$
In particular the curve is connected, since a nontrivial open-and-closed decomposition would give a nontrivial idempotent global function.
Its regular local rings are domains [@Har10a, Remark II.6.11.1A], so its irreducible components are disjoint and reduced; connectedness therefore makes it integral.
Step [](#s2){.pf-ref} identifies its arithmetic genus with this positive $h^1$.
On the other hand, $h^1(\PP_k^1,\OO)=0$ by [[P-AGH322FLASQUERESPONE]], so $p_a(\PP_k^1)=0$.
If $C$ were rational, it would be birational to $\PP_k^1$, contradicting step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove (a), step [](#s3){.pf-ref} proves (b), and steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (c) and its nonrationality conclusion.

:::

:::

:::
