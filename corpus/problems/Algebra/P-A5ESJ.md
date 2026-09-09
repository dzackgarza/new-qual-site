---
schema: qual/card@1
id: P-A5ESJ
kind: problem
title: $\mathrm{Gal}(x^3+4x+2/\QQ)\cong S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- Show that $\gal(x^3+4x+2)/\QQ \cong S_3$, a symmetric group.
:::


::: {.solution}
Let
\[
f(x)=x^3+4x+2\in\QQ[x],
\]
and let $L$ be its splitting field.

<1>1. The polynomial $f$ is irreducible over $\QQ$.
::: {.proof}
A reducible cubic over $\QQ$ has a rational root. Since $f$ is monic, the rational-root theorem says any rational root must be among $\pm1,\pm2$. Directly,
\[
f(1)=7,\quad f(-1)=-3,\quad f(2)=18,\quad f(-2)=-14,
\]
so none is a root. Hence $f$ is irreducible.
:::

<1>2. The polynomial $f$ has exactly one real root and two nonreal complex-conjugate roots.
::: {.proof}
Its derivative is
\[
f'(x)=3x^2+4>0
\]
for every real $x$. Thus $f$ is strictly increasing on $\RR$, so it has at most one real root. Since a real cubic has at least one real root, it has exactly one. The remaining two roots are nonreal and, because the coefficients are real, are complex conjugates.
:::

<1>3. The Galois group $G=\Gal(L/\QQ)$ is a transitive subgroup of $S_3$ containing a transposition.
::: {.proof}
Irreducibility of $f$ implies that $G$ acts transitively on its three roots. Complex conjugation fixes the unique real root and exchanges the two nonreal roots, so its action on the roots is a transposition. Therefore the permutation representation of $G$ is transitive and contains a transposition.
:::

<1>4. Hence
\[
\Gal(L/\QQ)\cong S_3.
\]
::: {.proof}
The transitive subgroups of $S_3$ are $A_3\cong C_3$ and $S_3$. The subgroup $A_3$ contains no transposition, whereas $G$ contains one by <1>3. Thus $G=S_3$.
:::
:::
