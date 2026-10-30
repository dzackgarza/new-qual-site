---
schema: qual/card@1
id: P-UCLARA11F-12
kind: problem
title: Differentiation preserves exponential type
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
An entire function $f:\CC\to\CC$ is of exponential type if there are constants $c_1,c_2>0$ such that
$$
\abs{f(z)}\le c_1e^{c_2\abs{z}}
\qquad\text{for every }z\in\CC.
$$
Show that $f$ is of exponential type if and only if $f'$ is of exponential type.
:::

::: {.solution}

## If $f$ is of exponential type, then $f'$ is of exponential type

Assume there are constants
$$
c_1,c_2>0
$$
such that
$$
\abs{f(z)}
\le
c_1e^{c_2\abs{z}}
$$
for all $z\in\CC$.

::: pf

::: pf-step

Fix $z\in\CC$ and apply Cauchy's derivative formula on the circle
$$
\abs{w-z}=1.
$$


::: pf-proof

The function $f$ is entire, so it is holomorphic on and inside every such circle.

:::

:::

::: pf-step

Cauchy's formula gives
$$
f'(z)
=
\frac1{2\pi i}
\int_{\abs{w-z}=1}
\frac{f(w)}{(w-z)^2}\,dw.
$$


::: pf-proof

This is the standard derivative form of Cauchy's integral formula.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\abs{f'(z)}
\le
\max_{\abs{w-z}=1}\abs{f(w)}.
$$


::: pf-proof

On the circle,
$$
\abs{w-z}=1,
$$
and its length is $2\pi$. Hence the $ML$-estimate gives
$$
\abs{f'(z)}
\le
\frac1{2\pi}(2\pi)\max_{\abs{w-z}=1}\abs{f(w)}.
$$

:::

:::

::: {.pf-step #s1-4}

If
$$
\abs{w-z}=1,
$$
then
$$
\boxed{\abs{w}\le \abs{z}+1}.
$$


::: pf-proof

By the triangle inequality,
$$
\abs{w}
\le
\abs{w-z}+\abs{z}
=
1+\abs{z}.
$$

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\abs{f'(z)}
\le
c_1e^{c_2(\abs{z}+1)}
=
c_1e^{c_2}e^{c_2\abs{z}}.
$$


::: pf-proof

Apply the exponential-type bound for $f$ to step [](#s1-3){.pf-ref} and use step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\abs{f'(z)}
\le
C_1e^{C_2\abs{z}}}
$$
for all $z$, with
$$
C_1=c_1e^{c_2},
\qquad
C_2=c_2.
$$


::: pf-proof

This is just a relabeling of the constants in step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Thus $f'$ is of exponential type.


::: pf-proof

Step [](#s1-6){.pf-ref} matches the definition.

:::

:::

::: {.pf-step #s1-8}

For every $z\in\CC$,
$$
\boxed{
f(z)-f(0)
=
\int_0^1
z\,f'(tz)\,dt}.
$$


::: pf-proof

Apply the fundamental theorem of calculus to the function
$$
t\longmapsto f(tz):
$$
$$
\frac{d}{dt}f(tz)
=
z\,f'(tz).
$$
Integrate from $0$ to $1$.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\abs{f(z)}
\le
\abs{f(0)}
+
\abs{z}
\int_0^1
\abs{f'(tz)}\,dt.
$$


::: pf-proof

Take absolute values in step [](#s1-8){.pf-ref} and use the triangle inequality.

:::

:::

::: {.pf-step #s1-10}

Using the exponential-type bound for $f'$,
$$
\abs{f(z)}
\le
\abs{f(0)}
+
a_1\abs{z}
\int_0^1
e^{a_2t\abs{z}}\,dt.
$$


::: pf-proof

Since
$$
\abs{tz}=t\abs{z}
$$
for $0\le t\le1$, substitute the assumed bound into step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

If $z\ne0$,
$$
\abs{z}
\int_0^1
e^{a_2t\abs{z}}\,dt
=
\frac{e^{a_2\abs{z}}-1}{a_2}.
$$


::: pf-proof

Integrate explicitly:
$$
\int_0^1
e^{a_2t\abs{z}}\,dt
=
\frac{e^{a_2\abs{z}}-1}{a_2\abs{z}}.
$$
Multiply by $\abs{z}$.

:::

:::

::: pf-step

Hence for $z\ne0$,
$$
\abs{f(z)}
\le
\abs{f(0)}
+
\frac{a_1}{a_2}
\left(
e^{a_2\abs{z}}-1
\right).
$$


::: pf-proof

Use steps [](#s1-10){.pf-ref} through [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Since
$$
e^{a_2\abs{z}}\ge1,
$$
one obtains
$$
\boxed{
\abs{f(z)}
\le
\left(
\abs{f(0)}+\frac{a_1}{a_2}
\right)
e^{a_2\abs{z}}}
$$
for every $z\in\CC$.


::: pf-proof

For $z\ne0$,
$$
\abs{f(0)}
\le
\abs{f(0)}e^{a_2\abs{z}}
$$
and
$$
\frac{a_1}{a_2}(e^{a_2\abs{z}}-1)
\le
\frac{a_1}{a_2}e^{a_2\abs{z}}.
$$
At $z=0$, the displayed inequality is immediate.

:::

:::

::: {.pf-step #s1-14}

Therefore $f$ is of exponential type.


::: pf-proof

Step [](#s1-13){.pf-ref} has exactly the required form.

:::

:::

::: {.pf-step #s1-15}

Consequently,
$$
\boxed{
f\text{ is of exponential type}
\iff
f'\text{ is of exponential type}.}
$$


::: pf-proof

The forward implication is step [](#s1-7){.pf-ref}, and the reverse implication is step [](#s1-14){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-15){.pf-ref} is the required equivalence.

:::

:::

:::
