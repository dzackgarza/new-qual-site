---
schema: qual/card@1
id: E-MUN-10-8
kind: problem
title: Well-ordering unions of disjoint well-ordered sets
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
(a) Let $A_{1}$ and $A_{2}$ be disjoint sets, well-ordered by $<_{1}$ and $<_{2}$, respectively.
Define an order relation on $A_{1} \cup A_{2}$ by letting $a < b$ either if $a, b \in A_{1}$ and $a <_{1} b$, or if $a, b \in A_{2}$ and $a <_{2} b$, or if $a \in A_{1}$ and $b \in A_{2}$. Show that this is a **well-ordering**.

(b) Generalize (a) to an arbitrary family of pairwise disjoint well-ordered sets $\{A_\alpha\}_{\alpha \in J}$, indexed by a well-ordered set $J$.
:::

::: {.solution}
Let $(J,<_J)$ be a well-ordered set, and for each $\alpha\in J$ let $(A_\alpha,<_\alpha)$ be a well-ordered set, with $A_\alpha\cap A_\beta=\varnothing$ for $\alpha\ne\beta$.
Put $A=\bigcup_{\alpha\in J}A_\alpha$.
For $a\in A$ let $\iota(a)\in J$ be the unique index with $a\in A_{\iota(a)}$, and define a relation $<$ on $A$ by
$$
a<b \iff \iota(a)<_J\iota(b)\quad\text{or}\quad\bigl(\iota(a)=\iota(b)\text{ and }a<_{\iota(a)}b\bigr).
$$
The generalization asked for in (b) is: $(A,<)$ is well-ordered.
Part (a) is the case $J=\{1,2\}$ with $1<_J2$, where the relation above is the order defined in (a).

<1>1. The relation $<$ is a simple order on $A$.

::: {.proof}
Let $a,b\in A$ with $\alpha=\iota(a)$ and $\beta=\iota(b)$.
If $\alpha\ne\beta$, exactly one of $\alpha<_J\beta$ and $\beta<_J\alpha$ holds, so exactly one of $a<b$ and $b<a$ holds, and $a\ne b$.
If $\alpha=\beta$, exactly one of $a<_\alpha b$, $b<_\alpha a$, $a=b$ holds, and these are exactly $a<b$, $b<a$, $a=b$.
So $<$ is comparable and nonreflexive.

For transitivity let $a<b$ and $b<c$ with $\gamma=\iota(c)$.
Then $\alpha\le_J\beta\le_J\gamma$.
If $\alpha<_J\gamma$, then $a<c$.
Otherwise $\alpha=\beta=\gamma$, so $a<_\alpha b<_\alpha c$, hence $a<_\alpha c$ and $a<c$.
:::

<1>2. Every nonempty subset $S\subseteq A$ has a smallest element.

::: {.proof}
The set $J_0=\{\alpha\in J : S\cap A_\alpha\ne\varnothing\}$ is nonempty because $S$ is, so it has a least element $\alpha_0$.
The nonempty subset $S\cap A_{\alpha_0}$ of the well-ordered set $A_{\alpha_0}$ has a least element $m_0$.
Let $s\in S$ and $\beta=\iota(s)$.
Then $\beta\in J_0$, so $\alpha_0\le_J\beta$.
If $\alpha_0<_J\beta$, then $m_0<s$.
If $\alpha_0=\beta$, then $s\in S\cap A_{\alpha_0}$, so $m_0\le_{\alpha_0}s$ and $m_0\le s$.
Hence $m_0$ is the smallest element of $S$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 show that $(A,<)$ is well-ordered, which is (b); taking $J=\{1,2\}$ gives (a).
:::
:::
