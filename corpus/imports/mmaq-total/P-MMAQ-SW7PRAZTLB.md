---
schema: qual/card@1
id: P-MMAQ-SW7PRAZTLB
kind: problem
title: If $f$ is a non-constant entire function, then $f(\mathbb{C})$ is
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
relations: []
review: draft
solved: true
---

::: problem
If $f$ is a non-constant entire function, then $f(\mathbb{C})$ is dense in the plane.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Prove that if $f: \mathbb{C} \to \mathbb{C}$ is a non-constant entire function, then its image $f(\mathbb{C})$ is dense in $\mathbb{C}$ (i.e. $\overline{f(\mathbb{C})} = \mathbb{C}$).

* * *

### Proof by Contradiction via Liouville's Theorem

<1>1. **Assume towards a contradiction that $f(\mathbb{C})$ is not dense in $\mathbb{C}$.** <2>1. If $f(\mathbb{C})$ is not dense, there exists a point $w_0 \in \mathbb{C}$ and an $\varepsilon > 0$ such that the open disk $D(w_0, \varepsilon)$ is disjoint from $f(\mathbb{C})$: $$D(w_0, \varepsilon) \cap f(\mathbb{C}) = \emptyset.$$ *Proof:* Definition of density in a metric space: a set is dense iff every non-empty open ball intersects it.
<2>2. This means that for all $z \in \mathbb{C}$, $|f(z) - w_0| \geq \varepsilon > 0$.
*Proof:* $f(z) \notin D(w_0, \varepsilon)$ for all $z \in \mathbb{C}$.
<2>3. Q.E.D.

<1>2. **Construct an auxiliary function $g(z) = \frac{1}{f(z) - w_0}$.** <2>1. Since $|f(z) - w_0| \geq \varepsilon > 0$, the denominator $f(z) - w_0$ never vanishes on $\mathbb{C}$.
*Proof:* $f(z) - w_0 \neq 0$ for all $z \in \mathbb{C}$.
<2>2. Because $f$ is entire and $f(z) - w_0 \neq 0$, the reciprocal $g(z) = \frac{1}{f(z) - w_0}$ is an entire function.
*Proof:* Quotient of entire functions with non-vanishing denominator.
<2>3. Q.E.D.

<1>3. **Show that $g(z)$ is bounded on $\mathbb{C}$.** <2>1. For all $z \in \mathbb{C}$: $$|g(z)| = \left| \frac{1}{f(z) - w_0} \right| = \frac{1}{|f(z) - w_0|} \leq \frac{1}{\varepsilon} < \infty.$$ *Proof:* Inverting the lower bound $|f(z) - w_0| \geq \varepsilon > 0$.
<2>2. Thus $g$ is a bounded entire function on $\mathbb{C}$.
*Proof:* Follows from <2>1. <2>3. Q.E.D.

<1>4. **Apply Liouville's Theorem to $g(z)$.** <2>1. By Liouville's Theorem, every bounded entire function is constant.
*Proof:* Fundamental theorem of complex analysis.
<2>2. Therefore, there exists a constant $c \in \mathbb{C}$ such that $g(z) = c$ for all $z \in \mathbb{C}$.
*Proof:* By <1>3 and <2>1. <2>3. Since $|g(z)| \leq 1/\varepsilon$, $c$ is a finite complex number, and $c \neq 0$ because $g(z) = \frac{1}{f(z)-w_0} \neq 0$.
*Proof:* The reciprocal of a complex number is non-zero.
<2>4. Q.E.D.

<1>5. **Deduce that $f(z)$ is constant, reaching a contradiction.** <2>1. From $g(z) = c$, we solve for $f(z)$: $$\frac{1}{f(z) - w_0} = c \implies f(z) = w_0 + \frac{1}{c}.$$ *Proof:* Algebraic rearrangement since $c \neq 0$.
<2>2. Thus $f(z)$ is identically constant on $\mathbb{C}$.
*Proof:* $w_0 + 1/c$ is a fixed constant.
<2>3. This contradicts the hypothesis that $f$ is non-constant.
*Proof:* Contradiction with the initial premise.
<2>4. Hence, $f(\mathbb{C})$ must be dense in $\mathbb{C}$.
*Proof:* Proof by contradiction complete.
<2>5. Q.E.D.
:::
