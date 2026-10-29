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

In addition, for a measurable space $(X,\mathcal M)$ and [[D-DHFN4|measurable functions]] $f,g\colon X\to\RR$, the following are measurable:

- $\varphi\circ f$ for continuous $\varphi\colon\RR\to\RR$;

- $fg$, and $f/g$ where $g$ does not vanish;

- a function $h$ such that $h|_{E_k}$ is measurable for each set $E_k$ in a countable measurable cover $\theset{E_k}$ of $X$.

Continuous functions and monotone functions $\RR\to\RR$ are Borel measurable, and a function equal almost everywhere to a Lebesgue measurable function is Lebesgue measurable.

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
Every Lebesgue measurable subset of $\RR$ of positive measure contains a non-measurable subset.
The Lebesgue $\sigma$-algebra is the completion of the Borel $\sigma$-algebra and strictly contains it.

:::

## Problems

[[P-TZJQI]]
