---
schema: qual/card@1
id: E-MUN-7-3
kind: problem
title: Bijection between $\mathcal{P}(\ZZ_+)$ and $X^{\omega}$
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §7 Exercise 3, printed p. 51; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.3,
    printed p. 84 (tmp/sources/munkres-solutions-whitman.pdf): the bijection sends a
    subset to its characteristic function and a binary sequence to the set of indices
    where it is 1. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the transcribed answer into numbered steps, separating the characteristic-function
    map, its injectivity and its surjectivity with the preimage written down. The mathematics is the
    earlier reading's and no defect was found. Not re-read this session: the Whitman page and
    Munkres printed p. 51.
---

::: {.exercise}

Let $X$ be the two-element set $\{0,1\}$ . Show there is a bijective correspondence between the set $\mathcal{P}(\ZZ_{+})$ and the cartesian product $X^{\omega}$ .
:::

::: {.solution}

The characteristic-function bijection is that of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.3, printed p. 84** (`tmp/sources/munkres-solutions-whitman.pdf`); the two directions are written out below.

Let $X=\{0,1\}$ and let $X^{\omega}$ be the set of sequences $(x_{1},x_{2},\dots)$ with $x_{n}\in X$.

::: pf

::: {.pf-step #map}
The rule $\chi_{S}(n)=1$ for $n\in S$ and $\chi_{S}(n)=0$ for $n\notin S$ defines a map $\Phi\colon\mathcal{P}(\ZZ_{+})\to X^{\omega}$, $\Phi(S)=\chi_{S}$.

::: pf-proof
For each $S\subset\ZZ_{+}$ the values $\chi_{S}(n)$ lie in $X$, and a sequence indexed by $\ZZ_{+}$ with values in $X$ is by definition an element of $X^{\omega}$; the rule determines $\chi_{S}$ from $S$ alone.
:::

:::

::: {.pf-step #injective}
$\Phi$ is injective.

::: pf-proof
Let $S\neq T$ be subsets of $\ZZ_{+}$; pick $n$ in one and not the other, say $n\in S\setminus T$. Then $\chi_{S}(n)=1$ and $\chi_{T}(n)=0$, so the sequences differ and $\Phi(S)\neq\Phi(T)$.
:::

:::

::: {.pf-step #surjective}
$\Phi$ is surjective, with $\Phi(S_{x})=x$ for $S_{x}=\{n\in\ZZ_{+}\mid x_{n}=1\}$.

::: pf-proof
Let $x=(x_{n})\in X^{\omega}$ and $S_{x}$ as defined. For $n\in S_{x}$ we have $x_{n}=1=\chi_{S_{x}}(n)$, and for $n\notin S_{x}$ we have $x_{n}=0$ because the only other element of $X$ is $0$; so $\chi_{S_{x}}=x$. Hence every element of $X^{\omega}$ is in the image.
:::

:::

::: {.pf-step}
$\Phi$ is a bijection between $\mathcal{P}(\ZZ_{+})$ and $X^{\omega}$.

::: pf-proof
Steps [](#map){.pf-ref}, [](#injective){.pf-ref} and [](#surjective){.pf-ref} show that $\Phi$ is a well-defined injective and surjective map, that is a bijective correspondence.
:::

:::

:::

:::
