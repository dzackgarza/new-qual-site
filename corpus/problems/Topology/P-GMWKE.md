---
schema: qual/card@1
id: P-GMWKE
kind: problem
title: Cohomology of $S^2 \vee S^2 \vee S^4$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the cohomology groups and cohomology ring $H^*(S^2 \vee S^2 \vee S^4; \mathbb{Z})$ of the wedge sum $X = S^2 \vee S^2 \vee S^4$.
:::

::: solution
**Goal:** Compute the cohomology groups $H^k(X; \mathbb{Z})$ and the cup product ring structure $H^*(X; \mathbb{Z})$ for $X = S_a^2 \vee S_b^2 \vee S^4$.

<1>1. Reduced cohomology of a wedge sum of CW complexes:
    *Proof:*
    <2>1. For any collection of well-pointed spaces $\{X_\alpha\}$, the reduced cohomology of their wedge sum is the direct product (direct sum for finitely many spaces):
        $$\widetilde{H}^k\left(\bigvee_\alpha X_\alpha; \mathbb{Z}\right) \cong \bigoplus_\alpha \widetilde{H}^k(X_\alpha; \mathbb{Z}) \quad \text{for all } k \ge 0.$$
    <2>2. Here $X = S_a^2 \vee S_b^2 \vee S^4$. The reduced cohomology of spheres is:
        $$\widetilde{H}^k(S^n; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & \text{if } k = n, \\ 0 & \text{if } k \ne n. \end{cases}$$

<1>2. Computation of Cohomology Groups $H^k(X; \mathbb{Z})$:
    *Proof:*
    <2>1. **$k = 0$:** $X$ is path-connected, so $H^0(X; \mathbb{Z}) \cong \mathbb{Z}$.
    <2>2. **$k = 1$:** $\widetilde{H}^1(X; \mathbb{Z}) \cong \widetilde{H}^1(S^2) \oplus \widetilde{H}^1(S^2) \oplus \widetilde{H}^1(S^4) = 0 \oplus 0 \oplus 0 = 0$.
    <2>3. **$k = 2$:** $\widetilde{H}^2(X; \mathbb{Z}) \cong \widetilde{H}^2(S_a^2) \oplus \widetilde{H}^2(S_b^2) \oplus \widetilde{H}^2(S^4) \cong \mathbb{Z} \oplus \mathbb{Z} \oplus 0 \cong \mathbb{Z}^2$.
    <2>4. **$k = 3$:** $\widetilde{H}^3(X; \mathbb{Z}) \cong 0 \oplus 0 \oplus 0 = 0$.
    <2>5. **$k = 4$:** $\widetilde{H}^4(X; \mathbb{Z}) \cong \widetilde{H}^4(S_a^2) \oplus \widetilde{H}^4(S_b^2) \oplus \widetilde{H}^4(S^4) \cong 0 \oplus 0 \oplus \mathbb{Z} \cong \mathbb{Z}$.
    <2>6. **$k \ge 5$:** $\widetilde{H}^k(X; \mathbb{Z}) = 0$.
    <2>7. Summary of cohomology groups:
        $$H^k(S^2 \vee S^2 \vee S^4; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & \text{if } k = 0, 4, \\ \mathbb{Z}^2 & \text{if } k = 2, \\ 0 & \text{otherwise}. \end{cases}$$

<1>3. Cohomology Ring Structure (Cup Product):
    *Proof:*
    <2>1. Let $1 \in H^0(X)$ be the identity element.
    <2>2. Let $\alpha, \beta \in H^2(X) \cong \mathbb{Z}^2$ be the generators corresponding to the two 2-spheres $S_a^2, S_b^2$, and let $\gamma \in H^4(X) \cong \mathbb{Z}$ be the generator corresponding to $S^4$.
    <2>3. For a wedge sum $\bigvee X_\alpha$, the cup product of any two positive-degree classes from different wedge summands (or the same sphere summand where cup products vanish) is zero:
        $$\widetilde{H}^p(X) \smile \widetilde{H}^q(X) \to \widetilde{H}^{p+q}(X)$$
        factors through the wedge point.
    <2>4. In particular:
        $$\alpha^2 = 0, \qquad \beta^2 = 0, \qquad \alpha \smile \beta = 0, \qquad \alpha \smile \gamma = 0, \qquad \beta \smile \gamma = 0, \qquad \gamma^2 = 0.$$
    <2>5. Thus, all cup products of positive-degree elements in $H^*(X; \mathbb{Z})$ are trivial.
    <2>6. Ring presentation: $H^*(X; \mathbb{Z}) \cong \mathbb{Z}[\alpha, \beta, \gamma] / (\alpha^2, \beta^2, \gamma^2, \alpha\beta, \alpha\gamma, \beta\gamma)$.

<1>4. Conclusion:
    The cohomology groups are $\mathbb{Z}, 0, \mathbb{Z}^2, 0, \mathbb{Z}, 0, \dots$ with trivial positive cup products. Q.E.D.
:::
