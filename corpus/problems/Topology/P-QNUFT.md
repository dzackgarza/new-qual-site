---
schema: qual/card@1
id: P-QNUFT
kind: problem
title: Paths with common endpoints in a simply connected space are homotopic
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
1. **Main idea**: just algebraic manipulations using the $\pi_1$ functor and unravelling definitions.

Let $X$ be path connected and simply connected, and let $x,y \in X$ be two arbitrary points.
Then consider two paths, $\gamma: I \into X, \gamma(0) = x, \gamma(1) = y$ $\alpha: I \into X, \alpha(0) = x, \alpha(1) = y$.

We would like to show $\gamma \homotopic \alpha$.
Since $X$ is simply connected, we know that $\pi_1(X) = 0$.
This means that for any $a,b \in \pi_1(X), a = b = e$, the identity element in this group.

So we construct two loops: one as $\gamma \bar\alpha$, the other as $\alpha\bar\gamma$.
Apply the $\pi_1$ functor yields $[\gamma\bar\alpha] = e = [c_x] = [\alpha\bar\gamma]$, where $[c_x]$ is the equivalence class of the constant path at $x$, and equivalently the identity element in $\pi_1(X)$.
Lemma: If $f\homotopic g$, then $f\circ h \homotopic g \circ h$ for any $h$.

But this says $\gamma\bar\alpha \homotopic c_x$ and $\alpha\bar\gamma \homotopic c_x$.
But $\gamma \homotopic c_x \circ \gamma \homotopic (\alpha\bar\gamma) \circ \gamma \homotopic \alpha\circ (\bar\gamma \circ\gamma) \homotopic \alpha$, which is what we desired.
:::

::: solution
**Goal:** Show that two paths in a simply connected space with common endpoints are homotopic rel endpoints.

<1>1. Let $\gamma,\alpha:I\to X$ satisfy $\gamma(0)=\alpha(0)=x$ and $\gamma(1)=\alpha(1)=y$.
    *Proof:* Since $X$ is simply connected, $\pi_1(X,x)=0$ and $\pi_1(X,y)=0$.
<1>2. The loops $\gamma * \overline{\alpha}$ at $x$ and $\overline{\alpha} * \alpha$ at $y$ are both null-homotopic:
    *Proof:* Triviality of the two fundamental groups gives
    \[
    \gamma * \overline{\alpha}\sim c_x,\qquad
    \overline{\alpha} * \alpha\sim c_y.
    \]
<1>3. Concatenate the first homotopy on the right with $\alpha$:
    *Proof:* If $u\sim v$ then $u * \alpha\sim v * \alpha$, so
    \[
    (\gamma * \overline{\alpha}) * \alpha \sim c_x * \alpha.
    \]
    Re-associating,
    \[
    \gamma * (\overline{\alpha} * \alpha)\sim \alpha.
    \]
<1>4. Replace $\overline{\alpha} * \alpha$ by $c_y$ and remove the unit loop:
    *Proof:* From the second homotopy,
    \[
    \gamma \sim \gamma * c_y \sim \gamma * (\overline{\alpha} * \alpha).
    \]
    Combining with step <1>3 gives $\gamma\sim\alpha$ by concatenating homotopies.
    Hence, with endpoints fixed, $\gamma$ and $\alpha$ are path-homotopic.
Q.E.D.
:::
