---
schema: qual/card@1
id: P-ALGS16F
kind: problem
title: Solvability by radicals of $x^5 - 16x + 2 = 0$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Is the equation $x^5 - 16x + 2 = 0$ solvable in radicals?
:::

::: {.solution}
<1>1. The polynomial \(f(x)=x^5-16x+2\) is irreducible over \(\mathbb Q\).
::: {.proof}
Eisenstein's criterion at \(2\) applies: \(2\) divides every nonleading coefficient and \(4
mid 2\). Hence \(f\) is irreducible over \(\mathbb Q\).
:::

<1>2. The Galois group \(G\le S_5\) of the splitting field acts transitively on the five roots and therefore contains a \(5\)-cycle.
::: {.proof}
Irreducibility gives transitivity. Thus \(5\mid |G|\) by orbit-stabilizer, and Cauchy's theorem gives an element of order \(5\), necessarily a \(5\)-cycle in \(S_5\).
:::

<1>3. The polynomial \(f\) has exactly three real roots and one nonreal conjugate pair.
::: {.proof}
We have
\[
f(-\infty)<0,\qquad f(0)=2>0,\qquad f(1)=-13<0,\qquad f(2)=2>0,
\]
so there are at least three distinct real roots. Since
\[
f'(x)=5x^4-16
\]
has exactly two real roots, Rolle's theorem implies that \(f\) has at most three real roots. Hence it has exactly three real roots and two nonreal roots, which are complex conjugates.
:::

<1>4. The group \(G\) contains a transposition.
::: {.proof}
Complex conjugation restricts to an automorphism of the splitting field over \(\mathbb Q\). It fixes the three real roots and swaps the two nonreal conjugate roots, so its permutation on the roots is a transposition.
:::

<1>5. A transitive subgroup of \(S_5\) containing a transposition is \(S_5\).
::: {.proof}
Let \(	au=(ab)\in G\). Form the graph on the five roots with edge set \(\{g\{a,b\}:g\in G\}\). Its connected components form a \(G\)-invariant partition. Since \(G\) is transitive, all components have equal size; because \(5\) is prime and the graph has an edge, the graph is connected. For every edge \(\{u,v\}\), the conjugate \(g	au g^{-1}=(uv)\) lies in \(G\). Edge-transpositions of a connected graph generate the full symmetric group, hence \(S_5\le G\). Therefore \(G=S_5\).
:::

<1>6. The equation is not solvable by radicals.
::: {.proof}
A polynomial over \(\mathbb Q\) is solvable by radicals exactly when its Galois group is solvable. Since \(G=S_5\) and \(A_5	rianglelefteq S_5\) is nonabelian simple, \(S_5\) is not solvable. Therefore \(x^5-16x+2=0\) is not solvable by radicals.
:::
:::
