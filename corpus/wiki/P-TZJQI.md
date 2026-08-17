---
schema: qual/card@1
id: P-TZJQI
kind: problem
title: "Show that $E$ is measurable iff $E$ is regular."
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Show that $E$ is measurable iff $E$ is regular.
:::
::: {.solution}
> **AI-Generated Solution**

*Setup note.* For Lebesgue measure on $\RR^n$, "regular" means: $\mu^*(E) = \inf\{\mu(G) : G \supseteq E,\ G \text{ open}\}$ (outer) and $\mu_*(E) = \sup\{\mu(F) : F \subseteq E,\ F \text{ compact}\}$ (inner, with $\mu_*(E) = \mu^*(E)$). We prove measurability is equivalent to regularity.

<1>1. Measurable $\Rightarrow$ outer regular.
Proof: for measurable $E$ with $\mu(E) < \infty$, by definition of $\mu^*$ there is a cover by boxes with total measure $< \mu(E) + \eps$; the open set $G$ obtained by enlarging the boxes slightly contains $E$ and has $\mu(G) \le \mu(E) + \eps$.
For $\mu(E) = \infty$, exhaust by $E \cap B(0,k)$ and take unions.
Hence $\mu(E) = \inf_{G \supseteq E \text{ open}}\mu(G)$.
<1>2. Measurable $\Rightarrow$ inner regular.
Proof: for measurable $E$ with $\mu(E) < \infty$, first approximate by closed sets: $E^c$ is measurable, so by <1>1 there is open $G \supseteq E^c$ with $\mu(G \setminus E^c) < \eps$, giving closed $F = G^c \subseteq E$ with $\mu(E \setminus F) = \mu(G \setminus E^c) < \eps$.
Then approximate the closed set by compact sets ($F \cap B(0,k) \nearrow F$), and for infinite measure decompose $E$ into finite-measure pieces.
Hence $\mu(E) = \sup_{F \subseteq E \text{ compact}}\mu(F)$.
<1>3. Regular $\Rightarrow$ measurable.
Proof: outer regularity gives open $G_k \supseteq E$ with $\mu(G_k) \le \mu^*(E) + 1/k$; let $V = \cap_k G_k$, a $G_\delta$ containing $E$, with $\mu(V) = \mu^*(E)$.
Similarly inner regularity gives compact $F_k \subseteq E$ with $\mu(F_k) \ge \mu_*(E) - 1/k$; let $H = \cup_k F_k$, an $F_\sigma$ inside $E$, with $\mu(H) = \mu_*(E)$.
Regularity means $\mu^*(E) = \mu_*(E)$, so $E = V \setminus (V \setminus H)$ with $V$ measurable and $V \setminus H$ null (as $\mu(V \setminus H) = \mu(V) - \mu(H) = 0$); hence $E$ is measurable.
<1>4. Q.E.D.
:::
