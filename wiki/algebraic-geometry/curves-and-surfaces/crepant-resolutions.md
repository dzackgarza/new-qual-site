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

## Discrepancy of a blowup

[[PR-VAREM1]]

A blowup of a smooth point of a smooth variety of dimension $n$ has $K_{\widetilde X}=\pi^*K_X+(n-1)E$, so its discrepancy along $E$ is $n-1$: a blowup of a smooth point is never crepant, and on a surface its discrepancy is $1$ ([[PR-VAREM1]], [[FE-SRFBLOW]]).

## Log resolutions

[[D-VARLOGRES]]

## Du Val singularities

[[D-SRFADE]]

## Exceptional curves and what a contraction may do

[[T-SRFCAST]]

Let $Y$ be a curve on a smooth projective surface $X$.
If $Y\cong\PP^1$ and $Y^2=-1$, there is a morphism $f\colon X\to X_0$ to a smooth projective surface exhibiting $X$ as the blowup of $X_0$ at a point $P$ with $Y$ the exceptional curve, so that $f$ contracts $Y$ to the smooth point $P$ [@Har77, Theorem V.5.7].
Conversely, let $f\colon X\to X_0$ be a birational morphism of smooth projective surfaces with $f(Y)=\theset{P}$ and $f$ an isomorphism of $X\sm Y$ onto $X_0\sm\theset{P}$, so that $Y$ is the whole exceptional locus and $Y$ is contractible to $P$ in the sense of [@Har77, Remark V.5.7.2].
Then $Y$ is the only curve of $X$ contracted by $f$, so $n(f)=1$ and $f$ is a single monoidal transformation [@Har77, Corollary V.5.4]; its exceptional curve is $Y$, so $Y\cong\PP^1$ and $Y^2=-1$ [@Har77, Proposition V.3.1], the converse announced in [@Har77, Remark V.3.1.1] and printed in [@Har77, Remark V.5.7.2].
The hypothesis that $Y$ be the whole exceptional locus cannot be weakened to "$f(Y)$ is a smooth point": if $\pi_1$ blows up a point $p\in\PP^2$ with exceptional curve $E_1$ and $\pi_2$ blows up a point $q\in E_1$ with exceptional curve $F$, then both exceptional curves have square $-1$ [@Har77, Proposition V.3.1], the strict transform of $E_1$ is $Y=\pi_2^*E_1-F$ [@Har77, Proposition V.3.6], and the intersection rules of [@Har77, Proposition V.3.2] give $Y\cong\PP^1$ with $Y^2=E_1^2+F^2=-2$, while $\pi_1\circ\pi_2$ maps $Y$ to the smooth point $p$; here $n(\pi_1\circ\pi_2)=2$, the curves contracted being $Y$ and $F$ [@Har77, Corollary V.5.4].
If the image is allowed to be singular, $Y\cong\PP^1$ with $Y^2<0$ is contractible to a point of a projective variety [@Har77, Remark V.5.7.2 and Exercise V.5.2].
A $(-2)$-curve is therefore contractible, and its image is not a smooth point: the contraction has $Y$ as its whole exceptional locus, and a smooth image would force $Y^2=-1$ by the converse above, whereas adjunction $2g(Y)-2=Y\cdot(Y+K_X)$ gives $Y\cdot K_X=0$ for $Y\cong\PP^1$ with $Y^2=-2$, and the image is a du Val point, so $K_{X_0}$ is Cartier there ([[D-SRFADE]]); hence $K_X-f^*K_{X_0}$ is supported on $Y$ and pairs to zero with it, and the contraction is crepant ([[D-VARCREPANT]], [[D-SRFADE]]).

## Blowups and the canonical class

[[FE-SRFBLOW]]

[[T-SRFZMT]]

## Toric crepant resolutions

[[FE-TORMINRES]]

[[PR-FULKSQ]]
