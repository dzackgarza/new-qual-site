---
schema: qual/card@1
id: P-ALGS12B
kind: problem
title: Localization of a UFD at a multiplicative system is a UFD
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Localization
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $R$ be a UFD. Let $S$ be any multiplicative system of nonzero elements in $R$, and let $S^{-1}R$ be the localization of $R$ at $S$.

(a) Let $x$ be an irreducible element of $R$.
Show that the element $\frac{x}{1}$ is either irreducible in $S^{-1}R$ or a unit.
Conversely, show that every irreducible in $S^{-1}R$ is an associate of $\frac{x}{1}$ for some $x$ which is irreducible in $R$.

(b) Show that (i) every element of $S^{-1}R$ is a finite product of irreducibles; and (ii) every irreducible element of $S^{-1}R$ is prime.
(It is well-known that these conditions imply that $S^{-1}R$ is a UFD, so you have proved that $S^{-1}R$ is also a UFD.)
:::

::: {.solution}
<1>1. Part (a): Irreducibles in $S^{-1}R$:
<2>1. Let $x \in R$ be irreducible. In the UFD $R$, every irreducible element is prime, so $(x)$ is a prime ideal.
::: {.proof}
prime and irreducible elements coincide in UFDs.
:::
<2>2. **Case 1: $(x) \cap S \neq \emptyset$.**
There exists $s \in S$ such that $s = rx$ for some $r \in R$.
Then $\frac{x}{1} \cdot \frac{r}{s} = \frac{rx}{s} = \frac{s}{s} = 1$, so $\frac{x}{1}$ is a unit in $S^{-1}R$.
::: {.proof}
definition of units in localization.
:::
<2>3. **Case 2: $(x) \cap S = \emptyset$.**
Suppose $\frac{x}{1} = \frac{a}{s_1} \frac{b}{s_2}$ for some $\frac{a}{s_1}, \frac{b}{s_2} \in S^{-1}R$.
Then $s_1 s_2 x = ab$ in $R$ (since $R$ is an integral domain).
Because $x$ is prime in $R$, $x \mid ab \implies x \mid a$ or $x \mid b$.
Without loss of generality, assume $x \mid a$, so $a = x a'$ for some $a' \in R$.
Substituting gives $s_1 s_2 x = x a' b \implies s_1 s_2 = a' b$.
Thus $b$ divides $s_1 s_2 \in S$. Setting $t = s_1 s_2 \in S$, we have $\frac{b}{s_2} \cdot \frac{a'}{s_1} = \frac{a' b}{s_1 s_2} = 1$, so $\frac{b}{s_2}$ is a unit in $S^{-1}R$.
Therefore $\frac{x}{1}$ is irreducible in $S^{-1}R$.
::: {.proof}
definition of irreducible element.
:::
<2>4. **Converse:** Let $\frac{y}{s} \in S^{-1}R$ be irreducible.
Since $\frac{1}{s}$ is a unit, $\frac{y}{s}$ is associate to $\frac{y}{1}$.
In the UFD $R$, factor $y = u p_1^{e_1} \cdots p_k^{e_k}$ into irreducibles.
In $S^{-1}R$, $\frac{y}{1} = \frac{u}{1} \left(\frac{p_1}{1}\right)^{e_1} \cdots \left(\frac{p_k}{1}\right)^{e_k}$.
Since $\frac{y}{1}$ is irreducible (hence a non-unit), at least one $p_i$ is a non-unit in $S^{-1}R$.
Because $\frac{y}{1}$ is irreducible, there can be exactly one such non-unit factor and its exponent must be 1.
All other factors are units in $S^{-1}R$.
Thus $\frac{y}{s}$ is an associate of $\frac{p_i}{1}$ for some irreducible $p_i \in R$.
::: {.proof}
factorization in $R$ maps to factorization in $S^{-1}R$.
:::

<1>2. Part (b): $S^{-1}R$ is a UFD:
<2>1. **(i) Existence of factorization into irreducibles:**
Let $\frac{a}{s} \in S^{-1}R$ be a non-zero non-unit.
Factor $a = u p_1 \cdots p_m$ into irreducibles in $R$.
Then $\frac{a}{s} = \frac{u}{s} \frac{p_1}{1} \cdots \frac{p_m}{1}$.
By Part (a), each $\frac{p_j}{1}$ is either a unit or an irreducible in $S^{-1}R$.
Absorbing all unit factors into $\frac{u}{s}$, $\frac{a}{s}$ is expressed as a unit times a product of irreducibles in $S^{-1}R$.
::: {.proof}
factoring the numerator in $R$.
:::
<2>2. **(ii) Every irreducible in $S^{-1}R$ is prime:**
Let $\frac{x}{1}$ be irreducible in $S^{-1}R$. By Part (a), $x$ is prime in $R$ and $(x) \cap S = \emptyset$.
Suppose $\frac{x}{1} \mid \frac{a}{s_1} \frac{b}{s_2}$ in $S^{-1}R$.
Then there exists $\frac{c}{s_3} \in S^{-1}R$ such that $\frac{ab}{s_1 s_2} = \frac{x c}{s_3} \implies s_3 ab = s_1 s_2 c x$ in $R$.
Since $x$ is prime in $R$, $x \mid s_3 ab \implies x \mid s_3$ or $x \mid a$ or $x \mid b$.
Since $(x) \cap S = \emptyset$ and $s_3 \in S$, $x \nmid s_3$.
Therefore $x \mid a$ or $x \mid b$.
If $x \mid a$, then $\frac{x}{1} \mid \frac{a}{s_1}$; if $x \mid b$, then $\frac{x}{1} \mid \frac{b}{s_2}$ in $S^{-1}R$.
Thus $\frac{x}{1}$ is prime in $S^{-1}R$.
::: {.proof}
localization preserves primality for primes disjoint from $S$.
:::
<2>3. Since every non-zero non-unit factors into irreducibles and every irreducible is prime, $S^{-1}R$ is a UFD.
::: {.proof}
standard criterion for unique factorization domains.
:::

<1>3. Conclusion:
$S^{-1}R$ satisfies all unique factorization domain axioms. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
