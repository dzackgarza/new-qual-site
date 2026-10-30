---
schema: qual/card@1
id: P-UCLARA17F-04
kind: problem
title: A bounded functional on $C([-1,1])$ mapping the unit ball onto an open set
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 4. Consider the Banach space $V=C([-1,1])$ of all real-valued continuous functions on $[-1,1]$, equipped with the supremum norm
$$
\norm{f}=\sup\{\abs{f(x)}:x\in[-1,1]\},\qquad f\in V.
$$
Let
$$
B=\{f\in V:\norm{f}\le1\}
$$
be the closed unit ball in $V$. Show that there exists a bounded linear functional $\Lambda:V\to\RR$ such that $\Lambda(B)$ is an open subset of $\RR$.
:::

::: {.solution}

Define
$$
\boxed{
\Lambda(f)
=
\int_0^1 f(x)\,dx
-
\int_{-1}^0 f(x)\,dx}.
$$

::: pf

::: pf-step

The map
$$
\Lambda:V\to\RR
$$
is linear.


::: pf-proof

Both integrals are linear in $f$, so their difference is linear.

:::

:::

::: {.pf-step #s1-2}

For every $f\in V$,
$$
\boxed{
\abs{\Lambda(f)}
\le
2\norm{f}_\infty}.
$$


::: pf-proof

By the triangle inequality,
$$
\begin{aligned}
\abs{\Lambda(f)}
&\le
\int_0^1\abs{f(x)}\,dx
+
\int_{-1}^0\abs{f(x)}\,dx\\
&\le
\norm{f}_\infty+\norm{f}_\infty\\
&=
2\norm{f}_\infty.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Hence $\Lambda$ is bounded and
$$
\boxed{
\norm{\Lambda}\le2}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} is exactly the operator-norm estimate.

:::

:::

::: pf-step

One has
$$
\boxed{
f_\varepsilon\in B}.
$$


::: pf-proof

The function is continuous at $\pm\varepsilon$, and
$$
\abs{f_\varepsilon(x)}\le1
$$
for all $x$. Hence
$$
\norm{f_\varepsilon}_\infty\le1.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{
\Lambda(f_\varepsilon)=2-\varepsilon}.
$$


::: pf-proof

Compute the positive-half integral:
$$
\begin{aligned}
\int_0^1 f_\varepsilon(x)\,dx
&=
\int_0^\varepsilon \frac{x}{\varepsilon}\,dx
+
\int_\varepsilon^1 1\,dx\\
&=
\frac{\varepsilon}{2}
+
1-\varepsilon\\
&=
1-\frac{\varepsilon}{2}.
\end{aligned}
$$
By odd symmetry of $f_\varepsilon$,
$$
\int_{-1}^0 f_\varepsilon(x)\,dx
=
-\left(
1-\frac{\varepsilon}{2}
\right).
$$
Therefore
$$
\Lambda(f_\varepsilon)
=
2\left(
1-\frac{\varepsilon}{2}
\right)
=
2-\varepsilon.
$$

:::

:::

::: pf-step

