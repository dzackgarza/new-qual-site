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
Find all entire functions $f:\mathbb C\to\mathbb C$ that obey
\[
f'(z)^2+f(z)^2=1.
\]
Prove that your list is exhaustive.
:::

::: {.solution}
<1>1. Every solution satisfies
\[
f'(z)\bigl(f''(z)+f(z)\bigr)=0
\qquad
(z\in\mathbb C).
\]

::: {.proof}
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

<1>2. For every solution, either
\[
f'\equiv0
\]
or
\[
f''+f\equiv0.
\]

::: {.proof}
The two functions
\[
f'
\qquad\text{and}\qquad
f''+f
\]
are entire, and their product is identically zero by step <1>1.

If $f'$ is not identically zero, choose $z_0$ with $f'(z_0)\ne0$. By continuity, $f'$ is nonzero on some neighborhood of $z_0$, so step <1>1 gives
\[
f''+f=0
\]
on that neighborhood. The identity theorem then gives
\[
f''+f\equiv0
\]
on all of $\mathbb C$. Thus one of the two alternatives holds.
:::

<1>3. If $f'\equiv0$, then
\[
f\equiv1
\qquad\text{or}\qquad
f\equiv-1.
\]

::: {.proof}
The condition $f'\equiv0$ makes $f$ constant, say $f\equiv c$. Substitution into the original equation gives
\[
c^2=1,
\]
so $c=\pm1$.
:::

<1>4. Every entire solution of
\[
f''+f=0
\]
has the form
\[
f(z)=a\cos z+b\sin z
\]
for unique constants $a,b\in\mathbb C$.

::: {.proof}
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

<1>5. A function
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

::: {.proof}
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

<1>6. The complete list of solutions is
\[
\boxed{
f(z)=a\cos z+b\sin z,
\qquad
a,b\in\mathbb C,
\qquad
a^2+b^2=1.
}
\]

::: {.proof}
By steps <1>2 through <1>5, every nonconstant solution has the boxed form. The constant solutions from step <1>3 are included as
\[
(a,b)=(1,0)
\qquad\text{and}\qquad
(a,b)=(-1,0).
\]
Conversely, step <1>5 shows that every function in the boxed family satisfies the original equation.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives all entire solutions and proves exhaustiveness.
:::
:::
