---
schema: qual/card@1
id: P-AYDDA
kind: problem
title: Carathéodory extension of a measure from an algebra
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Real Analysis (1) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMRA1, whose solution repeats this Carathéodory construction."
---

::: {.problem}
Describe the process that extends a measure on an algebra
$\mathcal{A}$ of subsets of $X$, to a complete measure defined on a
$\sigma$-algebra $\mathcal{B}$ containing $\mathcal{A}$. State the
corresponding definitions and results (without proofs).
:::

::: {.solution}

The exercise asks for the definitions and the theorems without proofs, so the statements are given here and the four elementary facts about the outer measure that the construction actually uses are proved; the two deep theorems are quoted and attributed as such.

Let $X$ be a set and $\mathcal A\subseteq\mathcal P(X)$ a collection of subsets of $X$.

- $\mathcal A$ is an **algebra** on $X$ when $\varnothing,X\in\mathcal A$, and $A\in\mathcal A$ implies $A^{c}\in\mathcal A$, and $A,B\in\mathcal A$ implies $A\cup B\in\mathcal A$.
- A **pre-measure** on $\mathcal A$ is $\mu_{0}:\mathcal A\to[0,\infty]$ with $\mu_{0}(\varnothing)=0$ and with $\mu_{0}\big(\bigcup_{n}A_{n}\big)=\sum_{n}\mu_{0}(A_{n})$ for every pairwise disjoint sequence in $\mathcal A$ whose union lies in $\mathcal A$.
- The **outer measure** induced by $\mu_{0}$ is
$$
\mu^{*}(E)=\inf\Big\{\sum_{n\ge1}\mu_{0}(A_{n}):A_{n}\in\mathcal A,\ E\subseteq\bigcup_{n\ge1}A_{n}\Big\},
$$
with $\inf\varnothing=\infty$.
- $E\subseteq X$ is **$\mu^{*}$-measurable** (Carathéodory) when $\mu^{*}(T)=\mu^{*}(T\cap E)+\mu^{*}(T\cap E^{c})$ for every test set $T\subseteq X$; the collection of such $E$ is $\mathcal M(\mu^{*})$.

::: pf

