---
schema: qual/card@1
id: E-3OJLH
kind: problem
title: $\abs{f(z)+f(-z)}\le2\abs z^2$ for a holomorphic self-map of $\DD$ fixing $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.exercise}
Suppose $f:\DD\to \DD$ is holomorphic and $f(0)=0$.
Show that
$$
\abs{f(z)+f(-z)}\le 2\abs z^2
\qquad(z\in\DD).
$$
If equality holds at some $z_0\neq0$, show that
$$
f(z)=\lambda z^2
$$
for some $\abs\lambda=1$.
:::

::: {.solution}
Let $g(z)=f(z)/z$ for $z\ne0$ and $g(0)=f'(0)$, and let
$$
h(z)=\frac{g(z)-g(-z)}2,\qquad e(z)=\frac{g(z)+g(-z)}2.
$$

::: pf

::: {.pf-step #g-bound}
$g$ and $h$ are holomorphic on $\DD$, $\abs g\le1$, and $\abs{h(z)}\le\abs z$.

::: pf-proof
By the Schwarz lemma $\abs{f(z)}\le\abs z$, so $g$ is holomorphic with $\abs g\le1$.
Then $h$ is holomorphic, $\abs h\le1$, and $h(0)=0$, so the Schwarz lemma gives $\abs{h(z)}\le\abs z$.
:::

:::

::: {.pf-step #inequality}
$\abs{f(z)+f(-z)}\le 2\abs z^2$ for $z\in\DD$.

::: pf-proof
$f(z)+f(-z)=z\bigl(g(z)-g(-z)\bigr)=2zh(z)$, and step [](#g-bound){.pf-ref} bounds $\abs{h(z)}$ by $\abs z$.
:::

:::

::: pf-step
If equality holds at some $z_0\ne0$, then $f(z)=\lambda z^2$ with $\abs\lambda=1$.

::: pf-proof

::: {.pf-step #h-rotation}
$h(z)=\lambda z$ for some $\abs\lambda=1$.

::: pf-proof
By the identity in step [](#inequality){.pf-ref}, equality at $z_0$ means $\abs{h(z_0)}=\abs{z_0}$, and the equality case of the Schwarz lemma applies.
:::

:::

::: {.pf-step #e-zero}
$e\equiv0$.

::: pf-proof
By step [](#h-rotation){.pf-ref}, $g(z)=e(z)+\lambda z$ and $g(-z)=e(z)-\lambda z$.
The parallelogram identity and $\abs g\le1$ give
$$
2\abs{e(z)}^2+2\abs{z}^2=\abs{g(z)}^2+\abs{g(-z)}^2\le2,
$$
so $\abs{e(z)}\le\sqrt{1-\abs z^2}$.
By the maximum modulus principle $\abs e\le\sqrt{1-r^2}$ on $\abs z\le r$ for each $r<1$, and letting $r\to1$ gives $e\equiv0$.
:::

:::

::: pf-step
$f(z)=\lambda z^2$.

::: pf-proof
By steps [](#h-rotation){.pf-ref} and [](#e-zero){.pf-ref}, $g=e+h=\lambda z$, so $f(z)=zg(z)=\lambda z^2$.
:::

:::

:::

:::

:::

:::
