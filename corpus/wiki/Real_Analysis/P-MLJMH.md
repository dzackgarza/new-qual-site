---
schema: qual/card@1
id: P-MLJMH
kind: problem
title: $L^\infty(\RR^n)$ is a Banach space, and $L^1\cap L^\infty\subset L^2$ with
  $\|f\|_2\le\|f\|_1^{1/2}\|f\|_\infty^{1/2}$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Lp Spaces
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
a. In parts:
  - Given a definition of $L^\infty(\RR^n)$.
  - Verify that $\norm{\wait}_\infty$ defines a norm on $L^\infty(\RR^n)$.
  - Carefully proved that $(L^\infty(\RR^n), \norm{\wait}_\infty)$ is a Banach space.

b. Prove that for any measurable $f:\RR^n \to \CC$,
\[
L^1(\RR^n) \intersect L^\infty(\RR^n) \subset L^2(\RR^n) \qtext{and} \norm{f}_2 \leq \norm{f}_1^{1\over 2} \cdot \norm{f}_\infty^{1\over 2}
.\]
:::
::: {.solution}
<1>1. (a) Definition: $L^\infty(\RR^n)$ is the space of (equivalence classes of) measurable $f : \RR^n \to \CC$ with $\|f\|_\infty := \inf\{M : |f(x)| \le M \text{ for a.e. } x\} < \infty$, the essential supremum.
    Proof: definition; functions equal a.e. are identified.

<1>2. $\|\cdot\|_\infty$ is a norm on $L^\infty$.
    <2>1. Positive definiteness: $\|f\|_\infty \ge 0$; $\|f\|_\infty = 0$ iff $f = 0$ a.e.
        Proof: $\|f\|_\infty = 0$ iff $|f| \le \eps$ a.e. for every $\eps > 0$, iff $f = 0$ a.e. (intersect the null sets).
    <2>2. Homogeneity: $\|\lambda f\|_\infty = |\lambda|\|f\|_\infty$.
        Proof: $|\lambda f(x)| \le M$ a.e. iff $|f(x)| \le M/|\lambda|$ a.e.
    <2>3. Triangle inequality: $\|f + g\|_\infty \le \|f\|_\infty + \|g\|_\infty$.
        Proof: $|f(x) + g(x)| \le |f(x)| + |g(x)| \le \|f\|_\infty + \|g\|_\infty$ a.e. (both inequalities hold off null sets; their union is null).

<1>3. $L^\infty$ is complete (a Banach space).
    <2>1. Let $(f_k)$ be Cauchy in $\|\cdot\|_\infty$; for $m, n$ large, $|f_m(x) - f_n(x)| \le \|f_m - f_n\|_\infty$ for a.e. $x$ — but the exceptional null set depends on the pair; take the union over all pairs of a countable subsequence to get a single null set $N$ off which $(f_k(x))$ is uniformly Cauchy.
        Proof: choose $k_j$ with $\|f_{k_{j+1}} - f_{k_j}\|_\infty < 2^{-j}$; off $N = \bigcup_j \{|f_{k_{j+1}} - f_{k_j}| > \|f_{k_{j+1}} - f_{k_j}\|_\infty\}$ (null), the subsequence converges uniformly to a limit $f$; define $f = 0$ on $N$.
    <2>2. $f$ is measurable and bounded a.e.: $f \in L^\infty$.
        Proof: $f$ is the pointwise limit of measurable functions (measurable); off $N$, $|f| \le \|f_{k_1}\|_\infty + \sum_j 2^{-j} < \infty$.
    <2>3. $\|f_k - f\|_\infty \to 0$.
        Proof: $\|f_k - f\|_\infty \le \|f_k - f_{k_j}\|_\infty + \|f_{k_j} - f\|_\infty$; both terms $\to 0$ (Cauchy data; uniform convergence on $X \setminus N$ gives the second).

<1>4. (b) For measurable $f$: $L^1 \cap L^\infty \subseteq L^2$ and $\|f\|_2 \le \|f\|_1^{1/2}\|f\|_\infty^{1/2}$.
    Proof: $\int |f|^2 = \int |f|^{1/2}|f|^{3/2}$-split... cleanly: $|f|^2 = |f| \cdot |f| \le |f|\cdot\|f\|_\infty$ a.e. (where $|f| \le \|f\|_\infty$ a.e.), so $\int |f|^2 \le \|f\|_\infty\int|f| = \|f\|_\infty\|f\|_1$; taking square roots gives $\|f\|_2 \le \|f\|_1^{1/2}\|f\|_\infty^{1/2}$.
:::
