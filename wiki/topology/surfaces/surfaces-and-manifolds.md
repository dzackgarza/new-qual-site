---
title: Surfaces, manifolds, and knots
order: 250
topics:
- Surfaces
- Manifolds
- Classification of Surfaces
- Classification
- Orientation
- Knot Theory
---

# Surfaces and manifolds

::: {.example title="Standard surfaces"}
\envlist

- the sphere $S^2$;

- the torus $T^2 \coloneqq  S^1\cross S^1$;

- the real projective plane $\RP^2$;

- the Klein bottle $\KK$;

- the Möbius band $\mobiusband$;

- the closed orientable surface of genus $g$, $\Sigma_g \coloneqq \#_{i=1}^g T^2$.

The Möbius band, the annulus $S^1\cross I$, $T^2$, $\KK$, and $\RP^2$ are quotients of a square by the edge identifications in these pasting diagrams:

![Pasting diagrams for the Möbius band, the annulus, $T^2$, $\KK$, and $\RP^2$](../../../../assets/assets/Topology/figures/PastingDiagrams.png)

:::

## Classification of surfaces

### The classification theorem

[[T-NBARV]]

::: {.remark}
A polygon model computes the orientability, $b$ and $\chi$ of a surface: the edge word of a polygon with identifications reduces to a normal form $a_1b_1\inverseof{a_1} \inverseof{b_1}\cdots a_gb_g\inverseof{a_g} \inverseof{b_g}$ or $a_1a_1\cdots a_ka_k$, together with the unpaired boundary edges.
For example, the torus and the annulus both have Euler characteristic $0$ and are not homeomorphic, since $b=0$ for the torus and $b=2$ for the annulus.

:::

[[FF-D5Q4S]] [[FF-WDTKX]]

[[PR-JL5JP]]

### Euler characteristic

[[FF-W3AIU]]

::: {.fact title="Closed surfaces by Euler characteristic"}
With $N_k \coloneqq \#_{i=1}^k\RP^2$, the closed surfaces by Euler characteristic are:

| Orientable | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
| ---------- | ---        | ----        | ----       | ---         | ---     | ---     | ---         |
| Yes | $\Sigma_3$ | none | $\Sigma_2$ | none | $T^2$ | none | $S^2$ |
| No | $N_6$ | $N_5$ | $N_4$ | $N_3$ | $\KK$ | $\RP^2$ | none |

With boundary, $\chi=0$ also includes the annulus $S^1\cross I$ and the Möbius band $\mobiusband$, and $\chi=1$ includes the disc $\DD^2$.

:::

[[FF-23V5J]]

[[FF-SM63J]]

[[FF-BOIT5]]

[[PR-QV4U5]]

[[C-CT2NX]]

### Connected sums and polygon decompositions

[[PR-GKRFP]]

[[PR-LIXWH]]

[[PR-BDH3V]]

## Manifolds

::: {.fact title="Local homology"}
If $M$ is an $n$-manifold and $x\in M$ is an interior point, then by excision $H_k(M, M\sm\theset x) \cong H_k(\RR^n,\RR^n\sm\theset 0) \cong \tilde H_{k-1}(S^{n-1})$, which is $\ZZ$ for $k=n$ and $0$ otherwise.
A space with a point at which these local homology groups differ from those of every $\RR^n$ is not a manifold near that point.

:::

[[PR-ZCPDD]]

[[PR-LR35S]]

[[D-QP7WI]]

[[T-QNYSB]]

[[PR-TU4G5]]

[[PR-3FB24]]

[[D-WX7JH]]

### 3-manifolds and knot complements

[[PR-UL3KL]]

[[PR-6HORN]]

[[PR-WCHFF]]
