---
schema: qual/card@1
id: P-UIHJF
kind: problem
title: A finitely generated group has finitely many subgroups of index $n$, and the
  possible numbers of index-$p$ subgroups of a finitely generated abelian group
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Abelian Groups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
(a) Suppose that $G$ is a finitely-generated group.
Let $n$ be a positive integer.
Prove that $G$ has only finitely many subgroups of index $n$.

(b) Let $p$ be a prime number.
If $G$ is any finitely-generated abelian group, let $t_p(G)$ denote the number of subgroups of $G$ of index $p$.
Determine the possible values of $t_p(G)$ as $G$ varies over all finitely-generated abelian groups.
:::

::: {.solution}
**Goal.** (a) A finitely generated group has finitely many subgroups of index $n$. (b) Determine the possible values of $t_p(G)$ for finitely generated abelian $G$.

::: pf

::: {.pf-step #s1}
(a) $G$ has finitely many subgroups of index $n$.

::: pf-proof

::: {.pf-step #s1-1}
Each subgroup $H \le G$ of index $n$ is the stabilizer of the point $1$ for some homomorphism $\rho_H: G \to S_n$.

::: pf-proof
$G$ acts on the $n$ cosets $G/H$ by left multiplication, and the stabilizer of the coset $H$ is $H$. Choose a bijection $G/H \to \theset{1, \dots, n}$ that sends $H$ to $1$. Transporting the action along this bijection gives $\rho_H$, and $H = \theset{g \in G : \rho_H(g)(1) = 1}$.
:::

:::

::: {.pf-step #s1-2}
There are finitely many homomorphisms $G \to S_n$.

::: pf-proof
$G$ is finitely generated, say by $g_1, \dots, g_m$; a homomorphism $G \to S_n$ is determined by the images of the generators, and there are $\cardinality{S_n}^m = (n!)^m$ choices.
:::

:::

::: pf-step
Hence there are finitely many subgroups of index $n$.

::: pf-proof
by step [](#s1-1){.pf-ref}, the subgroup $H$ is recovered from $\rho_H$ as the stabilizer of $1$, so $H \mapsto \rho_H$ is injective. By step [](#s1-2){.pf-ref} its target is finite.
:::

:::

:::

:::

::: {.pf-step #s2}
(b) The possible values of $t_p(G)$.

::: pf-proof

::: {.pf-step #s2-1}
Subgroups of index $p$ in $G$ correspond bijectively to the kernels of surjections $G \to \ZZ/p$, and two surjections have the same kernel exactly when they differ by an automorphism of $\ZZ/p$.

::: pf-proof
a subgroup $H$ of index $p$ gives $G/H \cong \ZZ/p$ (the only group of order $p$), and conversely the kernel of a surjection $G \to \ZZ/p$ has index $p$. Two surjections $f, f'$ with the same kernel $H$ both factor through isomorphisms $G/H \to \ZZ/p$, so $f' = \alpha \circ f$ for a unique $\alpha \in \Aut(\ZZ/p) \cong (\ZZ/p)^\times$, a group of order $p-1$.
:::

:::

::: {.pf-step #s2-2}
The number of surjections $G \to \ZZ/p$ is $p^r - 1$ where $r = \dim_{\ZZ/p}(G/pG)$.

::: pf-proof
$\Hom(G, \ZZ/p) \cong \Hom(G/pG, \ZZ/p) \cong (\ZZ/p)^r$, and a homomorphism to $\ZZ/p$ is surjective exactly when it is nonzero, so the surjections number $p^r - 1$.
:::

:::

::: {.pf-step #s2-3}
The integer $r$ takes every value $r \ge 0$ as $G$ varies.

::: pf-proof
By the structure theorem, $G \cong \ZZ^s \oplus \bigoplus_j \ZZ/m_j$, and $G/pG \cong (\ZZ/p)^s \oplus \bigoplus_j \ZZ/\gcd(m_j, p)$, so $r = s + t$ where $t$ is the number of $j$ with $p \mid m_j$. The group $G = \ZZ^r$ gives the value $r$.
:::

:::

::: pf-step
Hence the possible values of $t_p(G)$ are exactly
$$
t_p(G) = \frac{p^r - 1}{p - 1} = 1 + p + \cdots + p^{r-1}, \qquad r \ge 0.
$$

::: pf-proof
By steps [](#s2-1){.pf-ref} and [](#s2-2){.pf-ref}, the $p^r - 1$ surjections fall into classes of size $p - 1$, one class for each subgroup of index $p$. Step [](#s2-3){.pf-ref} shows that every $r \ge 0$ occurs.
:::

:::

:::

:::

::: pf-qed
step [](#s1){.pf-ref} proves (a); step [](#s2){.pf-ref} shows that the possible values of $t_p(G)$ are $\theset{(p^r - 1)/(p - 1) : r \ge 0}$.
:::

:::

:::
