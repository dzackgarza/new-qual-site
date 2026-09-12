---
schema: qual/card@1
id: P-TOP-WORKSHOP-D1-08
kind: problem
title: A compact subset of a product with the indiscrete two-point space
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against problem (8) in assets/attachments/Day_1_-_Compactness_Problems.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $X$ be a set with two elements $\{a,b\}$.
Give $X$ the indiscrete topology.
Give $X\times\mathbb R$ the product topology.
Let $A\subset X\times\mathbb R$ be $(\{a\}\times[0,1])\cup(\{b\}\times(0,1))$.
Prove that $A$ is compact.
:::

::: {.solution}
<1>1. Every nonempty open subset of $X\times\mathbb R$ is of the form $X\times V$ for some open $V\subseteq\mathbb R$.
::: {.proof}
The only nonempty open subset of the indiscrete space $X$ is $X$ itself.
Hence the basic open sets of the product topology are precisely the sets $X\times V$ with $V$ open in $\mathbb R$.
Arbitrary unions of such sets again have this form.
:::

<1>2. Every open subset of the subspace $A$ is therefore of the form
\[
A\cap(X\times V)
\]
for some open $V\subseteq\mathbb R$.
::: {.proof}
This is the definition of the subspace topology together with <1>1.
:::

<1>3. Let $\{A\cap(X\times V_i)\}_{i\in I}$ be an arbitrary open cover of $A$.
Then $\{V_i\}_{i\in I}$ covers $[0,1]$.
::: {.proof}
For every $t\in[0,1]$, the point $(a,t)$ belongs to $A$.
Since the displayed family covers $A$, there is an $i$ with $(a,t)\in X\times V_i$, hence $t\in V_i$.
:::

<1>4. The interval $[0,1]$ admits a finite subcover from $\{V_i\}_{i\in I}$.
::: {.proof}
We prove this directly.
Let
\[
S=\{x\in[0,1]:[0,x]\text{ is covered by finitely many }V_i\}.
\]
Some $V_i$ contains $0$, so $S$ is nonempty.
Let $s=\sup S$.
Choose $V_j$ containing $s$ and an open interval $(s-\varepsilon,s+\varepsilon)\subseteq V_j$.

If $s<1$, choose $x\in S$ with $x>s-\varepsilon/2$.
A finite family covers $[0,x]$, and adjoining $V_j$ covers
\[
[0,s+\varepsilon/2],
\]
contradicting the definition of $s$ as an upper bound for $S$.
Thus $s=1$.
Now choose $x\in S$ with $x>1-\varepsilon/2$; a finite cover of $[0,x]$ together with $V_j$ covers all of $[0,1]$.
:::

<1>5. The corresponding finitely many members of the original cover cover $A$.
::: {.proof}
Choose indices $i_1,\dots,i_n$ such that
\[
[0,1]\subseteq V_{i_1}\cup\cdots\cup V_{i_n}.
\]
Every point of $A$ has second coordinate in $[0,1]$, so it lies in
\[
A\cap(X\times V_{i_1}),\ldots,A\cap(X\times V_{i_n})
\]
for at least one index.
:::

<1>6. Therefore $A$ is compact.
::: {.proof}
The open cover in <1>3 was arbitrary, and <1>5 produced a finite subcover.
:::
:::
