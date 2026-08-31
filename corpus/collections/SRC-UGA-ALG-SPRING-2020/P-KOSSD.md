---
schema: qual/card@1
id: P-KOSSD
kind: problem
title: A normal subgroup of coprime order and index is the unique subgroup of that
  order
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: problem
Let $N$ be a normal subgroup of a finite group $G$ such that the order of $N$ and the index of $N$ in $G$ are relatively prime ($\gcd(|N|, [G : N]) = 1$).

Prove that $N$ is the unique subgroup of $G$ of order $|N|$.
:::

::: solution
**Goal:** Prove that if $N \trianglelefteq G$ has $\gcd(|N|, [G : N]) = 1$, then any subgroup $K \le G$ with $|K| = |N|$ satisfies $K = N$, using Bézout's identity and orders in the quotient group $G/N$.

<1>1. Setting up notation and Bézout's identity:
::: {.proof}
    <2>1. Let $n = |N|$ and $m = [G : N] = |G/N|$.
    <2>2. Since $N \trianglelefteq G$, the quotient group $G/N$ is well-defined and has order $|G/N| = m$.
    <2>3. By hypothesis, $\gcd(n, m) = 1$.
    <2>4. By Bézout's identity, there exist integers $s, t \in \mathbb{Z}$ such that
    $$n s + m t = 1.$$

:::

<1>2. Inclusion $K \subseteq N$ for any subgroup $K \le G$ of order $|K| = n$:
::: {.proof}
    <2>1. Let $K \le G$ be a subgroup with $|K| = n$.
    <2>2. Let $x \in K$ be an arbitrary element.
    <2>3. By Lagrange's Theorem in $K$, the element order $\operatorname{ord}(x)$ divides $|K| = n$, so $x^n = e$.
    <2>4. In the quotient group $G/N$, Lagrange's Theorem implies that the order of any coset divides $|G/N| = m$, so $(x N)^m = x^m N = e N = N$.
    <2>5. Rewrite $x$ using $n s + m t = 1$:
    $$x = x^1 = x^{n s + m t} = (x^n)^s \cdot (x^m)^t = e^s \cdot (x^m)^t = (x^m)^t.$$
    <2>6. Consider the coset $x N \in G/N$:
    $$x N = (x^m)^t N = (x^m N)^t = N^t = N.$$
    <2>7. Since $x N = N$, $x \in N$.
    <2>8. Since $x \in K$ was arbitrary, $K \subseteq N$.

:::

<1>3. Equality $K = N$:
::: {.proof}
    <2>1. $K \subseteq N$ and $|K| = |N| = n < \infty$.
    <2>2. Any subset of a finite set with the same cardinality must be the entire set.
    <2>3. Thus $K = N$.

:::

<1>4. Conclusion:
::: {.proof}
    $N$ is the unique subgroup of $G$ of order $|N|$.
:::
:::
