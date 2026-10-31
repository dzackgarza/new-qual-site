---
schema: qual/card@1
id: E-SS1.EX-5
kind: problem
title: An open set is connected if and only if it is pathwise connected
classification:
  areas:
    - complex-analysis
  topics: [Connectedness, Path Connectedness]
relations: []
review: draft
audit:
  - event: solution-written
    by: gemini-3.7-flash
    date: 2026-08-29
---

::: {.exercise}
A set $\Omega$ is said to be pathwise connected if any two points in $\Omega$ can be joined by a (piecewise-smooth) curve entirely contained in $\Omega$. The purpose of this exercise is to prove that an open set $\Omega$ is pathwise connected if and only if $\Omega$ is connected.

(a) Suppose first that $\Omega$ is open and pathwise connected, and that it can be written as $\Omega = \Omega_1 \cup \Omega_2$ where $\Omega_1$ and $\Omega_2$ are disjoint non-empty open sets. Choose two points $w_1 \in \Omega_1$ and $w_2 \in \Omega_2$ and let $\gamma$ denote a curve in $\Omega$ joining $w_1$ to $w_2$. Consider a parametrization $z \colon [0, 1] \to \Omega$ of this curve with $z(0) = w_1$ and $z(1) = w_2$, and let
$$
t^* = \sup_{0 \leq t \leq 1} \{t : z(s) \in \Omega_1 \text{ for all } 0 \leq s < t\}.
$$
Arrive at a contradiction by considering the point $z(t^*)$.

(b) Conversely, suppose that $\Omega$ is open and connected. Fix a point $w \in \Omega$ and let $\Omega_1 \subset \Omega$ denote the set of all points that can be joined to $w$ by a curve contained in $\Omega$. Also, let $\Omega_2 \subset \Omega$ denote the set of all points that cannot be joined to $w$ by a curve in $\Omega$. Prove that both $\Omega_1$ and $\Omega_2$ are open, disjoint and their union is $\Omega$. Finally, since $\Omega_1$ is non-empty (why?) conclude that $\Omega = \Omega_1$ as desired.

The proof actually shows that the regularity and type of curves we used to define pathwise connectedness can be relaxed without changing the equivalence between the two definitions when $\Omega$ is open. For instance, we may take all curves to be continuous, or simply polygonal lines.
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
