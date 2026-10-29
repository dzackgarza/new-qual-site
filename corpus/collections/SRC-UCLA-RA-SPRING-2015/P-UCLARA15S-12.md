---
schema: qual/card@1
id: P-UCLARA15S-12
kind: problem
title: Entire solutions of $f'^2+f^2=1$
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Find all entire functions $f:\CC\to\CC$ that obey
\[
f'(z)^2+f(z)^2=1.
\]
Prove that your list is exhaustive.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every solution satisfies
\[
f'(z)\bigl(f''(z)+f(z)\bigr)=0
\qquad
(z\in\CC).
\]


::: pf-proof

Differentiate
\[
f'(z)^2+f(z)^2=1.
\]
Since $f$ is entire,
\[
2f'f''+2ff'
=
2f'(f''+f)
=0.
\]

:::

:::

::: {.pf-step #s1-2}

For every solution, either
\[
f'\equiv0
\]
or
\[
f''+f\equiv0.
\]


::: pf-proof

The two functions
\[
f'
\qquad\text{and}\qquad
f''+f
\]
are entire, and their product is identically zero by step [](#s1-1){.pf-ref}.

If $f'$ is not identically zero, choose $z_0$ with $f'(z_0)\ne0$. By continuity, $f'$ is nonzero on some neighborhood of $z_0$, so step [](#s1-1){.pf-ref} gives
\[
f''+f=0
\]
on that neighborhood. The identity theorem then gives
\[
f''+f\equiv0
\]
on all of $\CC$. Thus one of the two alternatives holds.

:::

:::

::: {.pf-step #s1-3}

If $f'\equiv0$, then
\[
f\equiv1
\qquad\text{or}\qquad
f\equiv-1.
\]


::: pf-proof

The condition $f'\equiv0$ makes $f$ constant, say $f\equiv c$. Substitution into the original equation gives
\[
c^2=1,
\]
so $c=\pm1$.

:::

:::

::: pf-step

Every entire solution of
\[
f''+f=0
\]
has the form
\[
f(z)=a\cos z+b\sin z
\]
for unique constants $a,b\in\CC$.


::: pf-proof

Let
\[
a=f(0),
\qquad
b=f'(0),
\]
and define
\[
g(z)=a\cos z+b\sin z.
\]
Then
\[
g''+g=0,
\qquad
g(0)=f(0),
\qquad
g'(0)=f'(0).
\]
The difference
\[
h=f-g
\]
satisfies
\[
h''+h=0,
\qquad
h(0)=h'(0)=0.
\]
Writing
\[
h(z)=\sum_{n=0}^\infty c_n z^n,
\]
the differential equation gives
\[
(n+2)(n+1)c_{n+2}+c_n=0
\qquad
(n\ge0).
\]
Since $c_0=c_1=0$, this recurrence gives $c_n=0$ for every $n$. Thus $h\equiv0$, proving the claimed form. Uniqueness follows from the values at $0$ of $f$ and $f'$.

:::

:::

::: {.pf-step #s1-5}

A function
\[
f(z)=a\cos z+b\sin z
\]
satisfies
\[
f'(z)^2+f(z)^2=1
\]
if and only if
\[
a^2+b^2=1.
\]


::: pf-proof

One has
\[
f'(z)
=
-a\sin z+b\cos z.
\]
Therefore
\[
\begin{aligned}
f'(z)^2+f(z)^2
&=
(-a\sin z+b\cos z)^2
+
(a\cos z+b\sin z)^2\\
&=
a^2(\sin^2z+\cos^2z)
+
b^2(\sin^2z+\cos^2z)\\
&=
a^2+b^2.
\end{aligned}
\]
Hence the original equation holds exactly when $a^2+b^2=1$.

:::

:::

::: {.pf-step #s1-6}

The complete list of solutions is
\[
\boxed{
f(z)=a\cos z+b\sin z,
\qquad
a,b\in\CC,
\qquad
a^2+b^2=1.
}
\]


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref}, every nonconstant solution has the boxed form. The constant solutions from step [](#s1-3){.pf-ref} are included as
\[
(a,b)=(1,0)
\qquad\text{and}\qquad
(a,b)=(-1,0).
\]
Conversely, step [](#s1-5){.pf-ref} shows that every function in the boxed family satisfies the original equation.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives all entire solutions and proves exhaustiveness.

:::

:::

:::
