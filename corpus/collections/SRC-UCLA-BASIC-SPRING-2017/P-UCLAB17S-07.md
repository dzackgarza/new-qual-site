---
schema: qual/card@1
id: P-UCLAB17S-07
kind: problem
title: Existence and uniqueness for $f(x)=1-\bigl(\int_0^x tf(t)\,dt\bigr)^2$
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Prove existence and uniqueness of a nonnegative continuous function $f:[0,1]\to[0,1]$ satisfying
$$
f(x)=1-\left(\int_0^x t f(t)\,dt\right)^2.
$$
:::

::: {.solution}

Suppose first that $f:[0,1]\to[0,1]$ is a continuous solution, and define
$$
F(x)
=
\int_0^x t f(t)\,dt.
$$

::: pf

::: {.pf-step #s1-1}

The function $F$ is continuously differentiable and satisfies
$$
F'(x)=xf(x),
\qquad
F(0)=0.
$$


::: pf-proof

The integrand
$$
t\longmapsto tf(t)
$$
is continuous.
The fundamental theorem of calculus therefore gives
$$
F'(x)=xf(x).
$$
Also,
$$
F(0)=0.
$$

:::

:::

::: {.pf-step #s1-2}

The integral equation is equivalent to
$$
\boxed{
F'(x)=x\bigl(1-F(x)^2\bigr),
\qquad
F(0)=0.
}
$$


::: pf-proof

The original equation says
$$
f(x)=1-F(x)^2.
$$
Substitute this into the identity
$$
F'(x)=xf(x)
$$
from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

For every
$$
x\in[0,1],
$$
one has
$$
0\le F(x)\le\frac{x^2}{2}\le\frac12.
$$


::: pf-proof

Since
$$
0\le f(t)\le1,
$$
one has
$$
0
\le
F(x)
=
\int_0^x tf(t)\,dt
\le
\int_0^x t\,dt
=
\frac{x^2}{2}.
$$

:::

:::

::: {.pf-step #s1-4}

Since
$$
|F(x)|<1,
$$
one may divide the differential equation in step [](#s1-2){.pf-ref} by
$$
1-F(x)^2
$$
to obtain
$$
\frac{F'(x)}{1-F(x)^2}
=
x.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives
$$
0\le F(x)\le\frac12<1.
$$
Hence the denominator is strictly positive.

:::

:::

::: {.pf-step #s1-5}

Integrating from $0$ to $x$ gives
$$
\operatorname{arctanh}F(x)
=
\frac{x^2}{2}.
$$


::: pf-proof

An antiderivative of
$$
\frac1{1-u^2}
$$
on
$$
(-1,1)
$$
is
$$
\operatorname{arctanh}u.
$$
Thus step [](#s1-4){.pf-ref} gives
$$
\operatorname{arctanh}F(x)
-
\operatorname{arctanh}F(0)
=
\int_0^x s\,ds
=
\frac{x^2}{2}.
$$
Since
$$
F(0)=0,
$$
the initial term vanishes.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
F(x)
=
\tanh\left(\frac{x^2}{2}\right).
}
$$


::: pf-proof

Apply the inverse function
$$
\tanh
$$
to both sides of step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Any continuous solution must therefore satisfy
$$
\boxed{
f(x)
=
1-
\tanh^2\left(\frac{x^2}{2}\right)
=
\operatorname{sech}^2\left(\frac{x^2}{2}\right).
}
$$


::: pf-proof

The integral equation gives
$$
f(x)=1-F(x)^2.
$$
Substitute step [](#s1-6){.pf-ref} and use
$$
1-\tanh^2u
=
\operatorname{sech}^2u.
$$
This proves uniqueness if a solution exists.

:::

:::

::: pf-step

Define
$$
\boxed{
f_0(x)
=
\operatorname{sech}^2\left(\frac{x^2}{2}\right).
}
$$
Then
$$
f_0:[0,1]\to[0,1]
$$
is continuous and nonnegative.


::: pf-proof

The function $\operatorname{sech}^2$ is continuous and takes values in
$$
(0,1].
$$
Composing with
$$
x\mapsto x^2/2
$$
preserves continuity.

:::

:::

::: {.pf-step #s1-9}

For
$$
F_0(x)
=
\tanh\left(\frac{x^2}{2}\right),
$$
one has
$$
F_0'(x)
=
x f_0(x)
$$
and
$$
F_0(0)=0.
$$


::: pf-proof

Differentiate:
$$
\begin{aligned}
F_0'(x)
&=
\operatorname{sech}^2\left(\frac{x^2}{2}\right)
\cdot x\\
&=
x f_0(x).
\end{aligned}
$$
Also,
$$
F_0(0)=\tanh0=0.
$$

:::

:::

::: {.pf-step #s1-10}

Hence
$$
\int_0^x t f_0(t)\,dt
=
F_0(x)
=
\tanh\left(\frac{x^2}{2}\right).
$$


::: pf-proof

Integrate the differential identity in step [](#s1-9){.pf-ref} from $0$ to $x$.

:::

:::

::: {.pf-step #s1-11}

The function $f_0$ satisfies the original integral equation.


::: pf-proof

By step [](#s1-10){.pf-ref},
$$
\left(
\int_0^x t f_0(t)\,dt
\right)^2
=
\tanh^2\left(\frac{x^2}{2}\right).
$$
Therefore
$$
\begin{aligned}
1-
\left(
\int_0^x t f_0(t)\,dt
\right)^2
&=
1-\tanh^2\left(\frac{x^2}{2}\right)\\
&=
\operatorname{sech}^2\left(\frac{x^2}{2}\right)\\
&=
f_0(x).
\end{aligned}
$$
Thus existence holds.

:::

:::

::: {.pf-step #s1-12}

Therefore there exists exactly one nonnegative continuous solution, namely
$$
\boxed{
f(x)
=
\operatorname{sech}^2\left(\frac{x^2}{2}\right).
}
$$


::: pf-proof

Existence is step [](#s1-11){.pf-ref} and uniqueness is step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} is the required existence-and-uniqueness statement.

:::

:::

:::
