---
schema: qual/card@1
id: P-ALGF24E
kind: problem
title: Support of a finitely generated module equals $V(\operatorname{ann}(M))$
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Compared the definitions and conclusion with Problem 5 on page 7 of the official FA24 algebra exam PDF.
- event: solution-written
  by: gpt-6-astra-pro
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Checked both inclusions using the localization zero criterion and a finite product of denominators; the empty generating set covers the zero module.
---

::: problem
Suppose $A$ is a unital commutative ring and $\operatorname{Spec}(A)$ is the set of all the prime ideals of $A$.
For an $A$-module $M$ and $\mathfrak{p} \in \operatorname{Spec}(A)$, let $M_{\mathfrak{p}}$ be the localization of $M$ at $\mathfrak{p}$.
Let
\[
\operatorname{supp} M := \{\mathfrak{p} \in \operatorname{Spec}(A) \mid M_{\mathfrak{p}} \neq 0\}.
\]
Prove that for a finitely generated $A$-module $M$,
\[
\operatorname{supp} M = \{\mathfrak{p} \in \operatorname{Spec}(A) \mid \operatorname{ann}(M) \subseteq \mathfrak{p}\},
\]
where $\operatorname{ann}(M)$ is the annihilator of $M$.
:::

::: {.solution}
Fix $\mathfrak p\in\operatorname{Spec}(A)$ and put $S=A\setminus\mathfrak p$, a submonoid of $(A,\cdot)$.
The defining equality relation in $M_{\mathfrak p}=S^{-1}M$ gives
\[
\frac{x}{1}=0\quad\Longleftrightarrow\quad
sx=0\text{ for some }s\in S.
\]

<1>1. If $\operatorname{ann}(M)\nsubseteq\mathfrak p$, then $M_{\mathfrak p}=0$.
::: {.proof}
Choose $a\in\operatorname{ann}(M)\setminus\mathfrak p$.
Then $ax=0$ for every $x\in M$, and $a\in S$.
The localization criterion implies $x/1=0$ for every $x\in M$.
Every fraction $x/s$ is obtained from $x/1$ by multiplication by the unit $1/s\in A_{\mathfrak p}$, so every element of $M_{\mathfrak p}$ is zero.
:::

<1>2. If $M$ is finitely generated and $M_{\mathfrak p}=0$, then $\operatorname{ann}(M)\nsubseteq\mathfrak p$.
::: {.proof}
Choose generators $x_1,\ldots,x_r$ of $M$.
For each $i$, the equality $x_i/1=0$ gives $s_i\in S$ with $s_ix_i=0$.
Set
\[
s=\prod_{i=1}^r s_i.
\]
For an empty generating set, take $s=1$.
The submonoid $S$ is closed under finite products, so $s\notin\mathfrak p$.
For every $i$, commutativity of $A$ gives
\[
sx_i=\left(\prod_{j\ne i}s_j\right)s_ix_i=0.
\]
Hence $s$ annihilates every $A$-linear combination of the generators and belongs to $\operatorname{ann}(M)$.
This produces an element of $\operatorname{ann}(M)$ outside $\mathfrak p$.
:::

<1>3. The support is $V(\operatorname{ann}(M))$.
::: {.proof}
Steps <1>1 and <1>2 prove, for each prime $\mathfrak p$,
\[
M_{\mathfrak p}=0
\quad\Longleftrightarrow\quad
\operatorname{ann}(M)\nsubseteq\mathfrak p.
\]
Negating both conditions and using the definition of support gives
\[
\operatorname{supp}M
=\{\mathfrak p\in\operatorname{Spec}(A):\operatorname{ann}(M)\subseteq\mathfrak p\}
=V(\operatorname{ann}(M)).
\]
:::
:::
