---
schema: qual/card@1
id: P-UCLARA11F-08
kind: problem
title: Counting zeros in a right half-plane
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Determine the number of solutions of
$$
z-2-e^{-z}=0
$$
in the right half-plane $H=\{z\in\CC:\operatorname{Re}z>0\}$.
:::

::: {.solution}

Define
$$
F(z)=z-2-e^{-z}
$$
and
$$
G(z)=z-2.
$$

For $R>3$, let
$$
D_R
=
\{z\in\CC:\operatorname{Re}z>0,\ \abs{z}<R\},
$$
whose boundary consists of the vertical segment
$$
\{-iR\le z\le iR:\operatorname{Re}z=0\}
$$
and the right semicircle
$$
\{Re^{i\theta}:-\pi/2\le\theta\le\pi/2\}.
$$

::: pf

::: {.pf-step #s1-1}

On the imaginary-axis part of $\partial D_R$,
$$
\boxed{\abs{e^{-z}}=1}.
$$


::: pf-proof

If
$$
z=iy,
$$
then
$$
\abs{e^{-z}}
=
\abs{e^{-iy}}
=
1.
$$

:::

:::

::: {.pf-step #s1-2}

On the same boundary segment,
$$
\boxed{\abs{z-2}\ge2}.
$$


::: pf-proof

If $z=iy$, then
$$
\abs{z-2}
=
\abs{-2+iy}
=
\sqrt{4+y^2}
\ge2.
$$

:::

:::

::: {.pf-step #s1-3}

Hence on the imaginary-axis part,
$$
\boxed{\abs{e^{-z}}<\abs{z-2}}.
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

On the right semicircle,
$$
\boxed{\abs{e^{-z}}\le1}.
$$


::: pf-proof

There
$$
\operatorname{Re}z\ge0,
$$
so
$$
\abs{e^{-z}}
=
e^{-\operatorname{Re}z}
\le1.
$$

:::

:::

::: {.pf-step #s1-5}

On the right semicircle,
$$
\boxed{\abs{z-2}\ge R-2}.
$$


::: pf-proof

By the reverse triangle inequality,
$$
\abs{z-2}
\ge
\abs{\abs{z}-2}
=
R-2.
$$

:::

:::

::: {.pf-step #s1-6}

Since $R>3$,
$$
R-2>1.
$$


::: pf-proof

Subtract $2$ from $R>3$.

:::

:::

::: {.pf-step #s1-7}

Therefore on the right semicircle,
$$
\boxed{\abs{e^{-z}}<\abs{z-2}}.
$$


::: pf-proof

Use steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Thus on all of $\partial D_R$,
$$
\boxed{\abs{e^{-z}}<\abs{G(z)}}.
$$


::: pf-proof

The boundary is the union of the two pieces handled in steps [](#s1-3){.pf-ref} and [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

By Rouché's theorem, $F$ and $G$ have the same number of zeros in $D_R$, counted with multiplicity.


::: pf-proof

Since
$$
F=G-e^{-z},
$$
the perturbation $e^{-z}$ has modulus strictly smaller than $\abs{G}$ on the boundary by step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

The function
$$
G(z)=z-2
$$
has exactly one zero in $D_R$, namely
$$
\boxed{z=2}.
$$


::: pf-proof

The only zero of $G$ is $2$, and for $R>3$,
$$
\operatorname{Re}2>0,
\qquad
\abs{2}<R.
$$
It is a simple zero.

:::

:::

::: {.pf-step #s1-11}

Therefore $F$ has exactly one zero in $D_R$.


::: pf-proof

Apply step [](#s1-9){.pf-ref} using step [](#s1-10){.pf-ref}.

:::

:::

::: pf-step

Every zero of $F$ in the open right half-plane belongs to $D_R$ for all sufficiently large $R$.


::: pf-proof

If $z_0\in H$, then choose
$$
R>\max\{3,\abs{z_0}\}.
$$
Then $z_0\in D_R$.

:::

:::

::: {.pf-step #s1-13}

Hence $F$ has at most one zero in
$$
H=\{z:\operatorname{Re}z>0\}.
$$


::: pf-proof

If there were two distinct zeros in $H$, choose $R>3$ large enough to contain both. This would contradict step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-14}

Since step [](#s1-11){.pf-ref} gives one zero in every $D_R$ with $R>3$, $F$ has at least one zero in $H$.


::: pf-proof

Each $D_R$ is contained in $H$, and $F$ has one zero there.

:::

:::

::: {.pf-step #s1-15}

Therefore
$$
\boxed{
z-2-e^{-z}=0
\text{ has exactly one solution in }H},
$$
counted with multiplicity.


::: pf-proof

Combine steps [](#s1-13){.pf-ref} through [](#s1-14){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-15){.pf-ref} is the required zero count.

:::

:::

:::
