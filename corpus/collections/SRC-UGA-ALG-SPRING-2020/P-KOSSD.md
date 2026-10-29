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
::: {.problem}
Let $N$ be a normal subgroup of a finite group $G$ such that the order of $N$ and the index of $N$ in $G$ are relatively prime ($\gcd(|N|, [G : N]) = 1$).

Prove that $N$ is the unique subgroup of $G$ of order $|N|$.
:::

::: {.solution}

::: pf

::: pf-step

There exist integers $s,t$ such that $|N|s+[G:N]t=1$.

::: pf-proof

::: pf-step

Let $n = |N|$ and $m = [G : N] = |G/N|$.

:::

::: pf-step

Since $N \trianglelefteq G$, the quotient group $G/N$ is well-defined and has order $|G/N| = m$.

:::

::: pf-step

By hypothesis, $\gcd(n, m) = 1$.

:::

::: pf-step

By Bézout's identity, there exist integers $s, t \in \ZZ$ such that

:::

$$n s + m t = 1.$$

:::

:::

::: pf-step

Every subgroup $K\leq G$ with $|K|=|N|$ is contained in $N$.

::: pf-proof

::: pf-step

Let $K \le G$ be a subgroup with $|K| = n$.

:::

::: pf-step

Let $x \in K$ be an arbitrary element.

:::

::: pf-step

By Lagrange's Theorem in $K$, the element order $\operatorname{ord}(x)$ divides $|K| = n$, so $x^n = e$.

:::

::: pf-step

In the quotient group $G/N$, Lagrange's Theorem implies that the order of any coset divides $|G/N| = m$, so $(x N)^m = x^m N = e N = N$.

:::

::: pf-step

Rewrite $x$ using $n s + m t = 1$:
    $$x = x^1 = x^{n s + m t} = (x^n)^s \cdot (x^m)^t = e^s \cdot (x^m)^t = (x^m)^t.$$

:::

::: pf-step

Consider the coset $x N \in G/N$:
    $$x N = (x^m)^t N = (x^m N)^t = N^t = N.$$

:::

::: pf-step

Since $x N = N$, $x \in N$.

:::

::: pf-step

Since $x \in K$ was arbitrary, $K \subseteq N$.

:::

:::

:::

::: {.pf-step #s3}

Every subgroup $K$ of order $|N|$ equals $N$.

::: pf-proof

::: pf-step

$K \subseteq N$ and $|K| = |N| = n < \infty$.

:::

::: pf-step

Any subset of a finite set with the same cardinality must be the entire set.

:::

::: pf-step

Thus $K = N$.

:::

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the required uniqueness.

:::

:::

:::
