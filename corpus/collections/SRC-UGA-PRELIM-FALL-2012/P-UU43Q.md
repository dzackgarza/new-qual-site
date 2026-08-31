---
schema: qual/card@1
id: P-UU43Q
kind: problem
title: Path-independence of $\int_C (x+y^3)\,dx+(e^y+3xy^2)\,dy$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Prove that the line integral $\displaystyle\int_C (x+y^3)\,dx + (e^y+3xy^2)\,dy$ is path-independent; i.e., it depends only on the endpoints of $C$.
:::

::: solution
**Goal:** Prove that the vector field $\mathbf{F}(x, y) = (x + y^3)\mathbf{i} + (e^y + 3xy^2)\mathbf{j}$ is conservative on $\mathbb{R}^2$ by explicitly finding a scalar potential function $f(x, y)$, thereby establishing path-independence.

<1>1. Construction of a potential function $f(x, y)$:
    *Proof:*
    <2>1. Let $P(x, y) = x + y^3$ and $Q(x, y) = e^y + 3xy^2$ be the components of the 1-form $\omega = P\,dx + Q\,dy$.
    <2>2. We seek a $C^1$ function $f(x, y)$ on $\mathbb{R}^2$ such that $\nabla f = (P, Q)$, which requires:
    $$\frac{\partial f}{\partial x} = x + y^3, \qquad \frac{\partial f}{\partial y} = e^y + 3xy^2.$$
    <2>3. Integrating $\frac{\partial f}{\partial x} = x + y^3$ with respect to $x$ while holding $y$ constant yields
    $$f(x, y) = \int (x + y^3)\,dx = \frac{1}{2}x^2 + xy^3 + g(y),$$
    where $g(y)$ is an arbitrary differentiable function of $y$.
    <2>4. Differentiating this expression with respect to $y$:
    $$\frac{\partial f}{\partial y} = 3xy^2 + g'(y).$$
    <2>5. Setting $\frac{\partial f}{\partial y} = Q(x, y) = e^y + 3xy^2$ gives $3xy^2 + g'(y) = e^y + 3xy^2$, so $g'(y) = e^y$.
    <2>6. Integrating with respect to $y$ gives $g(y) = e^y + C$. Setting $C = 0$ yields the potential function
    $$f(x, y) = \frac{1}{2}x^2 + xy^3 + e^y.$$
    <2>7. Direct verification: $\frac{\partial f}{\partial x} = x + y^3 = P(x, y)$ and $\frac{\partial f}{\partial y} = 3xy^2 + e^y = Q(x, y)$, so $\nabla f = (P, Q)$ on all of $\mathbb{R}^2$.

<1>2. Path-independence via the Fundamental Theorem for Line Integrals:
    *Proof:*
    <2>1. Let $C$ be any piecewise smooth curve in $\mathbb{R}^2$ parameterized by $\mathbf{r}(t) = (x(t), y(t))$ for $a \le t \le b$, with initial point $A = \mathbf{r}(a)$ and terminal point $B = \mathbf{r}(b)$.
    <2>2. By the chain rule:
    $$\int_C (x + y^3)\,dx + (e^y + 3xy^2)\,dy = \int_a^b \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_a^b \frac{d}{dt}[f(\mathbf{r}(t))]\,dt.$$
    <2>3. By the Fundamental Theorem of Calculus:
    $$\int_C (x + y^3)\,dx + (e^y + 3xy^2)\,dy = f(\mathbf{r}(b)) - f(\mathbf{r}(a)) = f(B) - f(A).$$
    <2>4. The value of the line integral depends solely on the endpoints $A$ and $B$, and is completely independent of the path $C$ connecting them.

<1>3. Conclusion:
    *Proof:*
    The line integral is path-independent.
:::
