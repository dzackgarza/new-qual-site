---
schema: qual/card@1
id: P-BERK90S-01
kind: problem
title: A two-point boundary-value problem for $y''+y'-y=0$ has only the zero solution
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used the integrating factor to put the differential equation in
    self-adjoint form, then integrated its product with y and used the
    two boundary values to obtain a sum of nonnegative integrals.
---

::: {.problem}
Let $L>0$ and let $y:\RR\to\RR$ be smooth with
$$
y''+y'-y=0
$$
on $[0,L]$. Suppose
$$
y(0)=y(L)=0.
$$
Prove that $y\equiv0$ on $[0,L]$.
:::

::: {.solution}
::: pf

::: {.pf-step #self-adjoint-form}
The differential equation is equivalent on $[0,L]$ to
$$
(e^x y')'-e^x y=0.
$$

::: pf-proof
By the product rule,
$$
(e^x y')'=e^x(y''+y').
$$
Multiplying the given equation by $e^x$ therefore gives the displayed
identity.
:::

:::

::: {.pf-step #integral-identity}
One has
$$
\int_0^L e^x\bigl((y')^2+y^2\bigr)\,dx=0.
$$

::: pf-proof
Multiply the identity in step [](#self-adjoint-form){.pf-ref} by $y$ and integrate over $[0,L]$:
$$
0=\int_0^L y(e^x y')'\,dx-\int_0^L e^x y^2\,dx.
$$
Integration by parts in the first term gives
$$
0=
\left[e^x y y'\right]_0^L
-\int_0^L e^x(y')^2\,dx
-\int_0^L e^x y^2\,dx.
$$
Since $y(0)=y(L)=0$, the boundary term vanishes. Rearranging yields the
claim.
:::

:::

::: {.pf-step #y-vanishes}
The function $y$ vanishes identically on $[0,L]$.

::: pf-proof
The integrand in step [](#integral-identity){.pf-ref} is continuous and nonnegative because $e^x>0$.
Hence its integral can vanish only if
$$
e^x\bigl((y'(x))^2+y(x)^2\bigr)=0
$$
for every $x\in[0,L]$. In particular, $y(x)^2=0$ for every
$x\in[0,L]$, so $y\equiv0$ there.
:::

:::

::: pf-qed
Step [](#y-vanishes){.pf-ref} is the required conclusion.
:::

:::
:::
