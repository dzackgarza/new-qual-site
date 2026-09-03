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

:::{.slogan}
Two functions agreeing on a set with a limit point are equal on a domain.

:::

:::{.proof title="Using power series and topology"}
$1\implies 2$:
Take $z_k \da z_0 + C{1\over k}$ for any $z_0\in \Omega$, since $f(z_0) = 0$ for any such $z_k$.
Choose $C$ so that $z_k \in \Omega$ for all $k$.

$2\implies 3$:
Given such a $z_0$, expand about it.
For the minimal $m$ with $c_m \neq 0$,
\[
f(z) = \sum_{k\geq m}c_k (z-z_0)^k = (z-z_0)^m \sum_{k\geq m}c_k (z-z_0)^{k-m} \da (z-z_0)^m g(z)
,\]
where $g$ is holomorphic near $z_0$ and $g(z_0) = c_m \neq 0$.
By continuity $g$ is nonzero on a possibly smaller neighborhood $U \ni z_0$.
Since $0 = f(z_k) = (z_k - z_0)^m g(z_k)$ for all $k$ with $z_k \neq z_0$ and the $z_k$ distinct, infinitely many $z_k$ would have to equal $z_0$, a contradiction.
So $c_m = 0$ for all $m$ and $f\equiv 0$.

$3\implies 1$:
Pick $z_0$ with $f^{(k)}(z_0) = 0$ for all $k$.
Then $f = \sum_{k\geq 0} c_k (z-z_0)^k$ with $c_k \sim f^{(k)}(z_0)$, so every $c_k = 0$ and $f\equiv 0$ on a disc $D_r(z_0) \subseteq \Omega$.
Write $U \da \ts{z_0\in \Omega\st f^{(k)}(z_0) = 0 \text{ for all }k }$, which is open in $\Omega$.
It is also closed: if $w_0 \in V \da \Omega\sm U$ then $f^{(k)}(w_0)\neq 0$ for some $k$, and continuity of $f^{(k)}$ makes it nonzero on a neighborhood, so $V$ is open.
A nonempty subset of a connected set that is both open and closed is the whole set.

:::

:::{.remark title="Where the hypothesis really sits"}
The limit point must lie *inside* the domain.
A sequence of zeros accumulating at a boundary point proves nothing, and that is the standard trap: $\sin(1/z)$ on the punctured disc vanishes at $1/(k\pi) \to 0$, and $0$ is not in the domain.
Connectedness is the other load-bearing hypothesis, since the proof is a connectedness argument.

:::

[[T-OFMGU]]

:::{.example title="Transferring a real identity to the plane"}
Since $\sin^2(z)+\cos^2(z) = 1$ on $\RR$, which has limit points, the identity holds on $\CC$.
For the addition law, apply the same argument to $F(z, w) \da e^{z+w}-e^z e^w$, which vanishes on $\RR$ and therefore on $\CC$.

:::

## Exercises

[[E-IYBZP]]
[[E-G4N4D]]
[[E-5P24A]]
