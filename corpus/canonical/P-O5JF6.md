---
schema: qual/card@1
id: P-O5JF6
kind: problem
title: $\int_{\mathbb{R}} f=\int_0^\infty m(\{f>t\})\,dt$ for nonnegative measurable $f$
classification:
  areas:
  - real-analysis
  topics:
  - fubini-tonelli
relations: []
review: draft
solved: true
---

::: problem
Let $f \geq 0$ be a measurable function on $\RR$.
Show that
$$
\int_{\mathbb{R}} f=\int_{0}^{\infty} m(\{x: f(x)>t\}) d t
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

For any $x \in \RR$, since $f(x) \geq 0$, we can express $f(x)$ as:
$$
f(x) = \int_0^{f(x)} 1 \, dt = \int_0^\infty \mathbf{1}_{\{t : 0 \leq t < f(x)\}}(t) \, dt = \int_0^\infty \mathbf{1}_{\{(x,t) : f(x) > t\}}(x, t) \, dt.
$$

Consider the function $F(x, t) = \mathbf{1}_{\{(x,t) \in \RR \times [0, \infty) : f(x) > t\}}$.
Since $f$ is a non-negative measurable function on $\RR$, the set $E = \{(x, t) \in \RR \times [0, \infty) : f(x) > t\}$ is a measurable subset of $\RR^2$ (with the product $\sigma$-algebra).
Therefore, $F(x, t)$ is a non-negative measurable function on $\RR \times [0, \infty)$.

By **Tonelli's Theorem**, we can interchange the order of integration:
$$
\int_\RR f(x) \, dx = \int_\RR \left( \int_0^\infty \mathbf{1}_{\{f(x) > t\}}(x, t) \, dt \right) dx = \int_0^\infty \left( \int_\RR \mathbf{1}_{\{f(x) > t\}}(x, t) \, dx \right) dt.
$$

For each fixed $t \in [0, \infty)$:
$$
\int_\RR \mathbf{1}_{\{f(x) > t\}}(x, t) \, dx = \int_{\{x \in \RR : f(x) > t\}} 1 \, dx = m(\{x \in \RR : f(x) > t\}).
$$

Substituting this back gives:
$$
\int_\RR f = \int_0^\infty m(\{x \in \RR : f(x) > t\}) \, dt,
$$
as desired.
:::
