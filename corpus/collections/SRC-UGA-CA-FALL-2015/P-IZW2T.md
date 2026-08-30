---
schema: qual/card@1
id: P-IZW2T
kind: problem
title: Expand the following functions into Laurent series in the indicated
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Essential Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Expand the following functions into Laurent series in the indicated regions:

(a) $\displaystyle f(z) = \frac{z^2 - 1}{ (z+2)(z+3)}, \; \; 2 < |z| < 3$, $3 < |z| < + \infty$.

(b) $\displaystyle f(z) = \sin \frac{z}{1-z}, \; \; 0 < |z-1| < + \infty$
:::

::: solution
**Goal:** Write the Laurent series in each stated annulus.

<1> Part (a): expand
    $$f(z)=\frac{z^2-1}{(z+2)(z+3)}=\frac{-3}{z+2}+\frac{4}{z+3}.$$
    *Proof:*
    <2>1. For $2<|z|<3$:
        $$\frac1{z+2}=\frac1z\frac1{1+2/z}
        =\frac1z\sum_{k=0}^\infty\left(-\frac2z\right)^k
        =\sum_{k=0}^\infty(-2)^k z^{-k-1}.$$
    <2>2. For $2<|z|<3$, also
        $$\frac1{z+3}=\frac13\frac1{1+z/3}
        =\frac13\sum_{k=0}^\infty\left(-\frac z3\right)^k.$$
    <2>3. Hence on $2<|z|<3$,
        \[
        f(z)= -3\sum_{k=0}^\infty(-2)^k z^{-k-1}
        +\frac43\sum_{k=0}^\infty\left(-\frac z3\right)^k.
        \]
    <2>4. For $|z|>3$,
        $$\frac1{z+2}=\frac1z\sum_{k=0}^\infty\left(-\frac2z\right)^k,\qquad
          \frac1{z+3}=\frac1z\sum_{k=0}^\infty\left(-\frac3z\right)^k.$$
    <2>5. Hence on $3<|z|<\infty$,
        \[
        f(z)= -3\sum_{k=0}^\infty(-2)^k z^{-k-1}
        +4\sum_{k=0}^\infty(-3)^k z^{-k-1}.
        \]

<1> Part (b): set $w=z-1$.
    *Proof:*
    <2>1. On $0<|w|<\infty$, we have
        $$\frac{z}{1-z}=-\frac{1+w}{w}=-1-\frac1w.$$
    <2>2. So
        $$\sin\frac{z}{1-z}=-\sin\!\left(1+\frac1w\right)
        =-\sin1\cos\frac1w-\cos1\sin\frac1w.$$
    <2>3. Use
        \[
        \cos\frac1w=\sum_{m=0}^\infty\frac{(-1)^m}{(2m)!}w^{-2m},\qquad
        \sin\frac1w=\sum_{m=0}^\infty\frac{(-1)^m}{(2m+1)!}w^{-(2m+1)}.
        \]
    <2>4. Therefore
        $$
        \sin\frac{z}{1-z}
        =-\sin1\sum_{m=0}^\infty\frac{(-1)^m}{(2m)!}(z-1)^{-2m}
        -\cos1\sum_{m=0}^\infty\frac{(-1)^m}{(2m+1)!}(z-1)^{-(2m+1)}.
        $$
        This is valid for $0<|z-1|<\infty$.

Authored by **Codex 5.3 Spark Extra High**.
:::
