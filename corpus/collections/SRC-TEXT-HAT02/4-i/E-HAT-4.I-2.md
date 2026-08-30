---
schema: qual/card@1
id: E-HAT-4.I-2
kind: exercise
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

Using the Künneth formula, show that $\Sigma K(\mathbb{Z}_m \times \mathbb{Z}_n, 1) \simeq \Sigma K(\mathbb{Z}_m, 1) \vee \Sigma K(\mathbb{Z}_n, 1)$ if $m$ and $n$ are relatively prime.

::: {.solution}
<1>1. Suspension of a Cartesian product:
<2>1. For any pointed CW complexes $X$ and $Y$, there is a natural homotopy equivalence:
\[
\Sigma(X \times Y) \simeq \Sigma X \vee \Sigma Y \vee \Sigma(X \wedge Y).
\]
Proof: Hatcher Proposition 4I.1 (suspension splits product into wedges with the smash product).
<2>2. Let $X = K(\mathbb{Z}_m, 1)$ and $Y = K(\mathbb{Z}_n, 1)$. Since $K(G \times H, 1) \simeq K(G, 1) \times K(H, 1)$, we have:
\[
\Sigma K(\mathbb{Z}_m \times \mathbb{Z}_n, 1) \simeq \Sigma K(\mathbb{Z}_m, 1) \vee \Sigma K(\mathbb{Z}_n, 1) \vee \Sigma\big(K(\mathbb{Z}_m, 1) \wedge K(\mathbb{Z}_n, 1)\big).
\]
Proof: product of Eilenberg–MacLane spaces.

<1>2. Show that $\Sigma(X \wedge Y)$ is contractible when $\gcd(m, n) = 1$:
<2>1. The reduced homology groups $\widetilde{H}_i(X)$ are non-zero only in odd degrees, where $\widetilde{H}_{2k+1}(K(\mathbb{Z}_m, 1)) \cong \mathbb{Z}_m$. In particular, $m \cdot \widetilde{H}_i(X) = 0$ for all $i \ge 0$.
Proof: homology of lens spaces / $K(\mathbb{Z}_m, 1)$.
<2>2. Symmetrically, $n \cdot \widetilde{H}_j(Y) = 0$ for all $j \ge 0$.
Proof: homology of $K(\mathbb{Z}_n, 1)$.
<2>3. By Bézout’s Identity, $\gcd(m, n) = 1$ implies there exist integers $u, v \in \mathbb{Z}$ such that $um + vn = 1$.
Proof: Euclidean algorithm.
<2>4. For any $m$-torsion abelian group $A$ and $n$-torsion abelian group $B$:
- $A \otimes_\mathbb{Z} B = 0$, because $a \otimes b = (um + vn)(a \otimes b) = u(ma \otimes b) + v(a \otimes nb) = 0$.
- $\operatorname{Tor}_1^\mathbb{Z}(A, B) = 0$, because Tor is annihilated by both $m$ and $n$, hence by $\gcd(m, n) = 1$.
Proof: algebra of torsion abelian groups.
<2>5. By the Künneth formula for smash products:
\[
\widetilde{H}_k(X \wedge Y) \cong \bigoplus_{i+j=k} \big(\widetilde{H}_i(X) \otimes \widetilde{H}_j(Y)\big) \oplus \bigoplus_{i+j=k-1} \operatorname{Tor}_1^\mathbb{Z}\big(\widetilde{H}_i(X), \widetilde{H}_j(Y)\big) = 0 \quad \text{for all } k \ge 0.
\]
Proof: Künneth formula for spaces and <2>4.
<2>6. The suspension $\Sigma(X \wedge Y)$ is simply connected and has all reduced homology groups zero:
\[
\widetilde{H}_*(\Sigma(X \wedge Y)) \cong \widetilde{H}_{*-1}(X \wedge Y) = 0.
\]
Proof: suspension isomorphism in homology.
<2>7. By Whitehead’s Theorem for simply connected CW complexes with trivial homology, $\Sigma(X \wedge Y) \simeq *$.
Proof: Whitehead's Theorem and Hurewicz Theorem.

<1>3. Conclusion:
\[
\Sigma K(\mathbb{Z}_m \times \mathbb{Z}_n, 1) \simeq \Sigma K(\mathbb{Z}_m, 1) \vee \Sigma K(\mathbb{Z}_n, 1) \vee * \simeq \Sigma K(\mathbb{Z}_m, 1) \vee \Sigma K(\mathbb{Z}_n, 1).
\]
Q.E.D.
Proof: <1>1 and <1>2.
:::
