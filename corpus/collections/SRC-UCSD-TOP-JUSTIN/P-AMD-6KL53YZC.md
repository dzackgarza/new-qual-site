---
schema: qual/card@1
id: P-AMD-6KL53YZC
kind: problem
title: 'For $f: S^n\circlearrowleft$, show $\deg f = \deg \Sigma f$'
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
For $f: S^n\circlearrowleft$, show $\deg f = \deg \Sigma f$

1. Conclude $\pi_n(S^n) = \ZZ$
:::

::: {.solution}
**Goal:** Let $f \colon S^n \to S^n$ be a continuous map ($n \ge 1$), and let $\Sigma f \colon \Sigma S^n \cong S^{n+1} \to \Sigma S^n \cong S^{n+1}$ be its suspension. Prove that $\deg(\Sigma f) = \deg(f)$, and conclude that $\pi_n(S^n) \cong \mathbb{Z}$.

<1>1. Definition of degree and suspension isomorphism in homology.
  <2>1. For any continuous map $g \colon S^k \to S^k$ ($k \ge 1$), the degree $\deg(g) \in \mathbb{Z}$ is defined by the induced map on top homology: $g_*(\alpha) = (\deg g) \cdot \alpha$ for any generator $\alpha \in \widetilde{H}_k(S^k) \cong \mathbb{Z}$.
  <2>2. Decompose $\Sigma S^n$ as the union of two open cones $C_+ S^n$ and $C_- S^n$ intersecting along $S^n \times (-1, 1) \simeq S^n$.
  <2>3. The suspension isomorphism $\sigma \colon \widetilde{H}_n(S^n) \xrightarrow{\cong} \widetilde{H}_{n+1}(\Sigma S^n)$ is the connecting isomorphism in the Mayer-Vietoris sequence of the suspension:
  $$\widetilde{H}_{n+1}(C_+ S^n) \oplus \widetilde{H}_{n+1}(C_- S^n) \to \widetilde{H}_{n+1}(\Sigma S^n) \xrightarrow{\partial} \widetilde{H}_n(S^n) \to \widetilde{H}_n(C_+ S^n) \oplus \widetilde{H}_n(C_- S^n).$$
  Since cones are contractible, $\partial \colon \widetilde{H}_{n+1}(\Sigma S^n) \to \widetilde{H}_n(S^n)$ is an isomorphism, and $\sigma = \partial^{-1}$.
  <2>4. Proof: By Mayer-Vietoris sequence for suspension. Q.E.D.

<1>2. Prove $\deg(\Sigma f) = \deg(f)$.
  <2>1. The suspension map $\Sigma f \colon \Sigma S^n \to \Sigma S^n$ preserves the cones $C_+ S^n, C_- S^n$ and restricts on the equator $S^n$ to $f$.
  <2>2. By naturality of the Mayer-Vietoris connecting homomorphism $\partial$ (proved in P-AMD-2IFZW3JK), the following square commutes:
  $$
  \begin{CD}
  \widetilde{H}_{n+1}(\Sigma S^n) @>{\partial}>{\cong}> \widetilde{H}_n(S^n) \\
  @VV{(\Sigma f)_*}V @VV{f_*}V \\
  \widetilde{H}_{n+1}(\Sigma S^n) @>{\partial}>{\cong}> \widetilde{H}_n(S^n)
  \end{CD}
  $$
  <2>3. Let $\beta \in \widetilde{H}_{n+1}(\Sigma S^n)$ be a generator such that $\partial(\beta) = \alpha \in \widetilde{H}_n(S^n)$ is a generator.
  <2>4. Computing along the diagram:
  $$\partial((\Sigma f)_*(\beta)) = f_*(\partial(\beta)) = f_*(\alpha) = (\deg f) \alpha.$$
  <2>5. Applying $\sigma = \partial^{-1}$ yields:
  $$(\Sigma f)_*(\beta) = (\deg f) \beta.$$
  <2>6. By definition of degree, $(\Sigma f)_*(\beta) = (\deg \Sigma f) \beta$, hence $\deg(\Sigma f) = \deg(f)$.
  <2>7. Proof: By commutativity of the Mayer-Vietoris naturality square. Q.E.D.

<1>3. Conclude that $\pi_n(S^n) \cong \mathbb{Z}$ for all $n \ge 1$.
  <2>1. Base case $n = 1$: $\pi_1(S^1) \cong \mathbb{Z}$ via the degree map / winding number (fundamental group of the circle).
  <2>2. The degree map $\deg \colon \pi_n(S^n) \to \mathbb{Z}$ sending $[g] \mapsto \deg(g)$ is a well-defined group homomorphism for all $n \ge 1$.
  <2>3. $\deg$ is surjective: The map $z \mapsto z^d$ on $S^1$ has degree $d$. Taking $n-1$ successive suspensions $\Sigma^{n-1}(z \mapsto z^d)$ yields a map $S^n \to S^n$ of degree $d$ by <1>2.
  <2>4. $\deg$ is injective: By the Hopf degree theorem, two continuous maps $f, g \colon S^n \to S^n$ are homotopic if and only if $\deg(f) = \deg(g)$. (Equivalently, by the Hurewicz theorem, since $S^n$ is $(n-1)$-connected for $n \ge 2$, the Hurewicz homomorphism $h \colon \pi_n(S^n) \to H_n(S^n) \cong \mathbb{Z}$ given by $[f] \mapsto f_*([S^n]) = (\deg f)[S^n]$ is an isomorphism).
  <2>5. Therefore, $\pi_n(S^n) \cong \mathbb{Z}$.
  <2>6. Proof: By Hurewicz theorem and Hopf degree theorem. Q.E.D.

<1>4. Q.E.D.
  <2>1. Proof: Steps <1>1–<1>3 complete the proof.
:::

