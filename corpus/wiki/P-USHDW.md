---
schema: qual/card@1
id: P-USHDW
kind: problem
title: "Let $R$ be a commutative ring with multiplicative identity. Assume Zor\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Let $R$ be a commutative ring with multiplicative identity. Assume Zorn's Lemma.

a.
Show that
$$
N = \{r \in R \mid r^n = 0 \text{ for some } n > 0\}
$$
is an ideal which is contained in any prime ideal.

b.
Let $r$ be an element of $R$ not in $N$.
Let $S$ be the collection of all proper ideals of $R$ not containing any positive power of $r$. Use Zorn's Lemma to prove that
there is a prime ideal in $S$.

c.
Suppose that $R$ has exactly one prime ideal $P$ . Prove that every element $r$ of $R$ is either nilpotent or a unit.

:::{.concept}
\envlist

- Prime ideal: $\mathfrak{p}$ is prime iff $ab \in \mathfrak{p} \implies a\in \mathfrak{p}$ or $b\in \mathfrak{p}$.
- Silly fact: 0 is in every ideal!
 
- **Zorn's Lemma:** Given a poset, if every chain has an upper bound, then there is a maximal element. (Chain: totally ordered subset.)
 
- **Corollary:** If $S\subset R$ is multiplicatively closed with $0\not\in S$ then $\theset{I \normal R \suchthat J\intersect S = \emptyset}$ has a maximal element.

- **Theorem:** If $R$ is commutative, maximal $\implies$ prime for ideals.

- **Theorem:** Non-units are contained in a maximal ideal. (See HW?)

:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Let $\mathfrak{p}$ be prime and $x\in N$.
- Then $x^k = 0 \in \mathfrak{p}$ for some $k$, and thus $x^k = x x^{k-1} \in \mathfrak p$.
- Since $\mathfrak p$ is prime, inductively we obtain $x\in\mathfrak p$.
:::

:::{.proof title="of b"}
\envlist

- Let $S = \theset{r^k \mid k\in \NN}$ be the set of positive powers of $r$. 

- Then $S^2 \subseteq S$, since $r^{k_1}r^{k_2} = r^{k_1+k_2}$ is also a positive power of $r$, and $0\not\in S$ since $r\neq 0$ and $r\not\in N$.

- By the corollary, $\theset{I \normal R \suchthat I\intersect S = \emptyset}$ has a maximal element $\mathfrak{p}$.

- Since $R$ is commutative, $\mathfrak{p}$ is prime.

:::

:::{.proof title="of c"}
\envlist

- Suppose $R$ has a unique prime ideal $\mathfrak{p}$.

- Suppose $r\in R$ is not a unit, and toward a contradiction, suppose that $r$ is also not nilpotent.

- Since $r$ is not a unit, $r$ is contained in some maximal (and thus prime) ideal, and thus $r \in \mathfrak{p}$.

- Since $r\not\in N$, by (b) there is a maximal ideal $\mathfrak{m}$ that avoids all positive powers of $r$. 
Since $\mathfrak{m}$ is prime, we must have $\mathfrak{m} = \mathfrak{p}$.
  But then $r\not\in \mathfrak{p}$, a contradiction.

:::

:::
