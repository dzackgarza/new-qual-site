---
title: Is it measurable?
order: 0
topics:
- Measure Theory
- Measurable Functions
---

# Is it measurable?

## Closure properties

[[PR-552IH]]

::: {.proposition}
Let $(X,\mathcal M)$ be a measurable space and $f,g\colon X\to\RR$ [[D-DHFN4|measurable]] functions.
Then $f+g$ and $fg$ are measurable, and if $(f_n)$ is a sequence of measurable functions converging pointwise to $h$, then $h$ is measurable [@Fol99, Proposition 2.6 and Theorem 2.9].
If $X=\bigcup_{k\geq1}E_k$ with $E_k$ measurable and $h\restrict_{E_k}$ measurable for every $k$, then $h$ is measurable: the preimage of a Borel set is the union of its preimages in the pieces, which is to say the argument of [@Fol99, Exercise 2.21].
Continuous functions $\RR\to\RR$ are Borel measurable [@Fol99, Proposition 2.2], and a function equal almost everywhere to a Lebesgue measurable function is Lebesgue measurable, Lebesgue measure being complete [@Fol99, Proposition 2.11].

:::

## Order of composition

[[FF-UW3C7]]

[[PR-Z5VSQ]]

## Non-measurable sets

::: {.example title="The Vitali set"}
Choose, using the axiom of choice, one representative in $[0,1]$ of each coset of $\QQ$ in $\RR$, and let $V$ be the set of representatives.
The translates $V+r$ for $r\in\QQ\cap[-1,1]$ are pairwise disjoint, their union contains $[0,1]$, and it is contained in $[-1,2]$.
If $V$ were Lebesgue measurable, translation invariance and countable additivity would give $1\leq\sum_{r}m(V)\leq3$, which is impossible for $m(V)=0$ and for $m(V)>0$.

:::

::: {.remark}
The construction is not specific to $[0,1]$: it applies inside any Lebesgue measurable set of positive measure, so every such set contains a non-measurable subset.

:::

## Problems

[[P-TZJQI]]
