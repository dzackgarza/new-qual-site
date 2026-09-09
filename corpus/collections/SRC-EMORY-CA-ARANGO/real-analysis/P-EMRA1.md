---
schema: qual/card@1
id: P-EMRA1
kind: problem
title: "Extension of measure from algebra to sigma-algebra"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Real Analysis Problem 1 in the preserved Emory qualifying-problems compilation collected by Santiago Arango.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Describe the process that extends a measure on an algebra $\mathcal{A}$ of subsets of $X$ to a complete measure defined on a $\sigma$-algebra $\mathcal{B}$ containing $\mathcal{A}$.
State the corresponding definitions and results (without proofs).
:::

::: {.solution}
<1>1. Start with a premeasure on an algebra.
::: {.proof}
An **algebra** $\mathcal A\subseteq\mathcal P(X)$ contains $\varnothing$ and is closed under complements in $X$ and finite unions.

A map
\[
\mu_0:\mathcal A\to[0,\infty]
\]
is a **premeasure** if $\mu_0(\varnothing)=0$ and whenever $A_1,A_2,\ldots\in\mathcal A$ are pairwise disjoint and $\bigcup_nA_n\in\mathcal A$, one has
\[
\mu_0\!\left(\bigcup_{n=1}^\infty A_n\right)
=\sum_{n=1}^\infty\mu_0(A_n).
\]
This is the hypothesis needed for the extension theorem.
:::

<1>2. Form the induced outer measure.
::: {.proof}
For every $E\subseteq X$, define
\[
\mu^*(E)
=
\inf\left\{
\sum_{n=1}^\infty\mu_0(A_n):
A_n\in\mathcal A,
\ E\subseteq\bigcup_{n=1}^\infty A_n
\right\}.
\]
An **outer measure** is a map $\mu^*:\mathcal P(X)\to[0,\infty]$ satisfying
\[
\mu^*(\varnothing)=0,
\qquad
E\subseteq F\Longrightarrow\mu^*(E)\le\mu^*(F),
\]
and countable subadditivity
\[
\mu^*\!\left(\bigcup_nE_n\right)
\le\sum_n\mu^*(E_n).
\]
The preceding formula produces an outer measure from $\mu_0$.
:::

<1>3. Select the Carathéodory-measurable sets.
::: {.proof}
A set $E\subseteq X$ is **Carathéodory measurable** for $\mu^*$ if
\[
\mu^*(T)
=
\mu^*(T\cap E)+\mu^*(T\setminus E)
\qquad\text{for every }T\subseteq X.
\]
Let
\[
\mathcal B
=
\{E\subseteq X:E\text{ is Carathéodory measurable}\}.
\]
Carathéodory's theorem states that $\mathcal B$ is a $\sigma$-algebra and that
\[
\mu:=\mu^*|_{\mathcal B}
\]
is a complete measure on $\mathcal B$.
:::

<1>4. State the extension properties.
::: {.proof}
For the outer measure constructed from the premeasure $\mu_0$,
\[
\mathcal A\subseteq\mathcal B
\qquad\text{and}\qquad
\mu(A)=\mu_0(A)\quad(A\in\mathcal A).
\]
Thus $\mu$ is a complete measure extending $\mu_0$ to a $\sigma$-algebra containing $\mathcal A$; in particular,
\[
\sigma(\mathcal A)\subseteq\mathcal B.
\]

If $\mu_0$ is $\sigma$-finite on $\mathcal A$, then its extension to $\sigma(\mathcal A)$ is unique. The Carathéodory $\sigma$-algebra $\mathcal B$ contains the completion of $\sigma(\mathcal A)$ with respect to this extension, and $\mu$ is complete on all of $\mathcal B$.
:::
:::
