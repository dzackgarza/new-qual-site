---
schema: qual/card@1
id: P-TEVPO
kind: problem
title: $\lim_{x\to 0}f(x)=0$ and $g$ bounded imply $f(x)g(x)\to 0$, with a counterexample
  if $g$ is unbounded
classification:
  areas:
  - prelim
  topics:
  - Limits
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, and the boundedness hypothesis repaired. The prose wrote "suppose there exists M_g such that for all x, g(x) < M" and then divided by M_g; a one-sided bound and a possibly zero or negative M_g do not support that division. The card now takes M > 0 with |g(x)| <= M, which is what boundedness gives and what the estimate needs, and says so in a step. The example in (b) now defines g at 0 so that it is a function on all of R, and witnesses unboundedness by g(1/n) = n and the failure of the conclusion by f(x)g(x) = 1. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. The quantified statements of the exercise are unchanged.
---

::: {.problem}
Suppose $f$ and $g$ are functions mapping $\RR$ into itself with $\lim_{x\to 0} f(x) = 0$.

(a) Prove from the $\varepsilon$–$\delta$ definition that if $g$ is bounded, then $\lim_{x\to 0} f(x)g(x) = 0$ as well.

(b) Give an example to show that the boundedness hypothesis cannot be omitted from part (a).
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #bounded}
Boundedness of $g$ means there is $M>0$ with $\abs{g(x)}\le M$ for every $x\in\RR$.

::: pf-proof
A function $g:\RR\to\RR$ is bounded when there is a real $N$ with $\abs{g(x)}\le N$ for all $x$; taking $M=\max\{N,1\}>0$ gives a positive bound, and the bound $\abs{g(x)}\le M$ is preserved.
:::

:::

::: {.pf-step #parta}
If $g$ is bounded then $\lim_{x\to0}f(x)g(x)=0$.

::: pf-proof
Let $\varepsilon>0$ and let $M>0$ bound $\abs{g}$. Since $\lim_{x\to0}f(x)=0$, there is $\delta>0$ such that $0<\abs{x}<\delta$ implies $\abs{f(x)}<\varepsilon/M$, the number $\varepsilon/M$ being positive. With that $\delta$, for $0<\abs{x}<\delta$,
$$
\abs{f(x)g(x)}=\abs{f(x)}\abs{g(x)}<\frac{\varepsilon}{M}\cdot M=\varepsilon,
$$
so $\lim_{x\to0}f(x)g(x)=0$ by the $\varepsilon$-$\delta$ definition. (If $\abs{g}$ is bounded only by some $N\le0$, then $g\equiv0$ and the conclusion is immediate.)
:::

:::

::: {.pf-step #partb}
The boundedness hypothesis cannot be omitted.

::: pf-proof
Let $f(x)=x$ and let $g(x)=1/x$ for $x\ne0$, $g(0)=0$; both map $\RR$ into $\RR$. Then $\lim_{x\to0}f(x)=0$, and $g$ is unbounded on every neighbourhood of $0$, since $g(1/n)=n$. But $f(x)g(x)=1$ for every $x\ne0$, so $\lim_{x\to0}f(x)g(x)=1\ne0$. Thus the conclusion of part (a) fails without boundedness.
:::

:::

:::
:::
