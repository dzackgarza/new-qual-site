---
title: The Riemann mapping theorem
order: 50
topics:
- Riemann Mapping Theorem
- Simply Connected
- Univalent Functions

---

# The Riemann mapping theorem

::: {.slogan}
If $\Omega \subsetneq \CC$ is simply connected then $\Omega$ is biholomorphic to $\DD$.

:::

[[T-4MDS6]]

::: {.remark title="$\Omega\neq\CC$ and simple connectivity are necessary"}
$\Omega\neq\CC$: a holomorphic map $F\colon\CC\to\DD$ is bounded and entire, hence constant by Liouville's theorem, so $\CC$ is not biholomorphic to $\DD$.

$\Omega$ simply connected: a biholomorphism is a homeomorphism, and $\DD$ is simply connected.

:::

The proof maximizes $\abs{f'(z_0)}$ over the injective holomorphic maps $\Omega\to\DD$ carrying $z_0$ to $0$, and shows a maximizer is surjective [@SS03, Theorem 3.1 (p. 224)].

::: {.remark title="Ingredients of the proof"}
[[complex-analysis/conformal-maps/normal-families-and-montel|Montel's theorem]] gives a convergent maximizing subsequence, [[complex-analysis/counting-zeros/hurwitz|Hurwitz's theorem]] gives injectivity of the limit, [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|the Cauchy estimate]] gives $m<\infty$, and square roots on simply connected sets together with [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors]] give nonemptiness of $\mathcal F$ and the derivative increase.

:::

[[C-BKYF7]]

[[P-Z776N]]
