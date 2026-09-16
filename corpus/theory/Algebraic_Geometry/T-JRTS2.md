---
schema: qual/card@1
id: T-JRTS2
kind: theorem
title: Hilbert's Nullstellensatz
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nullstellensatz
  - Varieties
relations: []
review: draft
prompts:
- State the Nullstellensatz.
- What is $I(V(J))$?
- Where does the Nullstellensatz use that $k$ is algebraically closed?
- How is the Nullstellensatz proved?
---

::: {.theorem title="Hilbert's Nullstellensatz"}
Let $k$ be algebraically closed and let $J \subseteq k[x_1, \ldots, x_n]$ be an ideal.
Then
\[
I(V(J)) = \sqrt{J} .
\]
:::

::: {.proof}
1. *Zariski's lemma:* if $K$ is a field and $L \supseteq K$ is a field that is finitely generated as a $K$-algebra, then $L/K$ is a finite extension.

2. *Weak form:* let $J \neq (1)$ and choose a maximal ideal $\mfm \supseteq J$.
   The field $k[x_1, \ldots, x_n]/\mfm$ is a finitely generated $k$-algebra, so it is finite over $k$ by step 1, and equals $k$ because $k$ is algebraically closed.
   If $a_i \in k$ is the image of $x_i$, then $x_i - a_i \in \mfm$ for all $i$, so every $f \in J$ vanishes at $a = (a_1, \ldots, a_n)$ and $a \in V(J)$.

3. *Strong form:* $\sqrt{J} \subseteq I(V(J))$ holds because $f^m$ vanishing at a point forces $f$ to vanish there.
   Conversely let $f \in I(V(J))$ and set $J' = J k[x_1, \ldots, x_n, y] + (1 - y f)$.
   A zero of $J'$ is a zero $a$ of $J$ with $y f(a) = 1$, impossible since $f(a) = 0$; so $V(J') = \emptyset$ and $J' = (1)$ by step 2.
   Write $1 = \sum_i g_i h_i + g (1 - y f)$ with $h_i \in J$, substitute $y = 1/f$ in the fraction field, and clear denominators by a power $f^m$: this gives $f^m \in J$.
:::

::: {.remark}
The weak form is the case $J \neq k[x_1,\ldots,x_n] \implies V(J) \neq \emptyset$, and it is equivalent: the strong form follows from the weak one by the Rabinowitsch trick, adjoining a variable $y$ and the polynomial $1 - yf$.

Algebraic closure is not a convenience here.
Over $\RR$ the ideal $(x^2+1)$ is prime, hence radical, but $V(x^2+1) = \emptyset$ in $\AA^1_\RR$, so $I(V(J)) = (1) \neq \sqrt{J}$.
:::
