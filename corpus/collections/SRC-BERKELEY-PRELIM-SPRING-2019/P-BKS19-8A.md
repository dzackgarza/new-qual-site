---
schema: qual/card@1
id: P-BKS19-8A
kind: problem
title: The elementary symmetric polynomial map on $\CC^3$ is surjective but not injective
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 roots-to-coefficients argument. It is correct; the solution below writes the associated cubic explicitly and gives a concrete noninjectivity witness.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the Vieta coefficient formula, surjectivity via factorization of every monic cubic over $\CC$, and noninjectivity under permutation of distinct roots.
---

::: {.problem}
Show that $F:\CC^3\to\CC^3$ defined by
$$
F(u,v,w)=(-u-v-w,\ uv+uw+vw,\ -uvw)
$$
is surjective but not injective.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $u,v,w\in\CC$,
$$
(z-u)(z-v)(z-w)
=
z^3+F_1(u,v,w)z^2+F_2(u,v,w)z+F_3(u,v,w),
$$
where $F=(F_1,F_2,F_3)$.


::: pf-proof

Expanding gives
$$
(z-u)(z-v)(z-w)
=
z^3-(u+v+w)z^2+(uv+uw+vw)z-uvw,
$$
which is exactly the asserted coefficient vector.

:::

:::

::: {.pf-step #s1-2}

The map $F$ is surjective.


::: pf-proof

Let $(a,b,c)\in\CC^3$. By the fundamental theorem of algebra, the monic cubic
$$
p(z)=z^3+az^2+bz+c
$$
factors over $\CC$ as
$$
p(z)=(z-u)(z-v)(z-w)
$$
for some $u,v,w\in\CC$, with repeated roots allowed. Comparing with step [](#s1-1){.pf-ref} gives
$$
F(u,v,w)=(a,b,c).
$$
Thus every point of $\CC^3$ has a preimage.

:::

:::

::: {.pf-step #s1-3}

The map $F$ is not injective.


::: pf-proof

The formula for $F$ is symmetric in $u,v,w$. In particular,
$$
F(0,1,2)=F(1,0,2),
$$
while $(0,1,2)\neq(1,0,2)$. Hence $F$ is not injective.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves surjectivity and step [](#s1-3){.pf-ref} proves failure of injectivity.

:::

:::

:::
