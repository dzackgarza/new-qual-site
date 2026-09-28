---
title: Is it measurable?
order: 0
topics:
- Measure Theory
- Measurable Functions
---

# Is it measurable?

Measurability of a function is usually established from the closure properties of [[D-DHFN4|measurable functions]] rather than from the definition.

## Closure properties

Let $(X,\mathcal M)$ be a measurable space and $f, g, f_1, f_2,\ldots$ measurable functions $X\to\RR$.
Then the following are measurable:

- $\varphi\circ f$ for continuous $\varphi\colon\RR\to\RR$;

- $\lim_n f_n$ where it exists, and $\liminf_n f_n$, $\limsup_n f_n$, $\sup_n f_n$, $\inf_n f_n$;

- $f+g$, $fg$, and $f/g$ where $g$ does not vanish;

- a function $h$ such that $h|_{E_k}$ is measurable for each set $E_k$ in a countable measurable cover $\theset{E_k}$ of $X$.

Continuous functions and monotone functions $\RR\to\RR$ are Borel measurable, and a function equal almost everywhere to a Lebesgue measurable function is Lebesgue measurable.

## Order of composition

If $\varphi$ is continuous and $f$ is Lebesgue measurable, then $\varphi\circ f$ is Lebesgue measurable, since $(\varphi\circ f)^{-1}(U) = f^{-1}(\varphi^{-1}(U))$ and $\varphi^{-1}(U)$ is open.
A composition $f\circ\varphi$ with $f$ Lebesgue measurable and $\varphi$ continuous need not be Lebesgue measurable, because $\varphi^{-1}$ of a Lebesgue measurable set need not be Lebesgue measurable; the homeomorphism $x\mapsto x+c(x)$, for $c$ the Cantor function, maps the Cantor set onto a set of measure $1$ and gives an example.

[[FF-UW3C7]]

[[FE-YOIJM]]

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

## Exercises

[[P-QZT5B]]

[[P-TZJQI]]
