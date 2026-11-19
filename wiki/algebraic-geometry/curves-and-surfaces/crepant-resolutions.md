---
title: Crepant resolutions
order: 12
topics:
- Resolution of Singularities
- Du Val Singularities
- Discrepancy
---

# Crepant resolutions

[[D-VARCREPANT]]

For a proper birational morphism $f\colon Y\to X$ of normal varieties with $\QQ$-Cartier canonical divisors, write
$$
K_Y=f^*K_X+\sum_i a_iE_i
$$
over the $f$-exceptional prime divisors $E_i$. The numbers $a_i$ are the discrepancies of $f$, and $f$ is crepant when every $a_i=0$ ([[D-VARCREPANT]]).

## Discrepancy of a blowup

[[PR-VAREM1]]

A blowup of a smooth point of a smooth variety of dimension $n$ has $K_{\widetilde X}=\pi^*K_X+(n-1)E$, so its discrepancy along $E$ is $n-1$: a blowup of a smooth point is never crepant, and on a surface its discrepancy is $1$ ([[PR-VAREM1]], [[FE-SRFBLOW]]).

## Log resolutions

[[D-VARLOGRES]]

## Du Val singularities

[[D-SRFADE]]

## Exceptional curves and what a contraction may do

[[T-SRFCAST]]

Let $Y$ be a curve on a smooth projective surface $X$. If $Y\cong\PP^1$ and $Y^2=-1$, there is a morphism $f\colon X\to X_0$ to a smooth projective surface contracting $Y$ to a point, and a curve $Y\cong\PP^1$ that contracts to a smooth point has $Y^2=-1$ [@Har77, Theorem V.5.7, p. 414].
If the image is allowed to be singular, $Y\cong\PP^1$ with $Y^2<0$ is contractible to a point of a projective variety [@Har77, Remark V.5.7.2, p. 417 and Exercise V.5.2, p. 419].
A $(-2)$-curve is therefore contractible, and its image is not a smooth point: adjunction $2g(Y)-2=Y\cdot(Y+K_X)$ gives $Y\cdot K_X=0$ for $Y\cong\PP^1$ with $Y^2=-2$, so $K_X-f^*K_{X_0}$ is supported on $Y$ and pairs to zero with it, and the contraction is crepant ([[D-VARCREPANT]], [[D-SRFADE]]).

## Blowups and the canonical class

[[FE-SRFBLOW]]

[[T-SRFZMT]]

## Toric crepant resolutions

[[FE-TORMINRES]]

[[PR-FULKSQ]]
