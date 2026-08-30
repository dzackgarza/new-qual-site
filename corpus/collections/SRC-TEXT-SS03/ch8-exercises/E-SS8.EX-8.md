---
schema: qual/card@1
id: E-SS8.EX-8
kind: exercise
title: "Find a harmonic function u in the open first quadrant that extends continuously "
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
8. Find a harmonic function u in the open first quadrant that extends continuously up to the boundary except at the points 0 and 1, and that takes on the following boundary values: $u ( x , y ) = 1$ on the half-lines $\{ y = 0 , \ x > 1 \}$ and $\{ x = 0 , \ y > 0 \}$ , and $u ( x , y ) = 0$ on the segment $\{ 0 < x < 1 , y = 0 \}$

[Hint: Find conformal maps $F _ { 1 } , F _ { 2 } , \ldots , F _ { 5 }$ indicated in Figure 11. Note that $\textstyle { \frac { 1 } { \pi } } \arg ( z )$ is harmonic on the upper half-plane, equals 0 on the positive real axis, and 1 on the negative real axis.]
:::

::: solution
**Goal:** Find a harmonic function on the open first quadrant with the stated boundary values.

<1>1. Conformal reduction to the upper half-plane:
    *Proof:*
    <2>1. Let
    $$Q=\{z\in\mathbb C: \Re z>0,\; \Im z>0\}.$$
    <2>2. Define $F_1:Q\to\mathbb C$ by $F_1(z)=z^2$.
    <2>3. For $z\in Q$, $\arg z\in(0,\pi/2)$, so $\arg F_1(z)=2\arg z\in(0,\pi)$.
    Hence
    $$F_1(Q)=\{w\in\mathbb C:\Im w>0\},$$
    and the boundary pieces map as:
    $$\{y=0,x>0\}\mapsto (0,\infty),\qquad \{x=0,y>0\}\mapsto (-\infty,0).$$
    Also $(0,1)$ maps to $(0,1)$ and $(1,\infty)$ to $(1,\infty)$.

<1>2. Harmonic profile on the upper half-plane:
    *Proof:*
    <2>1. On $\mathbb H=\{\Im w>0\}$ define
        $$v(w)=1-\frac{1}{\pi}\arg\left(\frac{w}{w-1}\right),$$
        with the principal argument on $\mathbb H$.
    <2>2. Since argument is harmonic on $\mathbb H$, $v$ is harmonic on $\mathbb H$.
    <2>3. Boundary values:
        - $w\in(1,\infty)$: $\frac{w}{w-1}>0$, so $\arg=0$, hence $v=1$.
        - $w\in(0,1)$: $\frac{w}{w-1}<0$, so $\arg=\pi$, hence $v=0$.
        - $w\in(-\infty,0)$: $\frac{w}{w-1}>0$, so $\arg=0$, hence $v=1$.

<1>3. Pullback to the quadrant:
    *Proof:*
    <2>1. Set $u(z)=v(z^2)$ for $z\in Q$.
    <2>2. The map $z\mapsto z^2$ is conformal on $Q$, so $u$ is harmonic on $Q$.
    <2>3. Boundary values follow from Step 1 and Step 2:
        - On $\{y=0,x>1\}$, $z^2\in(1,\infty)$, so $u=1$.
        - On $\{0<x<1,y=0\}$, $z^2\in(0,1)$, so $u=0$.
        - On $\{x=0,y>0\}$, $z^2\in(-\infty,0)$, so $u=1$.

<1>4. Conclusion:
    $$u(z)=1-\frac{1}{\pi}\arg\left(\frac{z^2}{z^2-1}\right)$$
    is harmonic in $Q$, extends continuously to the boundary away from $0,1$, and has the required values. Q.E.D.
:::
