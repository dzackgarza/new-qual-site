---
schema: qual/card@1
id: E-C7KV4
kind: problem
title: The lower limit and K-topologies are not comparable
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §13 Exercise 6, printed p. 83, with the bases of
    R_l and R_K as defined in Examples 1 and 2 of §13 and Lemma 13.3 on printed p. 81; the
    stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 13.6, printed pp.
    145-146. Both failures of Lemma 13.3 are his: at 0 in the lower-limit basis element
    [0,1) every K-basis element contains a point a/2 < 0, and at 0 in (-1,1) - K every
    lower-limit basis element contains some 1/n. (tmp/sources/munkres-solutions-
    whitman.pdf).
---

::: {.exercise}

Show that the topologies of $\RR_\ell$ and $\RR_K$ are not comparable.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 13.6, printed pp. 145--146** (`tmp/sources/munkres-solutions-whitman.pdf`); both halves are his.

Recall that $\mathcal{B}_{\ell}=\{[a,b)\mid a<b\}$ is a basis for the lower limit topology and that $\mathcal{B}_{K}=\{(a,b)\mid a<b\}\cup\{(a,b)-K\mid a<b\}$, where $K=\{1/n\mid n\in\ZZ_{+}\}$, is a basis for the $K$-topology. We use Lemma 13.3: if $\mathcal{B},\mathcal{B}'$ are bases for topologies $\mathcal{T},\mathcal{T}'$, then $\mathcal{T}'\supset\mathcal{T}$ if and only if for every $x$ and every $B\in\mathcal{B}$ with $x\in B$ there is $B'\in\mathcal{B}'$ with $x\in B'\subset B$. So it suffices, in each direction, to exhibit a point at which the condition fails.

*$\RR_{K}$ is not finer than $\RR_{\ell}$.* Take the basis element $B=[0,1)\in\mathcal{B}_{\ell}$ and $x=0\in B$. Let $B_{K}\in\mathcal{B}_{K}$ contain $0$. Then $B_{K}=(a,b)$ or $B_{K}=(a,b)-K$ with $a<0<b$. In either case $a<a/2<0$, so $a/2\in(a,b)$ and $a/2\notin K$ (as $a/2<0$), hence $a/2\in B_{K}$; but $a/2<0$, so $a/2\notin[0,1)=B$. Thus no basis element of $\mathcal{B}_{K}$ containing $0$ is contained in $B$, and by Lemma 13.3 $\RR_{K}$ is not finer than $\RR_{\ell}$.

*$\RR_{\ell}$ is not finer than $\RR_{K}$.* Take the basis element $B_{K}=(-1,1)-K\in\mathcal{B}_{K}$ and $x=0\in B_{K}$. Let $B_{\ell}=[a,b)\in\mathcal{B}_{\ell}$ contain $0$, so $a\le0<b$. Choose $n\in\ZZ_{+}$ with $n>1/b$, which is possible since $\ZZ_{+}$ is unbounded; then $0<1/n<b$, so $1/n\in[0,b)\subset[a,b)=B_{\ell}$, while $1/n\in K$ and therefore $1/n\notin(-1,1)-K=B_{K}$. Thus no basis element of $\mathcal{B}_{\ell}$ containing $0$ is contained in $B_{K}$, and by Lemma 13.3 $\RR_{\ell}$ is not finer than $\RR_{K}$.

So neither topology is finer than the other: the topologies of $\RR_{\ell}$ and $\RR_{K}$ are not comparable.
:::
