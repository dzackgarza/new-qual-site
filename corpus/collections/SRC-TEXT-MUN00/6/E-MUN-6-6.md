---
schema: qual/card@1
id: E-MUN-6-6
kind: problem
title: Bijection between $\mathcal{P}(A)$ and $X^n$
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §6 Exercise 6, printed p. 44; both parts are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.6,
    printed pp. 78-79 (tmp/sources/munkres-solutions-whitman.pdf). He sends a subset to
    its indicator n-tuple and inverts by collecting the positions of the 1s; the card
    writes the same two maps, as characteristic functions. Part (b) transfers the
    bijection along a bijection of A with a section and quotes the finiteness of a
    finite product, which is his use of Corollary 6.8. No defect found.
---

::: {.exercise}

(a) Let $A = \{1, \ldots, n\}$ . Show there is a bijection of $\mathcal{P}(A)$ with the cartesian product $X^n$, where $X$ is the two-element set $X = \{0, 1\}$ .

(b) Show that if $A$ is finite, then $\mathcal{P}(A)$ is finite.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.6, printed pp. 78--79** (`tmp/sources/munkres-solutions-whitman.pdf`); the indicator-tuple bijection and the transfer along a bijection with a section are his.

::: pf

::: {.pf-step #indicator}

For $S\subseteq A$ the indicator tuple $(\chi_{S}(1),\dots,\chi_{S}(n))$, with $\chi_{S}(i)=1$ if $i\in S$ and $0$ otherwise, lies in $\{0,1\}^{n}$.

::: pf-proof

Each $\chi_{S}(i)$ is $0$ or $1$ by definition, and the tuple has one entry for each $i\in A=\{1,\dots,n\}$, so it is an element of the $n$-fold cartesian product $\{0,1\}^{n}$.

:::

:::

::: {.pf-step #bijection}

(a) $S\mapsto(\chi_{S}(1),\dots,\chi_{S}(n))$ is a bijection $\mathcal{P}(A)\to X^{n}$.

::: pf-proof

Its inverse candidate is $\Psi(x_{1},\dots,x_{n})=\{i\in A:x_{i}=1\}$. For $S\subseteq A$, $\Psi(\chi_{S})=\{i:i\in S\}=S$. For a tuple $x\in\{0,1\}^{n}$ and each $i$, the $i$-th entry of $\chi_{\Psi(x)}$ is $1$ exactly when $i\in\Psi(x)$, that is exactly when $x_{i}=1$, so $\chi_{\Psi(x)}=x$. A map with a two-sided inverse is a bijection.

:::

:::

::: {.pf-step #finite}

(b) If $A$ is finite then $\mathcal{P}(A)$ is finite.

::: pf-proof

A finite set $A$ admits a bijection $\varphi:A\to\{1,\dots,n\}$ for some $n\ge0$. Then $S\mapsto\varphi(S)$ is a bijection $\mathcal{P}(A)\to\mathcal{P}(\{1,\dots,n\})$ with inverse $T\mapsto\varphi^{-1}(T)$, since the two operations are mutually inverse on subsets. By step [](#bijection){.pf-ref}, applied for $n\ge1$, $\mathcal{P}(\{1,\dots,n\})$ is in bijection with the finite product $\{0,1\}^{n}$, which has $2^{n}$ elements; for $n=0$, $A=\varnothing$ and $\mathcal{P}(A)=\{\varnothing\}$ is a one-element, hence finite, set. A set in bijection with a finite set is finite, so
$$
\boxed{\mathcal{P}(A)\ \text{is finite whenever } A \text{ is, with } \cardinality{\mathcal{P}(A)}=2^{\cardinality{A}}.}
$$

:::

:::

:::

:::
