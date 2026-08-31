---
schema: qual/card@1
id: E-SS1.EX-5
kind: exercise
title: "A set Ω is said to be pathwise connected if any two points in Ω can be joined by"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: exercise
5. A set Ω is said to be pathwise connected if any two points in Ω can be joined by a (piecewise-smooth) curve entirely contained in Ω. The purpose of this exercise is to prove that an open set Ω is pathwise connected if and only if Ω is connected.

(a) Suppose first that Ω is open and pathwise connected, and that it can be written as $\Omega = \Omega _ { 1 } \cup \Omega _ { 2 }$ where $\Omega _ { 1 }$ and $\Omega _ { 2 }$ are disjoint non-empty open sets.
Choose two points $w _ { 1 } \in \Omega _ { 1 }$ and $w _ { 2 } \in \Omega _ { 2 }$ and let $\gamma$ denote a curve in Ω joining $w _ { 1 }$ to $w _ { 2 }$ . Consider a parametrization $z : [ 0 , 1 ] \to \Omega$ of this curve with $z ( 0 ) = w _ { 1 }$ and $z ( 1 ) = w _ { 2 }$ , and let

$$
t ^ {*} = \sup _ {0 \leq t \leq 1} \{t: z (s) \in \Omega_ {1} \text { for   all } 0 \leq s <   t \}.
$$

Arrive at a contradiction by considering the point $z ( t ^ { * } )$

(b) Conversely, suppose that Ω is open and connected.
Fix a point $w \in \Omega$ and let $\Omega _ { 1 } \subset \Omega$ denote the set of all points that can be joined to w by a curve contained in Ω. Also, let $\Omega _ { 2 } \subset \Omega$ denote the set of all points that cannot be joined to w by a curve in Ω. Prove that both $\Omega _ { 1 }$ and $\Omega _ { 2 }$ are open, disjoint and their union is Ω. Finally, since $\Omega _ { 1 }$ is non-empty (why?)
conclude that $\Omega = \Omega _ { 1 }$ as desired.

The proof actually shows that the regularity and type of curves we used to define pathwise connectedness can be relaxed without changing the equivalence between the two definitions when Ω is open.
For instance, we may take all curves to be continuous, or simply polygonal lines.<sup>2</sup>
:::

::: {.solution}
**Part (a).**

<1>1. $z(t^*) \in \Omega_1$ or $z(t^*) \in \Omega_2$, since $\Omega = \Omega_1 \cup \Omega_2$.
::: {.proof}
$z(t^*) \in \Omega$ and $\Omega$ is the disjoint union of $\Omega_1$ and $\Omega_2$.
:::

<1>2. $z(t^*) \notin \Omega_1$.
<2>1. If $z(t^*) \in \Omega_1$, then since $\Omega_1$ is open there is $\epsilon > 0$ with $z(t) \in \Omega_1$ for all $t \in (t^* - \epsilon, t^* + \epsilon)$.
::: {.proof}
continuity of $z$ and openness of $\Omega_1$.
:::
<2>2. This contradicts the definition of $t^*$ as the supremum.
::: {.proof}
then $z(s) \in \Omega_1$ for all $s < t^* + \epsilon$, so $t^*$ is not an upper bound.
:::

<1>3. $z(t^*) \notin \Omega_2$.
<2>1. If $z(t^*) \in \Omega_2$, then since $\Omega_2$ is open there is $\epsilon > 0$ with $z(t) \in \Omega_2$ for all $t \in (t^* - \epsilon, t^* + \epsilon)$.
::: {.proof}
continuity and openness.
:::
<2>2. But by definition of $t^*$, there are $s$ arbitrarily close to $t^*$ from below with $z(s) \in \Omega_1$.
::: {.proof}
$t^*$ is the supremum of the set of such $t$.
:::
<2>3. This contradicts $z(s) \in \Omega_2$ for those $s$ (since $\Omega_1 \cap \Omega_2 = \varnothing$).
::: {.proof}
<2>1 and <2>2.
:::

<1>4. Contradiction.
::: {.proof}
<1>1, <1>2, and <1>3 show $z(t^*)$ lies in neither $\Omega_1$ nor $\Omega_2$.
:::

<1>5. Hence $\Omega$ cannot be written as a disjoint union of two nonempty open sets, so $\Omega$ is connected.
::: {.proof}
<1>4.
:::

**Part (b).**

<1>1. $\Omega_1$ is open.
<2>1. Let $p \in \Omega_1$, joined to $w$ by a curve $\gamma$.
::: {.proof}
definition of $\Omega_1$.
:::
<2>2. Since $\Omega$ is open, there is a disk $D \subset \Omega$ centered at $p$.
::: {.proof}
openness of $\Omega$.
:::
<2>3. Every $q \in D$ is joined to $w$ by $\gamma$ followed by the straight segment from $p$ to $q$.
::: {.proof}
concatenate curves.
:::
<2>4. Hence $D \subset \Omega_1$, so $\Omega_1$ is open.
::: {.proof}
<2>3.
:::

<1>2. $\Omega_2$ is open.
<2>1. Let $p \in \Omega_2$ and $D \subset \Omega$ a disk centered at $p$.
::: {.proof}
openness of $\Omega$.
:::
<2>2. If some $q \in D$ were in $\Omega_1$, then $p$ would be joined to $w$ via $q$.
::: {.proof}
join $p$ to $q$ by a segment and $q$ to $w$ by a curve.
:::
<2>3. This contradicts $p \in \Omega_2$.
::: {.proof}
<2>2.
:::
<2>4. Hence $D \subset \Omega_2$, so $\Omega_2$ is open.
::: {.proof}
<2>3.
:::

<1>3. $\Omega_1$ and $\Omega_2$ are disjoint and $\Omega = \Omega_1 \cup \Omega_2$.
::: {.proof}
by definition, every point either can or cannot be joined to $w$.
:::

<1>4. $\Omega_1 \neq \varnothing$.
::: {.proof}
$w \in \Omega_1$ (joined to itself by the constant curve).
:::

<1>5. Hence $\Omega_2 = \varnothing$, so $\Omega = \Omega_1$.
::: {.proof}
$\Omega$ is connected, so it cannot be a disjoint union of two nonempty open sets; since $\Omega_1 \neq \varnothing$ and $\Omega_1$ is open, $\Omega_2$ must be empty.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5 shows every point of $\Omega$ is joined to $w$, so $\Omega$ is pathwise connected.
:::
:::
