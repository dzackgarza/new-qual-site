---
schema: qual/card@1
id: P-MMAQ-O4HLIPMOVO
kind: problem
title: $K\subseteq L$ for finite fields iff $\#K=p^r$ and $\#L=p^s$ for the same prime
  $p$ with $r\leq s$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $K$ and $L$ be finite fields.
Show that $K$ is contained in $L$ if and only if $\# K = p^r$ and $\# L = p^s$ for the same prime $p$, and $r \leq s$.
:::

::: {.solution}
<1>1. Forward direction ($K \subseteq L \implies \operatorname{char} K = \operatorname{char} L = p$ and $r \mid s$):
<2>1. If $K$ is a subfield of $L$, then $L$ is a finite-dimensional vector space over $K$.
Let $d = [L : K] \ge 1$ denote the degree of the extension.
Proof: subfields endow the larger field with a vector space structure.
<2>2. Since $K$ has characteristic $p$, $L$ must also have characteristic $p$.
The cardinality of $L$ is related to the cardinality of $K$ by:
\[
\# L = (\# K)^d = (p^r)^d = p^{rd}.
\]
Proof: a $d$-dimensional vector space over a field with $q$ elements contains $q^d$ elements.
<2>3. Since $\# L = p^s$, we have $s = rd$, which implies $r \mid s$ (and therefore $r \le s$).
Proof: equating prime powers $p^s = p^{rd}$.

<1>2. Reverse direction ($\#K = p^r, \, \#L = p^s$ with $r \mid s \implies K \hookrightarrow L$):
<2>1. If $r \mid s$, then $(p^r - 1) \mid (p^s - 1)$ because:
\[
x^k - 1 = (x - 1)(x^{k-1} + \dots + 1) \quad \text{applied to } x = p^r, \, s = kr.
\]
Proof: polynomial divisibility of $x^k - 1$ by $x - 1$.
<2>2. The multiplicative group $L^\times$ is a cyclic group of order $p^s - 1$.
Since $(p^r - 1) \mid (p^s - 1)$, $L^\times$ contains a unique cyclic subgroup $H$ of order $p^r - 1$.
Proof: subgroup classification of finite cyclic groups.
<2>3. The subset $K' = H \cup \{0\} \subseteq L$ consists precisely of all roots of the polynomial $f(x) = x^{p^r} - x \in \mathbb{F}_p[x]$ in $L$.
Since the map $\phi(x) = x^{p^r}$ is an automorphism of $L$ (the $r$-th power of the Frobenius automorphism), the fixed set:
\[
K' = \operatorname{Fix}(\phi) = \{\alpha \in L \mid \alpha^{p^r} = \alpha\}
\]
is a subfield of $L$.
Proof: fixed field of a field automorphism is a subfield.
<2>4. The subfield $K'$ has cardinality $\# K' = p^r = \# K$.
Since any two finite fields with $p^r$ elements are isomorphic, $K \cong K' \subseteq L$, so $K$ is isomorphic to a subfield of $L$.
Proof: uniqueness up to isomorphism of finite fields of order $p^r$.

<1>3. Conclusion:
$K \subseteq L$ if and only if $\# K = p^r$ and $\# L = p^s$ for the same prime $p$ with $r \mid s$ (which in particular implies $r \le s$). Q.E.D.
Proof: <1>1 and <1>2.
:::
