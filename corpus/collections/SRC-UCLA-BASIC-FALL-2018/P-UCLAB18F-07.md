---
schema: qual/card@1
id: P-UCLAB18F-07
kind: problem
title: Normal form of an idempotent linear transformation
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $T:\RR^n\to\RR^n$ be linear and satisfy $T^2=T$.
Show that there is a basis in which the matrix of $T$ is diagonal with entries consisting only of $1$'s followed by $0$'s.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
\RR^n
=
\operatorname{im}T
\oplus
\ker T.
$$


::: pf-proof

For every
$$
v\in\RR^n,
$$
write
$$
v
=
Tv+(v-Tv).
$$
The first term belongs to $\operatorname{im}T$.
Also
$$
T(v-Tv)
=
Tv-T^2v
=
Tv-Tv
=0,
$$
so
$$
v-Tv\in\ker T.
$$
Thus
$$
\RR^n
=
\operatorname{im}T+\ker T.
$$

If
$$
w\in\operatorname{im}T\cap\ker T,
$$
then
$$
w=Tu
$$
for some $u$, while
$$
Tw=0.
$$
But
$$
Tw=T^2u=Tu=w.
$$
Hence $w=0$.
Therefore the sum is direct.

:::

:::

::: {.pf-step #s1-2}

The restriction of $T$ to $\operatorname{im}T$ is the identity.


::: pf-proof

If
$$
w\in\operatorname{im}T,
$$
then
$$
w=Tu
$$
for some $u$.
Therefore
$$
Tw=T^2u=Tu=w.
$$

:::

:::

::: {.pf-step #s1-3}

The restriction of $T$ to $\ker T$ is zero.


::: pf-proof

This is the definition of the kernel:
$$
w\in\ker T
\quad\Longrightarrow\quad
Tw=0.
$$

:::

:::

::: {.pf-step #s1-4}

Choose a basis
$$
u_1,\ldots,u_m
$$
of $\operatorname{im}T$ and a basis
$$
v_1,\ldots,v_{n-m}
$$
of $\ker T$.
Then
$$
u_1,\ldots,u_m,v_1,\ldots,v_{n-m}
$$
is a basis of $\RR^n$.


::: pf-proof

This follows from the direct-sum decomposition in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

In the basis from step [](#s1-4){.pf-ref}, the matrix of $T$ is
$$
\boxed{
\operatorname{diag}
(\underbrace{1,\ldots,1}_{m},
\underbrace{0,\ldots,0}_{n-m})
}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
Tu_i=u_i
$$
for every $i=1,\ldots,m$.
By step [](#s1-3){.pf-ref},
$$
Tv_j=0
$$
for every $j=1,\ldots,n-m$.
Thus the coordinate matrix is diagonal with the stated entries.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required normal form.

:::

:::

:::
