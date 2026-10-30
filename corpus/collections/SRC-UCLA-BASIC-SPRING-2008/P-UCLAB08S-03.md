---
schema: qual/card@1
id: P-UCLAB08S-03
kind: problem
title: Error in the centered finite-difference approximation to a second derivative
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
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Assume $f\in C^4([a,b])$ is real-valued.
Derive a formula for the approximation error $E(h)$ when
$$
f''(x)\sim \frac{f(x+h)-2f(x)+f(x-h)}{h^2},
$$
where $x,x+h,x-h\in(a,b)$.
:::

::: {.solution}

Define the centered-difference approximation
$$
D_hf(x)
=
\frac{f(x+h)-2f(x)+f(x-h)}{h^2}.
$$
We take the approximation error to be
$$
E(h)=D_hf(x)-f''(x).
$$

::: pf

::: pf-step

Taylor's theorem gives
$$
\begin{aligned}
f(x+h)
&=
f(x)
+hf'(x)
+\frac{h^2}{2}f''(x)
+\frac{h^3}{6}f'''(x)
+\frac{h^4}{24}f^{(4)}(\xi_+)
\end{aligned}
$$
for some
$$
\xi_+
$$
between $x$ and $x+h$.


::: pf-proof

Apply Taylor's theorem with Lagrange remainder through degree $3$ to the function $f$ centered at $x$ and evaluated at $x+h$.
The hypothesis
$$
f\in C^4([a,b])
$$
ensures the theorem applies.

:::

:::

::: pf-step

Likewise,
$$
\begin{aligned}
f(x-h)
&=
f(x)
-hf'(x)
+\frac{h^2}{2}f''(x)
-\frac{h^3}{6}f'''(x)
+\frac{h^4}{24}f^{(4)}(\xi_-)
\end{aligned}
$$
for some
$$
\xi_-
$$
between $x-h$ and $x$.


::: pf-proof

Apply the same Taylor theorem with increment $-h$.
The odd powers acquire minus signs, while
$$
(-h)^4=h^4.
$$

:::

:::

::: {.pf-step #s1-3}

Adding the two Taylor formulas and subtracting $2f(x)$ gives
$$
\begin{aligned}
f(x+h)-2f(x)+f(x-h)
&=
h^2f''(x)\\
&\quad+
\frac{h^4}{24}
\left(
f^{(4)}(\xi_+)
+
f^{(4)}(\xi_-)
\right).
\end{aligned}
$$


::: pf-proof

The two linear terms
$$
\pm hf'(x)
$$
cancel.
The cubic terms
$$
\pm\frac{h^3}{6}f'''(x)
$$
also cancel.
The two quadratic terms add to
$$
h^2f''(x).
$$
The fourth-order remainders add as displayed.

:::

:::

::: {.pf-step #s1-4}

Dividing by $h^2$ yields
$$
\boxed{
D_hf(x)
=
f''(x)
+
\frac{h^2}{24}
\left(
f^{(4)}(\xi_+)
+
f^{(4)}(\xi_-)
\right)
}.
$$


::: pf-proof

Divide the identity from step [](#s1-3){.pf-ref} by
$$
h^2,
$$
which is nonzero because the centered difference is only defined for
$$
h\ne0.
$$

:::

:::

::: {.pf-step #s1-5}

Hence the approximation error satisfies
$$
\boxed{
E(h)
=
\frac{h^2}{24}
\left(
f^{(4)}(\xi_+)
+
f^{(4)}(\xi_-)
\right)
}.
$$


::: pf-proof

By definition,
$$
E(h)=D_hf(x)-f''(x).
$$
Subtract
$$
f''(x)
$$
from the formula in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Since $f^{(4)}$ is continuous, there exists
$$
\xi
$$
between $x-h$ and $x+h$ such that
$$
\boxed{
E(h)
=
\frac{h^2}{12}f^{(4)}(\xi)
}.
$$


::: pf-proof

The two points
$$
\xi_-
\quad\text{and}\quad
\xi_+
$$
lie in the interval with endpoints
$$
x-h
\quad\text{and}\quad
x+h.
$$
The number
$$
\frac{
f^{(4)}(\xi_+)+f^{(4)}(\xi_-)
}{2}
$$
lies between the two values
$$
f^{(4)}(\xi_+)
\quad\text{and}\quad
f^{(4)}(\xi_-).
$$
By continuity of $f^{(4)}$ and the intermediate value theorem, there exists a point $\xi$ between $\xi_-$ and $\xi_+$ such that
$$
f^{(4)}(\xi)
=
\frac{
f^{(4)}(\xi_+)+f^{(4)}(\xi_-)
}{2}.
$$
Substituting this into step [](#s1-5){.pf-ref} gives
$$
E(h)
=
\frac{h^2}{12}f^{(4)}(\xi).
$$

:::

:::

::: {.pf-step #s1-7}

In particular,
$$
\boxed{
\abs{E(h)}
\le
\frac{h^2}{12}
\max_{t\in[x-\abs{h},x+\abs{h}]}
\abs{f^{(4)}(t)}
},
$$
so the centered approximation has error
$$
E(h)=O(h^2).
$$


::: pf-proof

Apply absolute values to the formula in step [](#s1-6){.pf-ref}.
The maximum exists because $f^{(4)}$ is continuous on the compact interval between $x-h$ and $x+h$.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} give the exact remainder formula and the resulting second-order error estimate.
If the error is defined with the opposite sign,
$$
f''(x)-D_hf(x),
$$
the formulas differ only by an overall minus sign.

:::

:::

:::
