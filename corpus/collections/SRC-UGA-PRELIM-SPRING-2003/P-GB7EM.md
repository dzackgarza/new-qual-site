---
schema: qual/card@1
id: P-GB7EM
kind: problem
title: Differentiability in $\mathbb{R}^n$, and $xy/(x^2+y^2)$ is not differentiable
  at the origin
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Differentiation
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
a. Let $f$ be a real-valued function defined on $\mathbb{R}^n$.
Define differentiability of $f$ at a point $p$.
b. Show that the function $f: \mathbb{R}^2 \to \mathbb{R}$ defined by $$f(x,y) = \frac{xy}{x^2+y^2} \text{ for } (x,y) \neq (0,0), \text{ and } f(0,0) = 0$$ is not differentiable at $(0,0)$.
:::

::: {.solution}
<1>1. Part (a): Definition of differentiability:
<2>1. A function $f: \mathbb{R}^n \to \mathbb{R}$ is differentiable at a point $p \in \mathbb{R}^n$ if there exists a linear transformation $L: \mathbb{R}^n \to \mathbb{R}$ (or equivalently a gradient vector $\nabla f(p) \in \mathbb{R}^n$ such that $L(h) = \langle \nabla f(p), h \rangle$) satisfying:
\[
\lim_{h \to 0} \frac{|f(p + h) - f(p) - L(h)|}{\|h\|} = 0.
\]
Equivalently, $f(p + h) = f(p) + L(h) + o(\|h\|)$ as $\|h\| \to 0$.
Proof: standard definition of Fréchet differentiability on $\mathbb{R}^n$.

<1>2. Part (b): Non-differentiability of $f(x, y)$ at $(0, 0)$:
<2>1. If a function $f$ is differentiable at $p$, then $f$ is continuous at $p$.
Proof: $|f(p+h) - f(p)| \le |L(h)| + o(\|h\|) \le \|L\| \|h\| + o(\|h\|) \to 0$ as $h \to 0$.
<2>2. We evaluate the limit of $f(x, y) = \frac{xy}{x^2 + y^2}$ as $(x, y) \to (0, 0)$ along lines $y = mx$:
For $x \neq 0$:
\[
f(x, mx) = \frac{x(mx)}{x^2 + (mx)^2} = \frac{m x^2}{x^2(1 + m^2)} = \frac{m}{1 + m^2}.
\]
Proof: algebraic substitution $y = mx$.
<2>3. Along the line $y = 0$ ($m = 0$), $\lim_{x \to 0} f(x, 0) = 0$.
Along the line $y = x$ ($m = 1$), $\lim_{x \to 0} f(x, x) = \frac{1}{1 + 1^2} = \frac{1}{2} \neq f(0, 0)$.
Since the limit depends on the path of approach, $\lim_{(x, y) \to (0, 0)} f(x, y)$ does not exist.
Thus $f$ is discontinuous at $(0, 0)$.
Proof: non-uniqueness of directional limits.
<2>4. Since $f$ is not continuous at $(0, 0)$, by <2>1 $f$ cannot be differentiable at $(0, 0)$.
Proof: contrapositive of differentiability implies continuity.

<1>3. Conclusion:
$f$ is defined to be differentiable if its linear approximation error is $o(\|h\|)$, and $f(x, y) = \frac{xy}{x^2+y^2}$ is not differentiable at $(0, 0)$ due to discontinuity. Q.E.D.
Proof: <1>1 and <1>2.
:::
