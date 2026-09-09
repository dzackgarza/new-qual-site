---
schema: qual/card@1
id: P-HCAO46
kind: problem
title: Local generators generate a finite module globally
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Modules
  - Nakayama's Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $M$ be a finitely generated $A$-module, and let $x_1,\ldots,x_n\in M$.
Suppose that $x_1,\ldots,x_n$ generate $M_{\mathfrak m}$ for every maximal ideal $\mathfrak m$ of $A$.
Show that they generate $M$.
:::

::: solution
Let
\[
N=Ax_1+\cdots+Ax_n\subseteq M,
\qquad
Q=M/N.
\]
The quotient $Q$ is finitely generated.

<1>1. For every maximal ideal $\mathfrak m$ of $A$, one has $Q_{\mathfrak m}=0$.
::: proof
Localization is exact, so
\[
Q_{\mathfrak m}\cong M_{\mathfrak m}/N_{\mathfrak m}.
\]
By hypothesis the images of $x_1,\ldots,x_n$ generate $M_{\mathfrak m}$, hence
$N_{\mathfrak m}=M_{\mathfrak m}$.
:::

<1>2. Therefore $Q=0$.
::: proof
If $Q\ne0$, choose $0\ne q\in Q$ and a maximal ideal containing
$\operatorname{Ann}(q)$. The same annihilator argument as usual shows that
$q/1\ne0$ in that localization, contradicting <1>1.
:::

Thus $M=N$, so $x_1,\ldots,x_n$ generate $M$.
:::
