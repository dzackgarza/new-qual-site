---
schema: qual/card@1
id: P-AGH349TWOPLANES
kind: problem
title: Two planes meeting at a point are not a set-theoretic complete intersection
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomological Dimension
  - Complete Intersections
  - Affine Space
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the affine and projective assertions and the supported-cohomology hints with the retained Hartshorne Chapter III section 4 transcription. The proof computes the top Laurent-monomial quotient on punctured affine four-space, checks both vanishing terms in supported Mayer-Vietoris, and deduces the obstruction to two defining equations over any field.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X=\Spec k[x_1, x_2, x_3, x_4]$ be affine four-space over a field $k$.
Let $Y_1$ be the plane $x_1=x_2=0$ and let $Y_2$ be the plane $x_3=x_4=0$.
Show that $Y=Y_1 \union Y_2$ is not a set-theoretic complete intersection in $X$.
Therefore the projective closure $\bar{Y}$ in $\PP_k^4$ is also not a set-theoretic complete intersection.
:::

::: {.hint}
Use an affine analogue of (Ex. 4.8e).
Then show that $H^2(X-Y,\mco_X)\ne0$, using (Ex. 2.3) and (Ex. 2.4).
If $P=Y_1\cap Y_2$, imitate (Ex. 4.3) to show that $H^3(X-P,\mco_X)\ne0$.
:::

::: {.solution}
Put $A=k[x_1,x_2,x_3,x_4]$, let $P=V(x_1,x_2,x_3,x_4)$ be the origin, and write $U=X\setminus(Y_1\cup Y_2)$ and $W=X\setminus\{P\}$.
Whenever the structure sheaf of $X$ appears on an open subset, its restriction to that open is understood.

::: pf

::: {.pf-step #s1}

The group $H^3(W,\OO_W)$ is nonzero.

::: pf-proof

Cover $W$ by the four principal affine opens $D(x_i)$.
All their intersections are affine, so this cover computes cohomology by its Čech complex [@Har10a, Theorem III.4.5].
Its term in degree three is $A_{x_1x_2x_3x_4}$, and the image of the preceding differential is the sum of the four subrings in which only three of the variables have been inverted.
Consequently
$$
H^3(W,\OO_W)\cong
\frac{k[x_1^{\pm1},x_2^{\pm1},x_3^{\pm1},x_4^{\pm1}]}{
\displaystyle\sum_{j=1}^4 k[x_j,x_i^{\pm1}:i\ne j]}.
$$
Every Laurent monomial with at least one nonnegative exponent belongs to the denominator, and the denominator is spanned by exactly those monomials.
Uniqueness of Laurent coefficients therefore identifies the quotient with the direct sum of the one-dimensional spaces spanned by monomials having all four exponents negative.
In particular the class of $1/(x_1x_2x_3x_4)$ is nonzero.
This is the four-variable version of the calculation in [[P-AGH343PUNCTUREDPLANE]].

:::

:::

::: {.pf-step #s2}

One has $H_{Y_a}^3(X,\OO_X)=H_{Y_a}^4(X,\OO_X)=0$ for $a=1,2$, while $H_P^4(X,\OO_X)\ne0$.

::: pf-proof

For every closed subset $T\subseteq X$, the supported-cohomology exact sequence of [[P-AGH323SUPPORTS]], part (e), and affine vanishing give isomorphisms
$$
H^i(X\setminus T,\OO_X)\cong H_T^{i+1}(X,\OO_X)\qquad(i\ge1).
$$
Indeed, the adjacent terms $H^i(X,\OO_X)$ and $H^{i+1}(X,\OO_X)$ are both zero.

The complement of $Y_1$ is $D(x_1)\cup D(x_2)$ and that of $Y_2$ is $D(x_3)\cup D(x_4)$.
Each is a separated scheme with a two-affine cover, so its structure-sheaf cohomology vanishes in degrees at least two, by [[P-AGH348COHDIM]], part (c).
The preceding isomorphisms give the two vanishings for each $Y_a$.
For $T=P$ and $i=3$, the same isomorphism and step [](#s1){.pf-ref} give $H_P^4(X,\OO_X)\ne0$.

:::

:::

::: {.pf-step #s3}

The complement of the two planes has $H^2(U,\OO_U)\ne0$.

::: pf-proof

The supported Mayer--Vietoris sequence of [[P-AGH324MAYERVIETORIS]] for $Y_1,Y_2$, whose intersection is $P$, contains
$$
H_{Y_1}^3(X,\OO_X)\oplus H_{Y_2}^3(X,\OO_X)
\longrightarrow H_Y^3(X,\OO_X)
\longrightarrow H_P^4(X,\OO_X)
\longrightarrow H_{Y_1}^4(X,\OO_X)\oplus H_{Y_2}^4(X,\OO_X).
$$
The first and last terms vanish by step [](#s2){.pf-ref}.
Thus its middle arrow is an isomorphism.
The open-support comparison in step [](#s2){.pf-ref}, with $T=Y$, now gives
$$
H^2(U,\OO_U)\cong H_Y^3(X,\OO_X)
\cong H_P^4(X,\OO_X)\cong H^3(W,\OO_W)\ne0.
$$

:::

:::

::: {.pf-step #s4}

Neither $Y\subseteq\AA_k^4$ nor its projective closure in $\PP_k^4$ is a set-theoretic complete intersection.

::: pf-proof

Both planes have dimension two, so their union has codimension two in $X$.
If it were a set-theoretic complete intersection, there would be polynomials $f,g\in A$ with $Y=V(f,g)$ as closed subsets.
Then $U=D(f)\cup D(g)$ would have a two-affine cover.
The Čech bound in step [](#s2){.pf-ref} would force $H^2(U,\OO_U)=0$, contradicting step [](#s3){.pf-ref}.
This proves the affine assertion.

The projective closure is the union of the two projective planes obtained by closing $Y_1$ and $Y_2$; its dimension remains two, so its codimension in $\PP_k^4$ is also two.
If two projective hypersurfaces cut out this closure set-theoretically, restricting their equations to the affine chart $\AA_k^4$ would cut out $Y$ by two polynomials.
The intersection of the closure with this chart is exactly $Y$, since $Y$ is already closed in the chart.
This contradicts the affine assertion and proves the projective one.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove the cohomological obstruction indicated by the hints, and step [](#s4){.pf-ref} gives both set-theoretic complete-intersection conclusions.

:::

:::

:::
