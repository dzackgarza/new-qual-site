---
schema: qual/card@1
id: P-7XPOK
kind: problem
title: "Show that any disjoint intervals is countable. Show that\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - cantor-set
  - borel-cantelli
relations: []
review: draft
solved: true
---

::: problem
- Show that any disjoint intervals is countable.

- Show that every open $U \subseteq \RR$ is a countable union of disjoint open intervals.

- Show that every open $U \subseteq \RR^n$ is a countable union of *almost* disjoint closed cubes.

- Show that that Cantor middle-thirds set is compact, totally disconnected, and perfect, with outer measure zero.

- Prove the Borel-Cantelli lemma.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. A family of pairwise disjoint intervals in $\RR$, each with nonempty interior, is countable.
Proof: each such interval contains a rational number, and disjoint intervals contain distinct rationals; the rationals are countable, so the family embeds injectively into $\QQ$.
(The nondegeneracy hypothesis is necessary: $\{\{x\} : x \in \RR\}$ is an uncountable family of disjoint singletons.)

<1>2. Every open $U \subseteq \RR$ is a countable union of disjoint open intervals.
<2>1. Define an equivalence relation on $U$: $x \sim y$ iff $x$ and $y$ lie in a common open interval contained in $U$.
Proof: reflexivity, symmetry, and transitivity (concatenation of intervals).
<2>2. Each equivalence class is an open interval.
Proof: the union of all open intervals in $U$ containing a point is open, connected, hence an interval; the classes are the connected components of $U$.
<2>3. The classes are pairwise disjoint open intervals whose union is $U$, and there are countably many.
Proof: classes partition $U$ by construction; each class contains a rational (it is an open interval — nonempty interior), distinct classes contain distinct rationals, so there are countably many.

<1>3. Every open $U \subseteq \RR^n$ is a countable union of almost disjoint closed cubes.
Proof: consider the dyadic cubes contained in $U$ whose parent is not contained in $U$ (maximal dyadic cubes); they cover $U$ (every point of $U$ lies in a small dyadic cube inside $U$, hence in a maximal one), are countable (finitely many per level), and have pairwise disjoint interiors (dyadic cubes are nested or interior-disjoint, and maximality rules out containment).

<1>4. The Cantor middle-thirds set is compact, totally disconnected, and perfect, with outer measure zero.
<2>1. Compact: $C = \bigcap_n C_n$ with each $C_n$ a finite union of closed intervals, so $C$ is closed and bounded.
Proof: definition of the construction.
<2>2. Outer measure zero: $m^*(C) \le m(C_n) = (2/3)^n$ for all $n$.
Proof: $C_n$ is $2^n$ intervals of length $3^{-n}$.
<2>3. Totally disconnected: $C$ contains no interval of positive length (it has measure $0$), and any two distinct points are separated by a removed middle third (their ternary expansions differ at a digit where one has a $1$). Proof: <2>2 and the ternary-digit argument.
<2>4. Perfect: every $x \in C$ lies in one half of its stage-$n$ interval; the other half contains a point of $C$ (complete the ternary digits with $0$'s) at distance at least $3^{-(n+1)}$; letting $n \to \infty$ gives points of $C \setminus \{x\}$ arbitrarily close to $x$.
Proof: the two halves are separated by the removed middle third.

<1>5. Borel–Cantelli lemma: if $(E_n)$ is a sequence of measurable sets with $\sum_n \mu(E_n) < \infty$, then $\mu(\limsup_n E_n) = 0$.
<2>1. $\limsup_n E_n = \bigcap_N\bigcup_{n \ge N}E_n$ is measurable.
Proof: countable unions and intersections.
<2>2. $\mu(\limsup_n E_n) \le \sum_{n \ge N}\mu(E_n)$ for every $N$.
Proof: $\limsup_n E_n \subseteq \bigcup_{n \ge N}E_n$ and countable subadditivity.
<2>3. $\sum_{n \ge N}\mu(E_n) \to 0$ as $N \to \infty$.
Proof: $\sum_n\mu(E_n) < \infty$, so the tails vanish.
<2>4. Q.E.D. Proof: <2>2 and <2>3 force $\mu(\limsup_n E_n) = 0$.
:::
