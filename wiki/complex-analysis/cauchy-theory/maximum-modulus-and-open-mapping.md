---
title: Maximum modulus and open mapping
order: 60
topics:
- Maximum Modulus Principle
- Maximum Principle
- Minimum Principle
- Open Mapping Theorem

---

# Maximum modulus and open mapping

A nonconstant holomorphic function on a connected open set is an open map, and its modulus has no local maximum.

## The open mapping theorem

[[C-FRF33]]

## Maximum modulus

[[T-BYNL5]]

[[PR-6WOTK]]

[[PR-QW3ZK]]



## Minimum modulus

[[T-YLI6Y]]

The hypothesis that $f$ is nonvanishing is necessary; the witness is on [[complex-analysis/counterexamples#The maximum and minimum modulus principles|Counterexamples]].

::: {.example title="$1/(2-z)$ on the disc, bounded from the boundary"}
Let $f(z) = 1/(2-z)$ on $\DD$.
On the circle $\abs z = 1$ one has $\abs{2-z}\in[1,3]$, the extremes being taken at $z = 1$ and $z = -1$, so $\abs f$ ranges over $[1/3,1]$ there.
The boundary form of the maximum modulus principle [@SS03, ch. 3, Corollary 4.6] gives $\abs{f(z)}\leq 1$ on $\DD$, and the same bound applied to $1/f$, whose boundary values are $\abs{2-z}\leq 3$, gives $\abs{f(z)}\geq 1/3$.
The image is exactly the open disc $\abs{w-2/3}<1/3$: $z\mapsto 2-z$ carries $\DD$ onto $\abs{w-2}<1$, and $w\mapsto 1/w$ carries that disc onto the disc centred at $2/(4-1) = 2/3$ of radius $1/(4-1) = 1/3$, which is the openness the open mapping theorem [@SS03, ch. 3, Theorem 4.4] asserts, with the radius computed.
At $z = 0$ the value $\abs{f(0)} = 1/2$ lies strictly between the two bounds.
:::

## Problems

[[P-FHQAB]]
[[P-UMNCP-F11-07-F10-03]] [[P-UMNCP-S11-02]]
[[E-SS2.EX-15]]
[[E-ZC34M]]
[[E-ZDVLE]]
[[E-J3QMJ]]
[[E-TYPSR]]
[[E-6IZL3]]
