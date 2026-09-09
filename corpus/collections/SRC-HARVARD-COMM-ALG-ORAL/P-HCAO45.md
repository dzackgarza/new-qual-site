---
schema: qual/card@1
id: P-HCAO45
kind: problem
title: A finite module equal to every maximal-ideal multiple is zero
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Modules
  - Maximal Ideals
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
Let $M$ be a finitely generated $A$-module.
Suppose that $M=\mathfrak mM$ for every maximal ideal $\mathfrak m$ of $A$.
Show that $M=0$.
:::

::: solution
Assume for contradiction that $M\ne0$.

<1>1. There is a maximal ideal $\mathfrak m$ such that $M_{\mathfrak m}\ne0$.
::: proof
Choose $0\ne x\in M$. Its annihilator $\operatorname{Ann}(x)$ is a proper
ideal, so it lies in a maximal ideal $\mathfrak m$. If $x/1=0$ in
$M_{\mathfrak m}$, some $s\notin\mathfrak m$ would satisfy $sx=0$, forcing
$s\in\operatorname{Ann}(x)\subseteq\mathfrak m$, a contradiction.
:::

<1>2. Localizing the assumed equality $M=\mathfrak mM$ gives
\[
M_{\mathfrak m}=\mathfrak mA_{\mathfrak m}M_{\mathfrak m}.
\]
::: proof
Localization is exact and commutes with multiplication of a module by an ideal.
:::

<1>3. Nakayama's lemma gives $M_{\mathfrak m}=0$, contradiction.
::: proof
The module $M_{\mathfrak m}$ is finitely generated over the local ring
$A_{\mathfrak m}$, whose maximal ideal is $\mathfrak mA_{\mathfrak m}$.
Apply Nakayama to <1>2.
:::

Hence $M=0$.
:::
