---
schema: qual/card@1
id: P-BW6LF
kind: problem
title: A space with $H_*(X)\cong(\ZZ,0,0,0,0,\ZZ_4,0,\ldots)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Construct a space $X$ having $H_0(X;\ZZ) \cong \ZZ$ and $H_5(X;\ZZ) \cong \ZZ_4$, but having all other homology groups trivial.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the compiled `assets/attachments/UCSD_290_Qualifying_Exams.pdf` and no solutions sheet accompanies it. The earlier version of the card gave the construction only, in notation that did not compile, and computed no homology; the construction is kept and the computation is supplied here, using the cellular chain complex as in Hatcher, *Algebraic Topology* (2002), Theorem 2.35, and the cellular boundary formula in §2.2.

::: pf

::: {.pf-step #construction}
There is a connected CW complex $X$ with one $0$-cell, one $5$-cell and one $6$-cell, whose $5$-cell is attached by the constant map $S^{4}\to e^{0}$ and whose $6$-cell is attached by a map $\Phi\colon S^{5}\to X^{5}$ of degree $4$.

::: pf-proof
Take the one-point space $X^{0}=e^{0}$. Attaching a $5$-cell along the constant map sends all of $S^{4}=\partial B^{5}$ to the single point, so $X^{5}=e^{0}\cup_{c}e^{5}$ is homeomorphic to $S^{5}$, the quotient of $S^{5}$ collapsing nothing but presenting the two hemispheres as $e^{0}$ and $e^{5}$. A map of degree $4$ from $S^{5}$ to $S^{5}$ exists — for instance the quotient $S^{5}\to\bigvee_{4}S^{5}\to S^{5}$ that pinches four complementary hemispheres to points and then identifies the four copies — and composing with the homeomorphism $S^{5}\cong X^{5}$ gives $\Phi$. Attaching $e^{6}$ along $\Phi$ produces the CW complex $X=X^{5}\cup_{\Phi}e^{6}$.
:::

:::

::: {.pf-step #connected}
$X$ is path connected, so $H_{0}(X;\ZZ)\cong\ZZ$.

::: pf-proof
$X$ is a CW complex with a single $0$-cell, so any two points can be joined by a path in the $1$-skeleton, which here is the point $e^{0}$; hence $X$ is path connected, and the zeroth homology of a path-connected space is $\ZZ$.
:::

:::

::: {.pf-step #chain-complex}
In the cellular chain complex of $X$ one has $C_{6}=\ZZ$, $C_{5}=\ZZ$, $C_{k}=0$ for $k\geq1$, $k\neq5,6$, and the only nonzero boundary map is $d_{6}\colon C_{6}\to C_{5}$, multiplication by $4$.

::: pf-proof
The groups $C_{k}$ are free on the $k$-cells, so they are as stated. By the cellular boundary formula, $d_{n}$ on an $n$-cell $e^{n}$ is $\sum_{\beta}d_{\alpha\beta}e^{n-1}_{\beta}$, where $d_{\alpha\beta}$ is the degree of the map $S^{n-1}\to S^{n-1}$ obtained by collapsing the $(n-1)$-skeleton minus $e^{n-1}_{\beta}$ to a point. For $n=6$ there is one $6$-cell and one $5$-cell, and that collapsing map is exactly $\Phi$, of degree $4$; so $d_{6}$ is multiplication by $4$. There is no $4$-cell, so $d_{5}$ maps into $0$; and $d_{k}=0$ for the other $k\geq1$ because at least one of $C_{k},C_{k-1}$ vanishes.
:::

:::

::: {.pf-step #homology}
$H_{6}(X)=0$, $H_{5}(X)\cong\ZZ/4\ZZ$, and $H_{k}(X)=0$ for $k=1,2,3,4$ and for $k\geq7$.

::: pf-proof
By the cellular homology theorem $H_{k}(X)\cong\ker d_{k}/\operatorname{im}d_{k+1}$. Since $d_{6}$ is injective (multiplication by $4$ on $\ZZ$), $\ker d_{6}=0$, so $H_{6}=0$; since $d_{5}=0$ and $\operatorname{im}d_{6}=4\ZZ$, $H_{5}=\ZZ/4\ZZ$. For $k=1,2,3,4$ both $C_{k}$ and $C_{k+1}$ vanish, and for $k\geq7$ both do, so those homology groups are $0$.
:::

:::

::: pf-step
Therefore
$$
\boxed{H_{*}(X;\ZZ)\cong(\ZZ,0,0,0,0,\ZZ/4\ZZ,0,\ldots),}
$$
that is, $H_{0}\cong\ZZ$, $H_{5}\cong\ZZ_{4}$, and every other reduced homology group is trivial.

::: pf-proof
Steps [](#connected){.pf-ref} and [](#homology){.pf-ref} give the stated groups, and step [](#chain-complex){.pf-ref} identifies the complex from which they are computed. The space $X$ is the Moore space $M(\ZZ/4,5)$: a $5$-sphere with a $6$-cell attached by a degree-$4$ map.
:::

:::

:::

:::
