---
schema: qual/card@1
id: P-TOPS05C
kind: problem
title: 'Cohomology and homology of $\RP^2\times\RP^3$ and the Bockstein'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
  - Bockstein
  - Projective Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained exam assets/attachments/SP05_290_Topology_Qual_extracted.md,
    problem 3: part (a) asks for the integral and mod 2 cohomology and homology
    of RP^2 x RP^3 and for orientability, part (b) for the action of the
    Bockstein beta_1 on mod 2 cohomology. The card agrees.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The computation is correct. Kunneth over Z for the two factors gives Z in
    degree 0, (Z/2)^2 in degree 1, Z/2 in degree 2 from H_1 tensor H_1, Z plus
    Z/2 in degree 3 from the tensor term H_0 tensor H_3 and Tor(H_1, H_1), Z/2
    in degree 4 from H_1 tensor H_3, and nothing in degree 5. The universal
    coefficient theorem then gives Z, 0, (Z/2)^2, Z plus Z/2, Z/2, Z/2, which is
    what the card lists. With field coefficients the Kunneth theorem is a ring
    isomorphism, and F_2[x]/(x^3) tensor F_2[y]/(y^4) has the Betti numbers
    1,2,3,3,2,1 the card gives. H_5 vanishes, so the closed five-manifold is not
    orientable. The Bockstein of 0 -> Z/2 -> Z/4 -> Z/2 -> 0 is Sq^1, which sends
    each degree-one generator to its square and acts on monomials by the Cartan
    formula with Sq^1(t^r) = r t^(r+1) mod 2, so the displayed formula is right,
    including the vanishing beyond x^2 and y^3. Nothing was changed.
---

::: {.problem}
(a) Compute the integral and mod $2$ cohomology and homology of $\RP^2 \times \RP^3$.
Is $\RP^2 \times \RP^3$ orientable?

(b) Determine the action of the Bockstein
$$
\beta_1 : H^*(\RP^2 \times \RP^3; \ZZ_2) \to H^{*+1}(\RP^2 \times \RP^3; \ZZ_2).
$$
:::

::: {.solution}

::: pf

::: pf-step

The integral homology of the two factors is
$$H_*(\RP^2)=\bigl(\ZZ,\ZZ/2,0\bigr),\qquad
H_*(\RP^3)=\bigl(\ZZ,\ZZ/2,0,\ZZ\bigr).$$

::: pf-proof

This is the standard cellular homology computation for real projective spaces.

:::

:::

::: {.pf-step #s2}

The integral Künneth theorem gives
$$\boxed{H_k(\RP^2\times\RP^3;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,\\
(\ZZ/2)^2,&k=1,\\
\ZZ/2,&k=2,\\
\ZZ\oplus\ZZ/2,&k=3,\\
\ZZ/2,&k=4,\\
0,&k=5.
\end{cases}}$$

::: pf-proof

The tensor term $H_1(\RP^2)\otimes H_1(\RP^3)$ contributes $\ZZ/2$ in degree $2$; the Tor term $\operatorname{Tor}(\ZZ/2,\ZZ/2)$ contributes $\ZZ/2$ in degree $3$; and $H_1(\RP^2)\otimes H_3(\RP^3)$ contributes $\ZZ/2$ in degree $4$.

:::

:::

::: pf-step

By the integral cohomology universal coefficient theorem,
$$\boxed{H^k(\RP^2\times\RP^3;\ZZ)\cong
\begin{cases}
\ZZ,&k=0,\\
0,&k=1,\\
(\ZZ/2)^2,&k=2,\\
\ZZ\oplus\ZZ/2,&k=3,\\
\ZZ/2,&k=4,\\
\ZZ/2,&k=5.
\end{cases}}$$

::: pf-proof

Use $0\to\operatorname{Ext}(H_{k-1},\ZZ)\to H^k\to\operatorname{Hom}(H_k,\ZZ)\to0$ and $\operatorname{Ext}(\ZZ/2,\ZZ)\cong\ZZ/2$.

:::

:::

::: pf-step

With $\FF_2$ coefficients,
$$H^*(\RP^2\times\RP^3;\FF_2)
\cong \FF_2[x,y]/(x^3,y^4),\qquad \gradeddegree{x}=\gradeddegree{y}=1,$$
and the mod-$2$ homology dimensions in degrees $0,\dots,5$ are
$$\boxed{1,2,3,3,2,1}.$$

::: pf-proof

For $\RP^m$, mod-$2$ cohomology is $\FF_2[t]/(t^{m+1})$. The field-coefficient Künneth theorem gives the tensor-product ring and the stated Betti numbers.

:::

:::

::: pf-step

The product is nonorientable.

::: pf-proof

Its top integral homology $H_5$ vanishes by step [](#s2){.pf-ref}. Equivalently, the product of a nonorientable manifold with any connected manifold is nonorientable.

:::

:::

::: pf-step

For the Bockstein associated to
$$0\to\ZZ/2\to\ZZ/4\to\ZZ/2\to0,$$
one has
$$\beta_1(x)=x^2,\qquad \beta_1(y)=y^2,$$
and, for every monomial,
$$\boxed{\beta_1(x^iy^j)=(i\bmod2)x^{i+1}y^j+(j\bmod2)x^iy^{j+1}},$$
with terms beyond $x^2$ or $y^3$ understood to vanish.

::: pf-proof

This mod-$2$ Bockstein is $Sq^1$. On the degree-one generator of $H^*(\RP^m;\FF_2)$, $Sq^1(t)=t^2$, and the Cartan formula gives $Sq^1(x^iy^j)=Sq^1(x^i)y^j+x^iSq^1(y^j)$ with $Sq^1(t^r)=r t^{r+1}$ mod $2$.

:::

:::

:::

:::
