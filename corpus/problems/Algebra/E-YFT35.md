---
schema: qual/card@1
id: E-YFT35
kind: problem
title: $\mathbb{F}_{p^n}$ is the splitting field of $x^{p^n}-x$ over $\mathbb{F}_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Splitting Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Identified the root set as the unique field of p^n elements.
---

::: {.exercise}
Let $p$ be prime and $n\ge1$. Prove that $\mathbb F_{p^n}$ is the splitting field over $\mathbb F_p$ of
\[
x^{p^n}-x.
\]
:::

::: {.solution}
Let
\[
f(x)=x^{p^n}-x\in\mathbb F_p[x].
\]
Its derivative is
\[
f'(x)=-1,
\]
so all roots are simple.

In an algebraic closure of $\mathbb F_p$, let
\[
S=\{a:a^{p^n}=a\}.
\]
Because Frobenius powers respect addition and multiplication in characteristic $p$, $S$ is closed under addition, subtraction, and multiplication; if $a\ne0$ lies in $S$, then
\[
(a^{-1})^{p^n}=a^{-1}.
\]
Thus $S$ is a field. Since $f$ has degree $p^n$ and is separable, its splitting field contains exactly $p^n$ roots, so
\[
|S|=p^n.
\]
Therefore $S$ is the finite field $\mathbb F_{p^n}$.

Equivalently, every $a\in\mathbb F_{p^n}$ satisfies $a^{p^n}=a$: for $a\ne0$ this follows from $|\mathbb F_{p^n}^\times|=p^n-1$, and it is trivial for $a=0$. Hence $f$ splits completely over $\mathbb F_{p^n}$, and its roots generate that field. Thus $\mathbb F_{p^n}$ is its splitting field over $\mathbb F_p$.
:::
