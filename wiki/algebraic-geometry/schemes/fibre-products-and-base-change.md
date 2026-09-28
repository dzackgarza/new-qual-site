---
title: Fibre products and base change
order: 4
topics:
- Fibre Products
- Base Change
- Functor Of Points
---

# Fibre products and base change

For closed subschemes $Y,Z\subseteq X$, $Y\times_XZ$ is the scheme-theoretic intersection; for $f\colon X\to Y$ and $y\in Y$, $X\times_Y\Spec\kappa(y)$ is the fibre over $y$; for a field extension $L/k$ and a $k$-scheme $X$, $X\times_{\Spec k}\Spec L$ is the base change $X_L$.

[[D-SCHFPR]]

On affine schemes the construction is computed by a tensor product and then glued.
The underlying set of a scheme-theoretic fibre product need not be the fibre product of the underlying sets: $\Spec\CC\times_{\Spec\RR}\Spec\CC=\Spec(\CC\otimes_\RR\CC)\cong\Spec(\CC\times\CC)$ has two points.

## Fibres

[[PR-SCHFIB]]

For $\Spec k[x]\to\Spec k[t]$, $t\mapsto x^2$, with $\operatorname{char}k\neq2$, the fibre over $t=0$ is the double point $\Spec k[x]/(x^2)$.
For $\Spec\ZZ[i]\to\Spec\ZZ$, the fibre over $(3)$ is $\Spec\FF_9$, one point whose residue field has degree $2$ over $\FF_3$.

## Base change

[[D-SCHBC]]

A $k$-scheme $X$ is geometrically integral when $X_{\bar k}$ is integral; the fibre over $y$ is the base change along $\Spec\kappa(y)\to Y$; a scheme over the fraction field $K$ of a ring $R$ spreads out over $R$ when it is the base change of an $R$-scheme along $\Spec K\to\Spec R$.
Integrality is not stable under base change: $\Spec\CC$ is integral over $\RR$, and its base change $\Spec(\CC\otimes_\RR\CC)$ is not.

## The functor of points

[[PR-SCHFOP]]

The functor $h_X=\Hom(-,X)$ sends fibre products to fibre products: $h_{X\times_SY}(T)=h_X(T)\times_{h_S(T)}h_Y(T)$.
For a $k$-scheme $X$, $\Hom_k(\Spec K,X)$ is the set of $K$-points, and $\Hom_k(\Spec k[\varepsilon]/(\varepsilon^2),X)$ is the set of pairs of a $k$-point $x$ and a tangent vector in $(\mathfrak m_x/\mathfrak m_x^2)^\vee$.

## Fibres of families

[[D-SCHFIBRES]]
