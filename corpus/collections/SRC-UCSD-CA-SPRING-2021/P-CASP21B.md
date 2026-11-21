---
schema: qual/card@1
id: P-CASP21B
kind: problem
title: 'Polynomial approximation of $\bar z$ on arcs and on the unit circle'
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomial Approximation
  - Mergelyan Theorem
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the two answers already on the card, Yes and No,
    both correct. Added: the verification of Mergelyan's hypotheses for a proper closed arc —
    compactness, connectedness of the complement (the exterior and the disc joined through the
    open remainder of the circle), and the emptiness of the interior, which makes the
    holomorphy hypothesis vacuous; and, for (ii), the estimate turning uniform convergence on
    the circle into convergence of the integrals, with Cauchy's theorem giving 0 for each
    polynomial against the value 2 pi i for 1/z. Not claimed: a retained solution set; the
    provenance names the examination paper.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the two answers already on the card, Yes and No,
    both correct. Added: the verification of Mergelyan's hypotheses for a proper closed arc —
    compactness, connectedness of the complement (the exterior and the disc joined through the
    open remainder of the circle), and the emptiness of the interior, which makes the
    holomorphy hypothesis vacuous; and, for (ii), the estimate turning uniform convergence on
    the circle into convergence of the integrals, with Cauchy's theorem giving 0 for each
    polynomial against the value 2 pi i for 1/z. Not claimed: a retained solution set; the
    provenance names the examination paper.
---

::: {.problem}
Let $K$ be a proper closed arc of the unit circle $\abs{z} = 1$.

(i) Is there a sequence of polynomials $P_n(z)$ such that $P_n(z) \to \bar{z}$ uniformly in $K$?

(ii) Is there a sequence of polynomials $P_n(z)$ such that $P_n(z) \to \bar{z}$ uniformly on the circle $\abs{z} = 1$?

Please justify your answers.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2021 complex-analysis examination paper, which carries no solutions. The two answers — (i) yes, (ii) no — are the card's own and follow the card's previous prose, with the hypotheses of Mergelyan's theorem checked in (i) and the integration argument made explicit in (ii).

Throughout $K$ is a proper closed arc of the unit circle $\circlegroup=\theset{\abs z=1}$, and "uniformly approximable by polynomials on $E$" means: for every continuous $g$ on $E$ and $\varepsilon>0$ there is a polynomial $P$ with $\sup_E\abs{g-P}<\varepsilon$.

::: pf

::: {.pf-step #mergelyan}
Mergelyan's theorem applies to $K$: $K$ is compact, $\CC\setminus K$ is connected, and every continuous function on $K$ is uniformly approximable there by polynomials.

::: pf-proof
$K$ is a closed subset of the compact circle, hence compact. Its complement in the sphere is connected: $\CC\setminus K$ is the union of the open exterior of the circle $\theset{\abs z>1}$ with the open disk $\DD$ and the open arcs of the circle outside $K$; removing a proper closed arc leaves a connected remainder, and the exterior and disk are joined to it (each point of the circle outside $K$ is a limit of points of $\DD$ and of the exterior). Mergelyan's theorem states that for compact $E$ with $\CC\setminus E$ connected, every function continuous on $E$ and holomorphic on the interior of $E$ is uniformly approximable on $E$ by polynomials; here $K$ has empty interior, so the holomorphy hypothesis is vacuous and the theorem applies to every continuous function on $K$.

:::

:::

::: {.pf-step #part-i}
(i) there are polynomials $P_n$ with $P_n\to\bar z$ uniformly on $K$.

::: pf-proof
$z\mapsto\bar z$ is continuous on $K$ (it is continuous on $\CC$), so by step [](#mergelyan){.pf-ref} it is uniformly approximable on $K$ by polynomials: for each $n$ take $P_n$ with $\sup_K\abs{\bar z-P_n}<1/n$. Then $P_n\to\bar z$ uniformly on $K$.

:::

:::

::: {.pf-step #part-ii}
(ii) no sequence of polynomials converges uniformly to $\bar z$ on the whole circle.

::: pf-proof
On the circle $\bar z=1/z$. Suppose $P_n\to1/z$ uniformly on $\circlegroup$. Each $P_n$ is entire, so $\int_{\circlegroup}P_n(z)\,dz=0$ by Cauchy's theorem. Uniform convergence on the compact circle permits termwise integration of the limit:
$$
\abs{\int_{\circlegroup}P_n\,dz-\int_{\circlegroup}\frac{dz}{z}}\le2\pi\sup_{\circlegroup}\abs{P_n-\frac1z}\longrightarrow0,
$$
so $\int_{\circlegroup}dz/z=0$. But $\int_{\circlegroup}dz/z=2\pi i\ne0$. Contradiction.

:::

:::

::: {.pf-step #conclusion}
The answers are (i) yes and (ii) no.

::: pf-proof
Steps [](#part-i){.pf-ref} and [](#part-ii){.pf-ref}. The contrast is exactly the Mergelyan hypothesis: removing a proper arc makes $\CC\setminus K$ connected, and removing the whole circle does not.

:::

:::

:::
:::
