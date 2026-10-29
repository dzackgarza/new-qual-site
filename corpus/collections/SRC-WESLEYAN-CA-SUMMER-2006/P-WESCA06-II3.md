---
schema: qual/card@1
id: P-WESCA06-II3
kind: problem
title: "The maximum of $|f|+|g|$ occurs on the boundary"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Problems, problem 3 (August 9, 2006) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source assumed only that f and g are analytic on D, so the boundary maximum is undefined for f(z)=1/(1-z) on the unit disc; the statement now also assumes f and g continuous on the closure of D.
---

::: {.problem}
Let $D$ be a domain whose closure is compact in $\CC$, and let $f$ and $g$ be continuous on $\overline D$ and analytic on $D$.
Show that
\[
|f(z)|+|g(z)|
\]
takes its maximum on the boundary $\partial D$.

Hint: consider $f(z)e^{i\alpha}+g(z)e^{i\beta}$ for suitable $\alpha,\beta$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function
\[
h(z)
\coloneqq
|f(z)|+|g(z)|
\]
attains a maximum on $\overline D$.


::: pf-proof

The function $h$ is continuous on the compact set
\[
\overline D.
\]
By the extreme value theorem, there exists
\[
z_0\in\overline D
\]
such that
\[
h(z_0)
=
M
\coloneqq
\max_{z\in\overline D}h(z).
\]

:::

:::

::: {.pf-step #s1-2}

If
\[
z_0\in\partial D,
\]
then the desired conclusion already holds.


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
h(z_0)=M.
\]
Thus $h$ attains its maximum on the boundary.

:::

:::

::: {.pf-step #s1-3}

Suppose instead that
\[
z_0\in D.
\]
Choose real numbers
\[
\alpha,\beta
\]
such that
\[
e^{i\alpha}f(z_0)
=
|f(z_0)|
\]
and
\[
e^{i\beta}g(z_0)
=
|g(z_0)|.
\]


::: pf-proof

If
\[
f(z_0)\ne0,
\]
take
\[
e^{i\alpha}
=
\frac{\overline{f(z_0)}}{|f(z_0)|}.
\]
If
\[
f(z_0)=0,
\]
choose any $\alpha$.
The same construction gives $\beta$ for $g(z_0)$.

:::

:::

::: {.pf-step #s1-4}

Define
\[
F(z)
\coloneqq
e^{i\alpha}f(z)
+
e^{i\beta}g(z).
\]
Then $F$ is holomorphic on $D$ and continuous on $\overline D$.


::: pf-proof

It is a fixed complex linear combination of $f$ and $g$.

:::

:::

::: {.pf-step #s1-5}

For every
\[
z\in\overline D,
\]
\[
|F(z)|
\le
|f(z)|+|g(z)|
\le
M.
\]
At $z_0$,
\[
|F(z_0)|=M.
\]


::: pf-proof

The first inequality is the triangle inequality.
The second is the definition of $M$.

By the phase choice in step [](#s1-3){.pf-ref},
\[
F(z_0)
=
|f(z_0)|+|g(z_0)|
=
M,
\]
which is a nonnegative real number.
Hence
\[
|F(z_0)|=M.
\]

:::

:::

::: {.pf-step #s1-6}

Since $z_0$ is an interior point where $|F|$ attains its global
maximum, the maximum modulus principle implies that $F$ is constant on $D$.


::: pf-proof

The domain $D$ is connected and $F$ is holomorphic.
By step [](#s1-5){.pf-ref},
\[
|F(z)|
\le
M
\]
throughout $D$, with equality at the interior point $z_0$.
The strong maximum modulus principle therefore makes $F$ constant.

:::

:::

::: {.pf-step #s1-7}

For every boundary point
\[
\zeta\in\partial D,
\]
one has
\[
|F(\zeta)|=M.
\]


::: pf-proof

By step [](#s1-6){.pf-ref},
\[
F
\]
is constant on $D$.
Continuity on
\[
\overline D
\]
extends the same constant value to the boundary.
Therefore
\[
|F(\zeta)|
=
|F(z_0)|
=
M.
\]

:::

:::

::: {.pf-step #s1-8}

For every
\[
\zeta\in\partial D,
\]
\[
h(\zeta)=M.
\]


::: pf-proof

By the triangle inequality,
\[
|F(\zeta)|
\le
|f(\zeta)|+|g(\zeta)|
=
h(\zeta).
\]
Step [](#s1-7){.pf-ref} gives
\[
M
\le
h(\zeta).
\]
But by definition of $M$,
\[
h(\zeta)
\le
M.
\]
Therefore
\[
h(\zeta)=M.
\]

:::

:::

::: {.pf-step #s1-9}

Consequently,
\[
\boxed{
|f(z)|+|g(z)|
\text{ attains its maximum on }\partial D.
}
\]


::: pf-proof

If the maximizing point from step [](#s1-1){.pf-ref} lies on the boundary, apply
step [](#s1-2){.pf-ref}.
If it lies in the interior, step [](#s1-8){.pf-ref} shows that every boundary point also
has the same maximal value.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the assertion.

:::

:::

:::
