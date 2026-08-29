---
schema: qual/card@1
id: E-F6IXU
kind: exercise
title: Translation is continuous in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Density
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- $\star$: Prove continuity in $L^1$, i.e.
  \[
  f \in L^{1} \Longrightarrow \lim _{h \rightarrow 0} \int|f(x+h)-f(x)|=0
  .\]
:::


::: {.solution}
**Goal:** Prove continuity of translation in $L^1(\RR)$: for $f \in L^1$, $\lim_{h \to 0} \int |f(x+h) - f(x)|\,dx = 0$.

<1>1. The claim holds for $\varphi = \chi_{[a,b]}$, the indicator of a compact interval.
    <2>1. $\int |\chi_{[a,b]}(x+h) - \chi_{[a,b]}(x)|\,dx \leq 2|h|$.
        Proof: the symmetric difference of $[a,b]$ and $[a,b] - h$ has Lebesgue measure at most $2|h|$ (each endpoint contributes at most $|h|$).
    <2>2. Q.E.D.
        Proof: <2>1 tends to $0$ as $h \to 0$.
<1>2. The claim holds for every step function $s = \sum_{i=1}^k c_i \chi_{I_i}$ (finite linear combination of interval indicators).
    Proof: by <1>1 and the triangle inequality, $\int |s(x+h) - s(x)|\,dx \leq \sum_i |c_i| \int |\chi_{I_i}(x+h) - \chi_{I_i}(x)|\,dx \to 0$ as $h \to 0$.
<1>3. Step functions are dense in $L^1(\RR)$.
    Proof: step functions (finite linear combinations of interval indicators) contain the compactly supported continuous functions in the $L^1$ metric and are themselves dense in $L^1$; equivalently, simple functions approximate $f$ and each measurable set is approximated by finite unions of intervals in measure.
<1>4. The claim holds for arbitrary $f \in L^1$.
    <2>1. Fix $\eps > 0$ and choose a step function $s$ with $\norm{f - s}_1 < \eps/3$.
        Proof: density, <1>3.
    <2>2. For $|h|$ small, $\int |s(x+h) - s(x)|\,dx < \eps/3$.
        Proof: <1>2.
    <2>3. $\int |f(x+h) - f(x)|\,dx < \eps$.
        Proof: by the triangle inequality, $\int |f(x+h) - f(x)|\,dx \leq \int |f(x+h) - s(x+h)|\,dx + \int |s(x+h) - s(x)|\,dx + \int |s(x) - f(x)|\,dx = \norm{f - s}_1 + \int |s(x+h) - s(x)|\,dx + \norm{f - s}_1 < \eps/3 + \eps/3 + \eps/3 = \eps$, using translation invariance of the integral on the first term.
<1>5. Q.E.D.
    Proof: <1>4 shows the limit is $0$ for every $f \in L^1$.
:::
