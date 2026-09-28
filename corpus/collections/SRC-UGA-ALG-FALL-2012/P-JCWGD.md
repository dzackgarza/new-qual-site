---
schema: qual/card@1
id: P-JCWGD
kind: problem
title: The stabilizer is a subgroup, and the orbit-stabilizer bijection $G\cdot x\simeq
  G/G_x$
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a finite group and $X$ a set on which $G$ acts.

a. Let $x\in X$ and $G_x \definedas \theset{g\in G \suchthat g\cdot x = x}$. Show that
$G_x$ is a subgroup of $G$.

b. Let $x\in X$ and $G\cdot x \definedas \theset{g\cdot x \suchthat g\in G}$. Prove that
there is a bijection between elements in $G\cdot x$ and the left cosets of $G_x$ in $G$.
:::

::: {.solution}
<1>1. The stabilizer
\[
G_x=\{g\in G\mid g\cdot x=x\}
\]
is a subgroup of \(G\).
::: {.proof}
The identity satisfies \(e\cdot x=x\), so \(e\in G_x\). If \(g,h\in G_x\), then
\[
(gh^{-1})\cdot x=g\cdot(h^{-1}\cdot x).
\]
Since \(h\cdot x=x\), applying \(h^{-1}\) gives \(h^{-1}\cdot x=x\). Hence
\[
(gh^{-1})\cdot x=g\cdot x=x,
\]
so \(gh^{-1}\in G_x\). By the subgroup criterion, \(G_x\le G\).
:::

<1>2. Define
\[
\Phi:G/G_x\longrightarrow G\cdot x,
\qquad
\Phi(gG_x)=g\cdot x.
\]
Then \(\Phi\) is well defined.
::: {.proof}
Suppose \(gG_x=hG_x\). Then \(h^{-1}g\in G_x\), so
\[
(h^{-1}g)\cdot x=x.
\]
Applying \(h\) gives \(g\cdot x=h\cdot x\). Thus the value of \(\Phi\) depends only on
the left coset.
:::

<1>3. The map \(\Phi\) is injective.
::: {.proof}
If \(\Phi(gG_x)=\Phi(hG_x)\), then \(g\cdot x=h\cdot x\). Applying \(h^{-1}\) gives
\[
(h^{-1}g)\cdot x=x,
\]
so \(h^{-1}g\in G_x\). Hence \(gG_x=hG_x\).
:::

<1>4. The map \(\Phi\) is surjective.
::: {.proof}
Every element of the orbit \(G\cdot x\) has the form \(g\cdot x\) for some \(g\in G\),
and
\[
\Phi(gG_x)=g\cdot x.
\]
:::

<1>5. Therefore \(G\cdot x\) is in bijection with the set of left cosets \(G/G_x\).
::: {.proof}
By <1>2--<1>4, \(\Phi\) is a well-defined bijection.
:::
:::
