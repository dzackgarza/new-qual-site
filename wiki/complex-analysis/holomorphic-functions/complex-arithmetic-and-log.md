---
title: Complex arithmetic and the logarithm
order: 10
topics:
- Complex Numbers
- Complex Logarithm
---

# Complex arithmetic and the logarithm

## Roots

[[T-NRT7K]]

[[T-6XDRA]]

## The logarithm

[[D-4CSPM]]

[[D-T6INB]]

[[PR-MWUJS]]

Recall [[P-Y5SS5]]: on a simply connected domain a [[D-E7A5W|holomorphic]] function without zeros is $e^g$, and $e^{g/n}$ is then a holomorphic $n$th root.

[[T-NRSFZ]]

## Branch cuts and branch points

::: {.warnings}
Recall [[D-T6INB|the branch of $z^{1/n}$]] determined by a continuous branch $L$ of the logarithm: writing $z=re^{i\theta}$ with $\theta=\Im L(z)$, the branch takes the value $r^{1/n}e^{i\theta/n}$.
A different continuous argument shifts $\theta$ by $2\pi k$ and the value by $e^{2\pi ik/n}$, so on $\CC\sm\theset{0}$ no continuous choice exists, while on a simply connected domain avoiding $0$ one exists by [[PR-MWUJS]].
:::

::: {.example title="Where continuity fails"}
Take $\zeta \coloneqq x + i0$ with $x <0$, and approach it from either side along $\zeta_\pm \coloneqq x \pm i\varepsilon$ as $\varepsilon\to 0^+$.
For the principal branch:

- $\Log(\zeta_+) \to \log\abs x + i\pi$,
- $\Log(\zeta_-) \to \log\abs x - i\pi$.

So no value at $\zeta$ makes $\Log$ continuous across the negative real axis.
Removing the cut fixes the discontinuity, and the point $0$ remains: it is a [[D-9KMTV|branch point]], since $\Log$ has no continuous branch on any punctured neighborhood of the origin, whatever cut is chosen.
:::

[[P-Y5SS5]]

## The quadratic formula over $\CC$

[[T-QDRTC]]

## Exercises

[[P-4GDBQ]]
[[P-LHZGV]]
[[E-X4MBB]]
[[E-WNNSK]]
[[E-P7SIB]]
[[E-JWO2G]]
[[E-QVMUV]]
