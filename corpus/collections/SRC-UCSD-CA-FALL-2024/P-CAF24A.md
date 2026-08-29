---
schema: qual/card@1
id: P-CAF24A
kind: problem
title: Non-constant entire function takes positive real values at nonzero points
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $f : \mathbb{C} \to \mathbb{C}$ be a non-constant entire function.
Show that there exist complex numbers $z \neq 0$ for which $f(z)$ is positive real.

(You may not use Picard’s theorem for this question.)
:::

::: {.solution}
<1>1. Suppose for contradiction that $f(z)$ is not positive real for any $z \neq 0$.
Proof: assume the conclusion fails.

<1>2. Then $f(\mathbb{C} \setminus \{0\})$ avoids the positive real axis $(0, \infty)$.
Proof: <1>1.

<1>3. Since $f$ is entire (hence continuous), $f(\mathbb{C})$ avoids $(0, \infty)$ except possibly at $f(0)$.
Proof: <1>2 and continuity.

<1>4. The set $\mathbb{C} \setminus (0, \infty)$ is simply connected (it is the plane slit along the positive real axis).
Proof: the slit plane is simply connected.

<1>5. The principal branch of the square root maps $\mathbb{C} \setminus (0, \infty)$ into the upper half-plane $\{w : \operatorname{Im} w > 0\}$.
Proof: the square root of a point in the slit plane has argument in $(0, \pi)$.

<1>6. Hence $h(z) = \sqrt{f(z)}$ is an entire function mapping $\mathbb{C}$ into the upper half-plane.
Proof: <1>3 and <1>5.

<1>7. The Cayley transform $\phi(w) = \frac{w - i}{w + i}$ maps the upper half-plane into the unit disk, so $\phi \circ h$ is a bounded entire function.
Proof: <1>6 and the Cayley transform.

<1>8. By Liouville's theorem, $\phi \circ h$ is constant, so $h$ is constant, so $f = h^2$ is constant.
Proof: <1>7.

<1>9. This contradicts $f$ being non-constant, so there exists $z \neq 0$ with $f(z)$ positive real.
Proof: <1>8.

<1>10. Q.E.D.
Proof: <1>9.
:::
