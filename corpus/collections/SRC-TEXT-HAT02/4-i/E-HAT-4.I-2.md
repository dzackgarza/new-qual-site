---
schema: qual/card@1
id: E-HAT-4.I-2
kind: problem
title: "Suspension of $K(\\mathbb{Z}_m \\times \\mathbb{Z}_n, 1)$ for coprime $m, n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Using the Künneth formula, show that $\Sigma K(\mathbb{Z}_m \times \mathbb{Z}_n, 1) \simeq \Sigma K(\mathbb{Z}_m, 1) \vee \Sigma K(\mathbb{Z}_n, 1)$ if $m$ and $n$ are relatively prime.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suspension of a Cartesian product:

::: pf-proof

::: pf-step

For any pointed CW complexes $X$ and $Y$, there is a natural homotopy equivalence:
\[
\Sigma(X \times Y) \simeq \Sigma X \vee \Sigma Y \vee \Sigma(X \wedge Y).
\]

::: pf-proof

Hatcher Proposition 4I.1 (suspension splits product into wedges with the smash product).

:::

:::

::: pf-step

Let $X = K(\mathbb{Z}_m, 1)$ and $Y = K(\mathbb{Z}_n, 1)$. Since $K(G \times H, 1) \simeq K(G, 1) \times K(H, 1)$, we have:
\[
\Sigma K(\mathbb{Z}_m \times \mathbb{Z}_n, 1) \simeq \Sigma K(\mathbb{Z}_m, 1) \vee \Sigma K(\mathbb{Z}_n, 1) \vee \Sigma\big(K(\mathbb{Z}_m, 1) \wedge K(\mathbb{Z}_n, 1)\big).
\]

::: pf-proof

product of Eilenberg–MacLane spaces.

:::

:::

:::

:::

::: {.pf-step #s2}

Show that $\Sigma(X \wedge Y)$ is contractible when $\gcd(m, n) = 1$:

::: pf-proof

::: pf-step

The reduced homology groups $\widetilde{H}_i(X)$ are non-zero only in odd degrees, where $\widetilde{H}_{2k+1}(K(\mathbb{Z}_m, 1)) \cong \mathbb{Z}_m$. In particular, $m \cdot \widetilde{H}_i(X) = 0$ for all $i \ge 0$.

::: pf-proof

homology of lens spaces / $K(\mathbb{Z}_m, 1)$.

:::

:::

::: pf-step

Symmetrically, $n \cdot \widetilde{H}_j(Y) = 0$ for all $j \ge 0$.

::: pf-proof

homology of $K(\mathbb{Z}_n, 1)$.

:::

:::

::: pf-step

By Bézout’s Identity, $\gcd(m, n) = 1$ implies there exist integers $u, v \in \mathbb{Z}$ such that $um + vn = 1$.

::: pf-proof

Euclidean algorithm.

:::

:::

::: {.pf-step #s2-4}

For any $m$-torsion abelian group $A$ and $n$-torsion abelian group $B$:
- $A \otimes_\mathbb{Z} B = 0$, because $a \otimes b = (um + vn)(a \otimes b) = u(ma \otimes b) + v(a \otimes nb) = 0$.
- $\operatorname{Tor}_1^\mathbb{Z}(A, B) = 0$, because Tor is annihilated by both $m$ and $n$, hence by $\gcd(m, n) = 1$.

::: pf-proof

algebra of torsion abelian groups.

:::

:::

::: pf-step

By the Künneth formula for smash products:
\[
\widetilde{H}_k(X \wedge Y) \cong \bigoplus_{i+j=k} \big(\widetilde{H}_i(X) \otimes \widetilde{H}_j(Y)\big) \oplus \bigoplus_{i+j=k-1} \operatorname{Tor}_1^\mathbb{Z}\big(\widetilde{H}_i(X), \widetilde{H}_j(Y)\big) = 0 \quad \text{for all } k \ge 0.
\]

::: pf-proof

Künneth formula for spaces and step [](#s2-4){.pf-ref}.

:::

:::

::: pf-step

The suspension $\Sigma(X \wedge Y)$ is simply connected and has all reduced homology groups zero:
\[
\widetilde{H}_*(\Sigma(X \wedge Y)) \cong \widetilde{H}_{*-1}(X \wedge Y) = 0.
\]

::: pf-proof

suspension isomorphism in homology.

:::

:::

::: pf-step

By Whitehead’s Theorem for simply connected CW complexes with trivial homology, $\Sigma(X \wedge Y) \simeq *$.

::: pf-proof

Whitehead's Theorem and Hurewicz Theorem.

:::

:::

:::

:::

::: pf-step

Conclusion:
\[
\Sigma K(\mathbb{Z}_m \times \mathbb{Z}_n, 1) \simeq \Sigma K(\mathbb{Z}_m, 1) \vee \Sigma K(\mathbb{Z}_n, 1) \vee * \simeq \Sigma K(\mathbb{Z}_m, 1) \vee \Sigma K(\mathbb{Z}_n, 1).
\]
Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