Hence
$$
\boxed{
\norm{\Lambda}=2}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives $\norm{\Lambda}\le2$. Step [](#s1-5){.pf-ref} gives values
$$
\Lambda(f_\varepsilon)=2-\varepsilon
$$
with $\norm{f_\varepsilon}_\infty\le1$, so
$$
\norm{\Lambda}
\ge
2-\varepsilon
$$
for every $\varepsilon>0$. Let $\varepsilon\downarrow0$.

:::

:::

::: {.pf-step #s1-7}

Suppose $f\in B$ and
$$
\Lambda(f)=2.
$$
Then
$$
\boxed{
f(x)=1
\text{ for almost every }x\in[0,1]}.
$$


::: pf-proof

Since $\norm{f}_\infty\le1$,
$$
\int_0^1 f(x)\,dx\le1
$$
and
$$
-\int_{-1}^0f(x)\,dx\le1.
$$
Their sum is $2$. Therefore both inequalities must be equalities:
$$
\int_0^1 f(x)\,dx=1.
$$
Because
$$
f(x)\le1
$$
everywhere,
$$
\int_0^1(1-f(x))\,dx=0
$$
with nonnegative integrand. Hence
$$
f(x)=1
$$
almost everywhere on $[0,1]$.

:::

:::

::: pf-step

Under the same assumption,
$$
\boxed{
f(x)=-1
\text{ for almost every }x\in[-1,0]}.
$$


::: pf-proof

Equality in the second estimate from step [](#s1-7){.pf-ref} gives
$$
\int_{-1}^0f(x)\,dx=-1.
$$
Since
$$
f(x)\ge-1,
$$
$$
\int_{-1}^0(f(x)+1)\,dx=0
$$
with nonnegative integrand, so
$$
f=-1
$$
almost everywhere there.

:::

:::

::: {.pf-step #s1-9}

Continuity then forces
$$
f(x)=1
$$
for every $x\in[0,1]$ and
$$
f(x)=-1
$$
for every $x\in[-1,0]$.


::: pf-proof

A continuous function that equals a constant almost everywhere on an interval equals that constant everywhere. Otherwise, continuity would produce a nonempty open interval on which it differs from the constant, a set of positive measure.

:::

:::

::: {.pf-step #s1-10}

Step [](#s1-9){.pf-ref} is impossible at $x=0$.


::: pf-proof

It would require simultaneously
$$
f(0)=1
\qquad\text{and}\qquad
f(0)=-1.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{
2\notin\Lambda(B)}.
$$


::: pf-proof

The assumption that some $f\in B$ satisfies $\Lambda(f)=2$ led to the contradiction in step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Likewise,
$$
\boxed{
-2\notin\Lambda(B)}.
$$


::: pf-proof

If $\Lambda(f)=-2$, then
$$
\Lambda(-f)=2,
$$
and $-f\in B$, contradicting step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Hence
$$
\boxed{
\Lambda(B)\subseteq(-2,2)}.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives
$$
\abs{\Lambda(f)}\le2
$$
on $B$, and steps [](#s1-11){.pf-ref} through [](#s1-12){.pf-ref} exclude the endpoints.

:::

:::

::: {.pf-step #s1-14}

There exists $g\in B$ such that
$$
\boxed{
\Lambda(g)>\abs{t}}.
$$


::: pf-proof

Choose $\varepsilon>0$ so small that
$$
2-\varepsilon>\abs{t}.
$$
Then take
$$
g=f_\varepsilon
$$
from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-15}

Define
$$
h
=
\frac{t}{\Lambda(g)}\,g.
$$


::: pf-proof

Since
$$
\Lambda(g)>\abs{t}\ge0,
$$
the denominator is nonzero.

:::

:::

::: {.pf-step #s1-16}

One has
$$
\boxed{
h\in B}.
$$


::: pf-proof

Since $g\in B$,
$$
\norm{g}_\infty\le1.
$$
Also
$$
\abs{
\frac{t}{\Lambda(g)}
}
<1
$$
by step [](#s1-14){.pf-ref}. Therefore
$$
\norm{h}_\infty
<
1.
$$

:::

:::

::: {.pf-step #s1-17}

One has
$$
\boxed{
\Lambda(h)=t}.
$$


::: pf-proof

By linearity,
$$
\Lambda(h)
=
\frac{t}{\Lambda(g)}
\Lambda(g)
=
t.
$$

:::

:::

::: {.pf-step #s1-18}

Therefore
$$
\boxed{
(-2,2)\subseteq\Lambda(B)}.
$$


::: pf-proof

The number $t\in(-2,2)$ was arbitrary, and steps [](#s1-14){.pf-ref} through [](#s1-17){.pf-ref} produce $h\in B$ with image $t$.

:::

:::

::: pf-step

Combining the two inclusions,
$$
\boxed{
\Lambda(B)=(-2,2)}.
$$


::: pf-proof

Use steps [](#s1-13){.pf-ref} and [](#s1-18){.pf-ref}.

:::

:::

::: {.pf-step #s1-20}

Hence $\Lambda(B)$ is open in $\RR$.


::: pf-proof

The interval $(-2,2)$ is open.

:::

:::

::: pf-qed

Step [](#s1-20){.pf-ref} is the required conclusion.

:::

:::

:::
