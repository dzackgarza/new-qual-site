---
schema: qual/card@1
id: E-HAT-3.2-8
kind: problem
title: Spaces with isomorphic integral but distinct $\ZZ_p$ cohomology rings
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 8; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both coefficient computations: integrally both spaces are $\ZZ_p$ in degree $3$ and $\ZZ$
    in degree $4$, and every product of positive-dimensional classes vanishes for degree reasons,
    so the rings agree; over $\ZZ_p$ both are $\ZZ_p$ in degrees $2,3,4$, but in $X$ the class $x$
    restricts to the generator of $H^2(\CP^2)$, so $x^2\ne0$, while in $Y$ the class $y$ is
    supported on the Moore summand and $y^2=0$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 8 (p.229), with the printed description of X and Y intact. Rechecked integrally: d_3 = p and the other cellular boundaries vanish (Theorem 2.35 p.139, Cellular Boundary Formula p.141), so H_2 = Z_p, H_3 = 0, H_4 = Z; Theorem 3.2 p.195 then gives H^3 = Ext(Z_p,Z) = Z_p and H^4 = Z with everything else in positive degree zero, the same for Y, and all products vanish for degree reasons. Over Z_p both have one class in degrees 2,3,4; x^2 is nonzero by naturality of the inclusion CP^2 c X (which is an isomorphism in degrees 2 and 4), while y^2 lies in H^4(Y,S^4;Z_p) = H^4(M(Z_p,2);Z_p) = 0 by the relative cup product of p.209. So the rings differ. Not covered: nothing about higher powers, the rings having no classes above degree 4.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set covers this exercise — Guanyu Li's
    set treats Section 3.2 Exercises 1 through 7 under its own numbering, and none of the other
    retained Hatcher sets holds Section 3.2 — so the argument is the card's own and the card says
    so. Re-checked each step against Hatcher: the cellular chain complex of X has one generator in
    degrees 0, 2, 3, 4 with d_3 multiplication by p (Cellular Boundary Formula, p. 141) and d_4 = 0
    because the attaching map of the top cell of CP^2 lies in the 2-skeleton and so collapses to a
    point in the 3-skeleton modulo the open 3-cell; the integral homology and cohomology
    (Theorem 3.2, p. 195) then agree for X and Y, and all products of positive classes have degree
    at least 6 where both rings vanish. Over Z_p the tensored differentials vanish, so each space
    has one Z_p in degrees 2, 3 and 4; x^2 is nonzero because the inclusion of CP^2 induces
    isomorphisms on H_2 and H_4 with Z_p coefficients and alpha^2 generates H^4(CP^2;Z_p); and
    y^2 = 0 because every degree-two class of Y restricts to zero on the S^4 summand, hence comes
    from H^2(Y,S^4;Z_p), whose relative square lands in H^4(Y,S^4;Z_p) = H~^4(M(Z_p,2);Z_p) = 0
    (relative cup product, p. 209). That step replaces the earlier prose assertion with the long
    exact sequence of the pair and excision. Not claimed: any statement about higher powers or
    about classes above degree 4.
---

::: {.problem}
Let $X$ be $\CP^2$ with a cell $e^3$ attached by a map $S^2 \to \CP^1 \subset \CP^2$ of degree $p$, and let $Y = M(\ZZ_p, 2) \vee S^4$.
Thus $X$ and $Y$ have the same 3-skeleton but differ in the way their 4-cells are attached.
Show that $X$ and $Y$ have isomorphic cohomology rings with $\ZZ$ coefficients but not with $\ZZ_p$ coefficients.
:::

::: {.solution}
No retained solution set covers this exercise: Guanyu Li's set stops at Section 3.2 Exercise 7 (its numbering 3.2.1 through 3.2.7), and the other retained Hatcher sets hold no Section 3.2 solutions. The argument is therefore the card's own, checked against Hatcher, Algebraic Topology, Section 3.2 Exercise 8, with the Cellular Boundary Formula (§2.2), the universal coefficient theorem (Theorem 3.2) and the relative cup product (§3.2).

::: pf

