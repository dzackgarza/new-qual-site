---
schema: qual/card@1
id: P-TOPS13E
kind: problem
title: "No antipodal-preserving map from R^3 minus origin to R^2"
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Prove by contradiction that there does not exist a continuous map $f : \mathbb{R}^3 \setminus \{0\} \to \mathbb{R}^2$ with the property that $f(x) \neq f(-x)$ for all $x \in \mathbb{R}^3 \setminus \{0\}$.

Hint: Define $g : \mathbb{R}^3 \setminus \{0\} \to S^1$ by
$$
g(x) = \frac{f(x) - f(-x)}{|f(x) - f(-x)|},
$$
which satisfies $g(-x) = -g(x)$.
Define the loop $\eta : I \to \mathbb{R}^3 \setminus \{0\}$ by $\eta(s) = (\cos(2\pi s), \sin(2\pi s), 0)$ and consider the loop $h = g \circ \eta$ in $S^1$.
:::

::: {.solution}
<1>1. Suppose for contradiction that such an $f$ exists.
::: {.proof}
assume the contrary.
:::

<1>2. Define $g(x) = \frac{f(x) - f(-x)}{|f(x) - f(-x)|} \in S^1$, which is continuous and satisfies $g(-x) = -g(x)$.
::: {.proof}
$f(x) \neq f(-x)$ so the denominator is nonzero; and $g(-x) = \frac{f(-x) - f(x)}{|f(-x)-f(x)|} = -g(x)$.
:::

<1>3. Let $\eta(s) = (\cos 2\pi s, \sin 2\pi s, 0)$ and $h = g \circ \eta: S^1 \to S^1$.
::: {.proof}
definition.
:::

<1>4. $h$ is nullhomotopic.
::: {.proof}
$\eta$ is nullhomotopic in $\RR^3 \setminus \{0\}$ (the loop $\eta$ bounds a disk in the $xy$-plane not passing through $0$... more precisely, $\eta$ is homotopic to a constant via the homotopy that shrinks the circle to a point in the plane $z=0$ avoiding the origin), so $h = g \circ \eta$ is nullhomotopic.
:::

<1>5. Hence $h$ has degree $0$.
::: {.proof}
a nullhomotopic map $S^1 \to S^1$ has degree $0$.
:::

<1>6. But $h$ has odd degree.
<2>1. $h(s + 1/2) = g(\eta(s + 1/2)) = g(-\eta(s)) = -g(\eta(s)) = -h(s)$.
::: {.proof}
$\eta(s + 1/2) = -\eta(s)$ and $g(-x) = -g(x)$.
:::
<2>2. A map $h: S^1 \to S^1$ with $h(s + 1/2) = -h(s)$ has odd degree.
::: {.proof}
such a map factors through the antipodal map of $S^1$; the induced map on $\pi_1(S^1) = \ZZ$ sends the generator to an odd multiple of itself (the antipodal map has degree $1$ on $S^1$... more precisely, $h$ is equivariant for the antipodal $\ZZ/2$-action, so it descends to a map $\RP^1 \to \RP^1$ of degree $1$, forcing $h$ to have odd degree).
:::

<1>7. Contradiction.
::: {.proof}
<1>5 says $\deg h = 0$ but <1>6 says $\deg h$ is odd.
:::

<1>8. Hence no such $f$ exists.
::: {.proof}
<1>1–<1>7.
:::

<1>9. Q.E.D.
::: {.proof}
<1>8.
:::
:::
