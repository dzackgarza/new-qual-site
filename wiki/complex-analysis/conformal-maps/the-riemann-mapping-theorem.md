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
$\Omega\neq\CC$: a holomorphic map $F\colon\CC\to\DD$ is bounded and entire, hence constant by [[T-QHIHJ|Liouville's theorem]], so $\CC$ is not biholomorphic to $\DD$.

$\Omega$ simply connected: a biholomorphism is a homeomorphism, and $\DD$ is simply connected.

:::

The proof maximizes $\abs{f'(z_0)}$ over the injective holomorphic maps $\Omega\to\DD$ carrying $z_0$ to $0$, and shows a maximizer is surjective [@SS03, Theorem 3.1 (p. 224)].

::: {.remark title="Ingredients of the proof"}
[[complex-analysis/conformal-maps/normal-families-and-montel|Montel's theorem]] gives a convergent maximizing subsequence, [[complex-analysis/counting-zeros/hurwitz|Hurwitz's theorem]] gives injectivity of the limit, [[complex-analysis/cauchy-theory/cauchy-estimates-and-liouville|the Cauchy estimate]] gives $m<\infty$, and square roots on simply connected sets together with [[complex-analysis/conformal-maps/blaschke-factors-and-automorphisms|Blaschke factors]] give nonemptiness of $\mathcal F$ and the derivative increase.

:::

::: {.example title="The map of a strip, written down"}
For the strip $L = \theset{0<\Im z<\pi}$ the exponential carries $L$ onto $\HH$, and [[complex-analysis/conformal-maps/build-me-a-map|the Cayley map]] carries $\HH$ onto $\DD$, so
$$
F(z) = {e^z-i\over e^z+i}
$$
is a biholomorphism $L\to\DD$.
It is the normalized one at $z_0 = i\pi/2$: $F(i\pi/2) = 0$, and since $F'(z) = 2ie^z/(e^z+i)^2$,
$$
F'(i\pi/2) = {2i\cdot i\over (2i)^2} = \frac12 > 0,
$$
which is the pair of conditions under which [@SS03, Theorem 3.1 (p. 224)] makes the map unique.
The boundary lines land on the two semicircles: $\Im z = 0$ on the lower one, through $F(0) = -i$, and $\Im z = \pi$ on the upper one, through $F(i\pi) = i$, with both ends tending to $-1$ and to $1$.
Inside, $F(0.3+0.7i) = 0.1802\ldots-0.4527\ldots i$, of modulus $0.4872\ldots$
:::

[[C-BKYF7]]

[[P-Z776N]]
