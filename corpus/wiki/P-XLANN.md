---
schema: qual/card@1
id: P-XLANN
kind: problem
title: $\|g\|_p\to\|g\|_\infty$ as $p\to\infty$ on $[0,1]$, and $\|\Lambda_g\|_{(L^1)^*}=\|g\|_\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - L∞
  - Lp Spaces
  - Riesz Representation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Let $g\in L^\infty([0, 1])$.

a. Prove
\[
\norm{g}_{L^p([0, 1])}  \converges{p\to\infty}\to \norm{g}_{L^\infty([0, 1])}
.\]

b. Prove that the map
\[
\Lambda_g: L^1([0, 1]) &\to \CC \\
f &\mapsto \int_0^1 fg
\]
  defines an element of $L^1([0, 1])\dual$ with $\norm{\Lambda_g}_{L^1([0, 1])\dual}= \norm{g}_{L^\infty([0, 1])}$.
:::
::: {.solution}
<1>1. (a) $\norm{g}_{L^p} \to \norm{g}_{L^\infty}$ as $p \to \infty$.
    Proof: $\mu([0,1]) = 1 < \infty$. Upper bound: $\norm{g}_p \le \norm{g}_\infty \mu([0,1])^{1/p} = \norm{g}_\infty$, so $\limsup_p \norm{g}_p \le \norm{g}_\infty$. Lower bound: for any $M < \norm{g}_\infty$, $\mu\{|g| > M\} > 0$ and $\norm{g}_p \ge M\,\mu\{|g|>M\}^{1/p} \to M$; hence $\liminf_p \norm{g}_p \ge M$ for all $M < \norm{g}_\infty$, so $\liminf_p \norm{g}_p \ge \norm{g}_\infty$. Combining: the limit exists and equals $\norm{g}_\infty$. (If $\norm{g}_\infty = 0$ it is trivial.)
<1>2. (b) $\Lambda_g$ is well-defined and bounded on $L^1$.
    Proof: $\Lambda_g(f) = \int_0^1 fg$; since $|fg| \le |f|\norm{g}_\infty$, the integral converges and
    \[
    |\Lambda_g(f)| \le \int_0^1 |f||g| \le \norm{g}_\infty \int_0^1 |f| = \norm{g}_\infty \norm{f}_1,
    \]
    so $\Lambda_g \in L^1([0,1])\dual$ with $\norm{\Lambda_g} \le \norm{g}_\infty$.
<1>3. $\norm{\Lambda_g} \ge \norm{g}_\infty$.
    Proof: if $\norm{g}_\infty = 0$ there is nothing to prove. Otherwise fix $M < \norm{g}_\infty$ and let $E = \{|g| \ge M\}$ (or $> M$), a set of positive measure. Take
    \[
    f(x) = \frac{\overline{g(x)}}{|g(x)|}\,\frac{\chi_E(x)}{\mu(E)} \quad (\text{with the factor } 1 \text{ where } g = 0),
    \]
    so $f \in L^1$, $\norm{f}_1 = 1$, and $\Lambda_g(f) = \frac{1}{\mu(E)}\int_E |g| \ge M$. Hence $\norm{\Lambda_g} \ge M$ for all $M < \norm{g}_\infty$, so $\norm{\Lambda_g} \ge \norm{g}_\infty$.
<1>4. Equality.
    Proof: <1>2 and <1>3 give $\norm{\Lambda_g} = \norm{g}_\infty$. (This is the norm computation underlying Riesz's theorem: the map $g \mapsto \Lambda_g$ is an isometry of $L^\infty$ into $(L^1)\dual$.)
<1>5. Q.E.D.
:::
