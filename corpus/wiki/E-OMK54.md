---
schema: qual/card@1
id: E-OMK54
kind: exercise
title: Translation invariance of Lebesgue integral, $L^{1}$ continuity, and regularity
  of measurable sets
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Lp Spaces
relations: []
review: draft
---

::: {.exercise}
\envlist

- Prove the Lebesgue integral is translation/dilation invariant.

- Prove continuity in $L_1$: $\norm{\tau_hf - f}\converges{h\to 0}\too 0$.

- Prove that $E$ is measurable $\iff$ $E = F \disjoint Z$ with $F\in F_\sigma$ and $Z$ null $\iff$ $E = G\sm Z$ with $G\in G_\delta$ and $Z$ null.

- Show that $m(E) = \sup_{K \subseteq E}m(K) \iff$ there exists $K = K(\eps)$ with $m(K) \in [m(E) - \eps, m(E)]$.

  - What's most useful here is the proof technique, not so much the result itself.

- Apply Fubini and Tonelli to literally anything.

- Prove that $\norm{f}_p\to \norm{f}_\infty$ over a finite measure space.

- Apply Cauchy-Schwarz to literally anything, in the form of $\norm{fg}_1 \leq \norm{f}_2 \norm{g}_2$.
:::

::: {.solution}
> **AI-Generated Solution**

**Note:** the card mixes concrete theorems with study advice ("apply Fubini to literally anything", "apply Cauchy–Schwarz to anything"); the solution covers the concrete statements.

<1>1. Translation and dilation invariance of the Lebesgue integral: $\int \tau_h f = \int f$ where $\tau_h f(x) = f(x + h)$, and $\int f_\delta = \int f$ where $f_\delta(x) = \delta^{-n}f(x/\delta)$.
<2>1. Both hold for indicators: $m(E + h) = m(E)$ and $m(\delta E) = \delta^n m(E)$.
Proof: translation and dilation invariance of Lebesgue measure (for measurable $E$). <2>2. Both hold for non-negative simple functions, then for non-negative measurable $f$ by monotone convergence, then for $f \in L^1$ by positive/negative parts.
Proof: linearity, then the standard MCT argument.

<1>2. Continuity in $L^1$: for $f \in L^1$, $\|\tau_h f - f\|_1 \to 0$ as $h \to 0$.
<2>1. The claim holds for indicators of measurable sets of finite measure.
Proof: approximate by open sets / finite unions of boxes (regularity); the measure of the symmetric difference $E \triangle (E + h) \to 0$ as $h \to 0$.
<2>2. The claim holds for simple functions, then for all $f \in L^1$ by density and the $\eps/3$ argument.
Proof: simple functions are dense in $L^1$, and $\|\tau_h f - \tau_h s\|_1 = \|f - s\|_1$ by translation invariance.

<1>3. Measurability structure: $E$ measurable $\iff$ $E = F \disjoint Z$ with $F \in F_\sigma$ and $Z$ null $\iff$ $E = G \sm Z'$ with $G \in G_\delta$ and $Z'$ null.
<2>1. $E$ measurable $\implies$ $E = F \cup Z$ with $F \in F_\sigma$, $Z$ null: take closed $F_k \subseteq E$ with $m(E \setminus F_k) < 1/k$ (inner regularity), set $F = \bigcup_k F_k$ and $Z = E \setminus F$.
Proof: $Z = E \setminus F \subseteq E \setminus F_k$ for each $k$, so $m(Z) \le 1/k$ for all $k$; hence $m(Z) = 0$; $F$ is an $F_\sigma$ (countable union of closed sets), and $F \cap Z = \emptyset$.
<2>2. $E$ measurable $\implies$ $E = G \setminus Z'$ with $G \in G_\delta$, $Z'$ null: take open $G_k \supseteq E$ with $m(G_k \setminus E) < 1/k$, set $G = \bigcap_k G_k$ and $Z' = G \setminus E$.
Proof: dual argument to <2>1 (outer regularity); $G$ is a $G_\delta$ and $m(Z') = 0$.
<2>3. Conversely, $F \cup Z$ with $F \in F_\sigma$ and $Z$ null is measurable, and $G \setminus Z'$ with $G \in G_\delta$ and $Z'$ null is measurable.
Proof: $F_\sigma$ sets and $G_\delta$ sets are Borel, hence measurable; adding or removing null sets preserves measurability.
<2>4. Q.E.D. Proof: <2>1–<2>3.

<1>4. Inner regularity equivalence: $m(E) = \sup\{m(K) : K \subseteq E \text{ compact}\}$ iff for every $\eps > 0$ there is a compact $K \subseteq E$ with $m(K) \ge m(E) - \eps$.
<2>1. ($\Leftarrow$) is immediate: the condition says $m(E) - \eps$ is never an upper bound of the compact-measures below $E$; hence the supremum is $\ge m(E)$, and $\le m(E)$ since $K \subseteq E$ gives $m(K) \le m(E)$.
Proof: definition of supremum.
<2>2. ($\Rightarrow$) if $m(E) = \sup_K m(K)$, then for each $\eps$ the value $m(E) - \eps$ is not an upper bound, so some compact $K \subseteq E$ has $m(K) > m(E) - \eps$.
Proof: definition of supremum.
<2>3. Q.E.D. Proof: <2>1 and <2>2.

<1>5. For finite measure: $\|f\|_p \to \|f\|_\infty$ as $p \to \infty$.
Proof: upper bound $\|f\|_p \le \|f\|_\infty\mu(X)^{1/p} \to \|f\|_\infty$; lower bound $\|f\|_p \ge M\mu\{|f| > M\}^{1/p} \to M$ for $M < \|f\|_\infty$; sandwich.
:::
