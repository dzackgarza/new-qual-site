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

A polynomial $f\in F[x]$ is **solvable by radicals** if its splitting field is contained in a tower
\[
F=K_0\subset K_1\subset\cdots\subset K_r
\]
in which each $K_{i+1}=K_i(\alpha_i)$ with $\alpha_i^{n_i}\in K_i$ for some $n_i\ge2$ (after adjoining the necessary roots of unity in the standard formulation). Galois theory gives the criterion: $f$ is solvable by radicals if and only if its Galois group is solvable.

We prove that $A_5$ is simple. Its conjugacy classes have sizes
\[
1,\ 20,\ 15,\ 12,\ 12,
\]
corresponding respectively to the identity, the $3$-cycles, the double transpositions, and the two $A_5$-classes of $5$-cycles. A normal subgroup is a union of conjugacy classes containing the identity, and its order must divide $60$. The sums obtained from a proper nonempty selection of the four nontrivial class sizes are
\[
13,16,21,25,28,33,36,40,45,48,
\]
none of which divides $60$. Hence the only normal subgroups are $\{e\}$ and $A_5$, so $A_5$ is simple.

Now
\[
1\triangleleft A_5\triangleleft S_5
\]
has composition factors $A_5$ and $S_5/A_5\cong C_2$. Since $A_5$ is nonabelian simple, $S_5$ is not solvable. Therefore any quintic whose Galois group is $S_5$ is not solvable by radicals. Since quintics with Galois group $S_5$ exist, there can be no radical formula valid for all quintic polynomials.
:::
