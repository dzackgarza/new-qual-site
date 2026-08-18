---
order: 20
title: Sets and compactness
---

# Sets and compactness

## Compactness
    
[[T-YOZX6]]

## Topology / Sets

[[PR-25GM2]]

:::{.proof title="Compact iff sequentially compact, metric spaces"}
Let $(X,d)$ be a metric space.

- Compact $\implies$ sequentially compact.
  If a sequence $\theset{x_n}$ takes only finitely many values, some value occurs infinitely often and that constant subsequence converges.
  Otherwise pass to infinitely many distinct terms and write $S$ for their set.
  If no subsequence of $\theset{x_n}$ converges in $X$, then $S$ has no limit point in $X$, so $S$ is closed and discrete: each $s\in S$ has a ball $B_s$ with $B_s\cap S = \theset{s}$.
  Then $\theset{B_s}_{s\in S}$ together with $X\setminus S$ is an open cover with no finite subcover, so $X$ is not compact.

- Sequentially compact $\implies$ compact.
  A sequentially compact metric space is complete: a Cauchy sequence has a convergent subsequence, hence converges to the same limit.
  It is totally bounded: if not, some $\eps>0$ admits a sequence with $d(x_i,x_j)\geq \eps$ for $i\neq j$, and that sequence has no Cauchy (hence no convergent) subsequence.
  Complete and totally bounded metric spaces are compact: if an open cover $\mathcal{U}$ had no finite subcover, total boundedness would produce a nested sequence of nonempty closed sets $F_n$ with $\operatorname{diam} F_n \to 0$ and no $F_n$ covered by finitely many members of $\mathcal{U}$; completeness supplies a point of $\intersect_n F_n$, which lies in some $U\in\mathcal{U}$, and for large $n$ one has $F_n\subset U$.

:::

[[PR-FKJCO]]

:::{.proof title="?"}
Take $f_k(x) = x^n$, which converges to $\chi(x=1)$. 
The limit is not continuous, so no subsequence can converge.

:::

[[T-QPTHZ]]

[[PR-6C3GQ]]

[[C-WR7YV]]

[[PR-OGEEA]]

[[L-JBMRH]]

## Smallness for sets

[[PR-CZS5F]]

[[T-7FJFK]]

[[PR-JTFMW]]

:::{.proof title="?"}
Its complement is a union of open intervals, and can't contain an interval since intervals have positive measure and $m(C_n)$ tends to zero.

:::

[[C-44LL4]]

## Smallness for functions

[[PR-K5573]]

- **Arzela - Ascoli 1**:
If $\mathcal{F}$ is pointwise bounded and equicontinuous, then $\mathcal{F}$ is totally bounded in the uniform metric and its closure $\overline{\mathcal{F}} \in C(X)$ in the space of continuous functions is compact.

- **Arzela - Ascoli 2**:
If $\theset{f_k}$ is pointwise bounded and equicontinuous, then there exists a continuous $f$ such that $f_k \mapsvia{u} f$ on every compact set.

:::{.proof title="of Arzelà–Ascoli"}
Let $X$ be compact metric and $\mathcal{F}\subseteq C(X)$ pointwise bounded and equicontinuous.

- Totally bounded in the uniform metric.
  Given $\eps>0$, equicontinuity supplies $\delta>0$ such that $d(x,y)<\delta$ implies $\abs{f(x)-f(y)}<\eps$ for every $f\in\mathcal{F}$.
  Cover $X$ by finitely many $\delta$-balls with centres $x_1,\ldots,x_m$.
  Pointwise boundedness puts $\theset{(f(x_1),\ldots,f(x_m))\st f\in\mathcal{F}}$ in a bounded subset of $\RR^m$, hence in a totally bounded set: finitely many functions $f_1,\ldots,f_N\in\mathcal{F}$ $\eps$-net the values on the finite set $\theset{x_1,\ldots,x_m}$.
  For arbitrary $f\in\mathcal{F}$ some $f_j$ then satisfies $\abs{f(x_i)-f_j(x_i)}<\eps$ at each centre, and equicontinuity upgrades this to $\norm{f-f_j}_\infty < 3\eps$.

- Compactness of the closure.
  $C(X)$ is complete in $\norm{\,\cdot\,}_\infty$, so $\overline{\mathcal{F}}$ is complete and totally bounded, hence compact.
  Compactness in a metric space is sequential compactness, which is version 1.

- Version 2.
  Exhaust the domain by compact sets $K_n\nearrow$.
  Version 1 on each $K_n$ produces a subsequence uniformly Cauchy on $K_n$; the diagonal subsequence is uniformly Cauchy on every compact, and the uniform limit is continuous.

:::

- **Bolzano-Weierstrass**:
Every bounded sequence has a convergent subsequence.

- **Heine-Borel**:
$$
X \subseteq \RR^n \text{ is compact }
\iff
X \text{ is closed and bounded}
.$$

- **Baire Category Theorem:**
If $X$ is a complete metric space, then $X$ is a Baire space:

  - For any sequence $\theset{U_k}$ of open, dense sets, $\intersect_k U_k$ is also dense.
  - $X$ is *not* a countable union of nowhere-dense sets

- **Nested Interval Characterization of Completeness:**
$\RR$ being complete $\implies$ for any sequence of intervals $\theset{I_n}$ such that $I_{n+1} \subseteq I_n$, $\intersect I_n \neq \emptyset$.

- **Convergence Characterization of Completeness:**
$\RR$ being complete is equivalent to "absolutely convergent implies convergent" for sums of real numbers.

- Compacts subsets $K \subseteq \RR^n$ are also *sequentially compact*, i.e. every sequence in $K$ has a convergent subsequence.

- Closed subsets of compact sets are compact.

- Every compact subset of a Hausdorff space is closed

- **Urysohn's Lemma:**
For any two sets $A, B$ in a metric space or compact Hausdorff space $X$, there is a function $f:X \to I$ such that $f(A) = 0$ and $f(B) = 1$.

- Continuous compactly supported functions are
  - Bounded almost everywhere
  - Uniformly bounded
  - Uniformly continuous

    *Proof:*

    ![figures/2019-12-19-16-49-56.png](../../../../assets/assets/figures/2019-12-19-16-49-56.png)
		
- Uniform convergence allows commuting sums with integrals
