---
schema: qual/card@1
id: P-A2PAP
kind: problem
title: $A/A[p]$ versus $A^p$, and $A/A^p \cong A[p]$ when $A$ is finite
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both power-subgroup definitions, the two different quotients, and the finiteness assumption with June 2015 Groups 2 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the explicit quotient-to-image map and proved both equal cardinality and elementary-abelian structure before inferring the second isomorphism."
---

::: problem
Let $A$ be an abelian group (we will write the group multiplicatively in this problem).
For a prime number $p$, define the following subgroups of $A$: $$A^p := \{a^p : a \in A\}, \qquad A[p] := \{a \in A : a^p = 1\}.$$

a. Prove or give a counterexample: $A/A[p] \cong A^p$.

b. Prove: If $A$ is finite, then $A/A^p \cong A[p]$.
:::

::: solution
<1>1. The assertion in part (a) is true for every abelian group $A$.

::: proof
The power map $u:A\to A$, given by $u(a)=a^p$, is a homomorphism
because $A$ is abelian: $(ab)^p=a^pb^p$.
Its kernel is $A[p]$ and its image is $A^p$, so these are indeed
subgroups. Define
$$
\overline u:A/A[p]\longrightarrow A^p,
\qquad aA[p]\longmapsto a^p.
$$
It is well-defined: changing $a$ to $ac$ with $c^p=1$ does not
change $a^p$. It is a homomorphism and is onto by the definition
of $A^p$. If $a^p=b^p$, then $(b^{-1}a)^p=1$, so
$aA[p]=bA[p]$; thus it is also injective. This proves the first
isomorphism without any finiteness assumption.
:::

<1>2. If $A$ is finite, then $A/A^p$ and $A[p]$ have equal orders.

::: proof
Each fiber of $u$ is a coset of $A[p]$, so counting fibers gives
$|A|=|A[p]|\,|A^p|$. Therefore
$$
|A/A^p|=\frac{|A|}{|A^p|}=|A[p]|.
$$
:::

<1>3. Under the same finiteness assumption, the groups in part (b)
are isomorphic.

::: proof
Both groups are abelian and have exponent dividing $p$.
For $A[p]$ this is its defining property. For the quotient,
$$
(aA^p)^p=a^pA^p=A^p,
$$
since $a^p\in A^p$.

An abelian group $B$ of exponent dividing $p$ is a vector space
over $\mathbb F_p$: vector addition is the group operation and
scalar multiplication by the residue class of $n$ is $b\mapsto b^n$.
This is independent of the representative $n$ because $b^p=1$;
the vector-space identities follow from the laws of exponents
and commutativity. The group identity is the zero vector.

The two finite vector spaces $A/A^p$ and $A[p]$ have the same
cardinality by step <1>2. A finite-dimensional $\mathbb F_p$-space
of dimension $r$ has $p^r$ elements, so their dimensions are equal.
Choosing a basis in each and matching the bases gives a linear
isomorphism and hence the asserted group isomorphism. This also
covers the trivial groups, with dimension zero.
:::
:::
