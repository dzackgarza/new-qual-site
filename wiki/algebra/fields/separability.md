---
title: Separability
order: 30
topics:
- Separability
---

# Separability

Every algebraic extension of a field of characteristic $0$ or of a finite field is separable; inseparable extensions occur only over imperfect fields of characteristic $p$.

[[D-ZT46D]]

[[D-JGYLA]]

[[FD-6WSIA]] [[FD-OUWGL]]

[[PR-ENHVC]]

[[PR-OMKPN]]

[[PR-TLBPS]]

[[C-C2GYX]]

::: {.remark title="The derivative test"}
A polynomial $f$ over a field is separable if and only if $\gcd(f, f') = 1$.
An irreducible $f$ is inseparable if and only if $f' = 0$, which in characteristic $p$ happens if and only if $f(x) = g(x^p)$ for a polynomial $g$.
For example, over $\FF_p(t)$ the polynomial $x^p - t$ is irreducible and $x^p - t = (x - t^{1/p})^p$ over $\FF_p(t^{1/p})$, so $\FF_p(t^{1/p})/\FF_p(t)$ is inseparable.
:::

## Permanence and the Galois condition

A finite extension $L/K$ is separable if and only if the number of $K$-embeddings of $L$ into an algebraic closure of $K$ equals $[L:K]$.
Every algebraic extension of a [[D-KQFIV|perfect field]] is separable.
If $K\subseteq L\subseteq M$, then $M/K$ is separable if and only if $M/L$ and $L/K$ are separable, and a compositum of separable extensions is separable.

[[PR-3VQBI]]

[[PR-ZCKLJ]]

[[PR-MK2W6]]

[[PR-25FLW]]

[[PR-XB3O7]]

[[D-WB4M5]]

[[PR-YCTNC]]

[[PR-KFQJG]]

A finite extension is Galois if and only if it is normal and separable, if and only if it is the splitting field of a separable polynomial.
A splitting field need not be separable in characteristic $p$: $\FF_p(t^{1/p})$ is the splitting field of $x^p-t$ over $\FF_p(t)$, and it is not Galois over $\FF_p(t)$.
