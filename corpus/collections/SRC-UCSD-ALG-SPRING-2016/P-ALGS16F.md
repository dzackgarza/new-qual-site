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

::: {.problem}
Is the equation $x^5 - 16x + 2 = 0$ solvable in radicals?
:::

::: {.solution}
<1>1. The polynomial \(f(x)=x^5-16x+2\) is irreducible over \(\mathbb Q\), so its Galois group \(G\le S_5\) acts transitively on its five roots.
::: {.proof}
Eisenstein's criterion at \(2\) applies: every nonleading coefficient is divisible by \(2\), while the constant term \(2\) is not divisible by \(4\). Thus \(f\) is irreducible over \(\mathbb Q\). The Galois group of the splitting field therefore acts transitively on the roots.
:::

<1>2. The polynomial \(f\) has exactly three real roots and one pair of nonreal complex-conjugate roots.
::: {.proof}
We have
\[
f'(x)=5x^4-16,
\]
so \(f'\) has exactly two real zeros. Hence Rolle's theorem implies that \(f\) has at most three distinct real zeros. On the other hand,
\[
\lim_{x\to-\infty}f(x)=-\infty,
\qquad f(0)=2>0,
\qquad f(1)=-13<0,
\qquad f(2)=2>0.
\]
The intermediate value theorem therefore gives one real zero in each of \(( -\infty,0)\), \((0,1)\), and \((1,2)\). Thus there are exactly three real roots; the other two roots form a nonreal conjugate pair.
:::

<1>3. The group \(G\) contains a transposition.
::: {.proof}
Complex conjugation fixes the three real roots and interchanges the two nonreal conjugate roots. Its restriction to the splitting field is therefore an element of \(G\) acting as a transposition on the five roots.
:::

<1>4. A transitive subgroup of \(S_5\) containing a transposition is all of \(S_5\).
::: {.proof}
Let \(\tau=(ab)\in G\) be a transposition. Form a graph on the five roots whose edges are the pairs \(g\{a,b\}\) for \(g\in G\). The graph is nonempty and \(G\)-invariant, and every edge \(\{u,v\}\) yields the transposition \((uv)=g\tau g^{-1}\in G\). Its connected components form a \(G\)-invariant partition. Since \(G\) is transitive, all components have equal size. Their common size divides \(5\), and it is greater than \(1\) because the graph has an edge; hence the graph is connected. Transpositions along the edges of a connected graph generate the full symmetric group, so \(S_5\le G\). Thus \(G=S_5\).
:::

<1>5. The equation \(x^5-16x+2=0\) is not solvable by radicals over \(\mathbb Q\).
::: {.proof}
A polynomial over a characteristic-zero field is solvable by radicals exactly when its Galois group is solvable. By <1>4 the Galois group is \(S_5\), which is not solvable because \(A_5\) is a nonabelian simple normal subgroup. Hence the equation is not solvable by radicals.
:::
:::
