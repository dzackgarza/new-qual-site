---
schema: qual/card@1
id: E-HAT-2.2-3
kind: problem
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.2, Exercise 3.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both halves: $f(x)\ne x$ gives a homotopy from $f$ to the antipodal map and $f(x)\ne -x$
    one to the identity, each contradicting $\deg f=0$; the norm computation
    $(1-t)\norm{f(x)}=t\norm{x}$ forces $t=1/2$ and then $f(x)=x$; and the vector-field part
    normalizes $F$ on $D^n$, its boundary restriction is null-homotopic and so of degree zero on
    $S^{n-1}$, and the two halves give the outward and inward points.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, §2.2 Exercise 3, printed p. 155: the printed statement matches the card
    word for word, including "F(x) != 0 for all x" and both outward and inward points on the
    boundary. Checked: the norm computation (1-t)norm(f(x)) = t norm(x) forces t = 1/2 and then
    f(x) = x in the first half and f(y) = -y in the second, so both straight-line homotopies are
    defined; degree is defined only for n > 0, so n >= 1 throughout, as the exercise's hypothesis
    presupposes. The four degree properties cited are exactly (a), (b), (c) and (f) on printed
    p. 134. The boundary map g = F-tilde restricted to the boundary is homotopic to a constant,
    hence of degree zero for n >= 2, and the card's separate paragraph for n = 1 is correct: a
    continuous nonvanishing F on an interval has one sign throughout, giving outward at one
    endpoint and inward at the other, where no degree argument is available. No defect.
---

::: {.problem}
Let $f: S^n \to S^n$ be a map of degree zero.
Show that there exist points $x, y \in S^n$ with $f(x) = x$ and $f(y) = -y$.
Use this to show that if $F$ is a continuous vector field defined on the unit ball $D^n$ in $\RR^n$ such that $F(x) \neq 0$ for all $x$, then there exists a point on $\partial D^n$ where $F$ points radially outward and another point on $\partial D^n$ where $F$ points radially inward.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
Existence of a fixed point ($f(x) = x$):

::: pf-proof

::: pf-step
Suppose $f(x) \neq x$ for all $x \in S^n$.
Then $(1 - t)f(x) - tx \neq 0$ for all $t \in [0, 1]$ and $x \in S^n$.

::: pf-proof
If $(1-t)f(x) - tx = 0$, taking norms and using $\norm{f(x)} = \norm{x} = 1$ gives $1-t = t$, so $t = 1/2$ and then $f(x) = x$, contrary to hypothesis.
:::

:::

::: pf-step
Define the straight-line homotopy $H: S^n \times [0, 1] \to S^n$ by:
$$
H(x, t) = \frac{(1 - t)f(x) - tx}{\norm{(1 - t)f(x) - tx}}.
$$
$H$ is a homotopy from $f$ to the antipodal map $a(x) = -x$.

::: pf-proof
$H(x, 0) = f(x)$ and $H(x, 1) = -x$.
:::

:::

::: pf-step
Because homotopic maps have the same degree:
$$
\deg(f) = \deg(a) = (-1)^{n+1} \neq 0.
$$
This contradicts $\deg(f) = 0$.
Thus there exists $x \in S^n$ such that $f(x) = x$.

::: pf-proof
Property (c) of degree (Hatcher p. 134) gives $\deg f = \deg a$ for homotopic maps, and property (f) (p. 134) gives $\deg(-11) = (-1)^{n+1}$ for the antipodal map, which is nonzero.
:::

:::

:::

:::

::: {.pf-step #s2}
Existence of an antipodal point ($f(y) = -y$):

::: pf-proof

::: pf-step
Suppose for contradiction that $f(y) \neq -y$ for all $y \in S^n$.
Then $(1 - t)f(y) + ty \neq 0$ for all $t \in [0, 1]$ and $y \in S^n$.

::: pf-proof
identical norm argument.
:::

:::

::: pf-step
Define the straight-line homotopy $G: S^n \times [0, 1] \to S^n$ by:
$$
G(y, t) = \frac{(1 - t)f(y) + ty}{\norm{(1 - t)f(y) + ty}}.
$$
$G$ is a homotopy from $f$ to the identity map $\operatorname{id}_{S^n}$.

::: pf-proof
$G(y, 0) = f(y)$ and $G(y, 1) = y$.
:::

:::

::: pf-step
Thus $\deg(f) = \deg(\operatorname{id}_{S^n}) = 1$, contradicting $\deg(f) = 0$.
Therefore there exists $y \in S^n$ such that $f(y) = -y$.

::: pf-proof
Property (a) of degree (Hatcher p. 134) gives $\deg 11 = 1$, and property (c) (p. 134) transports it along the homotopy $G$ to $\deg f$.
:::

:::

:::

:::

::: {.pf-step #s3}
Application to continuous non-vanishing vector fields on $D^n$:

::: pf-proof

::: pf-step
Let $F: D^n \to \RR^n \setminus \{0\}$ be continuous.
Define the normalized map $\widetilde{F}: D^n \to S^{n-1}$ by $\widetilde{F}(z) = \frac{F(z)}{\norm{F(z)}}$, and let $g = \widetilde{F}\restrict_{\partial D^n}: S^{n-1} \to S^{n-1}$.

::: pf-proof
$F(z) \neq 0$ ensures $\widetilde{F}$ is well-defined and continuous.
:::

:::

::: pf-step
Since $g$ extends over $D^n$ via $\widetilde{F}$, the formula $H(x, t) = \widetilde{F}((1-t)x)$ is defined for $(1-t)x \in D^n$ and gives a homotopy from $g$ to the constant map at $\widetilde{F}(0)$, so $\deg(g) = 0$.

::: pf-proof
For $n-1 \ge 1$ a constant map of $S^{n-1}$ is not surjective, so it has degree $0$ by property (b) of degree (Hatcher p. 134), and property (c) (p. 134) gives $\deg g = 0$.
:::

:::

::: pf-step
Applying steps [](#s1){.pf-ref} and [](#s2){.pf-ref} to $g: S^{n-1} \to S^{n-1}$:

- There exists $x \in S^{n-1} = \partial D^n$ with $g(x) = x \implies F(x) = \norm{F(x)} x$, so $F$ points radially outward at $x$.

- There exists $y \in S^{n-1} = \partial D^n$ with $g(y) = -y \implies F(y) = -\norm{F(y)} y$, so $F$ points radially inward at $y$.

::: pf-proof
Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} applied to $S^{n-1}$, which is $S^m$ with $m = n-1 \ge 1$; for $n = 1$ the boundary is $S^0 = \{\pm1\}$, a continuous nonvanishing $F$ on the interval $D^1$ has one sign throughout, and at the two endpoints that sign points outward at one of them and inward at the other.
:::

:::

:::

:::

::: pf-step
Conclusion: Degree zero maps have fixed and antipodal points, which implies every non-vanishing vector field on $D^n$ has points on $\partial D^n$ pointing radially outward and inward.

::: pf-proof
Steps [](#s1){.pf-ref} through [](#s3){.pf-ref}.
:::

:::

:::

:::
