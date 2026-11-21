---
schema: qual/card@1
id: P-A4JGH
kind: problem
title: Negation of uniform convergence and a pointwise but nonuniform example
classification:
  areas:
  - prelim
  topics:
  - Logic and Quantifiers
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the negation is
    derived from the stated definition by reversing the quantifiers, and the witness for
    the example is verified (f_n(x) = x/n tends to 0 pointwise; with eps_0 = 1, n = N+1 and
    x = n give |f_n(x)| = 1). The statement is true as printed; the prose stated the
    negation and the witness without deriving or checking them. The collection's provenance
    is the examination paper only, so no retained solution set covers the exercise and the
    argument is the card's own.
---

::: {.problem}
A sequence $\{f_n:\RR\to\RR\}_{n=1}^{\infty}$ converges uniformly to $f:\RR\to\RR$ if, for every $\varepsilon>0$, there is a positive integer $N$ such that
$$
n>N\quad\Longrightarrow\quad \abs{f_n(x)-f(x)}<\varepsilon
$$
for all $x\in\RR$.

(a) What must one check to show that a sequence does not converge uniformly?

(b) Give an example such that $f_n(x)$ converges to $f(x)$ for every $x\in\RR$, but the sequence does not converge uniformly.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #negation}
(a) Uniform convergence fails if and only if
$$
\exists\varepsilon_0>0\ \forall N\in\NN\ \exists n>N\ \exists x\in\RR:\quad\abs{f_n(x)-f(x)}\ge\varepsilon_0 .
$$

::: pf-proof
The definition says $\forall\varepsilon>0\ \exists N\ \forall n>N\ \forall x\in\RR:\abs{f_n(x)-f(x)}<\varepsilon$. Negating a quantified statement reverses each quantifier and negates the final inequality, giving $\exists\varepsilon>0\ \forall N\ \exists n>N\ \exists x\in\RR:\abs{f_n(x)-f(x)}\ge\varepsilon$, which is the displayed form with $\varepsilon_0$ naming the witness; so to disprove uniform convergence one must produce a single $\varepsilon_0>0$ such that no $N$ works, that is, such that later and later $n$ still have a point where the distance is at least $\varepsilon_0$.
:::

:::

::: {.pf-step #pointwise}
For $f_n(x)\coloneqq\frac xn$ and $f\equiv0$, one has $f_n(x)\to f(x)$ for every $x\in\RR$.

::: pf-proof
For fixed $x$ the sequence $x/n$ tends to $0$; at $x=0$ every term is $0$.
:::

:::

::: {.pf-step #not-uniform}
With $\varepsilon_0\coloneqq1$, every $N$ admits $n>N$ and $x\in\RR$ with $\abs{f_n(x)-f(x)}\ge\varepsilon_0$.

::: pf-proof
Given $N$, take $n=N+1>N$ and $x=n$. Then $f_n(x)=\frac nn=1$, so $\abs{f_n(x)-f(x)}=\abs{1-0}=1\ge\varepsilon_0$.
:::

:::

::: {.pf-step}
(b) The sequence $f_n(x)=\frac xn$ converges to $0$ pointwise on $\RR$ but not uniformly.

::: pf-proof
Step [](#pointwise){.pf-ref} gives the pointwise convergence, and steps [](#negation){.pf-ref} and [](#not-uniform){.pf-ref} exhibit the $\varepsilon_0>0$ which no $N$ defeats, so the convergence is not uniform.
:::

:::

:::
:::
