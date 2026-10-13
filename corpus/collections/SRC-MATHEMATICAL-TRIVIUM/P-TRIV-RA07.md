---
schema: qual/card@1
id: P-TRIV-RA07
kind: problem
title: Minimum of the tilted double well $\frac\lambda4(x^2-v^2)^2-\epsilon x$ for small $\epsilon$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the minimal value of the function $f ( x ) = \frac { \lambda } { 4 } ( x ^ { 2 } - v ^ { 2 } ) ^ { 2 } - \epsilon x , \lambda , \epsilon > 0$ , to the leading order in $\epsilon \ll 1$
:::

::: {.remark}
The double-well interpretation assumes $v>0$. If $v=0$, the scaling of the
minimum is different. The solution below treats the intended $v>0$ case.
:::

::: {.solution}
<1>1. At $\epsilon=0$, the minima are at
$$
x=\pm v,
$$
with value $0$.

::: {.proof}
When $\epsilon=0$,
$$
f(x)=\frac\lambda4(x^2-v^2)^2\geq0,
$$
and equality occurs exactly at $x=\pm v$.
:::

<1>2. For $\epsilon>0$ small, the global minimum lies near $x=v$.

::: {.proof}
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

<1>3. Critical points satisfy
$$
\lambda x(x^2-v^2)-\epsilon=0.
$$

::: {.proof}
Differentiate:
$$
f'(x)
=
\lambda x(x^2-v^2)-\epsilon.
$$
:::

<1>4. Write the minimizing critical point as
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

::: {.proof}
Substitute $x=v+\delta$ into step <1>3:
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

<1>5. Hence
$$
\boxed{
\delta
=
\frac{\epsilon}{2\lambda v^2}
+
O(\epsilon^2).
}
$$

::: {.proof}
Equation <1>4 shows $\delta=O(\epsilon)$. Keeping the linear term gives
$$
2\lambda v^2\delta=\epsilon+O(\epsilon^2),
$$
and division by $2\lambda v^2$ gives the result.
:::

<1>6. At $x=v+\delta$,
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

::: {.proof}
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

<1>7. Substituting step <1>5 into step <1>6 gives
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

::: {.proof}
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

<1>8. Therefore the leading behavior is
$$
\boxed{f_{\min}\sim-\epsilon v}.
$$

::: {.proof}
The first correction in step <1>7 is of order $\epsilon^2$.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>7--<1>8 give the requested asymptotic minimum.
:::
:::