::: {.pf-step #properties}
$\mu^{*}$ satisfies $\mu^{*}(\varnothing)=0$, is monotone, and is countably subadditive.

::: pf-proof

::: {.pf-step #empty}
$\mu^{*}(\varnothing)=0$.

::: pf-proof
The sequence $A_{1}=\varnothing$ and $A_{n}=\varnothing$ for $n>1$ is a cover of $\varnothing$ by members of $\mathcal A$ with $\sum_{n}\mu_{0}(A_{n})=0$, so the infimum is at most $0$, and it is at least $0$ because all the values $\mu_{0}$ are nonnegative.
:::

:::

::: {.pf-step #monotone}
$E_{1}\subseteq E_{2}$ implies $\mu^{*}(E_{1})\le\mu^{*}(E_{2})$.

::: pf-proof
Every countable cover of $E_{2}$ by members of $\mathcal A$ is also a cover of $E_{1}$, so the set of numbers whose infimum defines $\mu^{*}(E_{1})$ contains the corresponding set for $E_{2}$, and the infimum of a larger set is at most the infimum of a smaller one.
:::

:::

::: {.pf-step #subadditive}
$\mu^{*}\big(\bigcup_{n}E_{n}\big)\le\sum_{n}\mu^{*}(E_{n})$.

::: pf-proof
Let $\varepsilon>0$. For each $n$ choose a cover $\{A_{n,k}\}_{k\ge1}$ of $E_{n}$ by members of $\mathcal A$ with $\sum_{k}\mu_{0}(A_{n,k})\le\mu^{*}(E_{n})+\varepsilon/2^{n}$, which is possible by the definition of infimum when $\mu^{*}(E_{n})<\infty$, and is trivially possible when $\mu^{*}(E_{n})=\infty$. The doubly indexed family $\{A_{n,k}\}_{n,k}$ is countable, covers $\bigcup_{n}E_{n}$, and satisfies
$$
\sum_{n}\sum_{k}\mu_{0}(A_{n,k})\le\sum_{n}\mu^{*}(E_{n})+\varepsilon ,
$$
so $\mu^{*}\big(\bigcup_{n}E_{n}\big)\le\sum_{n}\mu^{*}(E_{n})+\varepsilon$. As $\varepsilon>0$ was arbitrary, the inequality follows.
:::

:::

:::

:::

::: {.pf-step #consistency}
$\mu^{*}(A)=\mu_{0}(A)$ for every $A\in\mathcal A$.

::: pf-proof
$A$ itself is a countable cover of $A$ by a member of $\mathcal A$, so $\mu^{*}(A)\le\mu_{0}(A)$. Conversely let $\{A_{n}\}$ be any countable cover of $A$ by members of $\mathcal A$. The sets $A_{n}$ need not be disjoint, so first disjointise the cover: put $B_{n}=A_{n}\setminus\bigcup_{k<n}A_{k}$, which lies in $\mathcal A$ because an algebra is closed under finite unions and complements. The $B_{n}$ are pairwise disjoint and $\bigcup_{n}B_{n}=\bigcup_{n}A_{n}\supseteq A$, so
$$
A=\bigcup_{n}(A\cap B_{n})
$$
is a countable union of pairwise disjoint members of $\mathcal A$ (the sets $A\cap B_{n}$ are disjoint because the $B_{n}$ are) with union $A\in\mathcal A$. Countable additivity therefore applies and gives
$$
\mu_{0}(A)=\sum_{n}\mu_{0}(A\cap B_{n})\le\sum_{n}\mu_{0}(B_{n})\le\sum_{n}\mu_{0}(A_{n}),
$$
the first inequality because $A\cap B_{n}\subseteq B_{n}$ and the second because $B_{n}\subseteq A_{n}$ and $\mu_{0}$ is monotone on $\mathcal A$ (additivity on disjoint unions whose union lies in $\mathcal A$ gives monotonicity there in the usual way). Taking the infimum over all countable covers gives $\mu_{0}(A)\le\mu^{*}(A)$.
:::

:::

::: {.pf-step #caratheodory}
Carathéodory's theorem. For any outer measure $\mu^{*}$ on $X$: $\mathcal M(\mu^{*})$ is a $\sigma$-algebra containing every set of outer measure zero, the restriction $\mu=\restrictionof{\mu^{*}}{\mathcal M(\mu^{*})}$ is a countably additive measure, and $(X,\mathcal M(\mu^{*}),\mu)$ is complete.

::: pf-proof
This is quoted, as the exercise asks: the assertion is Carathéodory's theorem, proved in the course and in every account of the construction. The completeness is immediate from the definition of measurability — if $\mu^{*}(N)=0$ and $S\subseteq N$ then $\mu^{*}(S)=0$ by monotonicity, and for any $T$ one has $\mu^{*}(T\cap S)+\mu^{*}(T\cap S^{c})=\mu^{*}(T\cap S^{c})\le\mu^{*}(T)$, so $S$ is measurable — and the $\sigma$-algebra and measure assertions are the substance of the theorem.
:::

:::

::: {.pf-step #algebra-contained}
If $\mu^{*}$ is induced by a pre-measure $\mu_{0}$ on an algebra $\mathcal A$, then $\mathcal A\subseteq\mathcal M(\mu^{*})$, hence $\sigma(\mathcal A)\subseteq\mathcal M(\mu^{*})$.

::: pf-proof
Let $A\in\mathcal A$ and let $T\subseteq X$; measurability of $A$ is the inequality $\mu^{*}(T)\ge\mu^{*}(T\cap A)+\mu^{*}(T\cap A^{c})$ for all $T$. For $\varepsilon>0$ choose a cover $\{A_{n}\}$ of $T$ by members of $\mathcal A$ with $\sum_{n}\mu_{0}(A_{n})\le\mu^{*}(T)+\varepsilon$; then $\{A_{n}\cap A\}$ covers $T\cap A$ and $\{A_{n}\cap A^{c}\}$ covers $T\cap A^{c}$, both by members of $\mathcal A$ (an algebra is closed under finite intersections and complements), so
$$
\mu^{*}(T\cap A)+\mu^{*}(T\cap A^{c})\le\sum_{n}\mu_{0}(A_{n}\cap A)+\sum_{n}\mu_{0}(A_{n}\cap A^{c})=\sum_{n}\mu_{0}(A_{n})\le\mu^{*}(T)+\varepsilon,
$$
using additivity of $\mu_{0}$ on the disjoint pair $A_{n}\cap A$, $A_{n}\cap A^{c}$ whose union $A_{n}$ lies in $\mathcal A$. So $A\in\mathcal M(\mu^{*})$, and since $\mathcal M(\mu^{*})$ is a $\sigma$-algebra by step [](#caratheodory){.pf-ref} it contains the $\sigma$-algebra generated by $\mathcal A$.
:::

:::

::: {.pf-step #extension}
Hahn--Kolmogorov (Carathéodory) extension theorem. Let $\mu_{0}$ be a pre-measure on an algebra $\mathcal A$ and $\mu^{*}$ its outer measure. Then $\mu=\restrictionof{\mu^{*}}{\mathcal M(\mu^{*})}$ is a complete measure extending $\mu_{0}$; and if $\mu_{0}$ is $\sigma$-finite on $\mathcal A$, the restriction of $\mu$ to $\sigma(\mathcal A)$ is the unique extension of $\mu_{0}$ to a measure on $\sigma(\mathcal A)$, and $\mathcal M(\mu^{*})$ is the completion of $\sigma(\mathcal A)$ with respect to that restriction.

::: pf-proof
This is quoted, as the exercise asks. The existence half is the assembly of the preceding steps: $\mathcal M(\mu^{*})$ is a $\sigma$-algebra and $\mu$ a complete measure on it by step [](#caratheodory){.pf-ref}, and $\mathcal A\subseteq\mathcal M(\mu^{*})$ with $\mu=\mu_{0}$ on $\mathcal A$ by steps [](#algebra-contained){.pf-ref} and [](#consistency){.pf-ref}. The uniqueness half needs the hypothesis $\sigma$-finiteness, that $X=\bigcup_{n}A_{n}$ with $A_{n}\in\mathcal A$ and $\mu_{0}(A_{n})<\infty$: it is not a consequence of the construction, and no step above uses it. Hence the process is: start with $(X,\mathcal A,\mu_{0})$, form $\mu^{*}$ by infima over countable $\mathcal A$-covers, take $\mathcal B=\mathcal M(\mu^{*})$ as the sets satisfying Carathéodory's criterion, and restrict $\mu^{*}$ to $\mathcal B$; the result is a complete measure space containing $\sigma(\mathcal A)$ and extending $\mu_{0}$.
:::

:::

:::
:::
