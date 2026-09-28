---
schema: qual/card@1
id: E-OMK54
kind: problem
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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
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
Let $m$ be Lebesgue measure on $\RR^n$, $\tau_h f(x) = f(x + h)$, and $f_\delta(x) = \delta^{-n}f(x/\delta)$ for $\delta > 0$.

<1>1. For measurable $f \geq 0$ or $f \in L^1$, $\int \tau_h f = \int f$ and $\int f_\delta = \int f$.

<2>1. The identities hold for $f = \chi_E$ with $E$ measurable.

::: {.proof}
$\tau_h\chi_E = \chi_{E-h}$ and $(\chi_E)_\delta = \delta^{-n}\chi_{\delta E}$, and Lebesgue measure satisfies $m(E - h) = m(E)$ and $m(\delta E) = \delta^n m(E)$.
:::

<2>2. Q.E.D.

::: {.proof}
By linearity, step <2>1 gives the identities for nonnegative simple functions. For measurable $f \geq 0$ choose simple $0 \leq s_k \nearrow f$; then $\tau_h s_k \nearrow \tau_h f$ and $(s_k)_\delta \nearrow f_\delta$, and the monotone convergence theorem passes the identities to $f$. For $f \in L^1$ apply this to $f^+$ and $f^-$.
:::

<1>2. For $f \in L^1$, $\|\tau_h f - f\|_1 \to 0$ as $h \to 0$.

<2>1. The claim holds for $f = \chi_I$ with $I$ a bounded box.

::: {.proof}
$\|\tau_h\chi_I - \chi_I\|_1 = m(I \triangle (I - h))$, and $I \triangle (I-h)$ is contained in the set of points within distance $|h|$ of $\partial I$, whose measure tends to $0$ with $h$.
:::

<2>2. Step functions, finite linear combinations of indicators of bounded boxes, are dense in $L^1$.

::: {.proof}
Simple functions are dense in $L^1$. For $m(E) < \infty$ and $\eps > 0$, outer regularity gives an open $U \supseteq E$ with $m(U \setminus E) < \eps$. $U$ is a countable union of almost disjoint closed cubes, so a finite union $A$ of them has $m(U \setminus A) < \eps$, and $\|\chi_E - \chi_A\|_1 < 2\eps$.
:::

<2>3. Q.E.D.

::: {.proof}
Given $\eps > 0$, step <2>2 gives a step function $s$ with $\|f - s\|_1 < \eps/3$, and step <2>1 with the triangle inequality gives $\|\tau_h s - s\|_1 < \eps/3$ for $|h|$ small. By step <1>1, $\|\tau_h f - \tau_h s\|_1 = \|f - s\|_1$, so $\|\tau_h f - f\|_1 < \eps$ for $|h|$ small.
:::

<1>3. $E$ is measurable if and only if $E = F \sqcup Z$ with $F$ an $F_\sigma$ set and $Z$ null, if and only if $E = G \setminus Z'$ with $G$ a $G_\delta$ set and $Z'$ null.

<2>1. If $E$ is measurable, then $E = F \sqcup Z$ as stated.

::: {.proof}
Outer regularity applied to $E^c$ gives closed $F_k \subseteq E$ with $m(E \setminus F_k) < 1/k$. Put $F = \bigcup_k F_k$ and $Z = E \setminus F$. Then $F$ is $F_\sigma$, $F \cap Z = \emptyset$, and $m(Z) \leq m(E \setminus F_k) < 1/k$ for every $k$.
:::

<2>2. If $E$ is measurable, then $E = G \setminus Z'$ as stated.

::: {.proof}
Outer regularity gives open $G_k \supseteq E$ with $m(G_k \setminus E) < 1/k$. Put $G = \bigcap_k G_k$ and $Z' = G \setminus E$. Then $G$ is $G_\delta$, $E = G \setminus Z'$, and $m(Z') \leq m(G_k \setminus E) < 1/k$ for every $k$.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2 are the forward implications. Conversely, $F_\sigma$ and $G_\delta$ sets are Borel, null sets are Lebesgue measurable, and unions and differences of measurable sets are measurable.
:::

<1>4. $m(E) = \sup\theset{m(K) : K \subseteq E \text{ compact}}$ if and only if for every $\eps > 0$ there is a compact $K \subseteq E$ with $m(E) - \eps \leq m(K) \leq m(E)$.

::: {.proof}
Every compact $K \subseteq E$ has $m(K) \leq m(E)$, so $m(E)$ is an upper bound of the set $S = \theset{m(K)}$. The supremum equals the upper bound $m(E)$ exactly when no $m(E) - \eps$ with $\eps > 0$ is an upper bound of $S$, which is the stated condition.
:::

<1>5. If $\mu(X) < \infty$ and $f \in L^\infty(\mu)$, then $\|f\|_p \to \|f\|_\infty$ as $p \to \infty$.

::: {.proof}
If $\mu(X) = 0$ both sides vanish; assume $\mu(X) > 0$. Upper bound: $\|f\|_p \le \|f\|_\infty\mu(X)^{1/p} \to \|f\|_\infty$. Lower bound: for $0 < M < \|f\|_\infty$ the set $\theset{|f| > M}$ has positive finite measure, and $\|f\|_p \ge M\mu\theset{|f| > M}^{1/p} \to M$. So $M \le \liminf_p \|f\|_p \le \limsup_p \|f\|_p \le \|f\|_\infty$ for every such $M$.
:::
:::
