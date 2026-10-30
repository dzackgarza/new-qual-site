---
schema: qual/card@1
id: P-CHAVAN-CA-3-6
kind: problem
title: A unique real solution of $\lambda=z+e^{-z}$ in the right half-plane
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $\lambda>1$.
Show that the equation
$$
\lambda=z+e^{-z}
$$
has exactly one solution in the right half-plane, and that this solution is real.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every solution with $\operatorname{Re}z>0$ is real.


::: pf-proof

Write
$$
z=x+iy,
\qquad
x>0.
$$
Then
$$
e^{-z}=e^{-x}(\cos y-i\sin y).
$$
Since $\lambda$ is real, taking imaginary parts in
$\lambda=z+e^{-z}$ gives
$$
y-e^{-x}\sin y=0,
$$
or
$$
y=e^{-x}\sin y.
$$
If $y\ne0$, then
$$
\abs{y}
=e^{-x}\abs{\sin y}
\le\abs{\sin y}
<\abs{y},
$$
where the first inequality uses $e^{-x}<1$ and the strict inequality uses
$\abs{\sin y}<\abs{y}$ for $y\ne0$. This is impossible. Hence $y=0$, so every
solution in the right half-plane is real.

:::

:::

::: {.pf-step #s1-2}

The real function
$$
h(x)=x+e^{-x}
$$
is strictly increasing on $(0,\infty)$, satisfies
$$
\lim_{x\downarrow0}h(x)=1,
\qquad
\lim_{x\to\infty}h(x)=\infty.
$$


::: pf-proof

For $x>0$,
$$
h'(x)=1-e^{-x}>0,
$$
so $h$ is strictly increasing. The two limits follow directly from
the definition of $h$.

:::

:::

::: {.pf-step #s1-3}

There is a unique $x_\lambda>0$ such that
$$
h(x_\lambda)=\lambda.
$$


::: pf-proof

Since $\lambda>1$, step [](#s1-2){.pf-ref} and the intermediate value theorem give
an $x_\lambda>0$ with $h(x_\lambda)=\lambda$. Strict monotonicity in
step [](#s1-2){.pf-ref} makes this $x_\lambda$ unique.

:::

:::

::: {.pf-step #s1-4}

The equation $\lambda=z+e^{-z}$ has exactly one solution in the right half-plane, namely the real number
$$
\boxed{z=x_\lambda}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives one positive real solution, hence one solution in the
right half-plane. Step [](#s1-1){.pf-ref} shows that every solution in that
half-plane is real, and step [](#s1-3){.pf-ref} shows that the real solution is
unique.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives both the uniqueness and the reality of the required
solution.

:::

:::

:::