::: {.pf-step #cells}
$X$ has a CW structure with one cell in each of the dimensions $0,2,3,4$, and the integral cellular chain complex is
$$
0\longrightarrow C_4=\ZZ\longrightarrow C_3=\ZZ\longrightarrow C_2=\ZZ\longrightarrow C_1=0,
$$
with $d_3$ multiplication by $p$ and $d_2=d_4=0$.

:::: pf-proof

::: {.pf-step #d3}
$d_3$ is multiplication by $p$.

::: pf-proof
The $3$-cell is attached by a map $S^2\to\CP^1\subset\CP^2$ of degree $p$, and by the Cellular Boundary Formula the coefficient of $e^2$ in $d_3(e^3)$ is the degree of the composite of the attaching map with the collapse of the $2$-skeleton modulo its complement, that is the degree of the attaching map itself, which is $p$. There is only one $2$-cell, so $d_3$ is multiplication by $p$.
:::

:::

::: {.pf-step #d4}
$d_4=0$ and $d_2=0$.

::: pf-proof
$d_2$ lands in $C_1=0$. For $d_4$: the $4$-cell is the top cell of the $\CP^2$ that $X$ contains, so its attaching map is the Hopf map $S^3\to\CP^1$, whose image lies in the $2$-skeleton and therefore misses the interior of the $3$-cell; the composite of the attaching map with the collapse of the $3$-skeleton onto $S^3=S^2\cup e^3$ modulo the open $3$-cell factors through the collapsed $2$-skeleton, which is a point in that quotient, so it is constant and has degree $0$. By the Cellular Boundary Formula the coefficient of $e^3$ in $d_4(e^4)$ vanishes, so $d_4=0$.
:::

:::

::::

:::

::: {.pf-step #homologyX}
$H_2(X;\ZZ)\cong\ZZ_p$, $H_4(X;\ZZ)\cong\ZZ$, and the other reduced integral homology groups of $X$ vanish.

::: pf-proof
From step [](#cells){.pf-ref}, $H_2=\ker d_2/\operatorname{im}d_3=\ZZ/p\ZZ$ because $\ker d_2=C_2=\ZZ$ and $\operatorname{im}d_3=p\ZZ$; $H_3=\ker d_3/\operatorname{im}d_4=0$ because $d_3$ is injective; $H_4=\ker d_4=C_4=\ZZ$ because $C_5=0$; $H_1=0$ because $C_1=0$; and $H_0=\ZZ$ since $X$ is connected.
:::

:::

::: {.pf-step #homologyY}
$H_2(Y;\ZZ)\cong\ZZ_p$, $H_4(Y;\ZZ)\cong\ZZ$, and the other reduced integral homology groups of $Y$ vanish.

::: pf-proof
$Y=M(\ZZ_p,2)\vee S^4$, and the Moore space has a CW structure with cells in dimensions $0,2,3$ whose $3$-cell is attached by a degree $p$ map, so its reduced homology is $\ZZ_p$ in degree $2$ and $0$ in degree $3$. By the wedge axiom of homology, $Y$ has the same reduced integral homology as the Moore space in degrees $\le3$ together with $\ZZ$ in degree $4$ from $S^4$; hence $H_2=\ZZ_p$, $H_3=0$, $H_4=\ZZ$ and the rest vanish.
:::

:::

::: {.pf-step #integral}
With $\ZZ$ coefficients, $H^3(X;\ZZ)\cong\ZZ_p$, $H^4(X;\ZZ)\cong\ZZ$, the corresponding groups for $Y$ are the same, and all other positive-dimensional integral cohomology groups of both spaces vanish.

::: pf-proof
The universal coefficient theorem gives the split exact sequence
$$
0\longrightarrow\operatorname{Ext}(H_{n-1}(X),\ZZ)\longrightarrow H^n(X;\ZZ)\longrightarrow\operatorname{Hom}(H_n(X),\ZZ)\longrightarrow0 .
$$
For $n=3$: $\operatorname{Hom}(H_3,\ZZ)=0$ and $\operatorname{Ext}(H_2,\ZZ)=\operatorname{Ext}(\ZZ_p,\ZZ)\cong\ZZ_p$. For $n=4$: $\operatorname{Ext}(H_3,\ZZ)=0$ and $\operatorname{Hom}(H_4,\ZZ)=\operatorname{Hom}(\ZZ,\ZZ)\cong\ZZ$. For $n\ge5$ both terms involve groups that vanish, and for $n=2$ one gets $\operatorname{Hom}(\ZZ_p,\ZZ)=0$ and $\operatorname{Ext}(H_1,\ZZ)=0$, so $H^2(X;\ZZ)=0$. Step [](#homologyY){.pf-ref} gives the same computation with $Y$ in place of $X$.
:::

:::

::: {.pf-step #integralring}
The integral cohomology rings of $X$ and $Y$ are isomorphic.

::: pf-proof
By step [](#integral){.pf-ref} both rings are $\ZZ$ in degree $0$, $\ZZ_p$ in degree $3$, $\ZZ$ in degree $4$ and $0$ in every other positive degree. Every cup product of two positive-dimensional classes has degree at least $3+3=6$, where both rings vanish, so all products of positive-dimensional classes are zero in both rings. The identity on degree $0$ together with any isomorphism $\ZZ_p\to\ZZ_p$ in degree $3$ and $\ZZ\to\ZZ$ in degree $4$ is therefore an isomorphism of graded rings.
:::

:::

::: {.pf-step #modp}
With $\ZZ_p$ coefficients both spaces have one-dimensional cohomology in each of the degrees $2,3,4$ and nothing else in positive degrees.

::: pf-proof
Tensoring the cellular chain complexes of step [](#cells){.pf-ref} with $\ZZ_p$ makes every differential zero, since $d_3$ is multiplication by $p$; hence the homology with $\ZZ_p$ coefficients equals the chain groups, giving $\ZZ_p$ in degrees $2,3,4$ for $X$ and, for $Y$, $\ZZ_p$ in degrees $2,3$ from the Moore space and $4$ from $S^4$, with all other positive degrees zero. Over the field $\ZZ_p$ the universal coefficient theorem reduces to $H^n(-;\ZZ_p)\cong\operatorname{Hom}(H_n(-;\ZZ_p),\ZZ_p)$, so cohomology is the dual and is again one-dimensional in exactly those degrees.
:::

:::

::: {.pf-step #xclass}
There is a class $x\in H^2(X;\ZZ_p)$ with $x^2\neq0$.

::: pf-proof
Let $i:\CP^2\to X$ be the inclusion of the subcomplex; it carries the $2$-cell and the $4$-cell of $\CP^2$ to those of $X$. Over $\ZZ_p$ the differentials of both cellular complexes vanish, so $H_2(-;\ZZ_p)$ is generated by the $2$-cell and $H_4(-;\ZZ_p)$ by the $4$-cell, in $\CP^2$ and in $X$ alike; hence $i$ induces isomorphisms on $H_2$ and $H_4$ with $\ZZ_p$ coefficients, and dually on $H^2$ and $H^4$. Let $x$ be the class with $i^*x=\alpha$, a generator of $H^2(\CP^2;\ZZ_p)$. Since $i^*$ is a ring homomorphism, $i^*(x^2)=(i^*x)^2=\alpha^2$, and $\alpha^2$ generates $H^4(\CP^2;\ZZ_p)\cong\ZZ_p$ by the cup product structure of projective space, so $\alpha^2\neq0$; as $i^*$ is injective in degree $4$, $x^2\neq0$.
:::

:::

::: {.pf-step #yclass}
Every class $y\in H^2(Y;\ZZ_p)$ satisfies $y^2=0$.

::: pf-proof
Write $Y=M\vee S^4$ with $M=M(\ZZ_p,2)$, and let $j:S^4\to Y$ be the inclusion of the second summand. In the cohomology of the wedge, $H^2(Y;\ZZ_p)\cong H^2(M;\ZZ_p)\oplus H^2(S^4;\ZZ_p)=H^2(M;\ZZ_p)$ because $H^2(S^4)=0$, so every $y$ restricts to $0$ on $S^4$. In the long exact sequence of the pair $(Y,S^4)$ the restriction $H^2(Y;\ZZ_p)\to H^2(S^4;\ZZ_p)$ is zero and $H^1(S^4;\ZZ_p)=0$, so $y$ is the image of a relative class $\bar y\in H^2(Y,S^4;\ZZ_p)$. The relative cup product $H^2(Y,S^4)\times H^2(Y,S^4)\to H^4(Y,S^4)$ of §3.2 then gives $y^2\in H^4(Y,S^4;\ZZ_p)$. Excision identifies $H^4(Y,S^4;\ZZ_p)$ with $\widetilde H^4(Y/S^4;\ZZ_p)=\widetilde H^4(M;\ZZ_p)$, and $M$ has cells only in dimensions $2$ and $3$, so $\widetilde H^4(M;\ZZ_p)=0$. Hence $y^2=0$.
:::

:::

::: {.pf-step}
The $\ZZ_p$ cohomology rings of $X$ and $Y$ are not isomorphic, so the two spaces have isomorphic integral cohomology rings but non-isomorphic $\ZZ_p$ cohomology rings.

::: pf-proof
Steps [](#modp){.pf-ref}, [](#xclass){.pf-ref} and [](#yclass){.pf-ref} give the class $x\in H^2(X;\ZZ_p)$ with $x^2\neq0$ and the fact that the square of every degree-two class of $Y$ vanishes. A graded ring isomorphism $H^*(Y;\ZZ_p)\to H^*(X;\ZZ_p)$ would carry $y$ to some class $y'$ of degree $2$ and would satisfy $(y')^2=(y^2)$'s image $=0$; but every degree-two class of $X$ is a multiple $\lambda x$ of $x$, and $(\lambda x)^2=\lambda^2x^2\neq0$ when $\lambda\neq0$. So no isomorphism carries a generator of $H^2(Y;\ZZ_p)$ to a class of $X$, and the rings are not isomorphic. With step [](#integralring){.pf-ref} this is the exercise's assertion.
:::

:::

:::
:::
