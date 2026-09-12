---
schema: qual/card@1
id: P-4GWVV
kind: problem
title: A conformal map from the upper half-plane onto $\{-\pi/2<\Re w<\pi/2,\,\Im
  w>0\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Trigonometry
relations: []
review: draft
---

::: problem
Find the conformal map that takes the upper half-plane comformally
onto the half-strip $\{
w=x+iy:\ -\pi/2<x<\pi/2\ y>0\}$.
:::

::: solution
Let
\[
S=\left\{w:\ -\frac\pi2<\operatorname{Re}w<\frac\pi2,
\ \operatorname{Im}w>0\right\}.
\]
Consider
\[
\Phi(w)=\sin w.
\]
If $w=x+iy\in S$, then
\[
\operatorname{Im}\sin w=\cos x\,\sinh y>0,
\]
so $\Phi(S)\subset\mathbb H$.

The three boundary pieces map to the real axis as follows:
\[
\sin x\in(-1,1)\quad(y=0),
\]
while
\[
\sin\left(\frac\pi2+iy\right)=\cosh y\in(1,\infty),
\qquad
\sin\left(-\frac\pi2+iy\right)=-\cosh y\in(-\infty,-1).
\]
Moreover $\Phi'(w)=\cos w$ has no zero in $S$. The standard identity
\[
\sin w_1=\sin w_2
\iff
w_1-w_2\in2\pi\mathbb Z
\quad\text{or}\quad
w_1+w_2\in\pi+2\pi\mathbb Z
\]
shows that neither alternative can occur for two distinct points of $S$.
Thus $\Phi$ is injective. The boundary correspondence, or equivalently the
argument principle applied on exhausting rectangles in $S$, shows that its
image is all of $\mathbb H$.

Hence $\sin:S\to\mathbb H$ is biholomorphic, and the required map is its
inverse branch
\[
\boxed{z\longmapsto\arcsin z,}
\]
chosen so that
$-\pi/2<\operatorname{Re}(\arcsin z)<\pi/2$ and
$\operatorname{Im}(\arcsin z)>0$ for $z\in\mathbb H$.
:::
