---
schema: qual/card@1
id: P-MAXAT-6-11
kind: problem
title: Cohomology rings of $B\U(n)$ and $B\Orth(n)$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 11 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Find the cohomology ring of $B U ( n ) , B O ( n )$
:::

::: {.solution}

The natural coefficient choices are integral coefficients for $BU(n)$ and mod-$2$ coefficients for $BO(n)$.

::: pf

::: pf-step

Let
$$
\gamma_n^{\CC}\to BU(n)
$$
be the universal complex $n$-plane bundle.
Its Chern classes are
$$
c_i=c_i(\gamma_n^{\CC})
\in H^{2i}(BU(n);\ZZ),
\qquad 1\leq i\leq n.
$$


::: pf-proof

By definition, $BU(n)$ classifies rank-$n$ complex vector bundles.
Applying the universal Chern-class construction to the universal bundle gives the displayed classes in their standard degrees.

:::

:::

::: pf-step

The inclusion of a maximal torus
$$
T^n=U(1)^n\hookrightarrow U(n)
$$
induces
$$
BT^n=(\CP^{\infty})^n\longrightarrow BU(n).
$$
If $x_i\in H^2(BT^n;\ZZ)$ is the first Chern class of the $i$th universal line bundle, then
$$
c_k\longmapsto e_k(x_1,\ldots,x_n),
$$
the $k$th elementary symmetric polynomial.


::: pf-proof

The pullback of the universal $n$-plane bundle to $BT^n$ splits as the direct sum of the $n$ universal line bundles.
By the Whitney product formula,
$$
c(\gamma_n^{\CC}|_{BT^n})
=\prod_{i=1}^n(1+x_i).
$$
Comparing homogeneous components gives the elementary symmetric polynomials.

:::

:::

::: {.pf-step #s1-3}

Consequently
$$
\boxed{
H^*(BU(n);\ZZ)
\cong\ZZ[c_1,\ldots,c_n],
\qquad |c_i|=2i.}
$$


::: pf-proof

The splitting principle makes the map to the cohomology of the complete flag bundle injective, so a relation among the $c_i$ would yield a relation among the elementary symmetric polynomials $e_i(x_1,\ldots,x_n)$.
The fundamental theorem of symmetric polynomials says
$$
\ZZ[x_1,\ldots,x_n]^{S_n}
=\ZZ[e_1,\ldots,e_n]
$$
with the $e_i$ algebraically independent.
Conversely, the Schubert-cell decomposition of the infinite complex Grassmannian model of $BU(n)$ has only even-dimensional cells, and its Poincare series equals
$$
\prod_{i=1}^n\frac1{1-t^{2i}},
$$
the Hilbert series of $\ZZ[c_1,\ldots,c_n]$.
Thus these classes generate all integral cohomology and satisfy no relations.

:::

:::

::: pf-step

Let
$$
\gamma_n^{\RR}\to BO(n)
$$
be the universal real $n$-plane bundle.
Its Stiefel--Whitney classes are
$$
w_i=w_i(\gamma_n^{\RR})
\in H^i(BO(n);\FF_2),
\qquad1\leq i\leq n.
$$


::: pf-proof

The space $BO(n)$ classifies rank-$n$ real vector bundles.
Applying the universal Stiefel--Whitney-class construction gives these classes in degree $i$.

:::

:::

::: pf-step

Restriction to the diagonal subgroup
$$
O(1)^n\hookrightarrow O(n)
$$
gives
$$
(\RP^{\infty})^n\to BO(n),
$$
under which
$$
w_k\longmapsto e_k(y_1,\ldots,y_n),
\qquad |y_i|=1.
$$


::: pf-proof

The pulled-back universal real bundle is the direct sum of the $n$ universal real line bundles.
If their first Stiefel--Whitney classes are $y_i$, the Whitney formula gives
$$
w(\gamma_n^{\RR})\longmapsto
\prod_{i=1}^n(1+y_i).
$$
Again, homogeneous components are elementary symmetric polynomials.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
H^*(BO(n);\FF_2)
\cong\FF_2[w_1,\ldots,w_n],
\qquad |w_i|=i.}
$$


::: pf-proof

The mod-$2$ splitting principle reduces relations to symmetric-polynomial relations in
$$
H^*((\RP^{\infty})^n;\FF_2)
=\FF_2[y_1,\ldots,y_n].
$$
The elementary symmetric polynomials are algebraically independent and generate the invariant ring.
The Schubert-cell decomposition of the real Grassmannian model of $BO(n)$ gives the matching mod-$2$ Poincare series
$$
\prod_{i=1}^n\frac1{1-t^i},
$$
so the $w_i$ generate the entire ring.

:::

:::

::: {.pf-step #s1-7}

Therefore the standard cohomology-ring calculations are
$$
\boxed{H^*(BU(n);\ZZ)=\ZZ[c_1,\ldots,c_n]}
$$
and
$$
\boxed{H^*(BO(n);\FF_2)=\FF_2[w_1,\ldots,w_n].}
$$


::: pf-proof

These are steps [](#s1-3){.pf-ref} and [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives both requested classifying-space cohomology rings with their standard coefficient systems.

:::

:::

:::
