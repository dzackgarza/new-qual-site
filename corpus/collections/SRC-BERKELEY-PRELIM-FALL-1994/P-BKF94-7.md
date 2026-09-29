---
schema: qual/card@1
id: P-BKF94-7
kind: problem
title: An injective curve contained in a level set
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Split into the constant case and the nonconstant case; in the latter a
    nonzero gradient point exists, and the implicit function theorem gives an
    injectively parametrized local level-set arc.
---

::: {.problem}
Let $f:\mathbb R^2\to\mathbb R$ be continuously differentiable. Prove that there exists a continuous one-to-one map $g:[0,1]\to\mathbb R^2$ such that $f\circ g$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $f$ is constant, then the required map exists.

::: pf-proof

Define
$$
g(t)=(t,0),
\qquad
0\leq t\leq1.
$$
This map is continuous and one-to-one, and $f\circ g$ is constant because
$f$ is constant.

:::

:::

::: {.pf-step #s2}

If $f$ is nonconstant, then there is a point
$$
p\in\RR^2
$$
with
$$
\nabla f(p)\neq0.
$$

::: pf-proof

Suppose instead that $\nabla f=0$ everywhere. For any $x,y\in\RR^2$,
consider
$$
\gamma(t)=x+t(y-x),
\qquad
0\leq t\leq1.
$$
The chain rule gives
$$
\frac d{dt}f(\gamma(t))
=
\nabla f(\gamma(t))\cdot(y-x)
=0.
$$
Thus
$$
f(x)=f(y).
$$
Since $x$ and $y$ were arbitrary, $f$ would be constant, contrary to the
present assumption.

:::

:::

::: {.pf-step #s3}

If $f$ is nonconstant, then some level set of $f$ contains the graph
of a continuously differentiable function over a nondegenerate interval.

::: pf-proof

Choose $p=(p_1,p_2)$ as in step [](#s2){.pf-ref}. At least one partial derivative of
$f$ is nonzero at $p$. Interchanging the two coordinates if necessary,
assume
$$
\frac{\partial f}{\partial y}(p)\neq0.
$$
Set
$$
c\coloneqq f(p).
$$
By the implicit function theorem, there are $\varepsilon>0$ and a
continuously differentiable function
$$
\varphi:(p_1-\varepsilon,p_1+\varepsilon)\longrightarrow\RR
$$
such that
$$
f(x,\varphi(x))=c
$$
for every $x$ in that interval.

:::

:::

::: {.pf-step #s4}

In the nonconstant case there is a continuous one-to-one map
$$
g:[0,1]\longrightarrow\RR^2
$$
such that $f\circ g$ is constant.

::: pf-proof

Use the interval and function from step [](#s3){.pf-ref} and choose
$$
0<\delta<\varepsilon.
$$
Define
$$
x(t)=p_1-\delta+2\delta t
$$
and
$$
g(t)=\bigl(x(t),\varphi(x(t))\bigr).
$$
The map $g$ is continuous. Its first coordinate $x(t)$ is strictly
increasing, so $g$ is one-to-one. By step [](#s3){.pf-ref},
$$
f(g(t))=c
$$
for every $t\in[0,1]$.

:::

:::

::: {.pf-step #s5}

The required map exists for every continuously differentiable
$f:\RR^2\to\RR$.

::: pf-proof

Step [](#s1){.pf-ref} handles the constant case and step [](#s4){.pf-ref} handles the nonconstant
case.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves the claim.

:::

:::

:::
