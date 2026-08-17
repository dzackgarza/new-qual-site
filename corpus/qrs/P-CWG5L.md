---
schema: qual/card@1
id: P-CWG5L
kind: problem
title: An entire function omitting a bounded open set is constant
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - casorati-weierstrass
relations: []
review: draft
solved: true
---

::: problem
Let $f(z)$ be entire and assume values of $f(z)$ lie outside a *bounded* open set $\Omega$.
Show without using Picard's theorems that $f(z)$ is a constant.

Let $f(z)$ be entire and assume values of $f(z)$ lie outside a *bounded* open set $\Omega$.

Show without using Picard's theorems that $f(z)$ is a constant.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $f$ is entire and $f(\CC) \cap \Omega = \emptyset$ for some bounded open set $\Omega$, then $f$ is constant — without using Picard's theorems.

<1>1. Choose a point $w_0 \in \Omega$ and $\varepsilon > 0$ with $\overline{D_\varepsilon(w_0)} \subseteq \Omega$.
Proof: $\Omega$ is open, so some small closed disk around $w_0$ is contained in it.

<1>2. $\abs{f(z) - w_0} \geq \varepsilon$ for every $z \in \CC$.
Proof: If $\abs{f(z) - w_0} < \varepsilon$ for some $z$, then $f(z) \in D_\varepsilon(w_0) \subseteq \Omega$, contradicting that $f$ takes no values in $\Omega$.

<1>3. $g(z) \definedas \frac{1}{f(z) - w_0}$ is entire and bounded by $1/\varepsilon$.
Proof: By <1>2 the denominator never vanishes, so $g$ is holomorphic on $\CC$; and $\abs{g(z)} = \frac{1}{\abs{f(z) - w_0}} \leq \frac{1}{\varepsilon}$.

<1>4. $g$ is constant, hence $f$ is constant.
Proof: By Liouville's theorem, the bounded entire function $g$ from <1>3 is constant; then $f(z) = w_0 + 1/g(z)$ is constant.

<1>5. Q.E.D. Proof: <1>4 shows $f$ is constant, using only Liouville's theorem and not Picard's theorems.
:::
