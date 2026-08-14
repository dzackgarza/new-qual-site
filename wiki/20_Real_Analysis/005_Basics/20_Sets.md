---
order: 20
---

# Basics

## Compactness
    
[[T-YOZX6]]


## Topology / Sets

[[PR-25GM2]]

#todo Proof

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

#todo Proof



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
