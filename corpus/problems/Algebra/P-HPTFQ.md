---
schema: qual/card@1
id: P-HPTFQ
kind: problem
title: Cauchy's theorem
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Cosets and Lagrange
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
- Prove Cauchy's theorem.

> Induce on $\size G$.
> Assume $\size G > p$ and pick $g\neq 1$.
> If $p\divides \size g$, use cyclic group theory, so assume otherwise.
> Use that $\size G = \size G/N \size N$ so $p$ divides $\size G/N$, apply IH to get an element of order $p$ in the quotient.
> Then $y\not\in N$ but $y^p\in N$, so $\gens{y}\neq \gens{y^p}$ since $y^p\in N \implies \gens{y^p} \subseteq N$.
> Get $p\divides \size \gens{y}$, apply IH.
:::

::: solution
**Theorem.**  
Let $G$ be a finite group and let $p$ be a prime dividing $|G|$.
Then there exists $x\in G$ with order $p$.

*Proof.* Set
$$
X=\{(g_1,\dots,g_p)\in G^p\mid g_1g_2\cdots g_p=1_G\}.
$$
Define a cyclic shift action of $C_p=\langle \sigma\rangle$ on $X$ by
$$
\sigma(g_1,\dots,g_p)=(g_2,\dots,g_p,g_1).
$$

**Lemma 1.**  
The cardinality $|X|=|G|^{p-1}$ is divisible by $p$.

*Proof.* The condition determines $(g_1,\dots,g_{p-1})\in G^{p-1}$ and then $g_p$ uniquely.
Hence $|X|=|G|^{p-1}$, and $p\mid |G|$ implies $p\mid |X|$. ∎

**Lemma 2.**  
Any $C_p$-orbit in $X$ has size either $1$ or $p$.

*Proof.* The acting group has size $p$. Orbit size equals the index of the stabilizer and hence divides $p$. ∎

**Lemma 3.**  
There is a fixed point of the action outside
$\{(g,\dots,g): g^p\neq 1_G\}$.

*Proof.* Let $F$ be the fixed point set. By Lemma 2 and Lemma 1, $|X|-|F|$ is a multiple of $p$.
Since $|X|$ is a multiple of $p$, so is $|F|$. The trivial fixed points are exactly tuples $(g,\dots,g)$.
At least the tuple $(1,\dots,1)$ lies in $F$, so $|F|\ge p$. Therefore some
nontrivial tuple $(g,\dots,g)$ belongs to $F$ with $g\neq1$.  
Because fixedness gives $\sigma(g,\dots,g)=(g,\dots,g)$ and also
$(g,\dots,g)$ is in $X$, we have $g^p=1$. Hence $g$ has order $p$. ∎

Lemma 1 gives $p$ divisibility, Lemma 2 gives decomposition into orbits of sizes $1,p$,
and Lemma 3 gives a nontrivial fixed point, so $\operatorname{ord}(g)=p$. ∎
:::
