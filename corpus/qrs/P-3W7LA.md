---
schema: qual/card@1
id: P-3W7LA
kind: problem
title: "Prove Liouville's theorem: suppose $f:\\CC\\to\\CC$ is entire and bounded.\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - cauchy-estimates
  - entire-functions
relations: []
review: draft
solved: true
---
Prove Liouville's theorem: suppose $f:\CC\to\CC$ is entire and bounded. 
Use Cauchy's formula to prove that $f'\equiv 0$ and hence $f$ is constant.

:::{.solution}
:::{.concept}

:::
- Suffices to prove $f' = 0$ because $\CC$ is connected (see Stein Ch 1, 3.4)
  - Idea: Fix $w_0$, show $f(w) = f(w_0)$ for any $w\neq w_0$
  - Connected = Path connected in $\CC$, so take $\gamma$ joining $w$ to $w_0$.
  - $f$ is a primitive for $f'$, and $\int_\gamma f' = f(w) - f(w_0)$, but $f'=0$.
- Fix $z_0\in \CC$, let $B$ be the bound for $f$, so $\abs{f(z)} \leq B$ for all $z$.
- Apply Cauchy inequalities: if $f$ is holomorphic on $U\supset \bar D_R(z_0)$ then setting $\norm{f}_C \definedas \sup_{z\in C} \abs{f(z)}$,
  \begin{align*}
  \abs{f^{(n)} (z_0)} \leq {n! \norm{f}_C \over R^n}
  .\end{align*}
  - Yields $\abs{ f'(z_0) } \leq B/R$
- Take $R\to \infty$, QED.
:::


