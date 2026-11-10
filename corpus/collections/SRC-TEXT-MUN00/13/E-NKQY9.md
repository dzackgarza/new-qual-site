---
schema: qual/card@1
id: E-NKQY9
kind: problem
title: Countable rational-endpoint bases
classification:
  areas:
  - topology
  topics:
  - Bases
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §13 Exercise 8, printed pp. 83-84, with Lemma
    13.2 on printed p. 80 and Exercise 4.9(d) for the density of the rationals; both
    collections are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 13.8, printed p. 147.
    From him: (a) the rational open intervals are a basis generating the standard topology
    by Lemma 13.2, using density of the rationals to fit a rational interval inside a given
    one around a point; (b) the rational half-open intervals are a basis and generate a
    different topology, because [x, x+1) with x irrational is lower-limit open while no
    rational [a,b) containing x lies inside it. The two basis conditions are checked
    explicitly for both collections. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

(a) Apply Lemma 13.2 to show that the countable collection

$$
\mathcal{B} = \theset{(a, b) \mid a < b, \ a \text{ and } b \text{ rational}}
$$

is a basis that generates the standard topology on $\RR$.

(b) Show that the collection

$$
\mathcal{C} = \theset{[a, b) \mid a < b, \ a \text{ and } b \text{ rational}}
$$

is a basis that generates a topology different from the lower limit topology on $\RR$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 13.8, printed p. 147** (`tmp/sources/munkres-solutions-whitman.pdf`); both parts are his, with the two basis conditions checked explicitly in (a).

(a) Let $\mathcal{B}=\{(a,b)\mid a<b,\ a,b\in\QQ\}$ and let $\mathcal{T}$ be the standard topology on $\RR$.

$\mathcal{B}$ is a basis. If $x\in\RR$, choose rationals $a<x<b$; then $x\in(a,b)\in\mathcal{B}$. If $B_{1}=(a_{1},b_{1}),B_{2}=(a_{2},b_{2})\in\mathcal{B}$ and $x\in B_{1}\cap B_{2}$, then $a=\max(a_{1},a_{2})$ and $b=\min(b_{1},b_{2})$ are rational, $a\le x<b$, and $x\in(a,b)\in\mathcal{B}$ with $(a,b)\subset B_{1}\cap B_{2}$.

$\mathcal{B}$ generates $\mathcal{T}$. Every element of $\mathcal{B}$ is an open interval, hence open in $\mathcal{T}$. Conversely let $U\in\mathcal{T}$ and $x\in U$; by the definition of the standard topology there is a basis element $(a_{0},b_{0})$ with $x\in(a_{0},b_{0})\subset U$. Since $\QQ$ is order dense in $\RR$ (Exercise 4.9(d)) there are rationals $a,b$ with $a_{0}<a<x<b<b_{0}$; then $x\in(a,b)\in\mathcal{B}$ and $(a,b)\subset(a_{0},b_{0})\subset U$. By Lemma 13.2, $\mathcal{B}$ is a basis for the topology $\mathcal{T}$.

(b) Let $\mathcal{C}=\{[a,b)\mid a<b,\ a,b\in\QQ\}$ and let $\mathcal{T}_{\mathcal{C}}$ be the topology it generates, $\mathcal{T}_{\ell}$ the lower limit topology.

$\mathcal{C}$ is a basis. If $x\in\RR$, choose rationals $a\le x<b$; then $x\in[a,b)\in\mathcal{C}$. If $C_{1}=[a_{1},b_{1}),C_{2}=[a_{2},b_{2})\in\mathcal{C}$ and $x\in C_{1}\cap C_{2}$, then $a=\max(a_{1},a_{2})$ and $b=\min(b_{1},b_{2})$ are rational with $a\le x<b$, and $C=[a,b)\in\mathcal{C}$ satisfies $x\in C\subset C_{1}\cap C_{2}$.

$\mathcal{T}_{\mathcal{C}}\ne\mathcal{T}_{\ell}$. Let $x$ be irrational and let $U=[x,x+1)$, which is a basis element of the lower limit topology, so $U\in\mathcal{T}_{\ell}$. Let $C=[a,b)\in\mathcal{C}$ contain $x$. Then $a$ is rational and $a\le x$, so $a<x$; hence $a\in C$ but $a\notin[x,x+1)=U$, and $C\not\subset U$. So no basis element of $\mathcal{C}$ that contains $x$ is contained in $U$, and by Lemma 13.1 (an open set is one through each of whose points there is a basis element inside it) $U\notin\mathcal{T}_{\mathcal{C}}$. Hence the two topologies differ.
:::
