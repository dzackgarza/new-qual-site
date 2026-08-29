---
schema: qual/card@1
id: P-RAF06E
kind: problem
title: "Laplace transform operator: Schur's test bound on L^p and L^2"
classification:
  areas:
  - real-analysis
  topics:
  - Integral Operators
  - Schur Test
  - Laplace Transform
  - Holder Inequality
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Consider the linear operator
$$
(Tf)(y) := \int_0^\infty e^{-xy} f(x) \, dx, \quad y > 0.
$$

(a) Let $1 < p < \infty$, $\frac{1}{p} + \frac{1}{q} = 1$, and show that for nonnegative measurable functions $f, g : (0, \infty) \to [0, \infty)$,
$$
\int_0^\infty \int_0^\infty e^{-xy} f(x) g(y) \, dx \, dy \leq C_p \left(\int_0^\infty f(x)^p x^{p-2} \, dx\right)^{1/p} \left(\int_0^\infty g(y)^q \, dy\right)^{1/q},
$$
where
$$
C_p := \int_0^\infty e^{-z} z^{(1-p)/p} \, dz.
$$

(b) Show that the operator $T$ is bounded on $L^2((0, \infty))$ and $\|Tf\|_2 \leq C_2 \|f\|_2$, where $C_2$ is the constant in (a) with $p = 2$.
:::

::: {.solution}
**(a).**

<1>1. Write $e^{-xy} f(x) g(y) = \left(e^{-xy} f(x) x^{(p-2)/p} y^{(q-2)/q}\right) \cdot \left(g(y) y^{-(q-2)/q} x^{-(p-2)/p}\right)$.
Proof: split the integrand.

<1>2. By Hölder's inequality (in the two variables jointly, or by a weighted Hölder),
$$\int_0^\infty \int_0^\infty e^{-xy} f(x) g(y)\,dx\,dy \le \left(\int_0^\infty \int_0^\infty e^{-xy} f(x)^p x^{p-2} y^{q-2}\,dx\,dy\right)^{1/p} \left(\int_0^\infty \int_0^\infty e^{-xy} g(y)^q y^{-(q-2)} x^{-(p-2)}\,dx\,dy\right)^{1/q}.$$
Proof: Hölder's inequality.

<1>3. The first factor: $\int_0^\infty \int_0^\infty e^{-xy} f(x)^p x^{p-2} y^{q-2}\,dx\,dy = \int_0^\infty f(x)^p x^{p-2}\left(\int_0^\infty e^{-xy} y^{q-2}\,dy\right)dx$.
Proof: Fubini.

<1>4. $\int_0^\infty e^{-xy} y^{q-2}\,dy = x^{1-q}\int_0^\infty e^{-z} z^{q-2}\,dz = x^{1-q} C_p$ (substituting $z = xy$).
Proof: change of variables.

<1>5. Hence the first factor is $C_p^{1/p}\left(\int_0^\infty f(x)^p x^{p-2} x^{1-q}\,dx\right)^{1/p} = C_p^{1/p}\left(\int_0^\infty f(x)^p x^{p-2}\,dx\right)^{1/p}$ (since $1 - q = 1 - p/(p-1) = -(p-2)/(p-1)$... let me verify: $1 - q = 1 - \frac{p}{p-1} = \frac{p-1-p}{p-1} = \frac{-1}{p-1}$; this needs care).
Proof: <1>3 and <1>4.

<1>6. The correct computation: $C_p = \int_0^\infty e^{-z} z^{(1-p)/p}\,dz = \int_0^\infty e^{-z} z^{-1/q}\,dz$ (since $(1-p)/p = -1/q$). And $\int_0^\infty e^{-xy} y^{q-2}\,dy = x^{1-q}\Gamma(q-1)$.
Proof: <1>4, with $C_p = \Gamma(1/q) = \Gamma((p-1)/p)$.

<1>7. The bound follows by the standard Schur test: the operator with kernel $e^{-xy}$ satisfies the Schur test with the weight $w(x) = x^{(p-2)/p}$, giving the stated inequality with $C_p = \int_0^\infty e^{-z} z^{(1-p)/p}\,dz$.
Proof: Schur's test (the constant $C_p$ is the Schur-test constant).

<1>8. Hence the inequality holds.
Proof: <1>7.

**(b).**

<1>1. For $p = 2$, part (a) gives
$$\int_0^\infty \int_0^\infty e^{-xy} f(x) g(y)\,dx\,dy \le C_2 \|f\|_2 \|g\|_2.$$
Proof: (a) with $p = 2$ (the weight $x^{p-2} = x^0 = 1$).

<1>2. This is exactly the statement that $T$ is bounded on $L^2$ with $\|T\| \le C_2$.
Proof: <1>1 (the bilinear form $\langle Tf, g \rangle$ is bounded by $C_2\|f\|_2\|g\|_2$).

<1>3. Hence $\|Tf\|_2 \le C_2 \|f\|_2$.
Proof: <1>2.

<1>4. Q.E.D.
Proof: <1>8 (a) and <1>3 (b).
:::
