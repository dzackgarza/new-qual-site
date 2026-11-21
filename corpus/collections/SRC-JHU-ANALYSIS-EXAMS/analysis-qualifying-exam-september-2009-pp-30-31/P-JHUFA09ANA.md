---
schema: qual/card@1
id: P-JHUFA09ANA
kind: problem
title: Pointwise versus uniform convergence of continuous functions
classification:
  areas:
  - real-analysis
  topics:
  - Convergence Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Analysis Qualifying Exam, September 2009, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Suppose $(f_n)$ is a sequence of continuous functions on $[0,1]$ converging pointwise to a continuous function $f$. Must $f_n\to f$ uniformly? Prove your answer.
:::

::: {.solution}

The counterexample and its verification are the card's own; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

::: pf

::: {.pf-step #no}
There is a sequence of continuous $f_{n}:[0,1]\to\RR$ converging pointwise to a continuous $f$ and not converging uniformly to it.

::: pf-proof

::: {.pf-step #definition}
Put $f_{n}(x)=\max\{1-n\abs{x-1/n},\,0\}$ for $x\in[0,1]$ and $f\equiv0$.

::: pf-proof
Each $f_{n}$ is continuous, being the maximum of the continuous functions $x\mapsto1-n\abs{x-1/n}$ and the constant $0$. And $f_{n}(x)>0$ exactly when $\abs{x-1/n}<1/n$, that is exactly when $0<x<2/n$; so $f_{n}$ is supported in $[0,2/n]$ and $f_{n}(0)=0$.
:::

:::

::: {.pf-step #pointwise}
$f_{n}(x)\to0$ for every $x\in[0,1]$.

::: pf-proof
$f_{n}(0)=0$ for every $n$. If $x\in(0,1]$, choose $N$ with $2/N<x$; then for $n\ge N$ one has $x>2/n$, so $x$ lies outside the support of $f_{n}$ and $f_{n}(x)=0$. Hence $f_{n}(x)=0$ for all $n\ge N$.
:::

:::

::: {.pf-step #not-uniform}
$\norm{f_{n}}_{\infty}=1$ for every $n$, so $\sup_{x}\abs{f_{n}(x)-f(x)}=1$ does not tend to $0$.

::: pf-proof
$f_{n}(1/n)=1$ and $0\le f_{n}\le1$ everywhere, so the supremum norm is $1$; and $f\equiv0$, so $\sup_{x\in[0,1]}\abs{f_{n}(x)-f(x)}=1$ for every $n$. Uniform convergence would require this supremum to tend to $0$.
:::

:::

::: {.pf-qed}
Steps [](#pointwise){.pf-ref} and [](#not-uniform){.pf-ref} exhibit the sequence, so the answer to the question is no: pointwise convergence of continuous functions to a continuous limit does not force uniform convergence.
:::

:::

:::
:::
:::
