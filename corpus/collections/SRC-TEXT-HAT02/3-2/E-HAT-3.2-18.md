---
schema: qual/card@1
id: E-HAT-3.2-18
kind: problem
title: Cup product nondegenerality on surfaces
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
For the closed orientable surface $M$ of genus $g \geq 1$, show that for each nonzero $\alpha \in H^1(M; \mathbb{Z})$ there exists $\beta \in H^1(M; \mathbb{Z})$ with $\alpha \beta \neq 0$.
Deduce that $M$ is not homotopy equivalent to a wedge sum $X \vee Y$ of CW complexes with nontrivial reduced homology.
Do the same for closed nonorientable surfaces using cohomology with $\mathbb{Z}_2$ coefficients.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$H^1(M;\ZZ) \cong \ZZ^{2g}$, and the cup product pairing $H^1 \times H^1 \to H^2 \cong \ZZ$ is a nondegenerate symplectic form.

::: pf-proof

standard computation of the cohomology ring of a closed orientable surface of genus $g$; the cup product is the intersection form, which is symplectic (nondegenerate alternating).

:::

:::

::: {.pf-step #s2}

For each nonzero $\alpha \in H^1(M;\ZZ)$ there is $\beta \in H^1(M;\ZZ)$ with $\alpha \smile \beta \neq 0$.

::: pf-proof

nondegeneracy of the symplectic form in step [](#s1){.pf-ref}: if $\alpha \smile \beta = 0$ for all $\beta$, then $\alpha = 0$.

:::

:::

::: {.pf-step #s3}

$M$ is not homotopy equivalent to a wedge $X \vee Y$ with $\widetilde{H}_*(X) \neq 0$ and $\widetilde{H}_*(Y) \neq 0$.

::: pf-proof

::: {.pf-step #s3-1}

For a wedge $X \vee Y$, the cup product of any class in $H^1(X)$ with any class in $H^1(Y)$ is zero.

::: pf-proof

the cup product $H^1(X \vee Y) \times H^1(X \vee Y) \to H^2(X \vee Y)$ is zero, since $H^1(X \vee Y) \cong H^1(X) \oplus H^1(Y)$ and cross terms vanish (the two summands are "disjoint" in the wedge).

:::

:::

::: {.pf-step #s3-2}

But $M$ has a nonzero cup product $H^1 \times H^1 \to H^2$.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

::: pf-step

Hence $M$ is not homotopy equivalent to any such wedge.

::: pf-proof

the cup product structure is a homotopy invariant, and step [](#s3-1){.pf-ref} contradicts step [](#s3-2){.pf-ref}.

:::

:::

:::

:::

::: pf-step

Nonorientable case: for a closed nonorientable surface $N$, $H^1(N;\ZZ_2) \cong \ZZ_2^{g}$ (where $g$ is the genus), and the cup product pairing $H^1(N;\ZZ_2) \times H^1(N;\ZZ_2) \to H^2(N;\ZZ_2) \cong \ZZ_2$ is nondegenerate.

::: pf-proof

standard computation of the $\ZZ_2$-cohomology ring of a nonorientable surface.

:::

:::

::: {.pf-step #s5}

Hence for each nonzero $\alpha \in H^1(N;\ZZ_2)$ there is $\beta$ with $\alpha \smile \beta \neq 0$, and $N$ is not homotopy equivalent to a wedge $X \vee Y$ with nontrivial reduced homology.

::: pf-proof

the same argument as steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, with $\ZZ_2$ coefficients.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::
