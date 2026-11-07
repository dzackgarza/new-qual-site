---
schema: qual/card@1
id: E-HAT-2.2-4
kind: problem
title: Surjective map $S^n \to S^n$ of degree zero
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 4; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed using degree theory and orthogonal-group homotopies.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: $g$ carries the first wedge summand identically onto $S^n$, so
    $g\circ p$ is onto, and the pinch map sends $[S^n]$ to the sum of the two summand classes, so
    $\deg f=1+(-1)=0$.
---

::: {.problem}
Construct a surjective map $S^n \to S^n$ of degree zero, for each $n \geq 1$.
:::

::: {.solution}
Choose an embedded equatorial $(n-1)$-sphere in $S^n$ and collapse it to a point. This gives the pinch map
$$
p:S^n\longrightarrow S^n\vee S^n.
$$
Let
$$
g:S^n\vee S^n\longrightarrow S^n
$$
be the identity on the first summand and a reflection on the second summand. Set
$$
f=g\circ p.
$$

::: pf

::: pf-step

The map $f$ is surjective.

::: pf-proof

The first wedge summand is mapped by $g$ via the identity onto all of $S^n$, and $p$ is onto. Hence the composite $f$ is onto.

:::

:::

::: pf-step

The degree of $f$ is zero.

::: pf-proof

The wedge sum $S^n\vee S^n$ has a CW structure with one $0$ cell and two $n$ cells, so $H_n(S^n\vee S^n)\approx\ZZ^2$ and $H_i(S^n\vee S^n)=0$ for $i\ne 0,n$ by Theorem 2.35 (Hatcher p. 139). Let $e_+$, $e_-$ be the images in $H_n(S^n\vee S^n)$ of the fundamental class $[S^n]\in H_n(S^n)$ under the two maps $S^n\to S^n\vee S^n$ collapsing one closed hemisphere to the basepoint; these form a basis, and
$$
p_*[S^n]=e_++e_-,
$$
since $S^n$ is the union of its two closed hemispheres, each of which maps homeomorphically onto one summand. Since a reflection of $S^n$ has degree $-1$ by property (e) of degree (Hatcher p. 134) and the identity has degree $1$ by property (a) (p. 134),
$$
g_*(e_+)=[S^n],\qquad g_*(e_-)=-[S^n],
$$
hence
$$
f_*[S^n]=g_*(e_++e_-)=[S^n]-[S^n]=0,
$$
so
$$
\boxed{\deg f=0,}
$$
the degree being the integer $d$ with $f_*[S^n]=d[S^n]$ (Hatcher p. 134).

:::

:::

:::

Thus for every $n\ge1$ there is a surjective degree-zero map $S^n\to S^n$.
:::
