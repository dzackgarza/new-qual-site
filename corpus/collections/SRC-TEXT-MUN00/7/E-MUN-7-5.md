---
schema: qual/card@1
id: E-MUN-7-5
kind: problem
title: Countability of function spaces and subsets of $\ZZ_+$
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 5; the stored statement matches.
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
    Read against Munkres, Topology (2000), §7 Exercise 5, printed p. 51; all ten parts
    (a)-(j) are stored as printed, including the definitions of eventually zero and
    eventually constant.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.5,
    printed pp. 85-89 (tmp/sources/munkres-solutions-whitman.pdf). His verdicts are the
    card's - (a), (b), (c), (f), (g), (h), (i), (j) countable and (d), (e) uncountable -
    and each answer is obtained the same way: a finite or countable product for the
    countable cases, and for (d) the injection of {0,1}^omega by adding 1 to each
    coordinate. No defect found.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 7.5, printed pp. 85-89); statement and the ten verdicts unchanged, one step per part. The numbered results of §7 each part uses are now named with their pages, checked against the retained PDF: Corollary 7.3 (a subset of a countable set is countable) and Corollary 7.4 (Z+ x Z+) and Theorem 7.5 (countable unions) on printed p. 48, Theorem 7.6 (finite products) and Theorem 7.7 ({0,1}^omega uncountable) on printed p. 49, with Theorem 7.1 on printed p. 45 for the surjection criterion in (j); the exercise is on printed p. 51. Two steps supply what the prose left implicit: that the image of {0,1}^omega under x -> x+1 is uncountable because its domain is and a subset of a countable set would be countable, and why the surjection in (j) is surjective.

---

::: {.exercise}

Determine, for each of the following sets, whether or not it is countable.
Justify your answers.

(a) The set $A$ of all functions $f:\{0,1\} \to \ZZ_{+}$ .

(b) The set $B_{n}$ of all functions $f:\{1,\ldots ,n\} \to \ZZ_{+}$ .

(c) The set $C = \bigcup_{n\in \ZZ_{+}}B_{n}$ .

(d) The set $D$ of all functions $f: \ZZ_{+} \to \ZZ_{+}$ .

(e) The set $E$ of all functions $f:\ZZ_+\to\{0,1\}$.

(f) The set $F$ of all functions $f: \ZZ_{+} \to \{0,1\}$ that are "eventually zero."
[We say that $f$ is eventually zero if there is a positive integer $N$ such that $f(n) = 0$ for all $n \geq N$ .]

(g) The set $G$ of all functions $f: \ZZ_{+} \to \ZZ_{+}$ that are eventually 1.

(h) The set $H$ of all functions $f: \ZZ_{+} \to \ZZ_{+}$ that are eventually constant.

(i) The set $I$ of all two-element subsets of $\ZZ_{+}$ .

(j) The set $J$ of all finite subsets of $\ZZ_{+}$ .

:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.5** (`tmp/sources/munkres-solutions-whitman.pdf`); the ten verdicts and the justifications below are his, with the numbered results of §7 named for each.

Throughout, $X^\omega$ is the set of functions $\ZZ_+\to X$ and $X^n$ the set of functions $\{1,\dots,n\}\to X$; a set is countable when it is finite or countably infinite, and a subset of a countable set is countable (Corollary 7.3). The results used are: $\ZZ_+\times\ZZ_+$ countably infinite (Corollary 7.4), a countable union of countable sets countable (Theorem 7.5), a finite product of countable sets countable (Theorem 7.6), and $\{0,1\}^\omega$ uncountable (Theorem 7.7). The exercise is on printed p. 51.

::: pf

