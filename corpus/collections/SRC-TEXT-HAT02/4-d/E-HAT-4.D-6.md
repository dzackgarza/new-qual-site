---
schema: qual/card@1
id: E-HAT-4.D-6
kind: problem
title: Characterization of $\CP^n$-like manifolds
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that if $M$ is a manifold of dimension $2n$ for which there exists a fiber bundle $S^1 \to S^{2n+1} \to M$, then $M$ is simply-connected and $H^*(M; \ZZ) \approx H^*(\CP^n; \ZZ)$ as rings.
Conversely, if $M$ is simply-connected and $H^*(M; \ZZ) \approx H^*(\CP^n; \ZZ)$ as rings, show there is a bundle $S^1 \to E \to M$ where $E \simeq S^{2n+1}$.
:::

::: {.solution}
Take $n \ge 1$; for $n = 0$, $M$ is a point in both directions. All cohomology has $\ZZ$ coefficients. For an orientable circle bundle $S^1 \to E \xrightarrow{\pi} M$ with Euler class $e \in H^2(M)$, the Gysin sequence is
$$\cdots \to H^{j}(M) \xrightarrow{\smile e} H^{j+2}(M) \xrightarrow{\pi^*} H^{j+2}(E) \to H^{j+1}(M) \xrightarrow{\smile e} H^{j+3}(M) \to \cdots.$$

::: pf

::: {.pf-step #forward}
If $S^1 \to S^{2n+1} \xrightarrow{\pi} M$ is a fiber bundle, then $M$ is simply connected and $H^*(M) \cong \ZZ[e]/(e^{n+1})$ with $\gradeddegree{e} = 2$.

::: pf-proof

::: pf-step
$\pi_1(M) = 0$.

::: pf-proof
The long exact homotopy sequence contains $\pi_1(S^{2n+1}) \to \pi_1(M) \to \pi_0(S^1)$, and both ends are trivial.
:::

:::

::: pf-step
$M$ is a closed orientable $2n$-manifold, so $H^{2n}(M) \cong \ZZ$ and $H^k(M) = 0$ for $k > 2n$.

::: pf-proof
$M = \pi(S^{2n+1})$ is compact. A simply connected manifold is orientable.
:::

:::

::: {.pf-step #cup-iso}
$H^1(M) = 0$, and $\smile e: H^j(M) \to H^{j+2}(M)$ is an isomorphism for $0 \le j \le 2n - 2$.

::: pf-proof
The bundle is orientable since $M$ is simply connected, so the Gysin sequence applies. $H^k(S^{2n+1}) = 0$ for $1 \le k \le 2n$. The segment $0 \to H^1(M) \to H^1(S^{2n+1}) = 0$ gives $H^1(M) = 0$. For $0 \le j \le 2n - 2$, the map $\smile e: H^j(M) \to H^{j+2}(M)$ sits between $H^{j+1}(S^{2n+1}) = 0$ and $H^{j+2}(S^{2n+1}) = 0$, so it is an isomorphism.
:::

:::

::: pf-step
$H^*(M) \cong \ZZ[e]/(e^{n+1})$ as rings, which is $H^*(\CP^n)$.

::: pf-proof
By step [](#cup-iso){.pf-ref}, induction from $H^0(M) = \ZZ$ and $H^1(M) = 0$ gives $H^{2k}(M) = \ZZ e^k$ for $0 \le k \le n$ and $H^{2k+1}(M) = 0$ for $2k + 1 < 2n$. All higher groups vanish, so $e^{n+1} = 0$ and $H^*(M)$ is the truncated polynomial ring.
:::

:::

:::

:::

::: {.pf-step #converse}
If $M$ is simply connected and $H^*(M) \cong \ZZ[\alpha]/(\alpha^{n+1})$ with $\gradeddegree{\alpha} = 2$, then there is a circle bundle $S^1 \to E \to M$ with $E \simeq S^{2n+1}$.

::: pf-proof

::: pf-step
Let $c: M \to \CP^\infty$ classify $\alpha$, so $c^* u = \alpha$ for the generator $u \in H^2(\CP^\infty)$, and let $S^1 \to E \xrightarrow{\pi} M$ be the pullback of $S^1 \to S^\infty \to \CP^\infty$. Its Euler class is $\alpha$.

::: pf-proof
$\CP^\infty = K(\ZZ, 2)$, so $[M, \CP^\infty] = H^2(M)$. The universal bundle has Euler class $u$, and Euler classes are natural under pullback.
:::

:::

::: {.pf-step #E-cohomology}
$H^k(E) \cong \ZZ$ for $k = 0, 2n+1$ and $H^k(E) = 0$ otherwise.

::: pf-proof
In the ring $\ZZ[\alpha]/(\alpha^{n+1})$, $\smile \alpha: H^j(M) \to H^{j+2}(M)$ is an isomorphism for $0 \le j \le 2n - 2$, and odd groups vanish. In the Gysin sequence, $H^{k}(E)$ for $1 \le k \le 2n$ lies between a cokernel and a kernel of these isomorphisms or of maps between zero groups, so $H^k(E) = 0$. At the top, $0 = H^{2n+1}(M) \to H^{2n+1}(E) \to H^{2n}(M) \to H^{2n+2}(M) = 0$ gives $H^{2n+1}(E) \cong \ZZ$. Above that, the groups of $M$ vanish.
:::

:::

::: {.pf-step #E-simply-connected}
$\pi_1(E) = 0$.

::: pf-proof
The homotopy sequence gives $\pi_2(M) \xrightarrow{\partial} \pi_1(S^1) \to \pi_1(E) \to \pi_1(M) = 0$. By naturality, $\partial = \partial_\infty \circ c_*$, where $\partial_\infty: \pi_2(\CP^\infty) \to \pi_1(S^1)$ is an isomorphism because $S^\infty$ is contractible. Both $M$ and $\CP^\infty$ are simply connected, so by Hurewicz $c_*$ on $\pi_2$ is $c_*$ on $H_2$. Because $H_1 = 0$, $H^2 = \operatorname{Hom}(H_2, \ZZ)$, and $c^* u = \alpha$ is a generator, so $c_*$ on $H_2$ is an isomorphism. So $\partial$ is surjective and $\pi_1(E) = 0$.
:::

:::

::: pf-step
$E \simeq S^{2n+1}$.

::: pf-proof
$E$ is a closed manifold, so it has the homotopy type of a CW complex with finitely generated homology. By step [](#E-cohomology){.pf-ref} and universal coefficients, $\widetilde H_k(E) = 0$ for $k \le 2n$ and $H_{2n+1}(E) \cong \ZZ$. By step [](#E-simply-connected){.pf-ref} and Hurewicz, $E$ is $2n$-connected and $\pi_{2n+1}(E) \cong H_{2n+1}(E)$. A generator gives $\phi: S^{2n+1} \to E$ inducing an isomorphism on all homology groups. Both spaces are simply connected CW complexes, so $\phi$ is a homotopy equivalence by Whitehead's theorem.
:::

:::

:::

:::

:::

:::
