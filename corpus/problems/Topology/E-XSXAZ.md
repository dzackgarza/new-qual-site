---
schema: qual/card@1
id: E-XSXAZ
kind: problem
title: Six topologies on $\RR^{d}$
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Construct 6 distinct topologies on the set $\RR^d$ ($d \ge 1$), and order them by coarseness/fineness where applicable.
:::

::: {.solution}

Let $S=\RR^d$ and consider the following topologies on $S$:

- the indiscrete topology $\mathcal T_{\mathrm{ind}}=\{\varnothing,S\}$;
- the cofinite topology $\mathcal T_{\mathrm{cof}}=\{\varnothing\}\cup\{U\subseteq S:S\setminus U\text{ is finite}\}$;
- the cocountable topology $\mathcal T_{\mathrm{coc}}=\{\varnothing\}\cup\{U\subseteq S:S\setminus U\text{ is countable}\}$;
- the Euclidean topology $\mathcal T_{\mathrm{eucl}}$;
- the product of $d$ copies of the lower-limit topology, $\mathcal T_{\mathrm{Sorg}}$, with basis the boxes $\prod_{j=1}^d[a_j,b_j)$ with $a_j<b_j$;
- the discrete topology $\mathcal T_{\mathrm{disc}}=\mathcal P(S)$.

::: pf

::: {.pf-step #chain-1}

$\mathcal T_{\mathrm{ind}}\subsetneq\mathcal T_{\mathrm{cof}}\subsetneq\mathcal T_{\mathrm{coc}}\subsetneq\mathcal T_{\mathrm{disc}}$.

::: pf-proof

Each inclusion is immediate since finite sets are countable. Strictness: $S\setminus\{0\}$ is cofinite but not $S$; $S\setminus\QQ^d$ is cocountable but not cofinite; a nonempty bounded set is open in $\mathcal T_{\mathrm{disc}}$ but has uncountable complement.

:::

:::

::: {.pf-step #chain-2}

$\mathcal T_{\mathrm{cof}}\subsetneq\mathcal T_{\mathrm{eucl}}\subsetneq\mathcal T_{\mathrm{Sorg}}\subsetneq\mathcal T_{\mathrm{disc}}$.

::: pf-proof

Finite subsets of $S$ are Euclidean-closed, so cofinite sets are Euclidean-open; an open ball is Euclidean-open with uncountable complement, so it is not cofinite. Each open box $\prod_j(a_j,b_j)$ is the union of the boxes $\prod_j[a_j',b_j)$ with $a_j<a_j'$, so Euclidean-open sets are $\mathcal T_{\mathrm{Sorg}}$-open; the set $[0,1)\times\RR^{d-1}$ is $\mathcal T_{\mathrm{Sorg}}$-open but not Euclidean-open, since no Euclidean ball about the origin lies in it. A singleton is discrete-open but contains no box $\prod_j[a_j,b_j)$, so it is not $\mathcal T_{\mathrm{Sorg}}$-open.

:::

:::

::: {.pf-step #incomparable}

$\mathcal T_{\mathrm{coc}}$ is incomparable with $\mathcal T_{\mathrm{eucl}}$ and with $\mathcal T_{\mathrm{Sorg}}$.

::: pf-proof

An open ball lies in $\mathcal T_{\mathrm{eucl}}\subseteq\mathcal T_{\mathrm{Sorg}}$ but has uncountable complement, so it is not in $\mathcal T_{\mathrm{coc}}$. The set $S\setminus\QQ^d$ is cocountable, but every box $\prod_j[a_j,b_j)$ meets the dense set $\QQ^d$, so $S\setminus\QQ^d$ is open in neither $\mathcal T_{\mathrm{Sorg}}$ nor $\mathcal T_{\mathrm{eucl}}$.

:::

:::

::: pf-step

The six topologies are distinct, and their order by fineness is the two chains of steps [](#chain-1){.pf-ref} and [](#chain-2){.pf-ref}, which share the bottom $\mathcal T_{\mathrm{ind}}\subsetneq\mathcal T_{\mathrm{cof}}$ and the top $\mathcal T_{\mathrm{disc}}$, with $\mathcal T_{\mathrm{coc}}$ incomparable with $\mathcal T_{\mathrm{eucl}}$ and $\mathcal T_{\mathrm{Sorg}}$.

::: pf-proof

Strict inclusions separate the topologies within each chain, and step [](#incomparable){.pf-ref} separates $\mathcal T_{\mathrm{coc}}$ from $\mathcal T_{\mathrm{eucl}}$ and $\mathcal T_{\mathrm{Sorg}}$.

:::

:::

:::

:::
