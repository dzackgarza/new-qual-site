---
schema: qual/card@1
id: P-AGH346SQUAREZEROPIC
kind: problem
title: Picard groups under a square-zero thickening
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cech Cohomology
  - Picard Group
  - Infinitesimal Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the square-zero unit sequence and Picard segment with the retained Hartshorne Chapter III section 4 transcription. The proof checks unit lifting on stalks and identifies the Picard map by reduction of transition cocycles, without assuming surjectivity on global units.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $(X, \mco_X)$ be a ringed space, let $\mci$ be a sheaf of ideals with $\mci^2=0$, and let $X_0$ be the ringed space $(X, \mco_X/\mci)$.
Show that there is an exact sequence of sheaves of abelian groups on $X$,
$$
0 \to \mci \to \mco_X^* \to \mco_{X_0}^* \to 0,
$$
where $\mco_X^*$ (respectively, $\mco_{X_0}^*$) denotes the sheaf of (multiplicative) groups of units in the sheaf of rings $\mco_X$ (respectively, $\mco_{X_0}$), the map $\mci \to \mco_X^*$ is defined by $a \mapsto 1+a$, and $\mci$ has its usual (additive) group structure.
Conclude there is an exact sequence of abelian groups
$$
\cdots \to H^1(X, \mci) \to \Pic X \to \Pic X_0 \to H^2(X, \mci) \to \cdots.
$$
:::

::: {.solution}
All structure rings are commutative, and $X$ and $X_0$ have the same underlying topological space.
Write $\rho:\OO_X\to\OO_{X_0}$ for the quotient morphism and $\rho^\times$ for its restriction to the sheaves of units.
The zero symbols in the displayed exact sequences denote trivial abelian groups; the neutral element in a unit group is $1$.

::: pf

::: {.pf-step #s1}

The map $e:\mci\to\OO_X^\times$, $a\mapsto1+a$, is an injective homomorphism of abelian sheaves with image $\ker\rho^\times$.

::: pf-proof

For sections $a,b$ of $\mci$ on the same open set, their product is zero because $\mci^2=0$.
Thus
$$
(1+a)(1+b)=1+a+b,\qquad(1+a)(1-a)=1.
$$
The first equality proves the additive-to-multiplicative homomorphism property, and the second proves that $1+a$ is a unit.
The map commutes with restriction and is injective, since $1+a=1$ implies $a=0$.

Its image reduces to $1$ in the quotient sheaf.
Conversely, a section $u$ of $\OO_X^\times$ whose image is the identity satisfies $u-1\in\ker\rho=\mci$.
It is therefore $e(u-1)$.
This proves the kernel identification as sheaves.

:::

:::

::: {.pf-step #s2}

The morphism $\rho^\times$ is surjective as a morphism of sheaves.

::: pf-proof

The stalk of the sheaf of units at $x$ is the unit group of the ring $\OO_{X,x}$.
Indeed, a unit germ and its inverse have representatives whose product is $1$ after restricting to a sufficiently small common neighborhood; those representatives are inverse unit sections there.
Hence it suffices to prove that units lift across the stalk quotient $B\to B/J$, where $B=\OO_{X,x}$ and $J=\mci_x$ has $J^2=0$.

Let $\bar b\in(B/J)^\times$ and choose lifts $b,c\in B$ of $\bar b$ and its inverse.
Then $bc=1+a$ for $a\in J$.
Since $(1+a)^{-1}=1-a$, the element $c(1-a)$ is an inverse for $b$.
Thus $b$ is a unit lifting $\bar b$.
This proves surjectivity at every stalk and therefore surjectivity of sheaves.
Together with step [](#s1){.pf-ref} it proves the required short exact sequence.

:::

:::

::: {.pf-step #s3}

Its cohomology sequence gives the required Picard exact sequence, whose middle map is $[L]\mapsto[L\otimes_{\OO_X}\OO_{X_0}]$.

::: pf-proof

Apply the long exact sequence of derived global sections to the short exact sequence of abelian sheaves in steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.
Its beginning is
$$
\begin{aligned}
0&\to H^0(X,\mci)\to\Gamma(X,\OO_X^\times)
\to\Gamma(X,\OO_{X_0}^\times)\\
&\to H^1(X,\mci)\to H^1(X,\OO_X^\times)
\to H^1(X,\OO_{X_0}^\times)
\to H^2(X,\mci)\to\cdots.
\end{aligned}
$$
The [[P-AGH345PICH1|Picard and unit-cohomology identification]] applies to both ringed spaces and replaces the two degree-one unit groups by $\Pic X$ and $\Pic X_0$.
To identify the map between them, trivialize $L$ on an open cover and write its transition units as $g_{ij}$.
Tensoring with $\OO_{X_0}$ replaces these by their images $\rho^\times(g_{ij})$, which are exactly the images used by the cohomology map.
Thus the middle map is the stated reduction of invertible sheaves, and the exact segment is
$$
\cdots\to H^1(X,\mci)\to\Pic X\to\Pic X_0
\to H^2(X,\mci)\to\cdots.
$$
In particular, an invertible sheaf on $X_0$ lifts precisely when its connecting class in $H^2(X,\mci)$ is zero.
No assertion that the map on global units is surjective was needed.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove exactness of the sheaf sequence, and step [](#s3){.pf-ref} gives the cohomological and Picard conclusions.

:::

:::

:::
