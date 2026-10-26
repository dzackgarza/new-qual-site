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
---

::: {.problem}
Let $f$ and $g$ be analytic on a domain $D$ whose closure is compact in $\mathbb C$.
Show that
\[
|f(z)|+|g(z)|
\]
takes its maximum on the boundary $\partial D$.

Hint: consider $f(z)e^{i\alpha}+g(z)e^{i\beta}$ for suitable $\alpha,\beta$.
:::

As written, the source statement is missing a boundary-regularity hypothesis:
if $f$ and $g$ are only holomorphic on $D$, they need not extend to
$\partial D$.
The intended statement is correct if
\[
f,g\in C(\overline D)
\]
and are holomorphic on $D$.

::: pf

::: pf-step

The literal statement is false without boundary regularity.


::: pf-proof

Take
\[
D=\{z:|z|<1\},
\qquad
f(z)=\frac1{1-z},
\qquad
g(z)=0.
\]
Then $f$ and $g$ are holomorphic on $D$, and
\[
\overline D
\]
is compact.
But $f$ does not extend continuously to
\[
z=1\in\partial D,
\]
and
\[
|f(z)|
\longrightarrow
\infty
\]
as $z\to1$ from within $D$.
Thus the boundary maximum in the literal statement is not defined.

:::

:::

::: pf-step

Assume henceforth that $f$ and $g$ are continuous on
\[
\overline D
\]
and holomorphic on $D$.
Then
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

::: pf-step

If
\[
z_0\in\partial D,
\]
then the desired conclusion already holds.


::: pf-proof

By step <1>2,
\[
h(z_0)=M.
\]
Thus $h$ attains its maximum on the boundary.

:::

:::

::: pf-step

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

::: pf-step

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

::: pf-step

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

By the phase choice in step <1>4,
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

::: pf-step

Since $z_0$ is an interior point where $|F|$ attains its global
maximum, the maximum modulus principle implies that $F$ is constant on $D$.


::: pf-proof

The domain $D$ is connected and $F$ is holomorphic.
By step <1>6,
\[
|F(z)|
\le
M
\]
throughout $D$, with equality at the interior point $z_0$.
The strong maximum modulus principle therefore makes $F$ constant.

:::

:::

::: pf-step

For every boundary point
\[
\zeta\in\partial D,
\]
one has
\[
|F(\zeta)|=M.
\]


::: pf-proof

By step <1>7,
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

::: pf-step

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
Step <1>8 gives
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

::: pf-step

Consequently, under the intended boundary-continuity hypothesis,
\[
\boxed{
|f(z)|+|g(z)|
\text{ attains its maximum on }\partial D.
}
\]


::: pf-proof

If the maximizing point from step <1>2 lies on the boundary, apply
step <1>3.
If it lies in the interior, step <1>9 shows that every boundary point also
has the same maximal value.

:::

:::

::: pf-qed

Step <1>1 records the defect in the literal source statement.
Steps <1>2--<1>10 prove the corrected theorem using the source's
phase-alignment hint.

:::

:::