::: {.pf-step #a}
(a) $A=\{f:\{0,1\}\to\ZZ_+\}$ is countable.

::: pf-proof
The map $f\mapsto(f(0),f(1))$ is a bijection of $A$ with $\ZZ_+\times\ZZ_+$, which is countably infinite by Corollary 7.4.

:::

:::

::: {.pf-step #b}
(b) $B_n=\{f:\{1,\dots,n\}\to\ZZ_+\}$ is countable.

::: pf-proof
$f\mapsto(f(1),\dots,f(n))$ is a bijection $B_n\to(\ZZ_+)^n$, and $(\ZZ_+)^n$ is countable by Theorem 7.6 applied to the $n$ factors $\ZZ_+$.

:::

:::

::: {.pf-step #c}
(c) $C=\bigcup_{n\in\ZZ_+}B_n$ is countable.

::: pf-proof
$C$ is a countable union of the countable sets $B_n$ of step [](#b){.pf-ref}, hence countable by Theorem 7.5.

:::

:::

::: {.pf-step #d}
(d) $D=\ZZ_+^{\omega}$ is uncountable.

::: pf-proof
The map $\Phi:\{0,1\}^\omega\to D$, $(x_n)\mapsto(x_n+1)$, is injective, since $x_n+1=y_n+1$ gives $x_n=y_n$ for every $n$. The domain is uncountable by Theorem 7.7, so the image $\Phi(\{0,1\}^\omega)\subset D$ is uncountable; were $D$ countable, Corollary 7.3 would make that image countable. Hence $D$ is uncountable.

:::

:::

::: {.pf-step #e}
(e) $E=\{f:\ZZ_+\to\{0,1\}\}=\{0,1\}^\omega$ is uncountable.

::: pf-proof
This is Theorem 7.7 with $X=\{0,1\}$.

:::

:::

::: {.pf-step #f}
(f) $F=\{f:\ZZ_+\to\{0,1\}: f$ eventually zero$\}$ is countable.

::: pf-proof
Let $F_N=\{f\in F: f(n)=0$ for all $n\ge N\}$. Such an $f$ is determined by the $N-1$ values $f(1),\dots,f(N-1)$, so $F_N$ has at most $2^{N-1}$ elements and is finite. Every eventually zero $f$ lies in $F_N$ for some $N$, so $F=\bigcup_{N\ge1}F_N$ is a countable union of finite sets, hence countable by Theorem 7.5.

:::

:::

::: {.pf-step #g}
(g) $G=\{f:\ZZ_+\to\ZZ_+: f$ eventually $1\}$ is countable.

::: pf-proof
Let $G_N=\{f: f(n)=1$ for all $n\ge N\}$. Then $f\mapsto(f(1),\dots,f(N-1))$ is a bijection $G_N\to(\ZZ_+)^{N-1}$, so $G_N$ is countable by Theorem 7.6, and $G=\bigcup_{N\ge1}G_N$ is countable by Theorem 7.5.

:::

:::

::: {.pf-step #h}
(h) $H=\{f:\ZZ_+\to\ZZ_+: f$ eventually constant$\}$ is countable.

::: pf-proof
Let $H_{N,c}=\{f: f(n)=c$ for all $n\ge N\}$ for $N,c\in\ZZ_+$. As in step [](#g){.pf-ref}, $f\mapsto(f(1),\dots,f(N-1))$ is a bijection $H_{N,c}\to(\ZZ_+)^{N-1}$, so each $H_{N,c}$ is countable. The family is indexed by the countable set $\ZZ_+\times\ZZ_+$, and $H=\bigcup_{N,c}H_{N,c}$, so $H$ is countable by Theorem 7.5.

:::

:::

::: {.pf-step #i}
(i) $I$, the set of two-element subsets of $\ZZ_+$, is countable.

::: pf-proof
The map $\{(m,n)\in\ZZ_+\times\ZZ_+: m<n\}\to I$, $(m,n)\mapsto\{m,n\}$, is bijective: it is surjective because a two-element subset $\{a,b\}$ is the image of $(a,b)$ in the order making $a<b$, and injective because a two-element set $\{m,n\}$ determines its two elements and hence the ordered pair $(m,n)$ with $m<n$. Its domain is a subset of the countable set $\ZZ_+\times\ZZ_+$ (Corollary 7.4), so it is countable by Corollary 7.3, and so is $I$.

:::

:::

::: {.pf-step #j}
(j) $J$, the set of finite subsets of $\ZZ_+$, is countable.

::: pf-proof
Let $J_n$ be the family of subsets of $\ZZ_+$ with at most $n$ elements. The map $(\ZZ_+)^n\to J_n-\{\varnothing\}$, $(a_1,\dots,a_n)\mapsto\{a_1,\dots,a_n\}$, is surjective, because a subset with $k\le n$ elements $\{b_1,\dots,b_k\}$ is the image of the $n$-tuple $(b_1,\dots,b_k,b_1,\dots,b_1)$, repetitions being allowed. So $J_n-\{\varnothing\}$ is countable by Theorem 7.1, and $J_n$ is countable. Then $J=\{\varnothing\}\cup\bigcup_{n\ge1}J_n$ is a countable union of countable sets, hence countable by Theorem 7.5.

:::

:::

:::

:::
