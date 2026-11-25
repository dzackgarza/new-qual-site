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
$\Omega\neq\CC$ is necessary because $\CC$ is not biholomorphic to $\DD$, and simple connectivity because a biholomorphism is a homeomorphism; the classification of the simply connected models is [[C-BKYF7]].
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
which is the pair of conditions under which [@SS03, ch. 8, Theorem 3.1] makes the map unique.
The boundary lines land on the two semicircles: $\Im z = 0$ on the lower one, through $F(0) = -i$, and $\Im z = \pi$ on the upper one, through $F(i\pi) = i$, with both ends tending to $-1$ and to $1$.
Inside, $F(0.3+0.7i) = 0.1802\ldots-0.4527\ldots i$, of modulus $0.4872\ldots$
:::

[[C-BKYF7]]

[[P-Z776N]]
