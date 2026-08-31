---
schema: qual/card@1
id: E-SMI-8000E-CY8
kind: exercise
title: Transitive subgroups of S(p) containing a transposition are everything
classification:
  areas:
  - algebra
  topics:
  - Symmetric Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
Prove that if $H$ is a transitive subgroup of $S(n)$, any two of the equivalence classes defined in [[E-SMI-8000E-CY7]] have the same number of elements.
Hence a transitive subgroup of $S(p)$, where $p$ is prime, either contains no 2-cycles or all 2-cycles.
Thus a transitive subgroup of $S(p)$ containing one 2-cycle — e.g. a subgroup containing a 2-cycle and a $p$-cycle — is all of $S(p)$.
[Hint: use [[E-SMI-8000E-CY6]] and [[E-SMI-8000E-CY7]].]
:::

::: {.solution}
<1>1. The equivalence relation defined by transpositions:
<2>1. On the set $\Omega = \{1, 2, \dots, n\}$, define the relation $i \sim j$ if $i = j$ or the 2-cycle $(i \, j) \in H$.
::: {.proof}
definition of relation.
:::
<2>2. $\sim$ is reflexive and symmetric by definition.
::: {.proof}
$(i \, j) = (j \, i)$.
:::
<2>3. $\sim$ is transitive: if $i \sim j$ and $j \sim k$ with $i, j, k$ distinct, then $(i \, j), (j \, k) \in H$.
Then $(i \, k) = (i \, j)(j \, k)(i \, j) \in H$, so $i \sim k$.
Thus $\sim$ is an equivalence relation.
::: {.proof}
conjugation of transpositions in $H$.
:::
<2>4. Let $\mathcal{B} = \{B_1, \dots, B_k\}$ be the partition of $\Omega$ into equivalence classes under $\sim$.
::: {.proof}
fundamental theorem of equivalence relations.
:::

<1>2. $H$ permutes equivalence classes and blocks have equal size:
<2>1. For any $\sigma \in H$ and $i \sim j$ with $i \neq j$:
\[
(\sigma(i) \, \sigma(j)) = \sigma (i \, j) \sigma^{-1} \in H,
\]
which implies $\sigma(i) \sim \sigma(j)$.
Thus for every class $B_a$, $\sigma(B_a) = B_b$ for some class $B_b$.
::: {.proof}
normality of subgroup under conjugation by elements of $H$.
:::
<2>2. Since $H$ acts transitively on $\Omega$, the action of $H$ on the set of equivalence classes $\mathcal{B}$ is transitive.
::: {.proof}
for any $x \in B_a$ and $y \in B_b$, transitivity of $H$ provides $\sigma \in H$ with $\sigma(x) = y$, hence $\sigma(B_a) = B_b$.
:::
<2>3. Since each $\sigma \in H$ is a bijection on $\Omega$, $|B_b| = |\sigma(B_a)| = |B_a| = m$.
Thus all equivalence classes have the same size $m$, and $n = k \cdot m$.
::: {.proof}
bijections preserve cardinality.
:::

<1>3. Primality and classification for $S(p)$:
<2>1. Let $n = p$ be a prime. Since $p = k \cdot m$, the block size $m$ must divide $p$.
Thus either $m = 1$ or $m = p$.
::: {.proof}
$p$ is prime.
:::
<2>2. **If $m = 1$:** Every equivalence class is a singleton, so there are no pairs $i \neq j$ with $(i \, j) \in H$.
Thus $H$ contains **no 2-cycles**.
::: {.proof}
definition of $\sim$.
:::
<2>3. **If $m = p$:** There is a single equivalence class $B_1 = \{1, \dots, p\}$, so $i \sim j$ for all $i, j \in \Omega$.
Thus $(i \, j) \in H$ for every pair of distinct elements, so $H$ contains **all 2-cycles**.
::: {.proof}
single equivalence class of size $p$.
:::

<1>4. Generation of $S(p)$:
<2>1. If $H \le S(p)$ is transitive and contains at least one 2-cycle, then $m \ge 2$, forcing $m = p$.
::: {.proof}
$m \mid p$ and $m \ge 2 \implies m = p$.
:::
<2>2. By <1>3 step <2>3, $H$ contains all $\binom{p}{2}$ transpositions in $S(p)$.
::: {.proof}
<1>3.
:::
<2>3. Since the transpositions generate the entire symmetric group $S(p)$, $H = S(p)$.
In particular, any subgroup containing a $p$-cycle (which is transitive) and a 2-cycle must be all of $S(p)$.
::: {.proof}
$S(p) = \langle (i \, j) : 1 \le i < j \le p \rangle$.
:::

<1>5. Conclusion:
Transitive subgroups of $S(p)$ containing a 2-cycle equal $S(p)$. Q.E.D.
::: {.proof}
<1>1 through <1>4.
:::
:::
