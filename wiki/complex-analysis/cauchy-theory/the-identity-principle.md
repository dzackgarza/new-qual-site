---
title: The identity principle
order: 50
topics:
- Identity Theorem
- Analytic Continuation
---

# The identity principle

[[D-TFSPT]]

[[T-SVF2W]]

::: {.slogan}
Two holomorphic functions on a connected open set that agree on a set with a limit point in that open set are equal.

:::

::: {.example title="A limit point outside the domain, and a disconnected domain"}
The function $\sin(1/z)$ on $\CC\smz$ vanishes at the distinct points $1/(k\pi) \to 0$ and is not identically zero; the limit point $0$ is not in the domain.
On the disconnected open set $\DD\cup\DD_1(3)$, the function equal to $0$ on $\DD$ and to $1$ on $\DD_1(3)$ is holomorphic, vanishes on $\DD$, and is not identically zero.

:::

::: {.example title="Transferring a real identity to the plane"}
Since $\sin^2(z)+\cos^2(z) = 1$ on $\RR$, which has limit points in $\CC$, the identity holds on $\CC$.
For the addition law, let $F(z, w) \coloneqq e^{z+w}-e^z e^w$.
For fixed real $w$, $z\mapsto F(z,w)$ is entire and vanishes on $\RR$, so it vanishes on $\CC$.
Then for fixed $z\in\CC$, $w\mapsto F(z,w)$ is entire and vanishes on $\RR$, so it vanishes on $\CC$.

:::

## Problems

[[E-SS2.EX-13]]
