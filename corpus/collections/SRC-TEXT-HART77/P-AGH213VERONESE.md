---
schema: qual/card@1
id: P-AGH213VERONESE
kind: problem
title: Every curve on the Veronese surface is cut out by a hypersurface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Veronese Embedding
  - Hypersurfaces
  - Curves
relations:
- kind: uses
  target: P-AGH212DUPLE
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement with the retained Hartshorne I.2.13 transcription. The proof lifts an even-degree plane equation through the quadratic Veronese substitution and proves that the lifted hypersurface equation is irreducible. It distinguishes the requested equality of algebraic sets from equality of scheme-theoretic intersections.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be algebraically closed.
Let $Y$ be the image of the $2$-uple embedding of $\PP^2$ in $\PP^5$; this is the **Veronese surface**. A **curve** is a variety of dimension $1$.
If $Z \subseteq Y$ is a closed curve, show that there exists a hypersurface $V \subseteq \PP^5$ with $V \intersect Y = Z$.
:::

::: {.solution}
Let $\nu:\PP_k^2\to Y$ be the [[P-AGH212DUPLE|quadratic Veronese embedding]], with coordinates
$$
[x_0:x_1:x_2]\longmapsto[x_0^2:x_1^2:x_2^2:x_0x_1:x_0x_2:x_1x_2].
$$
Write $S=k[x_0,x_1,x_2]$, $T=k[y_0,\ldots,y_5]$, and let $\theta:T\to S$ be this monomial substitution.

::: pf

::: {.pf-step #pullback-curve-equation}
There is an irreducible homogeneous polynomial $f\in S$ of degree $e>0$ with $\nu^{-1}(Z)=Z(f)$.

::: pf-proof
The map $\nu$ is an isomorphism onto $Y$ by the coordinate calculation in [[P-AGH212DUPLE]].
Consequently $C=\nu^{-1}(Z)$ is a closed irreducible curve in $\PP^2$.
The [[P-AGH28HYPERSURFACE|homogeneous hypersurface criterion]] gives a positive-degree irreducible homogeneous equation $f$ for this codimension-one variety.
In particular, its full homogeneous ideal is $(f)$.
:::

:::

::: {.pf-step #lift-f-to-veronese-ring}
There is a positive-degree homogeneous $F\in T$ such that
$$
\theta(F)=
\begin{cases}
f,&e\text{ even},\\
f^2,&e\text{ odd}.
\end{cases}
$$

::: pf-proof
For every $m\ge0$, the substitution map $T_m\to S_{2m}$ is surjective.
Indeed, every monomial of degree $2m$ is a product of $2m$ variables, with repetition, and pairing these factors expresses it as a product of $m$ quadratic monomials.
All six quadratic monomials occur among the images of the $y_i$.
Since monomials span $S_{2m}$, the map is surjective.

For even $e$, apply this with $m=e/2$ to lift $f$.
For odd $e$, apply it with $m=e$ to lift $f^2$.
Both choices have $m>0$, and the lifted polynomial is nonzero because its image is nonzero.
:::

:::

::: {.pf-step #lifted-polynomial-irreducible}
The polynomial $F$ from step [](#lift-f-to-veronese-ring){.pf-ref} is irreducible.

::: pf-proof
Suppose $F=GH$ with nonconstant factors in $T$.
Since $F$ is homogeneous and $T$ is a graded domain, both factors are homogeneous: the least and greatest nonzero degrees of a product add, so equality of those degrees in the product forces equality in each factor.
The nonzero polynomials $\theta(G)$ and $\theta(H)$ then have positive even degrees, twice the respective degrees of $G$ and $H$.
They are nonzero because their product is the nonzero polynomial in step [](#lift-f-to-veronese-ring){.pf-ref}.

The polynomial ring $S$ is a UFD, and $f$ is irreducible.
If $e$ is even, the equation $\theta(G)\theta(H)=f$ contradicts irreducibility of $f$, since both factors have positive degree.
If $e$ is odd, unique factorization in $\theta(G)\theta(H)=f^2$ and positivity of the two degrees force
$$
\theta(G)=cf,\qquad \theta(H)=c^{-1}f
$$
for some $c\in k^\times$.
Their degrees would then be the odd number $e$, contradicting the even degrees just established.
Both cases exclude the proposed factorization.
:::

:::

::: {.pf-step #hypersurface-cuts-out-z}
The required hypersurface is $\boxed{V=Z(F)\subseteq\PP_k^5}$, and $V\cap Y=Z$.

::: pf-proof
By step [](#lifted-polynomial-irreducible){.pf-ref}, $F$ is irreducible and homogeneous of positive degree.
Its zero set is nonempty: it contains $\nu(C)=Z$ by the substitution in step [](#lift-f-to-veronese-ring){.pf-ref}.
Thus [[P-AGH28HYPERSURFACE]] makes it a hypersurface in $\PP^5$.

For every $a\in\PP^2$, the equation $F(\nu(a))=0$ is equivalent to $f(a)=0$, whether the substituted polynomial is $f$ or $f^2$.
Hence
$$
\nu^{-1}(V\cap Y)=Z(\theta(F))=Z(f)=C.
$$
The bijection $\nu:\PP^2\to Y$ gives $V\cap Y=\nu(C)=Z$.
Moreover $V$ does not contain $Y$, because $\theta(F)$ is a nonzero homogeneous polynomial and $I(\PP^2)=(0)$.
:::

:::

::: pf-qed
Steps [](#pullback-curve-equation){.pf-ref}, [](#lift-f-to-veronese-ring){.pf-ref} and [](#lifted-polynomial-irreducible){.pf-ref} construct the irreducible hypersurface equation, and step [](#hypersurface-cuts-out-z){.pf-ref} proves the required intersection equality.
:::

:::

:::

::: {.remark title="Set-theoretic and scheme-theoretic intersection"}
The equality in this exercise is an equality of algebraic sets.
When the plane curve $C$ has odd degree $e$, the constructed hypersurface pulls back to the equation $f^2$ and therefore cuts out the double divisor $2C$ scheme-theoretically.
When $e$ is even, its pullback is $f$ and the scheme-theoretic intersection is reduced.
:::
