---
schema: qual/card@1
id: E-AMD-KJNCPPCB
kind: problem
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
Show that $\sqrt{I}$ is the intersection of all prime ideals containing $I$.
:::

::: solution
**Goal:** Prove that for any ideal $I$ in a commutative ring $R$ with identity:
$$\sqrt{I} = \bigcap_{\substack{\mathfrak{p} \supseteq I \\ \mathfrak{p} \text{ prime}}} \mathfrak{p}.$$

<1>1. Forward inclusion $\sqrt{I} \subseteq \bigcap_{\mathfrak{p} \supseteq I} \mathfrak{p}$:
    *Proof:*
    <2>1. Let $x \in \sqrt{I}$, so $x^n \in I$ for some $n \ge 1$.
    <2>2. For any prime $\mathfrak{p} \supseteq I$, $x^n \in I \subseteq \mathfrak{p}$.
    <2>3. Since $\mathfrak{p}$ is prime, $x^n \in \mathfrak{p} \implies x \in \mathfrak{p}$ (by induction: $x \cdot x^{n-1} \in \mathfrak{p}$ forces $x \in \mathfrak{p}$ or $x^{n-1} \in \mathfrak{p}$).
    <2>4. Thus $x \in \bigcap_{\mathfrak{p} \supseteq I} \mathfrak{p}$.

<1>2. Reverse inclusion via Zorn's Lemma:
    *Proof:*
    <2>1. Let $f \notin \sqrt{I}$, so $f^n \notin I$ for all $n \ge 0$. Set $S = \{1, f, f^2, \dots\}$.
    <2>2. Consider $\mathcal{F} = \{J \trianglelefteq R \mid I \subseteq J, \, J \cap S = \varnothing\}$. Since $I \cap S = \varnothing$, $I \in \mathcal{F}$.
    <2>3. Every chain in $\mathcal{F}$ has an upper bound (union), so Zorn's Lemma yields a maximal element $\mathfrak{p}$.
    <2>4. **$\mathfrak{p}$ is prime:** Suppose $a, b \notin \mathfrak{p}$. By maximality, $\mathfrak{p} + (a)$ and $\mathfrak{p} + (b)$ both meet $S$, so $f^k \in \mathfrak{p} + (a)$ and $f^m \in \mathfrak{p} + (b)$. Then $f^{k+m} \in (\mathfrak{p} + (a))(\mathfrak{p} + (b)) \subseteq \mathfrak{p} + (ab)$. If $ab \in \mathfrak{p}$, then $f^{k+m} \in \mathfrak{p}$, contradicting $\mathfrak{p} \cap S = \varnothing$. Thus $ab \notin \mathfrak{p}$.
    <2>5. So $\mathfrak{p} \supseteq I$ is prime and $f \notin \mathfrak{p}$, proving $f \notin \bigcap_{\mathfrak{p} \supseteq I} \mathfrak{p}$.

<1>3. Conclusion:
    $\sqrt{I} = \bigcap_{\mathfrak{p} \supseteq I} \mathfrak{p}$. Q.E.D.
:::
