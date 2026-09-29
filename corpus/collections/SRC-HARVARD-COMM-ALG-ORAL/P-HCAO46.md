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

::: {.problem}
Let $M$ be a finitely generated $A$-module, and let $x_1,\ldots,x_n\in M$.
Suppose that $x_1,\ldots,x_n$ generate $M_{\mathfrak m}$ for every maximal ideal $\mathfrak m$ of $A$.
Show that they generate $M$.
:::

::: {.solution}
Let
\[
N=Ax_1+\cdots+Ax_n\subseteq M,
\qquad
Q=M/N.
\]
The quotient $Q$ is finitely generated.

::: pf

::: {.pf-step #q-localizes-to-zero}
For every maximal ideal $\mathfrak m$ of $A$, one has $Q_{\mathfrak m}=0$.

::: pf-proof
Localization is exact, so
\[
Q_{\mathfrak m}\cong M_{\mathfrak m}/N_{\mathfrak m}.
\]
By hypothesis the images of $x_1,\ldots,x_n$ generate $M_{\mathfrak m}$, hence
$N_{\mathfrak m}=M_{\mathfrak m}$.
:::

:::

::: pf-step
Therefore $Q=0$.

::: pf-proof
If $Q\ne0$, choose $0\ne q\in Q$. The ideal $\operatorname{Ann}(q)$ is proper,
so it lies in a maximal ideal $\mathfrak m$. If $q/1=0$ in $Q_{\mathfrak m}$,
some $s\notin\mathfrak m$ would satisfy $sq=0$, so
$s\in\operatorname{Ann}(q)\subseteq\mathfrak m$, a contradiction. Hence
$Q_{\mathfrak m}\ne0$, contradicting step [](#q-localizes-to-zero){.pf-ref}.

Thus $M=N$, so $x_1,\ldots,x_n$ generate $M$.
:::

:::

:::
:::
