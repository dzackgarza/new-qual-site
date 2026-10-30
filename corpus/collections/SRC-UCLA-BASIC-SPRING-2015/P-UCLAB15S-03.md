---
schema: qual/card@1
id: P-UCLAB15S-03
kind: problem
title: A Lipschitz function with vanishing forward difference quotients
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
Let $f:\RR\to\RR$ be Lipschitz.
Suppose that for every $x\in\RR$,
$$
\lim_{n\to\infty}n\left[f\left(x+\frac1n\right)-f(x)\right]=0.
$$
Prove that $f$ is differentiable.
:::

::: {.solution}

Let
$$
L\ge0
$$
be a Lipschitz constant for $f$:
$$
\abs{f(x)-f(y)}
\le
L\abs{x-y}
$$
for all $x,y\in\RR$.

::: pf

::: {.pf-step #s1-1}

Define
$$
g_n(x)
=
n\left[
f\left(x+\frac1n\right)-f(x)
\right].
$$
Then
$$
\abs{g_n(x)}\le L
$$
for every $x$ and $n$.


::: pf-proof

By the Lipschitz estimate,
$$
\abs{
f\left(x+\frac1n\right)-f(x)
}
\le
\frac Ln.
$$
Multiplying by $n$ gives
$$
\abs{g_n(x)}\le L.
$$

:::

:::

::: {.pf-step #s1-2}

For every fixed $x\in\RR$,
$$
g_n(x)\to0.
$$


::: pf-proof

This is exactly the hypothesis of the problem.

:::

:::

::: {.pf-step #s1-3}

Fix real numbers
$$
a<b.
$$
Then
$$
\int_a^b g_n(x)\,dx
\longrightarrow0.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
g_n(x)\to0
$$
pointwise on $[a,b]$ and
$$
\abs{g_n(x)}\le L.
$$
The constant function $L$ is integrable on $[a,b]$.
Therefore the dominated convergence theorem gives
$$
\int_a^b g_n(x)\,dx
\to
\int_a^b0\,dx
=0.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
\int_a^b g_n(x)\,dx
=
n
\left[
\int_b^{b+1/n}f(u)\,du
-
\int_a^{a+1/n}f(u)\,du
\right].
$$


::: pf-proof

By definition,
$$
\begin{aligned}
\int_a^b g_n(x)\,dx
&=
n\int_a^b
\left[
f\left(x+\frac1n\right)-f(x)
\right]dx\\
&=
n
\left[
\int_a^b f\left(x+\frac1n\right)dx
-
\int_a^b f(x)\,dx
\right].
\end{aligned}
$$
In the first integral, set
$$
u=x+\frac1n.
$$
Then
$$
\int_a^b f\left(x+\frac1n\right)dx
=
\int_{a+1/n}^{b+1/n}f(u)\,du.
$$
Subtracting the integral over $[a,b]$ leaves exactly the two boundary pieces in the displayed formula.

:::

:::

::: {.pf-step #s1-5}

One has
$$
n\int_b^{b+1/n}f(u)\,du
\longrightarrow
f(b).
$$


::: pf-proof

By continuity of $f$ at $b$,
$$
\sup_{u\in[b,b+1/n]}
\abs{f(u)-f(b)}
\to0.
$$
Hence
$$
\begin{aligned}
\abs{
n\int_b^{b+1/n}f(u)\,du-f(b)
}
&=
\abs{
n\int_b^{b+1/n}
\bigl(f(u)-f(b)\bigr)\,du
}\\
&\le
\sup_{u\in[b,b+1/n]}
\abs{f(u)-f(b)}
\to0.
\end{aligned}
$$
The function is continuous because every Lipschitz function is continuous.

:::

:::

::: {.pf-step #s1-6}

Likewise,
$$
n\int_a^{a+1/n}f(u)\,du
\longrightarrow
f(a).
$$


::: pf-proof

Apply the same argument as in step [](#s1-5){.pf-ref} at the point $a$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\int_a^b g_n(x)\,dx
\longrightarrow
f(b)-f(a).
$$


::: pf-proof

Use the identity in step [](#s1-4){.pf-ref} and the limits in steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

One has
$$
\boxed{f(a)=f(b)}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} says
$$
\int_a^b g_n(x)\,dx\to0,
$$
while step [](#s1-7){.pf-ref} says the same sequence of integrals converges to
$$
f(b)-f(a).
$$
Limits are unique, so
$$
f(b)-f(a)=0.
$$

:::

:::

::: pf-step

The function $f$ is constant on $\RR$.


::: pf-proof

The points
$$
a<b
$$
were arbitrary.
Step [](#s1-8){.pf-ref} therefore shows that every two real points have the same $f$-value.

:::

:::

::: {.pf-step #s1-10}

Consequently $f$ is differentiable everywhere, with
$$
\boxed{f'(x)=0}
$$
for every $x\in\RR$.


::: pf-proof

Every constant function is differentiable at every point, with derivative zero.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
