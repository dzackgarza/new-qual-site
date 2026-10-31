---
schema: qual/card@1
id: P-TRIV-RA07
kind: problem
title: Minimum of the tilted double well $\frac\lambda4(x^2-v^2)^2-\epsilon x$ for small $\epsilon$
classification:
  areas: [real-analysis]
  topics:
  - Extrema
  - Perturbation Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the minimal value of the function $f(x) = \frac{\lambda}{4}(x^2 - v^2)^2 - \epsilon x$, $\lambda, \epsilon > 0$, to the leading order in $\epsilon \ll 1$.
:::

::: {.remark}
The double-well interpretation assumes $v>0$. If $v=0$, the scaling of the
minimum is different. The solution below treats the intended $v>0$ case.
:::

::: {.solution}

::: pf

::: pf-step

At $\epsilon=0$, the minima are at
$$
x=\pm v,
$$
with value $0$.


::: pf-proof

When $\epsilon=0$,
$$
f(x)=\frac\lambda4(x^2-v^2)^2\geq0,
$$
and equality occurs exactly at $x=\pm v$.

:::

:::

::: pf-step

For $\epsilon>0$ small, the global minimum lies near $x=v$.


::: pf-proof

At the two unperturbed minima,
$$
f(v)=-\epsilon v,
$$
while
$$
f(-v)=\epsilon v.
$$
Thus the linear tilt lowers the well near $+v$ and raises the one near $-v$.
For sufficiently small $\epsilon$, continuity of the critical points preserves
this ordering.

:::

:::

::: {.pf-step #s1-3}

Critical points satisfy
$$
\lambda x(x^2-v^2)-\epsilon=0.
$$


::: pf-proof

Differentiate:
$$
f'(x)
=
\lambda x(x^2-v^2)-\epsilon.
$$

:::

:::

::: {.pf-step #s1-4}

Write the minimizing critical point as
$$
x=v+\delta.
$$
Then
$$
2\lambda v^2\delta
+
3\lambda v\delta^2
+
\lambda\delta^3
=
\epsilon.
$$


::: pf-proof

Substitute $x=v+\delta$ into step [](#s1-3){.pf-ref}:
$$
x^2-v^2
=
2v\delta+\delta^2,
$$
so
$$
x(x^2-v^2)
=
(v+\delta)(2v\delta+\delta^2)
=
2v^2\delta+3v\delta^2+\delta^3.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\delta
=
\frac{\epsilon}{2\lambda v^2}
+
O(\epsilon^2).
}
$$


::: pf-proof

Equation [](#s1-4){.pf-ref} shows $\delta=O(\epsilon)$. Keeping the linear term gives
$$
2\lambda v^2\delta=\epsilon+O(\epsilon^2),
$$
and division by $2\lambda v^2$ gives the result.

:::

:::

::: {.pf-step #s1-6}

At $x=v+\delta$,
$$
f(x)
=
-\epsilon v
+
\lambda v^2\delta^2
-
\epsilon\delta
+
O(\delta^3).
$$


::: pf-proof

Since
$$
(x^2-v^2)^2
=
(2v\delta+\delta^2)^2
=
4v^2\delta^2+O(\delta^3),
$$
one has
$$
\frac\lambda4(x^2-v^2)^2
=
\lambda v^2\delta^2+O(\delta^3).
$$
Also
$$
-\epsilon x
=
-\epsilon v-\epsilon\delta.
$$

:::

:::

::: {.pf-step #s1-7}

Substituting step [](#s1-5){.pf-ref} into step [](#s1-6){.pf-ref} gives
$$
\boxed{
f_{\min}
=
-\epsilon v
-
\frac{\epsilon^2}{4\lambda v^2}
+
O(\epsilon^3).
}
$$


::: pf-proof

Using
$$
\delta
=
\frac{\epsilon}{2\lambda v^2}
+
O(\epsilon^2),
$$
the quadratic contribution is
$$
\lambda v^2\delta^2
=
\frac{\epsilon^2}{4\lambda v^2}
+
O(\epsilon^3),
$$
while
$$
-\epsilon\delta
=
-\frac{\epsilon^2}{2\lambda v^2}
+
O(\epsilon^3).
$$
Add them to the term $-\epsilon v$.

:::

:::

::: {.pf-step #s1-8}

Therefore the leading behavior is
$$
\boxed{f_{\min}\sim-\epsilon v}.
$$


::: pf-proof

The first correction in step [](#s1-7){.pf-ref} is of order $\epsilon^2$.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} give the requested asymptotic minimum.

:::

:::

:::
