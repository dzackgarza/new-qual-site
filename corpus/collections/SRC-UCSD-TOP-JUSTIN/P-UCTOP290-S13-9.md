---
schema: qual/card@1
id: P-UCTOP290-S13-9
kind: problem
title: Every map from the sphere to the torus has degree zero
classification:
  areas:
  - topology
  topics:
  - Degree
  - Cohomology Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 13, Problem 9 in its checked-in extraction.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 13, problem 9
    (assets/attachments/UCSD_290_F14_sheet13.pdf, printed page 389), from the
    checked-in extraction and a 300 dpi render. The printed problem defines the
    degree of a map between connected closed oriented n-manifolds by
    f_*[M] = deg(f)[N] and asks to use cohomology rings to show that any map from
    the 2-sphere to the torus has degree zero. The card states this, so no repair
    was needed.
---

::: {.problem}
Use cohomology rings to show that every map
$f:S^2\to T^2$ has degree zero.
:::

::: {.solution}

Let $f\colon S^2\to T^2$ be a continuous map between the closed oriented
surfaces $S^2$ and $T^2$, with $\deg f$ defined by $f_*[S^2]=\deg(f)[T^2]$ in
$H_2$.

::: pf

::: {.pf-step #generators}

$H^1(S^2;\ZZ)=0$, while $H^1(T^2;\ZZ)$ is free on classes $u,v$ with $u\smile
v$ the orientation class of $H^2(T^2;\ZZ)$.

::: pf-proof

$S^2$ is simply connected, so $H^1(S^2;\ZZ)=\Hom(H_1(S^2),\ZZ)=0$ by the
universal coefficient theorem. $T^2=S^1\times S^1$ has $H_1=\ZZ^2$ generated
by the two circle factors and $H^2=\ZZ$; by the Künneth formula the two
degree-one classes $u,v$ dual to the factors have $u\smile v$ generating
$H^2$, which is the orientation class for a suitable choice of the two
generators.

:::

:::

::: {.pf-step #pullback}

$f^*u=f^*v=0$, hence $f^*(u\smile v)=0$.

::: pf-proof

$f^*$ is a ring homomorphism $H^*(T^2;\ZZ)\to H^*(S^2;\ZZ)$, so $f^*u$ and
$f^*v$ lie in $H^1(S^2;\ZZ)=0$ by step [](#generators){.pf-ref}. Naturality of
the cup product gives $f^*(u\smile v)=f^*u\smile f^*v=0\smile0=0$.

:::

:::

::: {.pf-step #degree}

$\deg f=0$.

::: pf-proof

Since $f^*(u\smile v)=0$ and $u\smile v$ is a generator of $H^2(T^2;\ZZ)$, the
map $f^*\colon H^2(T^2;\ZZ)\to H^2(S^2;\ZZ)$ is zero. For maps of closed
oriented manifolds of the same dimension $f^*$ on top cohomology is
multiplication by $\deg f$: pairing $f_*[S^2]=\deg(f)[T^2]$ with a cohomology
class $\alpha$ and using naturality of the Kronecker pairing gives $\langle
f^*\alpha,[S^2]\rangle=\langle\alpha,f_*[S^2]\rangle=\deg(f)\langle\alpha,[T^2]\rangle$.
So multiplication by $\deg f$ is the zero map on $\ZZ=H^2(S^2;\ZZ)$, which
forces $\deg f=0$.

:::

:::

:::


:::
