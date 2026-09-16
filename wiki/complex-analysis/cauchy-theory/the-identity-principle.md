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
Two holomorphic functions on a connected open set that agree on a set with a limit point in the set are equal.

:::

::: {.proof title="Using power series and topology"}
$1\implies 2$:
Choose $z_0\in\Omega$ and $r>0$ with $D_r(z_0)\subseteq\Omega$, and take the distinct points $z_k \coloneqq z_0 + r/(k+1)$, which are zeros of $f$ converging to $z_0$.

$2\implies 3$:
Expand $f$ in a power series $\sum_k c_k(z-z_0)^k$ about the accumulation point $z_0\in\Omega$.
Suppose some $c_m\neq 0$, and take $m$ minimal.
Then
$$
f(z) = \sum_{k\geq m}c_k (z-z_0)^k = (z-z_0)^m \sum_{k\geq m}c_k (z-z_0)^{k-m} \coloneqq (z-z_0)^m g(z)
,$$
where $g$ is holomorphic near $z_0$ and $g(z_0) = c_m \neq 0$.
By continuity $g$ is nonzero on a neighborhood $U \ni z_0$, so $f$ has no zeros in $U\sm\ts{z_0}$.
Since the $z_k$ are distinct and converge to $z_0$, infinitely many of them lie in $U\sm\ts{z_0}$, a contradiction.
So every $c_k = f^{(k)}(z_0)/k!$ vanishes.

$3\implies 1$:
Let $U \coloneqq \ts{w\in \Omega\st f^{(k)}(w) = 0 \text{ for all }k }$, which contains $z_0$.
For $w\in U$, the power series of $f$ about $w$ has all coefficients $f^{(k)}(w)/k! = 0$, so $f\equiv 0$ on a disc about $w$ and that disc lies in $U$; hence $U$ is open.
Each set $\ts{f^{(k)} = 0}$ is closed in $\Omega$ by continuity of $f^{(k)}$, so their intersection $U$ is closed in $\Omega$.
Since $\Omega$ is connected and $U$ is nonempty, $U=\Omega$ and $f\equiv 0$.

:::

::: {.example title="The hypotheses are necessary"}
The function $\sin(1/z)$ on $\CC\sm\ts{0}$ vanishes at the distinct points $1/(k\pi) \to 0$ and is not identically zero; the limit point $0$ is not in the domain.
On the disconnected open set $\DD\cup D_1(3)$, the function equal to $0$ on $\DD$ and to $1$ on $D_1(3)$ is holomorphic, vanishes on $\DD$, and is not identically zero.

:::

[[T-OFMGU]]

::: {.example title="Transferring a real identity to the plane"}
Since $\sin^2(z)+\cos^2(z) = 1$ on $\RR$, which has limit points in $\CC$, the identity holds on $\CC$.
For the addition law, let $F(z, w) \coloneqq e^{z+w}-e^z e^w$.
For fixed real $w$, $z\mapsto F(z,w)$ is entire and vanishes on $\RR$, so it vanishes on $\CC$.
Then for fixed $z\in\CC$, $w\mapsto F(z,w)$ is entire and vanishes on $\RR$, so it vanishes on $\CC$.

:::

## Exercises

[[E-IYBZP]]
[[E-G4N4D]]
[[E-5P24A]]
