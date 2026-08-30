---
schema: qual/card@1
id: P-AMD-LWL6CAW2
kind: problem
title: 'Given: $|G| < \infty, N \normal G, (|N|, [G:N]) =1$'
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Given: $|G| < \infty, N \normal G, (|N|, [G:N]) =1$

Show: $N$ is the unique subgroup of order $|N|$
:::

::: {.solution}
<1>1. Setup and projection to the quotient group:
<2>1. Let $H \le G$ be any subgroup of $G$ with $|H| = |N|$.
Let $\pi: G \to G/N$ be the canonical quotient homomorphism defined by $\pi(g) = gN$.
Proof: definition of canonical projection onto the quotient group.
<2>2. The image $\pi(H) = HN/N$ is a subgroup of $G/N$.
By the Second Isomorphism Theorem:
\[
\pi(H) = HN/N \cong H / (H \cap N).
\]
Proof: Second Isomorphism Theorem for groups.

<1>2. Divisibility of $|\pi(H)|$:
<2>1. From the isomorphism $\pi(H) \cong H / (H \cap N)$, the order of $\pi(H)$ satisfies:
\[
|\pi(H)| = \frac{|H|}{|H \cap N|} \implies |\pi(H)| \text{ divides } |H| = |N|.
\]
Proof: Lagrange's Theorem applied to the subgroup $H \cap N \le H$.
<2>2. Since $\pi(H) \le G/N$, by Lagrange's Theorem for the quotient group:
\[
|\pi(H)| \text{ divides } |G/N| = [G : N].
\]
Proof: Lagrange's Theorem applied to $\pi(H) \le G/N$.

<1>3. Coprimality and triviality of the quotient image:
<2>1. The order $|\pi(H)|$ is a positive integer that simultaneously divides $|N|$ and $[G : N]$.
Therefore:
\[
|\pi(H)| \text{ divides } \gcd(|N|, [G : N]) = 1.
\]
Thus $|\pi(H)| = 1$, which means $\pi(H) = \{eN\}$ is the trivial subgroup of $G/N$.
Proof: common divisor of coprime positive integers is 1.

<1>4. Deduction that $H = N$:
<2>1. Because $\pi(H) = \{eN\}$, for every element $h \in H$ we have $\pi(h) = hN = N$, which means $h \in N$.
Thus:
\[
H \subseteq N.
\]
Proof: kernel definition $\ker(\pi) = N$.
<2>2. Since $H \subseteq N$ and $|H| = |N| < \infty$, we must have $H = N$.
Proof: pigeonhole principle for finite sets of equal cardinality.

<1>5. Conclusion:
$N$ is the unique subgroup of $G$ of order $|N|$. Q.E.D.
Proof: <1>1 through <1>4.
:::
