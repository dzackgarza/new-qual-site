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
(a) Define solvability by radicals for a polynomial $f(x) \in F[x]$ and state the Abel--Ruffini / Galois criterion.

(b) Prove that the alternating group $A_5$ is a simple group.

(c) Explain why the symmetric group $S_5$ is not solvable, and why there is no general radical formula for quintic polynomials.
:::

::: {.solution}
Let $F$ have characteristic $0$.

::: pf

::: pf-step
(a) $f\in F[x]$ is $\dfn{solvable by radicals}$ if its splitting field is contained in a field $K_r$ of a tower $F=K_0\subset K_1\subset\cdots\subset K_r$ with $K_{i+1}=K_i(\alpha_i)$ and $\alpha_i^{n_i}\in K_i$ for some $n_i\ge1$. Galois's criterion: $f$ is solvable by radicals if and only if $\Gal(f/F)$ is a solvable group.

::: pf-proof
The criterion is Galois's theorem on solvability by radicals.
:::

:::

::: {.pf-step #a5-simple}
(b) $A_5$ is simple.

::: pf-proof
The conjugacy classes of $A_5$ have sizes $1$ (identity), $20$ ($3$-cycles), $15$ (double transpositions), $12$ and $12$ (the two $A_5$-classes of $5$-cycles). A normal subgroup is a union of conjugacy classes containing the identity, and its order divides $60$. Adding $1$ to the sum of a proper nonempty subcollection of $20,15,12,12$ gives one of $13,16,21,25,28,33,36,40,45,48$, none of which divides $60$. Hence the only normal subgroups are $\{e\}$ and $A_5$.
:::

:::

::: {.pf-step #s5}
(c) $S_5$ is not solvable.

::: pf-proof
$1\triangleleft A_5\triangleleft S_5$ is a composition series with factors $A_5$ and $C_2$, by step [](#a5-simple){.pf-ref}. Since $A_5$ is a nonabelian composition factor, $S_5$ is not solvable.
:::

:::

::: pf-step
(c) There is no radical formula valid for all quintic polynomials over $\QQ$.

::: pf-proof
The polynomial $f=x^5-4x+2$ is irreducible over $\QQ$ by Eisenstein's criterion at $2$, so $\Gal(f/\QQ)\le S_5$ contains a $5$-cycle. Since $f(-2)<0$, $f(0)>0$, $f(1)<0$, $f(2)>0$, and $f'=5x^4-4$ has only two real zeros, $f$ has exactly three real roots, so complex conjugation acts as a transposition. A $5$-cycle and a transposition generate $S_5$, so $\Gal(f/\QQ)=S_5$, which is not solvable by step [](#s5){.pf-ref}. By Galois's criterion, $f$ is not solvable by radicals, so no radical formula covers it.
:::

:::

:::
:::
