---
order: 20
title: Sets and compactness
topics:
- Compactness
- Metric Spaces
- Completeness
- Euclidean Spaces
- Countability
- Closure
---

# Sets and compactness

## Compactness

[[T-YOZX6]]

[[PR-25GM2]]

::: {.proof title="Compact if and only if sequentially compact, for metric spaces"}
Let $(X,d)$ be a metric space.

- Compact $\implies$ sequentially compact.
  If a sequence $\theset{x_n}$ takes only finitely many values, some value occurs infinitely often and that constant subsequence converges.
  Otherwise pass to infinitely many distinct terms and write $S$ for their set.
  If no subsequence of $\theset{x_n}$ converges in $X$, then $S$ has no limit point in $X$, so $S$ is closed and discrete: each $s\in S$ has a ball $B_s$ with $B_s\cap S = \theset{s}$.
  Then $\theset{B_s}_{s\in S}$ together with $X\setminus S$ is an open cover with no finite subcover, so $X$ is not compact.

- Sequentially compact $\implies$ compact.
  A sequentially compact metric space is complete: a Cauchy sequence has a convergent subsequence, hence converges to the same limit.
  It is totally bounded: if not, some $\varepsilon>0$ admits a sequence with $d(x_i,x_j)\geq \varepsilon$ for $i\neq j$, and that sequence has no Cauchy subsequence, hence no convergent subsequence.
  Complete and totally bounded metric spaces are compact: if an open cover $\mathcal{U}$ had no finite subcover, total boundedness would produce a nested sequence of nonempty closed sets $F_n$ with $\operatorname{diam} F_n \to 0$ and no $F_n$ covered by finitely many members of $\mathcal{U}$; completeness supplies a point of $\bigcap_n F_n$, which lies in some $U\in\mathcal{U}$, and for large $n$ one has $F_n\subseteq U$.

:::

[[PR-FKJCO]]

::: {.proof}
The functions $f_n(x)\coloneqq x^n$ lie in the closed unit ball of $C([0,1])$.
A subsequence converging in $\norm{\wait}_\infty$ would converge uniformly to its pointwise limit $\chi_{\theset1}$, which is not continuous; so no subsequence converges, and the unit ball is not sequentially compact, hence not compact.

:::

[[T-QPTHZ]]

## Series and suprema

[[PR-6C3GQ]]

[[C-WR7YV]]

[[PR-OGEEA]]

[[L-JBMRH]]

## Nowhere dense sets

[[PR-CZS5F]]

[[T-7FJFK]]

[[FT-6WPJI]]

[[PR-JTFMW]]

::: {.proof}
Let $C_n$ be the union of the $2^n$ closed intervals of length $3^{-n}$ remaining at stage $n$, so $C = \bigcap_n C_n$.
Each $C_n$ is closed, so $C$ is closed.
An interval contained in $C$ lies in some component of $C_n$ for every $n$, so has length at most $3^{-n}$ for every $n$; hence $C$ contains no interval and has empty interior.

:::

[[C-44LL4]]

## Compactness in function spaces

[[PR-HRAOC]]

::: {.theorem title="Arzelà--Ascoli"}
Let $X$ be a compact metric space and $\mathcal F\subseteq C(X)$.
If $\mathcal{F}$ is pointwise bounded and equicontinuous, then $\mathcal{F}$ is totally bounded in the metric $\norm{\wait}_\infty$, and its closure in $C(X)$ is compact.

If $U\subseteq\RR^n$ is open and $(f_k)$ is a pointwise bounded, equicontinuous sequence in $C(U)$, then some subsequence converges uniformly on every compact subset of $U$ to a continuous function.

:::

::: {.proof}
Let $\mathcal{F}\subseteq C(X)$ be pointwise bounded and equicontinuous, with $X$ compact.

- Total boundedness.
  Given $\varepsilon>0$, equicontinuity supplies $\delta>0$ such that $d(x,y)<\delta$ implies $\abs{f(x)-f(y)}<\varepsilon$ for every $f\in\mathcal{F}$.
  Cover $X$ by finitely many $\delta$-balls with centres $x_1,\ldots,x_m$.
  Pointwise boundedness puts $\theset{(f(x_1),\ldots,f(x_m))\st f\in\mathcal{F}}$ in a bounded, hence totally bounded, subset of $\RR^m$, so there are $f_1,\ldots,f_N\in\mathcal{F}$ such that every $f\in\mathcal F$ has some $f_j$ with $\abs{f(x_i)-f_j(x_i)}<\varepsilon$ for all $i$.
  For $x\in X$ choose $i$ with $d(x,x_i)<\delta$; then $\abs{f(x)-f_j(x)}\leq\abs{f(x)-f(x_i)}+\abs{f(x_i)-f_j(x_i)}+\abs{f_j(x_i)-f_j(x)}<3\varepsilon$, so $\norm{f-f_j}_\infty < 3\varepsilon$.

- Compactness of the closure.
  $C(X)$ is complete in $\norm{\wait}_\infty$, so the closure $\overline{\mathcal{F}}$ is complete, and it is totally bounded because $\mathcal F$ is; hence $\overline{\mathcal F}$ is compact.

- Sequences on an open set $U\subseteq\RR^n$.
  Write $U = \bigcup_n K_n$ with $K_n$ compact and $K_n\subseteq\operatorname{int}K_{n+1}$.
  By the first part applied on each $K_n$ and sequential compactness of compact metric spaces, there are successive subsequences converging uniformly on $K_1, K_2,\ldots$; the diagonal subsequence converges uniformly on every $K_n$, hence on every compact subset of $U$, and its limit is continuous.

:::

## Standard facts

- **Bolzano--Weierstrass.** Every bounded sequence in $\RR^n$ has a convergent subsequence.

- **Heine--Borel.** A subset of $\RR^n$ is compact if and only if it is closed and bounded.

- **Baire category theorem.** If $X$ is a complete metric space and $U_k\subseteq X$ are open and dense, then $\bigcap_k U_k$ is dense; in particular, a nonempty complete metric space is not a countable union of nowhere dense sets.

- **Nested intervals.** If $I_n = [a_n,b_n]$ are nonempty closed bounded intervals with $I_{n+1} \subseteq I_n$, then $\bigcap_n I_n \neq \emptyset$.

- **Completeness via series.** A normed space is complete if and only if every absolutely convergent series in it converges.

- Closed subsets of compact sets are compact, and compact subsets of Hausdorff spaces are closed.

- **Urysohn's lemma.** If $A$ and $B$ are disjoint closed subsets of a metric space or of a compact Hausdorff space $X$, there is a continuous $f\colon X \to [0,1]$ with $f|_A = 0$ and $f|_B = 1$.

- A continuous function with compact support on $\RR^n$ is bounded and uniformly continuous; see [[real-analysis/undergraduate/continuity#Uniform continuity|Continuity]] for the proof of the Heine--Cantor theorem.
