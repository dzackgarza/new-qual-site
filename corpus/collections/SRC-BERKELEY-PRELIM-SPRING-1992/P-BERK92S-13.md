---
schema: qual/card@1
id: P-BERK92S-13
kind: problem
title: Jacobian determinant from infinitesimal volume distortion
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
- event: source-checked
  by: chatgpt
  date: 2026-09-23
  note: Compared Problem 13 against the retained Spring92.pdf; the source has lim sup on the right-hand side, correcting the ordinary limit in the extracted card.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $f:\mathbb R^3\to\mathbb R^3$ be one-to-one and $C^1$, and let $J$ be its Jacobian determinant. For $x_0\in\mathbb R^3$, let $Q_r(x_0)$ be the cube centered at $x_0$, of side length $r$, with edges parallel to the coordinate axes. Prove that
\[
|J(x_0)|
=\lim_{r\to0}r^{-3}\operatorname{vol}(f(Q_r(x_0)))
\le
\limsup_{x\to x_0}
\frac{\|f(x)-f(x_0)\|^3}{\|x-x_0\|^3}.
\]
Here $\|\cdot\|$ is the Euclidean norm.
:::

::: {.solution}
Put
$$
L\coloneqq Df(x_0).
$$

::: pf

::: {.pf-step #s1}

$$
\lim_{r\to0}r^{-3}\operatorname{vol}(f(Q_r(x_0)))
=\abs{\det L}.
$$

::: pf-proof

Because $f$ is one-to-one and $C^1$, the area formula in equal
dimensions gives
$$
\operatorname{vol}(f(Q_r(x_0)))
=
\int_{Q_r(x_0)}\abs{\det Df(x)}\,dx.
$$
The cube has volume $r^3$. Hence
$$
r^{-3}\operatorname{vol}(f(Q_r(x_0)))
=
\frac1{\operatorname{vol}(Q_r(x_0))}
\int_{Q_r(x_0)}\abs{\det Df(x)}\,dx.
$$
Since $Df$ is continuous, so is $\abs{\det Df}$. The average of this
continuous function over cubes shrinking to $x_0$ therefore tends to
its value at $x_0$, namely
$$
\abs{\det Df(x_0)}=\abs{J(x_0)}.
$$

:::

:::

::: {.pf-step #s2}

$$
\limsup_{x\to x_0}
\frac{\norm{f(x)-f(x_0)}}{\norm{x-x_0}}
=\norm{L}_{\mathrm{op}}.
$$

::: pf-proof

Differentiability at $x_0$ gives, for $h\to0$,
$$
f(x_0+h)-f(x_0)=Lh+o(\norm h).
$$
Therefore
$$
\frac{\norm{f(x_0+h)-f(x_0)}}{\norm h}
\le
\norm{L}_{\mathrm{op}}+o(1),
$$
so the limsup is at most $\norm{L}_{\mathrm{op}}$.

Conversely, choose a unit vector $v$ with
$\norm{Lv}=\norm{L}_{\mathrm{op}}$. Along $h=tv$ with $t\to0$,
$$
\frac{\norm{f(x_0+tv)-f(x_0)}}{\abs t}
\longrightarrow
\norm{Lv}
=\norm{L}_{\mathrm{op}}.
$$
Thus the limsup is exactly the operator norm.

:::

:::

::: {.pf-step #s3}

$$
\abs{\det L}\le\norm{L}_{\mathrm{op}}^3.
$$

::: pf-proof

Let $e_1,e_2,e_3$ be the standard orthonormal basis. By Hadamard's
determinant inequality,
$$
\abs{\det L}
\le
\prod_{j=1}^3\norm{Le_j}
\le
\norm{L}_{\mathrm{op}}^3.
$$

:::

:::

::: {.pf-step #s4}

$$
\abs{J(x_0)}
\le
\limsup_{x\to x_0}
\frac{\norm{f(x)-f(x_0)}^3}{\norm{x-x_0}^3}.
$$

::: pf-proof

The quotient inside the limsup is nonnegative and is the cube of the
quotient in step [](#s2){.pf-ref}. Hence step [](#s2){.pf-ref} gives
$$
\limsup_{x\to x_0}
\frac{\norm{f(x)-f(x_0)}^3}{\norm{x-x_0}^3}
=\norm{L}_{\mathrm{op}}^3.
$$
Combine this with step [](#s3){.pf-ref} and
$\abs{J(x_0)}=\abs{\det L}$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} gives the asserted volume limit, and step [](#s4){.pf-ref} gives the
asserted inequality.

:::

:::

:::
