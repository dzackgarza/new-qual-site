---
title: Intersection theory on surfaces
order: 8
topics:
- Intersection Theory
- Adjunction
- Hodge Index Theorem
---

# Intersection theory on surfaces

For a divisor $D$ and an integral curve $C$ on a smooth projective surface $X$, $D\cdot C=\deg_C\OO_X(D)|_C$.

[[D-SRFINT]]

For a smooth curve $C\subset X$, $C^2=\deg N_{C/X}=\deg\OO_X(C)|_C$.
It can be negative: the exceptional curve $E$ of a blowup at a point has $E^2=-1$.

[[T-SRFADJ]]

On $\PP^2$, with $K=-3H$, adjunction gives $g=\tfrac{1}{2}(d-1)(d-2)$ for a smooth curve of degree $d$.
On $\PP^1\times\PP^1$, with $K=(-2,-2)$, it gives $g=(a-1)(b-1)$ for a smooth curve of type $(a,b)$.

[[T-SRFRR]]

Since $h^2(\OO_X(D))=h^0(\OO_X(K-D))$ by Serre duality,
$$
h^0(\OO_X(D))+h^0(\OO_X(K-D))\ge\chi(\OO_X)+\tfrac{1}{2}D\cdot(D-K).
$$

## The Néron--Severi group and the Hodge index theorem

[[D-SRFNS]]

Algebraically equivalent divisors have equal intersection numbers, so the pairing factors through the finitely generated group $\NS(X)=\Pic X/\Pic^0X$.
It is nondegenerate on $\NS(X)$ modulo torsion.

[[T-SRFHODGE]]

On $\NS(X)\otimes\RR$ the pairing has signature $(1,\rho-1)$: an ample $H$ has $H^2>0$, and $H^\perp$ is negative definite.
For divisors $D,E$ with $D^2>0$, it follows that $(D\cdot E)^2\ge D^2E^2$.

[[T-SRFNAKAI]]

By the Nakai--Moishezon criterion, ampleness of $D$ depends only on its class in $\NS(X)$.
The condition on curves is not implied by $D^2>0$: on the blowup $\pi$ of $\PP^2$ at a point, $(\pi^*H)^2=1$ and $\pi^*H\cdot E=0$.

## Chow rings in any dimension

[[D-CHOWRING]]

## The Todd genus

[[D-VARTODD]]
