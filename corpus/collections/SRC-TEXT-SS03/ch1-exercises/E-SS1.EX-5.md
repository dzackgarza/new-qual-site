---
schema: qual/card@1
id: E-SS1.EX-5
kind: problem
title: An open set is connected if and only if it is pathwise connected
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

::: {.exercise}
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
For instance, we may take all curves to be continuous, or simply polygonal lines.
:::

::: {.solution}

::: pf

::: pf-step

(a) An open pathwise connected set $\Omega$ is connected.

::: pf-proof

::: {.pf-step #s1-1}

With $\Omega=\Omega_1\sqcup\Omega_2$, $w_1,w_2$, $z$, and $t^*$ as in the statement, $z(t^*) \notin \Omega_1$.

::: pf-proof

Suppose $z(t^*) \in \Omega_1$. Since $z(1)=w_2\in\Omega_2$ and $\Omega_1\cap\Omega_2=\varnothing$, $t^*<1$. By continuity of $z$ and openness of $\Omega_1$ there is $\varepsilon > 0$ with $z(t) \in \Omega_1$ for all $t \in (t^* - \varepsilon, t^* + \varepsilon)\cap[0,1]$. Together with the definition of $t^*$, this gives $z(s)\in\Omega_1$ for all $0\le s<\min(t^*+\varepsilon,1)$, so $t^*$ is not the supremum.

:::

:::

::: {.pf-step #s1-2}

$z(t^*) \notin \Omega_2$.

::: pf-proof

Since $z(0)=w_1\in\Omega_1$ and $\Omega_1$ is open, $t^*>0$, and by definition of $t^*$ there are $s<t^*$ arbitrarily close to $t^*$ with $z(s) \in \Omega_1$. If $z(t^*) \in \Omega_2$, then openness of $\Omega_2$ and continuity give $\varepsilon>0$ with $z(s)\in\Omega_2$ for $\abs{s-t^*}<\varepsilon$, contradicting $\Omega_1 \cap \Omega_2 = \varnothing$.

:::

:::

::: pf-qed

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, $z(t^*)\in\Omega$ lies in neither $\Omega_1$ nor $\Omega_2$, which contradicts $\Omega=\Omega_1\cup\Omega_2$. Hence $\Omega$ is not a disjoint union of two nonempty open sets, so $\Omega$ is connected.

:::

:::

:::

::: pf-step

(b) An open connected set $\Omega$ is pathwise connected.

::: pf-proof

::: {.pf-step #s2-1}

With $w$, $\Omega_1$, $\Omega_2$ as in the statement, $\Omega_1$ is open.

::: pf-proof

Let $p \in \Omega_1$ be joined to $w$ by a curve $\gamma$ in $\Omega$, and let $D \subset \Omega$ be a disc centered at $p$. Every $q \in D$ is joined to $w$ by $\gamma$ followed by the segment from $p$ to $q$, which lies in $D$. Hence $D \subset \Omega_1$.

:::

:::

::: {.pf-step #s2-2}

$\Omega_2$ is open.

::: pf-proof

Let $p \in \Omega_2$ and let $D \subset \Omega$ be a disc centered at $p$. If some $q \in D$ lay in $\Omega_1$, then the segment from $p$ to $q$ followed by a curve from $q$ to $w$ would join $p$ to $w$ in $\Omega$, contradicting $p\in\Omega_2$. Hence $D \subset \Omega_2$.

:::

:::

::: pf-qed

By definition $\Omega_1$ and $\Omega_2$ are disjoint with union $\Omega$, and $w \in \Omega_1$ via the constant curve. By steps [](#s2-1){.pf-ref} and [](#s2-2){.pf-ref} both sets are open. Since $\Omega$ is connected and $\Omega_1\ne\varnothing$, $\Omega_2 = \varnothing$, so $\Omega = \Omega_1$: every point of $\Omega$ is joined to $w$, and any two points are joined through $w$.

:::

:::

:::

:::

:::
