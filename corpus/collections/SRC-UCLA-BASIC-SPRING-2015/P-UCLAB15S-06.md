---
schema: qual/card@1
id: P-UCLAB15S-06
kind: problem
title: Unique continuous solution of a scalar integral equation
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Prove that the integral equation
\[
f(t)=e^{t^2}+\frac12\int_0^1\cos(s)f(s)\,ds
\]
admits a unique continuous solution $f:[0,1]\to\mathbb R$.
:::

::: pf

::: pf-step

If $f$ is a solution, then the quantity
\[
c
=
\frac12\int_0^1\cos(s)f(s)\,ds
\]
is a constant independent of $t$, and
\[
\boxed{f(t)=e^{t^2}+c}.
\]


::: pf-proof

The integral in the equation is taken over the fixed interval $[0,1]$ and contains no $t$ outside the function value $f(s)$.
Thus it is a single real number.
Denote that number by $c$.
The equation then becomes
\[
f(t)=e^{t^2}+c.
\]

:::

:::

::: pf-step

Substituting the expression from step <1>1 into the definition of $c$ gives
\[
c
=
\frac12
\int_0^1
\cos(s)e^{s^2}\,ds
+
\frac c2
\int_0^1\cos(s)\,ds.
\]


::: pf-proof

By step <1>1,
\[
f(s)=e^{s^2}+c.
\]
Therefore
\[
\begin{aligned}
c
&=
\frac12\int_0^1\cos(s)\bigl(e^{s^2}+c\bigr)\,ds\\
&=
\frac12\int_0^1\cos(s)e^{s^2}\,ds
+
\frac c2\int_0^1\cos(s)\,ds.
\end{aligned}
\]

:::

:::

::: pf-step

One has
\[
\int_0^1\cos(s)\,ds
=
\sin1.
\]


::: pf-proof

An antiderivative of $\cos s$ is $\sin s$, so
\[
\int_0^1\cos(s)\,ds
=
\sin1-\sin0
=
\sin1.
\]

:::

:::

::: pf-step

Hence $c$ must satisfy
\[
\left(
1-\frac{\sin1}{2}
\right)c
=
\frac12
\int_0^1\cos(s)e^{s^2}\,ds.
\]


::: pf-proof

Substitute step <1>3 into step <1>2 and move the term
\[
\frac c2\sin1
\]
to the left.

:::

:::

::: pf-step

The coefficient
\[
1-\frac{\sin1}{2}
\]
is nonzero.


::: pf-proof

Since
\[
|\sin1|\le1,
\]
one has
\[
1-\frac{\sin1}{2}
\ge
\frac12
>
0.
\]

:::

:::

::: pf-step

Therefore there is exactly one possible value
\[
\boxed{
c
=
\frac{
\frac12\int_0^1\cos(s)e^{s^2}\,ds
}{
1-\frac12\sin1
}.
}
\]


::: pf-proof

Solve the linear equation from step <1>4 using the nonzero coefficient from step <1>5.

:::

:::

::: pf-step

Define
\[
\boxed{
f(t)
=
e^{t^2}+c
}
\]
with $c$ as in step <1>6.
Then $f$ is continuous on $[0,1]$.


::: pf-proof

The map
\[
t\longmapsto e^{t^2}
\]
is continuous, and adding a constant preserves continuity.

:::

:::

::: pf-step

The function from step <1>7 satisfies the integral equation.


::: pf-proof

By the defining equation for $c$ from step <1>2,
\[
\frac12
\int_0^1
\cos(s)
\bigl(e^{s^2}+c\bigr)
\,ds
=
c.
\]
Hence
\[
\frac12
\int_0^1
\cos(s)f(s)\,ds
=
c.
\]
Therefore
\[
e^{t^2}
+
\frac12
\int_0^1\cos(s)f(s)\,ds
=
e^{t^2}+c
=
f(t).
\]

:::

:::

::: pf-step

The continuous solution is unique.


::: pf-proof

Any solution must have the form
\[
f(t)=e^{t^2}+c
\]
by step <1>1.
Its constant $c$ must satisfy the scalar equation from step <1>4.
By step <1>5, that equation has exactly one solution, namely the value in step <1>6.
Thus no second continuous solution can exist.

:::

:::

::: pf-step

Therefore the equation admits a unique continuous solution.


::: pf-proof

Existence is step <1>8 and uniqueness is step <1>9.

:::

:::

::: pf-qed

Step <1>10 is the required conclusion.

:::

:::
