---
schema: qual/card@1
id: P-UCLAB14S-05
kind: problem
title: Nonuniqueness of least-squares minimizers
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
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Suppose that $V$ is a finite-dimensional real inner-product space with inner product $(\cdot,\cdot)$, that $L\in\operatorname{Hom}(V,V)$, and that $b\in V$ is fixed.
Suppose that $u,v\in V$ both minimize
$$
D(x)=\norm{ L(x)-b}.
$$
Show that $u-v\in\ker L$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
y=L(u)-b,
\qquad
z=L(v)-b.
$$
Since $u$ and $v$ are both minimizers, there is a number $m\geq0$ such that
$$
\norm{y}=\norm{z}=m.
$$


::: pf-proof

By definition, $D(u)=\norm{L(u)-b}=\norm{y}$ and $D(v)=\norm{L(v)-b}=\norm{z}$. Both equal the minimum value of $D$.

:::

:::

::: {.pf-step #s1-2}

The midpoint
$$
w=\frac{u+v}{2}
$$
satisfies
$$
L(w)-b=\frac{y+z}{2}.
$$


::: pf-proof

Linearity of $L$ gives
$$
L(w)-b
=\frac{L(u)+L(v)}2-b
=\frac{(L(u)-b)+(L(v)-b)}2
=\frac{y+z}{2}.
$$

:::

:::

::: {.pf-step #s1-3}

Since $u$ is a minimizer,
$$
m\leq D(w)=\norm{\frac{y+z}{2}}.
$$


::: pf-proof

The minimum value of $D$ is $m$ by step [](#s1-1){.pf-ref}, so $D(x)\geq m$ for every $x\in V$, in particular for $x=w$. Step [](#s1-2){.pf-ref} gives the displayed expression.

:::

:::

::: {.pf-step #s1-4}

The triangle inequality gives the reverse bound
$$
\norm{\frac{y+z}{2}}
\leq\frac{\norm{y}+\norm{z}}{2}=m.
$$


::: pf-proof

Apply homogeneity and the triangle inequality, then use $\norm{y}=\norm{z}=m$ from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\norm{\frac{y+z}{2}}=m.
$$


::: pf-proof

Combine the lower bound in step [](#s1-3){.pf-ref} with the upper bound in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

The parallelogram identity implies
$$
\norm{y-z}^2=0.
$$


::: pf-proof

The parallelogram identity is
$$
\norm{y+z}^2+\norm{y-z}^2
=2\norm{y}^2+2\norm{z}^2.
$$
By step [](#s1-5){.pf-ref}, $\norm{y+z}=2m$, while step [](#s1-1){.pf-ref} gives $\norm{y}=\norm{z}=m$. Therefore
$$
4m^2+\norm{y-z}^2=4m^2,
$$
so $\norm{y-z}^2=0$.

:::

:::

::: {.pf-step #s1-7}

Thus
$$
y=z,
$$
and consequently
$$
L(u-v)=0.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} gives $y-z=0$. By the definitions in step [](#s1-1){.pf-ref},
$$
y-z=(L(u)-b)-(L(v)-b)=L(u)-L(v)=L(u-v).
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{u-v\in\ker L.}
$$


::: pf-proof

This is exactly the statement $L(u-v)=0$ from step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} proves the claim.

:::

:::

:::
