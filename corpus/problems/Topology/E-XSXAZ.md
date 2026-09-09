---
schema: qual/card@1
id: E-XSXAZ
kind: problem
title: Six topologies on $\mathbb{R}^{d}$
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

::: exercise
Construct 6 distinct topologies on the set $\mathbb{R}^d$ ($d \ge 1$), and order them by coarseness/fineness where applicable.
:::

::: solution
Let $S=\mathbb R^d$.

<1>1. The following are six distinct topologies on $S$:
<2>1. The indiscrete topology
\[
\mathcal T_{\mathrm{ind}}=\{\varnothing,S\}.
\]
<2>2. The cofinite topology
\[
\mathcal T_{\mathrm{cof}}=\{\varnothing\}\cup\{U\subseteq S:S\setminus U\text{ is finite}\}.
\]
<2>3. The cocountable topology
\[
\mathcal T_{\mathrm{coc}}=\{\varnothing\}\cup\{U\subseteq S:S\setminus U\text{ is countable}\}.
\]
<2>4. The Euclidean topology $\mathcal T_{\mathrm{eucl}}$.
<2>5. The $d$-fold lower-limit (Sorgenfrey product) topology $\mathcal T_{\mathrm{Sorg}}$, with basis
\[
\prod_{j=1}^d[a_j,b_j),\qquad a_j<b_j.
\]
<2>6. The discrete topology
\[
\mathcal T_{\mathrm{disc}}=\mathcal P(S).
\]

<1>2. The following strict inclusions hold:
\[
\mathcal T_{\mathrm{ind}}
\subsetneq\mathcal T_{\mathrm{cof}}
\subsetneq\mathcal T_{\mathrm{coc}}
\subsetneq\mathcal T_{\mathrm{disc}},
\]
and
\[
\mathcal T_{\mathrm{ind}}
\subsetneq\mathcal T_{\mathrm{cof}}
\subsetneq\mathcal T_{\mathrm{eucl}}
\subsetneq\mathcal T_{\mathrm{Sorg}}
\subsetneq\mathcal T_{\mathrm{disc}}.
\]
<2>1. Every cofinite open set is Euclidean-open because finite subsets of $\mathbb R^d$ are Euclidean-closed.
<2>2. Every Euclidean-open set is Sorgenfrey-open: each Euclidean-open rectangle is a union of half-open basic rectangles.
<2>3. Strictness of $\mathcal T_{\mathrm{eucl}}\subsetneq\mathcal T_{\mathrm{Sorg}}$ is witnessed by $[0,1)\times\mathbb R^{d-1}$.

<1>3. The Euclidean and cocountable topologies are incomparable.
<2>1. A bounded Euclidean open ball is not cocountable, since its complement is uncountable.
<2>2. The set
\[
S\setminus\mathbb Q^d
\]
is cocountable because $\mathbb Q^d$ is countable, but it is not Euclidean-open because $\mathbb Q^d$ is dense.

<1>4. These observations also distinguish all six topologies. In particular, the cofinite topology is strictly below both the Euclidean and cocountable topologies, while the discrete topology is strictly above all of them.
:::
