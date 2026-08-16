---
schema: qual/card@1
id: E-AMD-4M4FKNN3
kind: exercise
title: Show that Sylow $p_i\dash$subgroups $S_{p_1}, S_{p_2}$ for distinct…
classification:
  areas:
  - algebra
  topics:
  - sylow-theory
  - p-groups
relations: []
review: draft
---

::: {.exercise}
Show that Sylow $p_i\dash$subgroups $S_{p_1}, S_{p_2}$ for distinct primes $p_1\neq p_2$ intersect trivially.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $G$ be a finite group, and let $p_1, p_2$ be distinct prime numbers ($p_1 \neq p_2$).
Let $S_{p_1}$ be a Sylow $p_1$-subgroup of $G$ and $S_{p_2}$ be a Sylow $p_2$-subgroup of $G$.

Consider the intersection subgroup:
$$
H = S_{p_1} \cap S_{p_2}.
$$

1. Since $H \leq S_{p_1}$, by Lagrange's Theorem the order $|H|$ divides $|S_{p_1}| = p_1^{a_1}$ (for some $a_1 \geq 1$).
   Thus, $|H| = p_1^{k_1}$ for some integer $k_1 \geq 0$.

2. Since $H \leq S_{p_2}$, by Lagrange's Theorem the order $|H|$ divides $|S_{p_2}| = p_2^{a_2}$ (for some $a_2 \geq 1$).
   Thus, $|H| = p_2^{k_2}$ for some integer $k_2 \geq 0$.

3. Therefore:
   $$
   |H| = p_1^{k_1} = p_2^{k_2}.
   $$
   Since $p_1$ and $p_2$ are distinct prime numbers, $\gcd(p_1^{a_1}, p_2^{a_2}) = 1$.
   The only positive integer that is simultaneously a power of $p_1$ and a power of $p_2$ is $1$.

Thus $|H| = 1$, which means:
$$
H = S_{p_1} \cap S_{p_2} = \{e\} = 1.
$$
The intersection is trivial.
:::
