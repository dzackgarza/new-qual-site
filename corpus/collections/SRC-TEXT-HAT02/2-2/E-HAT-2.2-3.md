---
schema: qual/card@1
id: E-HAT-2.2-3
kind: exercise
title: Degree zero map has fixed and antipodal points; Hairy Ball Theorem
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Point Theorems
  - Vector Fields
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Let $f: S^n \to S^n$ be a map of degree zero.
Show that there exist points $x, y \in S^n$ with $f(x) = x$ and $f(y) = -y$.
Use this to show that if $F$ is a continuous vector field defined on the unit ball $D^n$ in $\mathbb{R}^n$ such that $F(x) \neq 0$ for all $x$, then there exists a point on $\partial D^n$ where $F$ points radially outward and another point on $\partial D^n$ where $F$ points radially inward.

::: {.solution}
<1>1. Existence of a fixed point ($f(x) = x$): <2>1. Suppose for contradiction that $f(x) \neq x$ for all $x \in S^n$.
Then $f(x)$ is never antipodal to $-x$, so $(1 - t)f(x) - tx \neq 0$ for all $t \in [0, 1]$ and $x \in S^n$.
::: {.proof}
if $(1-t)f(x) - tx = 0$, taking norms gives $1-t = t \implies t = 1/2$, so $f(x) = x$, contradiction.
:::
<2>2. Define the straight-line homotopy $H: S^n \times [0, 1] \to S^n$ by:
\[
H(x, t) = \frac{(1 - t)f(x) - tx}{\|(1 - t)f(x) - tx\|}.
\]
$H$ is a homotopy from $f$ to the antipodal map $a(x) = -x$.
::: {.proof}
$H(x, 0) = f(x)$ and $H(x, 1) = -x$.
:::
<2>3. Because homotopic maps have the same degree:
\[
\deg(f) = \deg(a) = (-1)^{n+1} \neq 0.
\]
This contradicts $\deg(f) = 0$.
Thus there exists $x \in S^n$ such that $f(x) = x$.
::: {.proof}
degree of antipodal map on $S^n$.
:::

<1>2. Existence of an antipodal point ($f(y) = -y$): <2>1. Suppose for contradiction that $f(y) \neq -y$ for all $y \in S^n$.
Then $(1 - t)f(y) + ty \neq 0$ for all $t \in [0, 1]$ and $y \in S^n$.
::: {.proof}
identical norm argument.
:::
<2>2. Define the straight-line homotopy $G: S^n \times [0, 1] \to S^n$ by:
\[
G(y, t) = \frac{(1 - t)f(y) + ty}{\|(1 - t)f(y) + ty\|}.
\]
$G$ is a homotopy from $f$ to the identity map $\operatorname{id}_{S^n}$.
::: {.proof}
$G(y, 0) = f(y)$ and $G(y, 1) = y$.
:::
<2>3. Thus $\deg(f) = \deg(\operatorname{id}_{S^n}) = 1$, contradicting $\deg(f) = 0$.
Therefore there exists $y \in S^n$ such that $f(y) = -y$.
::: {.proof}
degree of identity map on $S^n$.
:::

<1>3. Application to continuous non-vanishing vector fields on $D^n$: <2>1. Let $F: D^n \to \mathbb{R}^n \setminus \{0\}$ be continuous.
Define the normalized map $\widetilde{F}: D^n \to S^{n-1}$ by $\widetilde{F}(z) = \frac{F(z)}{\|F(z)\|}$, and let $g = \widetilde{F}|_{\partial D^n}: S^{n-1} \to S^{n-1}$.
::: {.proof}
$F(z) \neq 0$ ensures $\widetilde{F}$ is well-defined and continuous.
:::
<2>2. Since $g$ extends to the contractible disk $D^n$ via $\widetilde{F}$, $g$ is null-homotopic, so $\deg(g) = 0$.
::: {.proof}
maps extending to a contractible space are null-homotopic.
:::
<2>3. Applying <1>1 and <1>2 to $g: S^{n-1} \to S^{n-1}$:

- There exists $x \in S^{n-1} = \partial D^n$ with $g(x) = x \implies F(x) = \|F(x)\| x$, so $F$ points radially outward at $x$.

- There exists $y \in S^{n-1} = \partial D^n$ with $g(y) = -y \implies F(y) = -\|F(y)\| y$, so $F$ points radially inward at $y$.
  ::: {.proof}
  <1>1 and <1>2 applied to $S^{n-1}$.
  :::

<1>4. Conclusion: Degree zero maps have fixed and antipodal points, which implies every non-vanishing vector field on $D^n$ has points on $\partial D^n$ pointing radially outward and inward.
::: {.proof}
<1>1 through <1>3.
:::
Q.E.D.
:::
