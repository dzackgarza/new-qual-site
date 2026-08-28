---
schema: qual/card@1
id: E-AMD-HWVXZVE4
kind: exercise
title: The radical of an ideal is the intersection of the primes containing it
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Prime Ideals
  - Nilpotence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that for an ideal $I\trianglelefteq R$ in a commutative ring $R$, its radical $\sqrt{I}$ is the intersection of all prime ideals containing $I$.
:::

::: solution
**Goal:** Prove that for any ideal $I$ in a commutative ring with identity $R$:
$$\sqrt{I} = \bigcap_{\substack{\mathfrak{p} \in \operatorname{Spec}(R) \\ I \subseteq \mathfrak{p}}} \mathfrak{p}.$$

<1>1. Forward inclusion $\sqrt{I} \subseteq \bigcap_{I \subseteq \mathfrak{p}} \mathfrak{p}$:
    *Proof:*
    <2>1. Let $x \in \sqrt{I}$, so $x^n \in I$ for some integer $n \ge 1$.
    <2>2. Let $\mathfrak{p}$ be any prime ideal containing $I$.
    <2>3. Since $I \subseteq \mathfrak{p}$, we have $x^n \in \mathfrak{p}$.
    <2>4. By the definition of a prime ideal, $x^n \in \mathfrak{p} \implies x \in \mathfrak{p}$.
    <2>5. Since this holds for every prime ideal $\mathfrak{p} \supseteq I$, $x \in \bigcap_{I \subseteq \mathfrak{p}} \mathfrak{p}$.

<1>2. Reverse inclusion via Zorn's Lemma and localization:
    *Proof:*
    <2>1. Suppose $f \notin \sqrt{I}$. We construct a prime ideal $\mathfrak{p} \supseteq I$ such that $f \notin \mathfrak{p}$.
    <2>2. Consider the multiplicative set $S = \{f^n \mid n \ge 0\}$.
    <2>3. Since $f \notin \sqrt{I}$, $S \cap I = \varnothing$.
    <2>4. Let $\mathcal{F} = \{J \subseteq R \mid J \text{ is an ideal of } R, \, I \subseteq J, \text{ and } J \cap S = \varnothing\}$, partially ordered by inclusion.
    <2>5. $\mathcal{F} \neq \varnothing$ because $I \in \mathcal{F}$.
    <2>6. Every non-empty chain in $\mathcal{F}$ has an upper bound in $\mathcal{F}$ given by the union of ideals in the chain.
    <2>7. By Zorn's Lemma, $\mathcal{F}$ has a maximal element $\mathfrak{p}$.
    <2>8. **$\mathfrak{p}$ is prime:** Suppose $a, b \notin \mathfrak{p}$.
        - By maximality of $\mathfrak{p}$ in $\mathcal{F}$, the strictly larger ideals $\mathfrak{p} + (a)$ and $\mathfrak{p} + (b)$ intersect $S$.
        - There exist $k, m \ge 0$ such that $f^k \in \mathfrak{p} + (a)$ and $f^m \in \mathfrak{p} + (b)$.
        - Multiplying gives $f^{k+m} \in (\mathfrak{p} + (a))(\mathfrak{p} + (b)) \subseteq \mathfrak{p} + (ab)$.
        - If $ab \in \mathfrak{p}$, then $f^{k+m} \in \mathfrak{p}$, which contradicts $\mathfrak{p} \cap S = \varnothing$.
        - Thus $ab \notin \mathfrak{p}$, proving $\mathfrak{p}$ is a prime ideal.
    <2>9. By construction, $I \subseteq \mathfrak{p}$ and $f \notin \mathfrak{p}$.
    <2>10. Thus $f \notin \bigcap_{I \subseteq \mathfrak{q}} \mathfrak{q}$.

<1>3. Conclusion:
    Combining <1>1 and <1>2 gives $\sqrt{I} = \bigcap_{I \subseteq \mathfrak{p}} \mathfrak{p}$. Q.E.D.
:::
