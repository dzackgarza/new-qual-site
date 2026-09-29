---
schema: qual/card@1
id: P-HCAX4
kind: problem
title: Normalized conformal map onto the slit plane
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Mapping Theorem
  - Univalent Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let
\[
\Omega=\mathbb C\setminus(-\infty,-1/4].
\]

a. Show that there is a conformal isomorphism $f:\mathbb D\to\Omega$ with $f(0)=0$.

b. Give a normalization which makes $f$ unique.

c. Write $f(z)=\sum_{j\geq 1}a_jz^j$.
Use another conformal map expressed in terms of $f$ and $-z$ to determine a ring containing all coefficients $a_j$.

d. Compute the coefficients $a_j$.
:::

::: {.solution}
::: pf

::: pf-step
(a) There is a conformal isomorphism $f\colon\DD\to\Omega$ with
$f(0)=0$.

::: pf-proof
$\Omega$ is the complement in $\CC$ of a closed ray, so it is simply connected
and not all of $\CC$. The Riemann mapping theorem gives a conformal
isomorphism $g\colon\DD\to\Omega$. Since $0\in\Omega$, let
$a=g^{-1}(0)$ and $f=g\circ\phi_a^{-1}$, where
$\phi_a(z)=(z-a)/(1-\overline az)$ is the disk automorphism with
$\phi_a(a)=0$. Then $f(0)=g(a)=0$.
:::

:::

::: {.pf-step #s2}
(b) There is exactly one such $f$ with $f(0)=0$ and $f'(0)>0$.

::: pf-proof
This is the uniqueness part of the Riemann mapping theorem: if $f_1,f_2$ both
qualify, then $f_2^{-1}\circ f_1$ is a disk automorphism fixing $0$ with
positive derivative at $0$, hence the identity by Schwarz's lemma.
:::

:::

::: {.pf-step #s3}
(c) For the normalized $f$ of step [](#s2){.pf-ref}, every $a_j$ is real.

::: pf-proof
$\Omega$ is invariant under complex conjugation. Hence
$g(z)=\overline{f(\overline z)}$ is a conformal isomorphism $\DD\to\Omega$
with $g(0)=0$ and $g'(0)=\overline{f'(0)}=f'(0)>0$. By step [](#s2){.pf-ref}, $g=f$.
Since $g(z)=\sum_j\overline{a_j}z^j$, comparing coefficients gives
$a_j=\overline{a_j}$, so all $a_j$ lie in $\RR$.
:::

:::

::: pf-step
(d) $f(z)=\dfrac{z}{(1-z)^2}$ and $a_j=j$ for all $j\ge1$; in
particular every $a_j$ lies in $\ZZ$.

::: pf-proof
The Koebe function $k(z)=z/(1-z)^2$ maps $\DD$ conformally onto
$\CC\setminus(-\infty,-1/4]$, with $k(0)=0$ and $k'(0)=1>0$, so $k=f$ by step
[](#s2){.pf-ref}. Expanding,
$$
\frac{z}{(1-z)^2}=z\sum_{j=0}^\infty(j+1)z^j=\sum_{j=1}^\infty jz^j.
$$
:::

:::

:::
:::

::: {.remark}
The map $z\mapsto f(-z)$ named in part (c) is a conformal isomorphism $\DD\to\Omega$ fixing $0$ with derivative $-f'(0)<0$, so step [](#s2){.pf-ref} does not identify it with $f$, and it gives no relation among the $a_j$. The reflection $\overline{f(\overline z)}$ of step [](#s3){.pf-ref} does.
:::
