---
schema: qual/card@1
id: P-WESCA06-I2
kind: problem
title: "Define the multiplicity of an analytic function at a point"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Theorems and Definitions, item 2 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Define the multiplicity of an analytic function $f$ at a point $z_0$ in the domain of $f$.
:::

::: {.solution}

Let
$$
f(z)
=
\sum_{n=0}^{\infty}
a_n(z-z_0)^n
$$
be the Taylor expansion of $f$ at $z_0$.

::: pf

::: {.pf-step #s1-1}

If $f$ is not locally constant near $z_0$, the **multiplicity of
$f$ at $z_0$** is the least positive integer
$$
m\ge1
$$
such that
$$
a_m\ne0.
$$


::: pf-proof

Equivalently,
$$
a_1=a_2=\cdots=a_{m-1}=0,
\qquad
a_m\ne0.
$$
Since
$$
a_n
=
\frac{f^{(n)}(z_0)}{n!},
$$
this means
$$
f'(z_0)
=
\cdots
=
f^{(m-1)}(z_0)
=
0,
\qquad
f^{(m)}(z_0)
\ne
0.
$$

:::

:::

::: {.pf-step #s1-2}

Equivalently, $m$ is the order of the zero of
$$
f(z)-f(z_0)
$$
at $z_0$.


::: pf-proof

The Taylor series gives
$$
f(z)-f(z_0)
=
a_m(z-z_0)^m
+
a_{m+1}(z-z_0)^{m+1}
+
\cdots.
$$
Factor:
$$
f(z)-f(z_0)
=
(z-z_0)^m g(z),
$$
where
$$
g
$$
is holomorphic near $z_0$ and
$$
g(z_0)=a_m\ne0.
$$
Thus the zero has order $m$.

:::

:::

::: {.pf-step #s1-3}

If
$$
f(z_0)=0,
$$
then the multiplicity of $f$ at $z_0$ is exactly the usual multiplicity of
the zero $z_0$.


::: pf-proof

In this case
$$
f(z)-f(z_0)
=
f(z),
$$
so step [](#s1-2){.pf-ref} becomes the usual zero-order definition.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give the requested definition and its standard equivalent
formulations.

:::

:::

:::
