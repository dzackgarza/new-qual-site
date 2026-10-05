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

::: {.solution}
<1>1. If $f$ is a solution, then the quantity
\[
c
=
\frac12\int_0^1\cos(s)f(s)\,ds
\]
is a constant independent of $t$, and
\[
\boxed{f(t)=e^{t^2}+c}.
\]

::: {.proof}
The integral in the equation is taken over the fixed interval $[0,1]$ and contains no $t$ outside the function value $f(s)$.
Thus it is a single real number.
Denote that number by $c$.
The equation then becomes
\[
f(t)=e^{t^2}+c.
\]
:::

<1>2. Substituting the expression from step <1>1 into the definition of $c$ gives
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

::: {.proof}
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

<1>3. One has
\[
\int_0^1\cos(s)\,ds
=
\sin1.
\]

::: {.proof}
An antiderivative of $\cos s$ is $\sin s$, so
\[
\int_0^1\cos(s)\,ds
=
\sin1-\sin0
=
\sin1.
\]
:::

<1>4. Hence $c$ must satisfy
\[
\left(
1-\frac{\sin1}{2}
\right)c
=
\frac12
\int_0^1\cos(s)e^{s^2}\,ds.
\]

::: {.proof}
Substitute step <1>3 into step <1>2 and move the term
\[
\frac c2\sin1
\]
to the left.
:::

<1>5. The coefficient
\[
1-\frac{\sin1}{2}
\]
is nonzero.

::: {.proof}
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

<1>6. Therefore there is exactly one possible value
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

::: {.proof}
Solve the linear equation from step <1>4 using the nonzero coefficient from step <1>5.
:::

<1>7. Define
\[
\boxed{
f(t)
=
e^{t^2}+c
}
\]
with $c$ as in step <1>6.
Then $f$ is continuous on $[0,1]$.

::: {.proof}
The map
\[
t\longmapsto e^{t^2}
\]
is continuous, and adding a constant preserves continuity.
:::

<1>8. The function from step <1>7 satisfies the integral equation.

::: {.proof}
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

<1>9. The continuous solution is unique.

::: {.proof}
Any solution must have the form
\[
f(t)=e^{t^2}+c
\]
by step <1>1.
Its constant $c$ must satisfy the scalar equation from step <1>4.
By step <1>5, that equation has exactly one solution, namely the value in step <1>6.
Thus no second continuous solution can exist.
:::

<1>10. Therefore the equation admits a unique continuous solution.

::: {.proof}
Existence is step <1>8 and uniqueness is step <1>9.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the required conclusion.
:::
:::
