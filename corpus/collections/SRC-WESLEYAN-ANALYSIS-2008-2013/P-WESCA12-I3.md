---
schema: qual/card@1
id: P-WESCA12-I3
kind: problem
title: 'Define poles, pole order, and essential singularities'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Basic facts, item 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Define each of the following for an analytic function:

1. a pole;

2. the order of a pole;

3. an essential singularity.
:::

::: {.solution}

Let
$$
z_0\in\CC
$$
be an isolated singularity of $f$, meaning that for some
$$
r>0
$$
the function $f$ is holomorphic on
$$
0<\abs{z-z_0}<r.
$$

::: pf

::: {.pf-step #s1-1}

The point $z_0$ is a **pole** of $f$ if
$$
\abs{f(z)}\longrightarrow\infty
\qquad
(z\to z_0).
$$


::: pf-proof

Equivalently, $z_0$ is a pole if there exists an integer
$$
m\ge1
$$
and a function $g$ holomorphic near $z_0$ such that
$$
g(z_0)\ne0
$$
and
$$
f(z)
=
\frac{g(z)}
{(z-z_0)^m}.
$$

Equivalently, the Laurent series of $f$ at $z_0$ has a finite nonzero
principal part.

:::

:::

::: {.pf-step #s1-2}

The **order** of a pole $z_0$ is the unique integer
$$
m\ge1
$$
such that
$$
(z-z_0)^m f(z)
$$
extends holomorphically across $z_0$ with a nonzero value there.


::: pf-proof

Equivalently, if
$$
f(z)
=
\sum_{n=-m}^{\infty}
a_n(z-z_0)^n,
\qquad
a_{-m}\ne0,
$$
then the pole has order $m$.

It is also the least positive integer $m$ such that
$$
(z-z_0)^m f(z)
$$
has a removable singularity at $z_0$.

:::

:::

::: {.pf-step #s1-3}

The isolated singularity $z_0$ is **essential** if it is neither
removable nor a pole.


::: pf-proof

Equivalently, the Laurent expansion
$$
f(z)
=
\sum_{n=-\infty}^{\infty}
a_n(z-z_0)^n
$$
has infinitely many nonzero negative-power coefficients.

Thus the three isolated-singularity types are:

1. removable: no negative Laurent terms;
2. pole: finitely many negative Laurent terms, at least one nonzero;
3. essential: infinitely many nonzero negative Laurent terms.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give the requested definitions and their standard
equivalent formulations.

:::

:::

:::
