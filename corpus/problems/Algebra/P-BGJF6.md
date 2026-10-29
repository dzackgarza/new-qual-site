---
schema: qual/card@1
id: P-BGJF6
kind: problem
title: Definition of a splitting field
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Polynomials
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
State the definition of the splitting field of a polynomial $f(x) \in F[x]$ over a field $F$.
Prove the existence and uniqueness (up to $F$-isomorphism) of splitting fields.
:::

::: {.solution}
A splitting field of $f\in F[x]$ is an extension $L/F$ such that

1. $f$ splits into linear factors in $L[x]$, and
2. $L$ is generated over $F$ by the roots of $f$.

::: pf

::: pf-step

A splitting field of $f$ over $F$ exists.

::: pf-proof

We show by induction on $\deg f$ that some extension of $F$ contains a field over which $f$ splits; the base case $\deg f\le1$ is trivial. If $f$ does not split over $F$, choose an irreducible factor $p$ of $f$ with $\deg p>1$ and set $E=F[x]/(p)$, a field because $p$ is irreducible. The class $\alpha$ of $x$ is a root of $p$, hence of $f$, so $f=(x-\alpha)f_1$ in $E[x]$ with $\deg f_1<\deg f$. By induction there is an extension $K/E$ over which $f_1$, and hence $f$, splits. The subfield of $K$ generated over $F$ by the roots of $f$ is a splitting field of $f$ over $F$.

:::

:::

::: {.pf-step #extend}

Let $L_1,L_2$ be splitting fields of $f$ over $F$, let $F\subseteq E\subseteq L_1$, and let $\varphi:E\to L_2$ be an $F$-embedding. For each root $\alpha\in L_1$ of $f$, $\varphi$ extends to an embedding $E(\alpha)\to L_2$.

::: pf-proof

Let $m\in E[x]$ be the minimal polynomial of $\alpha$ over $E$. Since $m\mid f$ in $E[x]$ and $\varphi$ fixes the coefficients of $f$, the transported polynomial $\varphi(m)$ divides $f$ in $\varphi(E)[x]$. Because $f$ splits in $L_2$, $\varphi(m)$ has a root $\beta\in L_2$. Since $E(\alpha)\cong E[x]/(m)$ and $\varphi(m)(\beta)=0$, the map $\varphi$ extends to $E(\alpha)\to L_2$ with $\alpha\mapsto\beta$.

:::

:::

::: pf-step

Any two splitting fields $L_1,L_2$ of $f$ over $F$ are $F$-isomorphic.

::: pf-proof

Starting from $E=F$ and the inclusion $F\to L_2$, apply step [](#extend){.pf-ref} once for each of the finitely many roots of $f$ in $L_1$. Since $L_1$ is generated over $F$ by these roots, this gives an $F$-embedding $\psi:L_1\to L_2$. The polynomial $f$ splits over $\psi(L_1)$, so $\psi(L_1)$ contains every root of $f$ in $L_2$. Since $L_2$ is generated over $F$ by those roots, $\psi(L_1)=L_2$, and $\psi$ is an $F$-isomorphism.

:::

:::

:::

:::
