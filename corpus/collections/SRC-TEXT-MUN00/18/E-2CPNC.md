---
schema: qual/card@1
id: E-2CPNC
kind: problem
title: Pasting over a locally finite closed cover
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $\ts{A_\alpha}$ be a collection of subsets of $X$; let $X = \bigcup_\alpha A_\alpha$.
Let $f: X \to Y$; suppose that $f \mid A_\alpha$ is continuous for each $\alpha$.

(a) Show that if the collection $\ts{A_\alpha}$ is finite and each set $A_\alpha$ is closed, then $f$ is continuous.

(b) Find an example where the collection $\ts{A_\alpha}$ is countable and each $A_\alpha$ is closed, but $f$ is not continuous.

(c) An indexed family of sets $\ts{A_\alpha}$ is said to be locally finite if each point $x$ of $X$ has a neighborhood that intersects $A_\alpha$ for only finitely many values of $\alpha$.
Show that if the family $\ts{A_\alpha}$ is locally finite and each $A_\alpha$ is closed, then $f$ is continuous.
:::

::: solution
**Goal:** Prove the Pasting Lemma for finite closed covers and locally finite closed covers, and provide a counterexample for infinite non-locally finite closed covers.

<1>1. Part (a): Pasting over a finite closed cover.
    *Proof:*
    <2>1. Let $\{A_1, \dots, A_n\}$ be a finite closed cover of $X$, and let $C \subseteq Y$ be an arbitrary closed set.
    <2>2. The preimage is:
        $$f^{-1}(C) = f^{-1}(C) \cap \left(\bigcup_{i=1}^n A_i\right) = \bigcup_{i=1}^n \left(f^{-1}(C) \cap A_i\right) = \bigcup_{i=1}^n (f|_{A_i})^{-1}(C).$$
    <2>3. Since $f|_{A_i}: A_i \to Y$ is continuous and $C$ is closed in $Y$, each set $(f|_{A_i})^{-1}(C)$ is closed in the subspace topology of $A_i$.
    <2>4. Since each $A_i$ is closed in $X$, each $(f|_{A_i})^{-1}(C)$ is closed in $X$.
    <2>5. A finite union of closed sets in $X$ is closed, so $f^{-1}(C)$ is closed in $X$.
    <2>6. Therefore $f: X \to Y$ is continuous.

<1>2. Part (b): Counterexample for a countable closed cover.
    *Proof:*
    <2>1. Let $X = \mathbb{R}$, $Y = \mathbb{R}$, and define the countable collection of closed sets:
        $$A_0 = (-\infty, 0], \quad A_n = \left[\frac{1}{n}, \infty\right) \quad \text{for } n \in \mathbb{Z}_+.$$
    <2>2. Then $\bigcup_{n=0}^\infty A_n = (-\infty, 0] \cup (0, \infty) = \mathbb{R}$, and each $A_n$ is closed in $\mathbb{R}$.
    <2>3. Define $f: \mathbb{R} \to \mathbb{R}$ by $f(x) = 0$ for $x \le 0$ and $f(x) = 1$ for $x > 0$.
    <2>4. On $A_0$, $f|_{A_0} \equiv 0$ is constant (hence continuous). For each $n \ge 1$, $f|_{A_n} \equiv 1$ is constant (hence continuous).
    <2>5. However, $f$ is discontinuous at $x = 0$ because $\lim_{x \to 0^+} f(x) = 1 \neq 0 = f(0)$.

<1>3. Part (c): Pasting over a locally finite closed cover.
    *Proof:*
    <2>1. Let $\{A_\alpha\}_{\alpha \in J}$ be a locally finite collection of closed subsets covering $X$.
    <2>2. Let $C \subseteq Y$ be closed. As in <1>1, $f^{-1}(C) = \bigcup_{\alpha \in J} F_\alpha$, where $F_\alpha = (f|_{A_\alpha})^{-1}(C)$ is closed in $X$ and $F_\alpha \subseteq A_\alpha$.
    <2>3. Since $\{A_\alpha\}$ is locally finite and $F_\alpha \subseteq A_\alpha$, the family $\{F_\alpha\}_{\alpha \in J}$ is locally finite.
    <2>4. Lemma: The union of any locally finite family of closed sets is closed.
        - Let $F = \bigcup_{\alpha \in J} F_\alpha$, and let $x \in \overline{F}$.
        - By local finiteness, there exists an open neighborhood $U$ of $x$ intersecting only finitely many members $F_{\alpha_1}, \dots, F_{\alpha_k}$.
        - Then $U \cap F = U \cap \left(\bigcup_{i=1}^k F_{\alpha_i}\right)$.
        - Since $x \in \overline{F}$, $x \in \overline{U \cap F} \subseteq \overline{\bigcup_{i=1}^k F_{\alpha_i}} = \bigcup_{i=1}^k \overline{F_{\alpha_i}} = \bigcup_{i=1}^k F_{\alpha_i} \subseteq F$.
        - Thus $\overline{F} = F$, so $F$ is closed in $X$.
    <2>5. Hence $f^{-1}(C) = F$ is closed in $X$, which proves that $f$ is continuous. Q.E.D.
:::
