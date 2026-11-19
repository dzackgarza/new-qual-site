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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subsections suffice, and the 12
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    mathematics was re-checked: $P=x+y^3$ and $Q=e^y+3xy^2$ have the potential $f=x^2/2+xy^3+e^y$, whose
    two partial derivatives are $P$ and $Q$, and along a parameterized curve the integrand is the
    derivative of $f\circ r$, so the fundamental theorem of calculus reduces the integral to the values at
    the endpoints. Checked against the statement on the card, from the UGA Fall 2012 preliminary exam.
    Nothing in the statement was changed.

---

::: {.problem}
Prove that the line integral $\displaystyle\int_C (x+y^3)\,dx + (e^y+3xy^2)\,dy$ is path-independent; i.e., it depends only on the endpoints of $C$.
:::

::: {.solution}
**Goal:** Prove that the vector field $\mathbf{F}(x, y) = (x + y^3)\mathbf{i} + (e^y + 3xy^2)\mathbf{j}$ is conservative on $\RR^2$ by explicitly finding a scalar potential function $f(x, y)$, thereby establishing path-independence.

::: pf

::: pf-step

Construction of a potential function $f(x, y)$:
*Proof:*

::: pf-proof

::: pf-step

Let $P(x, y) = x + y^3$ and $Q(x, y) = e^y + 3xy^2$ be the components of the 1-form $\omega = P\,dx + Q\,dy$.


::: pf-proof
These are the coefficient functions of the differential form.
:::

:::

::: pf-step

We seek a $C^1$ function $f(x, y)$ on $\RR^2$ such that $\nabla f = (P, Q)$, which requires:
$$\frac{\partial f}{\partial x} = x + y^3, \qquad \frac{\partial f}{\partial y} = e^y + 3xy^2.$$


::: pf-proof
A potential would make the integral a difference of the values of $f$ at the endpoints.
:::

:::

::: pf-step

Integrating $\frac{\partial f}{\partial x} = x + y^3$ with respect to $x$ while holding $y$ constant yields
$$f(x, y) = \int (x + y^3)\,dx = \frac{1}{2}x^2 + xy^3 + g(y),$$
where $g(y)$ is an arbitrary differentiable function of $y$.


::: pf-proof
Integrating in $x$ treats $y$ as a constant, so the constant of integration may depend on $y$.
:::

:::

::: pf-step

Differentiating this expression with respect to $y$:
$$\frac{\partial f}{\partial y} = 3xy^2 + g'(y).$$


::: pf-proof
Differentiating the expression term by term, with $g$ the only part depending on $y$ alone.
:::

:::

::: pf-step

Setting $\frac{\partial f}{\partial y} = Q(x, y) = e^y + 3xy^2$ gives $3xy^2 + g'(y) = e^y + 3xy^2$, so $g'(y) = e^y$.


::: pf-proof
The two coefficients of $y$ must agree, which isolates $g'$.
:::

:::

::: pf-step

Integrating with respect to $y$ gives $g(y) = e^y + C$. Setting $C = 0$ yields the potential function
$$f(x, y) = \frac{1}{2}x^2 + xy^3 + e^y.$$


::: pf-proof
The terms $3xy^2$ cancel, integrating $e^y$ gives $e^y$, and the additive constant may be taken to be $0$.
:::

:::

::: pf-step

Direct verification: $\frac{\partial f}{\partial x} = x + y^3 = P(x, y)$ and $\frac{\partial f}{\partial y} = 3xy^2 + e^y = Q(x, y)$, so $\nabla f = (P, Q)$ on all of $\RR^2$.


::: pf-proof
Differentiating the resulting $f$ in each variable returns $P$ and $Q$.
:::

:::

:::

:::

::: pf-step

Path-independence via the Fundamental Theorem for Line Integrals:
*Proof:*

::: pf-proof

::: pf-step

Let $C$ be any piecewise smooth curve in $\RR^2$ parameterized by $\mathbf{r}(t) = (x(t), y(t))$ for $a \le t \le b$, with initial point $A = \mathbf{r}(a)$ and terminal point $B = \mathbf{r}(b)$.


::: pf-proof
This is arbitrary data: a piecewise smooth curve with a parameterization.
:::

:::

::: pf-step

By the chain rule:
$$\int_C (x + y^3)\,dx + (e^y + 3xy^2)\,dy = \int_a^b \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt = \int_a^b \frac{d}{dt}[f(\mathbf{r}(t))]\,dt.$$


::: pf-proof
The integrand is the derivative of the composite $f\circ r$ along the curve, by the chain rule.
:::

:::

::: pf-step

By the Fundamental Theorem of Calculus:
$$\int_C (x + y^3)\,dx + (e^y + 3xy^2)\,dy = f(\mathbf{r}(b)) - f(\mathbf{r}(a)) = f(B) - f(A).$$


::: pf-proof
This is the fundamental theorem of calculus for the $C^1$ function $t\mapsto f(r(t))$.
:::

:::

::: pf-step

The value of the line integral depends solely on the endpoints $A$ and $B$, and is completely independent of the path $C$ connecting them.


::: pf-proof
The expression involves only the values of $f$ at the two endpoints of the curve.
:::

:::

:::

:::

::: pf-step

Conclusion:


::: pf-proof
A potential exists, so the integral depends only on the endpoints.
:::

:::

:::

*Proof:*
The line integral is path-independent.
:::
