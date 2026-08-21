---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W1
kind: problem
title: Stone–Weierstrass and a polynomial algebra with high-degree terms
classification:
  areas:
  - real-analysis
  topics:
  - Stone-Weierstrass
  - Polynomials
  - Function Spaces
relations:
- kind: uses
  target: T-RA-WORKSHOP-D7-6-7
review: draft
solved: true
---

::: {.problem title="?"}
Give a precise statement of the Stone–Weierstrass theorem for real-valued continuous functions.
Then, verify that the set of all polynomials of the form $$\left\{\sum_{j=2017}^{N}a_jx^j:N\in\mathbb N,\ N\ge2017,\ a_j\in\mathbb R\right\}$$ along with the zero function is an algebra over $[-2,2]\subset\mathbb R$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** (1) State Stone–Weierstrass for real-valued continuous functions; (2) verify that $\mathcal A = \{\sum_{j=2017}^{N}a_jx^j : N \ge 2017,\ a_j \in \mathbb R\} \cup \{0\}$ is an algebra over $[-2,2]$.

<1>1. Statement of the theorem (real-valued version).
Proof: If $X$ is a compact Hausdorff space and $\mathcal A \subseteq C(X;\mathbb R)$ is a subalgebra that (i) contains the constant functions, (ii) separates points of $X$ (for every $x \neq y$ there is $h \in \mathcal A$ with $h(x) \neq h(y)$), then $\mathcal A$ is dense in $C(X;\mathbb R)$ with the sup norm.

<1>2. $\mathcal A$ is the set of all polynomials divisible by $x^{2017}$ (together with the zero polynomial), restricted to $[-2,2]$.
Proof: a polynomial $p(x) = \sum_{j=0}^{N}a_jx^j$ has no terms of degree $< 2017$ exactly when $p(x) = x^{2017}q(x)$ for a polynomial $q$; the zero polynomial is included explicitly.

<1>3. $\mathcal A$ is a vector subspace of $C[-2,2]$ closed under products.
<2>1. $0 \in \mathcal A$ by definition.
<2>2. Sums and scalar multiples stay in $\mathcal A$: $\sum_{j\ge2017}a_jx^j + \sum_{j\ge2017}b_jx^j = \sum_{j\ge2017}(a_j+b_j)x^j$, and $c\sum a_jx^j = \sum (ca_j)x^j$.
Proof: the lowest degree present remains $\ge 2017$.
<2>3. Products stay in $\mathcal A$: $(x^{2017}p)(x^{2017}q) = x^{2017}(x^{2017}pq)$, and the lowest degree of a product of two terms of degree $\ge 2017$ is $\ge 2017 + 2017 \ge 2017$.
Proof: $x^{2017}p \cdot x^{2017}q = x^{2017} \cdot [x^{2017}pq]$, and $x^{2017}pq$ is a polynomial; so the product is of the form $x^{2017}\cdot(\text{polynomial}) \in \mathcal A$.
<2>4. Q.E.D. Proof: <2>1–<2>3 are the axioms of a subalgebra of $C[-2,2]$ (scalars over $\mathbb R$). No constant functions beyond $0$ belong to $\mathcal A$, so the algebra does not contain the constants — it is a subalgebra, and the problem only asks to verify it is an algebra, not that it satisfies the Stone–Weierstrass hypotheses.
:::
