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
$$
f(t)=e^{t^2}+\frac12\int_0^1\cos(s)f(s)\,ds
$$
admits a unique continuous solution $f:[0,1]\to\RR$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $f$ is a solution, then the quantity
$$
c
=
\frac12\int_0^1\cos(s)f(s)\,ds
$$
is a constant independent of $t$, and
$$
\boxed{f(t)=e^{t^2}+c}.
$$


::: pf-proof

The integral in the equation is taken over the fixed interval $[0,1]$ and contains no $t$ outside the function value $f(s)$.
Thus it is a single real number.
Denote that number by $c$.
The equation then becomes
$$
f(t)=e^{t^2}+c.
$$

:::

:::

::: {.pf-step #s1-2}

Substituting the expression from step [](#s1-1){.pf-ref} into the definition of $c$ gives
$$
c
=
\frac12
\int_0^1
\cos(s)e^{s^2}\,ds
+
\frac c2
\int_0^1\cos(s)\,ds.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
f(s)=e^{s^2}+c.
$$
Therefore
$$
\begin{aligned}
c
&=
\frac12\int_0^1\cos(s)\bigl(e^{s^2}+c\bigr)\,ds\\
&=
\frac12\int_0^1\cos(s)e^{s^2}\,ds
+
\frac c2\int_0^1\cos(s)\,ds.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_0^1\cos(s)\,ds
=
\sin1.
$$


::: pf-proof

An antiderivative of $\cos s$ is $\sin s$, so
$$
\int_0^1\cos(s)\,ds
=
\sin1-\sin0
=
\sin1.
$$

:::

:::

::: {.pf-step #s1-4}

Hence $c$ must satisfy
$$
\left(
1-\frac{\sin1}{2}
\right)c
=
\frac12
\int_0^1\cos(s)e^{s^2}\,ds.
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref} and move the term
$$
\frac c2\sin1
$$
to the left.

:::

:::

::: {.pf-step #s1-5}

The coefficient
$$
1-\frac{\sin1}{2}
$$
is nonzero.


::: pf-proof

Since
$$
\abs{\sin1}\le1,
$$
one has
$$
1-\frac{\sin1}{2}
\ge
\frac12
>
0.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore there is exactly one possible value
$$
\boxed{
c
=
\frac{
\frac12\int_0^1\cos(s)e^{s^2}\,ds
}{
1-\frac12\sin1
}.
}
$$


::: pf-proof

Solve the linear equation from step [](#s1-4){.pf-ref} using the nonzero coefficient from step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Define
$$
\boxed{
f(t)
=
e^{t^2}+c
}
$$
with $c$ as in step [](#s1-6){.pf-ref}.
Then $f$ is continuous on $[0,1]$.


::: pf-proof

The map
$$
t\longmapsto e^{t^2}
$$
is continuous, and adding a constant preserves continuity.

:::

:::

::: {.pf-step #s1-8}

The function from step [](#s1-7){.pf-ref} satisfies the integral equation.


::: pf-proof

By the defining equation for $c$ from step [](#s1-2){.pf-ref},
$$
\frac12
\int_0^1
\cos(s)
\bigl(e^{s^2}+c\bigr)
\,ds
=
c.
$$
Hence
$$
\frac12
\int_0^1
\cos(s)f(s)\,ds
=
c.
$$
Therefore
$$
e^{t^2}
+
\frac12
\int_0^1\cos(s)f(s)\,ds
=
e^{t^2}+c
=
f(t).
$$

:::

:::

::: {.pf-step #s1-9}

The continuous solution is unique.


::: pf-proof

Any solution must have the form
$$
f(t)=e^{t^2}+c
$$
by step [](#s1-1){.pf-ref}.
Its constant $c$ must satisfy the scalar equation from step [](#s1-4){.pf-ref}.
By step [](#s1-5){.pf-ref}, that equation has exactly one solution, namely the value in step [](#s1-6){.pf-ref}.
Thus no second continuous solution can exist.

:::

:::

::: {.pf-step #s1-10}

Therefore the equation admits a unique continuous solution.


::: pf-proof

Existence is step [](#s1-8){.pf-ref} and uniqueness is step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
