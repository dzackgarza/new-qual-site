---
title: Is it measurable?
order: 0
topics:
- Measure Theory
- Measurable Functions
---

# Is it measurable?

## Closure properties

[[PR-EWXRO]]

[[PR-552IH]]

::: {.proposition}
Let $(X,\mathcal M)$ be a measurable space and let $h\colon X\to\RR$.
If $X=\bigcup_{k\geq1}E_k$ with $E_k$ measurable and $h\restrict_{E_k}$ measurable for every $k$, then $h$ is measurable: the preimage of a Borel set is the union of its preimages in the pieces, which is the argument of [@Fol99, Exercise 2.5] applied to the countably many pieces.
Continuous functions $\RR\to\RR$ are Borel measurable [@Fol99, Corollary 2.2], and a function equal almost everywhere to a Lebesgue measurable function is Lebesgue measurable, Lebesgue measure being complete [@Fol99, Proposition 2.11].

:::

## Order of composition

[[FF-UW3C7]]

[[PR-Z5VSQ]]

## Non-measurable sets

::: {.example title="The Vitali set"}
Choose, using the axiom of choice, one representative in $[0,1]$ of each coset of $\QQ$ in $\RR$, and let $V$ be the set of representatives.
The translates $V+r$ for $r\in\QQ\cap[-1,1]$ are pairwise disjoint, their union contains $[0,1]$, and it is contained in $[-1,2]$.
If $V$ were Lebesgue measurable, translation invariance and countable additivity would give $1\leq\sum_{r}m(V)\leq3$, which is impossible for $m(V)=0$ and for $m(V)>0$.

Two properties are used: [[PR-LF7SW|the properties of Lebesgue outer measure]] — translation invariance and the bound $m^*([a,b])\le b-a$ together with $m^*([0,1])=1$ — and the countable additivity of $m$ on the measurable sets.
:::

::: {.proposition}
Let $E\subseteq\RR$ be [[D-MDJII|Lebesgue measurable]] with $m(E)>0$.
Then $E$ contains a subset that is not Lebesgue measurable [@Fol99, Exercise 1.29(b)].
:::

## Problems

[[P-TZJQI]]
