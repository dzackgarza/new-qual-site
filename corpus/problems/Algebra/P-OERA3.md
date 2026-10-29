---
schema: qual/card@1
id: P-OERA3
kind: problem
title: Sufficient conditions for a degree $5$ polynomial to have Galois group $S_5$
  over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Discuss sufficient conditions on a polynomial of degree 5 to have Galois group $S_5$ over $\QQ$ and prove your statements."; the statement asks for one sufficient condition with proof.'
---

::: {.problem}
Give a sufficient condition on a polynomial of degree $5$ over $\QQ$ for its Galois group to be $S_5$, and prove it.
:::

::: {.solution}
Let $f\in\QQ[x]$ be irreducible of degree $5$ with exactly three real roots, and let $G\le S_5$ be its Galois group acting on the five complex roots of $f$. We prove that $G=S_5$.

::: pf

::: {.pf-step #transitive}

$G$ acts transitively on the roots.

::: pf-proof

The roots are distinct because $f$ is irreducible over a field of characteristic $0$. For two roots $\alpha,\beta$, there is a $\QQ$-isomorphism $\QQ(\alpha)\to\QQ(\beta)$ sending $\alpha$ to $\beta$, and it extends to an automorphism of the splitting field.

:::

:::

::: {.pf-step #transposition}

$G$ contains a transposition.

::: pf-proof

Complex conjugation restricts to an automorphism of the splitting field. It fixes the three real roots and swaps the two nonreal roots, which are conjugate.

:::

:::

::: pf-step

$G=\boxed{S_5}$.

::: pf-proof

Let $T\subseteq G$ be the set of transpositions in $G$; it is nonempty by step [](#transposition){.pf-ref}. Form the graph on the five roots whose edges are the pairs $\{a,b\}$ with $(a\ b)\in T$. Since $g(a\ b)g^{-1}=(g(a)\ g(b))$, every $g\in G$ is a graph automorphism, so $G$ permutes the connected components. The components are therefore blocks of the transitive action of step [](#transitive){.pf-ref}, so they all have the same size, which divides $5$. Since some component contains an edge, that size is $5$ and the graph is connected. The relation "$a=b$ or $(a\ b)\in G$" is an equivalence relation, because $(a\ b)(b\ c)(a\ b)=(a\ c)$; its classes contain the components, so $G$ contains every transposition. Transpositions generate $S_5$.

:::

:::

:::

:::

::: {.remark}
Irreducibility gives $5\mid\abs{G}$, so by Cauchy's theorem $G$ contains an element of order $5$, necessarily a $5$-cycle. A transitive subgroup of $S_5$ containing a $5$-cycle and a transposition is $S_5$; this is the form of the criterion that holds for every prime degree $p$.
:::
