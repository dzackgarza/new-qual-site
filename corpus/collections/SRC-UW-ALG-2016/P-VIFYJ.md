---
schema: qual/card@1
id: P-VIFYJ
kind: problem
title: $\CC[x,y]/(y^2-(x-1)^3-(x-1)^2)$ is a domain, its real points, and its integral
  closure
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $A = \CC[x,y]/(y^2-(x-1)^3 - (x-1)^2)$.

- Show that $A$ is an integral domain and sketch the $\RR$-points of $\text{Spec} A$.

- Find the integral closure of $A$.
  Recall that for an integral domain $A$ with fraction field $K$, the integral closure of $A$ in $K$ is the set of all elements of $K$ integral over $A$.
:::

::: {.solution}
<1>1. Proof that $A$ is an integral domain:
<2>1. The defining relation is $f(x, y) = y^2 - (x-1)^3 - (x-1)^2 = y^2 - x(x-1)^2$.
View $f(x, y)$ as a monic polynomial of degree 2 in $y$ over the UFD $R = \mathbb{C}[x]$:
\[
f(x, y) = y^2 - x(x-1)^2 \in R[y].
\]
<2>2. The polynomial $f(x, y)$ is irreducible in $\mathbb{C}(x)[y]$ if and only if $x(x-1)^2$ is not a square in $\mathbb{C}(x)$.
Since $x$ has odd multiplicity $1$ in $\mathbb{C}[x]$, $\sqrt{x(x-1)^2} = (x-1)\sqrt{x} \notin \mathbb{C}(x)$.
Because $f$ is monic in $y$, Gauss's Lemma implies $f(x, y)$ is irreducible in $\mathbb{C}[x, y]$.
<2>3. Since $\mathbb{C}[x, y]$ is a commutative ring and $f(x, y)$ is irreducible, the principal ideal $\langle f(x, y) \rangle$ is prime.
Therefore $A = \mathbb{C}[x, y]/\langle f(x, y) \rangle$ is an integral domain.

<1>2. Description of the real points of $\operatorname{Spec}(A)$:
<2>1. The real locus consists of all $(x, y) \in \mathbb{R}^2$ satisfying $y^2 = x(x-1)^2$.
Since $y^2 \ge 0$ and $(x-1)^2 \ge 0$, real solutions exist if and only if $x \ge 0$.
<2>2. Geometric features of the curve $y = \pm (x-1)\sqrt{x}$:
- At $x = 0$, $y = 0$, forming a smooth endpoint with vertical tangent ($x \sim y^2$).
- For $0 < x < 1$, the curve splits into two branches $y = \pm (1-x)\sqrt{x}$, forming a closed loop bounded between $x = 0$ and $x = 1$.
- At $(1, 0)$, the loop crosses itself: the two branches have tangents $y \approx \pm(x-1)$, creating an ordinary double point (node).
- For $x > 1$, the two branches $y = \pm (x-1)\sqrt{x}$ extend to infinity.

<1>3. Integral closure of $A$:
<2>1. Let $K = \operatorname{Frac}(A)$ be the fraction field of $A$.
Define $t = \frac{y}{x-1} \in K$.
Then:
\[
t^2 = \frac{y^2}{(x-1)^2} = \frac{x(x-1)^2}{(x-1)^2} = x \implies x = t^2.
\]
<2>2. Express $y$ in terms of $t$:
\[
y = t(x - 1) = t(t^2 - 1) = t^3 - t.
\]
Thus $A = \mathbb{C}[x, y] = \mathbb{C}[t^2, t^3 - t] \subseteq \mathbb{C}[t] \subset K$.
<2>3. The element $t$ is integral over $A$ since $t^2 - x = 0$ is a monic polynomial in $A[T]$.
Thus $\mathbb{C}[t]$ is an integral extension of $A$.
<2>4. The polynomial ring $\mathbb{C}[t]$ is a PID, hence integrally closed in its fraction field $\operatorname{Frac}(\mathbb{C}[t]) = \mathbb{C}(t) = K$.
Therefore $\mathbb{C}[t]$ is the integral closure of $A$ in $K$, with normalization isomorphism $\widetilde{A} \cong \mathbb{C}[t]$.

<1>4. Conclusion:
$A$ is an integral domain, its real points form a nodal cubic curve with a loop on $[0, 1]$, and its integral closure is $\mathbb{C}[t]$ where $t = \frac{y}{x-1}$. Q.E.D.
:::
