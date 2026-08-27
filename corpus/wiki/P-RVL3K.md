---
schema: qual/card@1
id: P-RVL3K
kind: problem
title: $L^p$ norms tend to $L^\infty$, the converse of dominated convergence, translation
  continuity, and $L^p$ inclusions
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
- Show that if $E\subseteq \RR^n$ is measurable with $\mu(E) < \infty$ and $f\in L^p(X)$ then $$\norm{f}_{L^p(X)} \converges{p\to\infty}\to \norm{f}_\infty.$$
- Is it true that the converse to the DCT holds? 
  I.e. if $\int f_n \to \int f$, is there a $g\in L^p$ such that $f_n < g$ a.e. for every $n$?
- Prove continuity in $L^p$: If $f$ is uniformly continuous then for all $p$, $$\norm{\tau_h f - f}_p \converges{h\to 0}\to 0.$$ 
- Prove the following inclusions of $L^p$ spaces for $m(X) < \infty$:
\[
L^\infty(X) &\subset L^2(X) \subset L^1(X) \\
\ell^2(\ZZ) &\subset \ell^1(\ZZ) \subset \ell^\infty(\ZZ)
.\]
:::
::: {.solution}
*Setup note.* The card bundles four facts; the inclusion line $\ell^2(\ZZ) \subset \ell^1(\ZZ)$ is backwards (the true inclusions are $\ell^1 \subset \ell^2 \subset \ell^\infty$), which we correct below. We treat $E \subseteq \RR^n$ with $\mu(E) < \infty$ and $f \in L^p(E)$.

<1>1. $\norm{f}_{L^p} \to \norm{f}_\infty$ as $p \to \infty$.
    Proof: for $p > q \ge 1$ with $f \in L^p \cap L^q$, Hölder gives $\norm{f}_p \le \norm{f}_\infty \mu(E)^{1/p}$, so $\limsup \norm{f}_p \le \norm{f}_\infty$. Conversely, if $\norm{f}_\infty > M$, then $\mu\{|f| > M\} > 0$ and $\norm{f}_p \ge M\,\mu\{|f|>M\}^{1/p}$, so $\liminf \norm{f}_p \ge M$; letting $M \nearrow \norm{f}_\infty$ gives $\liminf \norm{f}_p \ge \norm{f}_\infty$.
<1>2. The converse of the DCT fails.
    Proof: take $f_n = n\chi_{[1/(n+1),\,1/n)}$ on $[0,1]$; then $\int f_n = n/(n(n+1)) = 1/(n+1) \to 0 = \int 0$, but $\sup_n f_n$ is not integrable ($\int \sup_n f_n = \sum_n \frac{1}{n+1} = \infty$), so no dominating $g \in L^p$ exists.
<1>3. Continuity in $L^p$: if $f$ is uniformly continuous, then $\norm{\tau_h f - f}_p \to 0$ as $h \to 0$.
    Proof: $\tau_h f(x) = f(x-h)$. For uniformly continuous $f$: first for $f \in L^p$ with compact support, uniform continuity makes $\norm{\tau_h f - f}_\infty \to 0$, hence $\norm{\tau_h f - f}_p \le \mu(\supp)^{1/p}\norm{\tau_h f - f}_\infty \to 0$; for general $f \in L^p$, truncate to a large set where the $L^p$ tail is small ($\eps/3$ argument), using that the truncation is uniformly continuous and the tail is controlled by $L^p$-continuity of translation on a finite-measure set.
<1>4. $L^\infty(E) \subset L^2(E) \subset L^1(E)$ when $\mu(E) < \infty$.
    Proof: $\norm{f}_1 \le \mu(E)^{1/2}\norm{f}_2$ and $\norm{f}_2 \le \mu(E)^{1/2}\norm{f}_\infty$ by Hölder; so $f \in L^\infty \Rightarrow f \in L^2 \Rightarrow f \in L^1$. The discrete analogues (counting measure) run the other way: $\norm{a}_{\ell^2} \le \norm{a}_{\ell^1}$ and $\norm{a}_{\ell^\infty} \le \norm{a}_{\ell^2}$, i.e. $\ell^1(\ZZ) \subset \ell^2(\ZZ) \subset \ell^\infty(\ZZ)$ (the card's line has the first inclusion reversed); a counterexample to $\ell^2 \subset \ell^1$ is $a_n = 1/n$.
<1>5. Q.E.D.
:::
