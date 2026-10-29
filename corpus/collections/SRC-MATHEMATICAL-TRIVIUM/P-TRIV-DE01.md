---
schema: qual/card@1
id: P-TRIV-DE01
kind: problem
title: Separable equation $y'=xe^{x^2-2\log y}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Solve $y ^ { \prime } ( x ) = x e ^ { x ^ { 2 } - 2 \log y ( x ) }$
:::

::: {.solution}

Because the equation contains $\log y$, work on an interval on which
$$
y(x)>0.
$$

::: pf

::: {.pf-step #s1-1}

Rewrite the differential equation as
$$
y'
=
x e^{x^2}y^{-2}.
$$


::: pf-proof

Use
$$
e^{-2\log y}
=
y^{-2}
$$
for $y>0$.

:::

:::

::: {.pf-step #s1-2}

Multiply by $y^2$:
$$
y^2y'
=
x e^{x^2}.
$$


::: pf-proof

This is an algebraic rearrangement of step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The left-hand side is
$$
y^2y'
=
\frac13
\frac d{dx}(y^3).
$$


::: pf-proof

Differentiate $y^3$ by the chain rule:
$$
\frac d{dx}(y^3)
=
3y^2y'.
$$

:::

:::

::: {.pf-step #s1-4}

The right-hand side is
$$
x e^{x^2}
=
\frac12
\frac d{dx}e^{x^2}.
$$


::: pf-proof

Differentiate $e^{x^2}$:
$$
\frac d{dx}e^{x^2}
=
2x e^{x^2}.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\frac13y^3
=
\frac12e^{x^2}
+
C_0.
$$


::: pf-proof

Integrate step [](#s1-2){.pf-ref} using steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Equivalently,
$$
\boxed{
y^3
=
C
+
\frac32e^{x^2}
}
$$
for an arbitrary constant $C\in\RR$.


::: pf-proof

Multiply step [](#s1-5){.pf-ref} by $3$ and absorb the factor $3$ into the integration
constant.

:::

:::

::: {.pf-step #s1-7}

Thus the solutions are
$$
\boxed{
y(x)
=
\left(
C
+
\frac32e^{x^2}
\right)^{1/3},
}
$$
on every interval where
$$
C+\frac32e^{x^2}>0.
$$


::: pf-proof

Take the real cube root in step [](#s1-6){.pf-ref}. The strict positivity condition is
required by the original logarithm $\log y$.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives the complete family of real solutions on the natural domains
of the equation.

:::

:::

:::
