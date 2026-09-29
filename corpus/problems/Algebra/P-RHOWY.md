---
schema: qual/card@1
id: P-RHOWY
kind: problem
title: Solvability by radicals, $S_5$, and simplicity of $A_5$
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Galois Theory
  - Simple Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.problem}
(1) Define **solvability by radicals** for a polynomial $f(x) \in F[x]$ and state the Abel–Ruffini / Galois criterion.
(2) Prove that the alternating group $A_5$ is a **simple group**.
(3) Explain why the symmetric group $S_5$ is **not solvable**, and why there is no general radical formula for quintic polynomials.
:::

::: {.solution}

::: pf

::: pf-step
A polynomial $f\in F[x]$ is **solvable by radicals** if its splitting field is contained in a tower
\[
F=K_0\subset K_1\subset\cdots\subset K_r
\]
in which each $K_{i+1}=K_i(\alpha_i)$ with $\alpha_i^{n_i}\in K_i$ for some $n_i\ge2$ (after adjoining the necessary roots of unity in the standard formulation). Galois theory gives the criterion: $f$ is solvable by radicals if and only if its Galois group is solvable.

::: pf-proof

::: pf-step
A polynomial $f(x) \in F[x]$ is **solvable by radicals** if its roots lie in a radical extension tower:
$$F = K_0 \subseteq K_1 \subseteq K_2 \subseteq \cdots \subseteq K_m$$
where each step $K_{i+1} = K_i(\alpha_i)$ with $\alpha_i^{n_i} \in K_i$ for some integer $n_i \ge 2$.

:::

::: pf-step
**Theorem (Galois):** A polynomial $f(x) \in F[x]$ is solvable by radicals if and only if its Galois group $\operatorname{Gal}(f/F)$ is a **solvable group**.

:::

:::

:::

::: pf-step
Simplicity of $A_5$:

::: pf-proof

::: pf-step
The alternating group $A_5$ has order $|A_5| = 5!/2 = 60$.

:::

::: pf-step
We compute the conjugacy classes of $A_5$ by cycle types:

- Identity: $1$ element ($e$).
- 3-cycles: $\binom{5}{3} \times 2 = 20$ elements.
- Products of two disjoint 2-cycles: $\frac{1}{2} \binom{5}{2}\binom{3}{2} = 15$ elements.
- 5-cycles: In $S_5$ there are $4! = 24$ 5-cycles. In $A_5$, the centralizer of a 5-cycle has order 5, so the class splits into two $A_5$-conjugacy classes of size $\frac{60}{5} = 12$ each.

:::

::: pf-step
The sizes of all conjugacy classes in $A_5$ are:
$$\{1, 15, 20, 12, 12\}.$$

:::

::: pf-step
Any normal subgroup $N \trianglelefteq A_5$ must be a union of conjugacy classes containing $e$ ($1 \in N$), and by Lagrange's Theorem, $|N|$ must divide $|A_5| = 60$.

:::

::: pf-step
The possible proper divisors of 60 are $1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30$.

:::

::: pf-step
Testing all sums of conjugacy class sizes containing 1:

- $1 + 12 = 13 \nmid 60$.
- $1 + 15 = 16 \nmid 60$.
- $1 + 20 = 21 \nmid 60$.
- $1 + 12 + 12 = 25 \nmid 60$.
- $1 + 12 + 15 = 28 \nmid 60$.
- $1 + 12 + 20 = 33 \nmid 60$.
- $1 + 15 + 20 = 36 \nmid 60$.
- $1 + 12 + 12 + 15 = 40 \nmid 60$.
- $1 + 12 + 12 + 20 = 45 \nmid 60$.
- $1 + 12 + 15 + 20 = 48 \nmid 60$.
- $1 + 12 + 12 + 15 + 20 = 60 = |A_5|$.

:::

::: pf-step
Thus the only divisors obtainable as class sums are $1$ and $60$.

:::

::: pf-step
Therefore, the only normal subgroups of $A_5$ are $\{e\}$ and $A_5$, proving $A_5$ is **simple**.

:::

:::

:::

::: pf-step
Insolvability of $S_5$ and General Quintics:

::: pf-proof

::: pf-step
The composition series of $S_5$ is:
$$\{e\} \triangleleft A_5 \triangleleft S_5.$$

:::

::: pf-step
The composition factors are:

- $S_5/A_5 \cong \mathbb{Z}_2$ (abelian).
- $A_5/\{e\} \cong A_5$ (non-abelian simple group of order 60).

:::

::: pf-step
Since $A_5$ is simple and non-abelian ($|A_5| = 60$ is not prime), its composition series cannot be refined to abelian factors.

:::

::: pf-step
Therefore, $S_5$ is **not solvable**.

:::

::: pf-step
By Galois Theory, any quintic polynomial over $\mathbb{Q}$ with Galois group $S_5$ (e.g. $f(x) = x^5 - 4x - 2$) cannot be solved by radicals (Abel-Ruffini Theorem).

:::

:::

:::

::: pf-qed
Conclusion:
$A_5$ is simple via class size sums $\{1, 12, 12, 15, 20\}$, making $S_5$ non-solvable and preventing radical solutions for quintics.
:::

:::

:::
