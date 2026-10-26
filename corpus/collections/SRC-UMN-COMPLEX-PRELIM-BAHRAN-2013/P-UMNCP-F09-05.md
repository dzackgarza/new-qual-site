---
schema: qual/card@1
id: P-UMNCP-F09-05
kind: problem
title: An entire function into the upper half-plane is constant
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Fall 2009, 5 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation.
---

::: {.problem}
Let \(f\) be entire and suppose
\[
f(\mathbb C)\subseteq\{z\in\mathbb C:\operatorname{Im}z>0\}.
\]
Show that \(f\) is constant.
:::

Define
$$
g(z)
\coloneqq
e^{if(z)}.
$$

::: pf

::: pf-step

The function $g$ is entire.


::: pf-proof

The function $f$ is entire by hypothesis, multiplication by $i$ preserves entire functions, and the exponential is entire. Therefore their composition $g$ is entire.

:::

:::

::: pf-step

The function $g$ is bounded:
$$
\boxed{|g(z)|<1}
$$
for every $z\in\CC$.


::: pf-proof

Write
$$
f(z)=u(z)+iv(z),
$$
with
$$
v(z)=\operatorname{Im}f(z)>0.
$$
Then
$$
if(z)
=
iu(z)-v(z),
$$
so
$$
|g(z)|
=
|e^{iu(z)-v(z)}|
=
e^{-v(z)}
<1.
$$

:::

:::

::: pf-step

The function $g$ is constant.


::: pf-proof

By step <1>1, $g$ is entire, and by step <1>2 it is bounded. Liouville's theorem therefore implies that $g$ is constant.

:::

:::

::: pf-step

The derivative $f'$ vanishes identically.


::: pf-proof

Since $g$ is constant,
$$
g'(z)=0
$$
for every $z$. But
$$
g'(z)
=
i f'(z)e^{if(z)}.
$$
The exponential never vanishes, so
$$
f'(z)=0
$$
for every $z\in\CC$.

:::

:::

::: pf-step

Therefore $f$ is constant.


::: pf-proof

An entire function with identically zero derivative is constant on the connected domain $\CC$.

:::

:::

::: pf-qed

Step <1>5 is the required conclusion.

:::

:::
