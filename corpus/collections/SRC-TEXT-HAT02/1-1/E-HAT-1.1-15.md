---
schema: qual/card@1
id: E-HAT-1.1-15
kind: problem
title: Naturality square for basepoint-change homomorphisms
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Natural Transformations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the square directly from the conjugation formula for basepoint change.
---

::: {.problem}
Given a map $f: X \to Y$ and a path $h: I \to X$ from $x_0$ to $x_1$, show that $f_* \beta_h = \beta_{fh} f_*$ in the diagram:

$$\begin{array}{rcl}
\pi_1(X, x_1) & \xrightarrow{\beta_h} & \pi_1(X, x_0) \\
\downarrow f_* & & \downarrow f_* \\
\pi_1(Y, f(x_1)) & \xrightarrow{\beta_{fh}} & \pi_1(Y, f(x_0))
\end{array}$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $[\gamma]\in\pi_1(X,x_1)$.
Then
\[
(f_*\beta_h)([\gamma])
=
[f\circ(h\cdot\gamma\cdot\bar h)].
\]

::: pf-proof

By definition,
\[
\beta_h([\gamma])=[h\cdot\gamma\cdot\bar h]
\]
as a loop based at $x_0$, and $f_*$ is induced by postcomposition with $f$.

:::

:::

::: {.pf-step #s2}

One has
\[
f\circ(h\cdot\gamma\cdot\bar h)
=
(f\circ h)\cdot(f\circ\gamma)\cdot\overline{f\circ h}
\]
up to the standard concatenation parametrization.

::: pf-proof

Postcomposition with $f$ preserves each of the three pieces of the concatenation, and
\[
f\circ\bar h=\overline{f\circ h}.
\]

:::

:::

::: pf-step

Therefore
\[
(f_*\beta_h)([\gamma])
=
(\beta_{fh}f_*)([\gamma]).
\]

::: pf-proof

Using steps [](#s1){.pf-ref} and [](#s2){.pf-ref},
\[
\begin{aligned}
(f_*\beta_h)([\gamma])
&=[(fh)\cdot(f\gamma)\cdot\overline{fh}]\\
&=\beta_{fh}([f\gamma])\\
&=(\beta_{fh}f_*)([\gamma]).
\end{aligned}
\]

:::

:::

::: pf-step

Hence
\[
f_*\beta_h=\beta_{fh}f_*.
\]

::: pf-proof

The element $[\gamma]$ in step [](#s1){.pf-ref} was arbitrary.

:::

:::

:::

:::
