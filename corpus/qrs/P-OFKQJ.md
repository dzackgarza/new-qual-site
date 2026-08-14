---
schema: qual/card@1
id: P-OFKQJ
kind: problem
title: "Let $a_n(z)$ be an analytic sequence in a domain $D$ such that $\\displaystyle \\sum_{n=0}^\\infty |a_n(z)|$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-convergence
  - series-of-functions
  - cauchy-estimates
  - holomorphic-functions
relations: []
review: draft
---

::: {.problem title="?"}
Let $a_n(z)$ be an analytic sequence in a domain $D$ such that $\displaystyle \sum_{n=0}^\infty |a_n(z)|$ converges uniformly on bounded and closed sub-regions of $D$.
Show that $\displaystyle \sum_{n=0}^\infty |a'_n(z)|$ converges uniformly on bounded and closed sub-regions of $D$.
:::

::: {.solution}
\envlist

- Show a stronger statement: if $f_n\to f$ uniformly with each $f_n$ holomorphic on every compact subset of $D$ then $f_n'\to f'$ on every compact subset of $D$.

- We have $\norm{f_n-f}_{\infty, D}\to 0$, the sup norm on $D$.

- Pick a $\gamma$ in $\interior{D}$
:::
