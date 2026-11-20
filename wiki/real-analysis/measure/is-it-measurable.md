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
Then $\varphi\circ f$ is measurable for every continuous $\varphi\colon\RR\to\RR$, and $fg$ and $f/g$ are measurable, where $g$ does not vanish.
If $\theset{E_k}$ is a countable measurable cover of $X$ and $h\restrict_{E_k}$ is measurable for every $k$, then $h$ is measurable.
Continuous functions and monotone functions $\RR\to\RR$ are Borel measurable, and a function equal almost everywhere to a Lebesgue measurable function is Lebesgue measurable [@Fol99, §2.1].

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
