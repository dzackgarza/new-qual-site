---
schema: qual/card@1
id: P-CH9S-T47
kind: problem
title: A normal subgroup of prime index contains $H$ or satisfies $NH=G$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: '2026-09-14'
  note: Checked against Team Problem Solutions for Ch 9, problem 47, in the deterministic
    MinerU Flash extraction assets/attachments/Ch9Sltns_extracted.md.
---

::: {.problem}
Suppose that N is a normal subgroup of a finite group G and H is a subgroup of G. If |G/N| is prime, prove that H is contained in N or that N H = G.
:::

::: {.solution}

Let
$$
\pi:G\longrightarrow G/N
$$
be the quotient homomorphism.

::: pf

::: {.pf-step #s1-1}

The subgroup $\pi(H)$ is either $\{N\}$ or all of $G/N$.


::: pf-proof

Because $H\leq G$ and $\pi$ is a homomorphism, $\pi(H)$ is a subgroup
of $G/N$. By hypothesis $\cardinality{G/N}$ is prime. A group of prime order has
no subgroups other than the identity subgroup and the whole group, so
$$
\pi(H)=\{N\}
\qquad\text{or}\qquad
\pi(H)=G/N.
$$

:::

:::

::: {.pf-step #s1-2}

If $\pi(H)=\{N\}$, then $H\subseteq N$.


::: pf-proof

For every $h\in H$, the assumption $\pi(H)=\{N\}$ gives
$$
hN=N.
$$
This is equivalent to $h\in N$. Hence every element of $H$ lies in
$N$, so $H\subseteq N$.

:::

:::

::: {.pf-step #s1-3}

If $\pi(H)=G/N$, then $NH=G$.


::: pf-proof

Let $g\in G$. Since $\pi(H)=G/N$, there is an $h\in H$ with
$$
gN=hN.
$$
Thus $gh^{-1}\in N$, so for some $n\in N$ one has
$$
g=nh\in NH.
$$
Hence $G\subseteq NH$. The reverse inclusion is immediate from
$N,H\subseteq G$, so $NH=G$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the only two cases. Step [](#s1-2){.pf-ref} gives $H\subseteq N$ in
the first case, and step [](#s1-3){.pf-ref} gives $NH=G$ in the second.

:::

:::

:::
