---
schema: qual/card@1
id: P-DURCM
kind: problem
title: "Let $R$ be a ring and $f: M\\to N$ and $g: N\\to M$ be $R\\dash$module homomorphisms such that $g\\circ f = \\id_M$\u2026"
classification:
  areas:
  - algebra
  topics:
  - exact-sequences
  - modules
  - projective-modules
relations: []
review: draft
---
Let $R$ be a ring and $f: M\to N$ and $g: N\to M$ be $R\dash$module homomorphisms such that $g\circ f = \id_M$.
Show that $N \cong \im f \oplus \ker g$.


:::{.solution}
\envlist

- We have the following situation:

\begin{tikzcd}
	M &&& N
	\arrow["f", from=1-1, to=1-4]
	\arrow["g"', curve={height=24pt}, dashed, from=1-4, to=1-1]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsMixbMCwwLCJNIl0sWzMsMCwiTiJdLFswLDEsImYiXSxbMSwwLCJnIiwyLHsiY3VydmUiOjQsInN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ==)

- Claim: $\im f + \ker g \subseteq N$, and this is in fact an equality.
  - For $n\in N$, write
  \[
  n = n + (f\circ g)(n) - (f\circ g)(n) = \qty{n - (f\circ g)(n) } + (f\circ g)(n)
  .\]
  - The first term is in $\ker g$:
  \[
  g \qty{ n - (f\circ g)(n) }
  &= g(n) - (g\circ f \circ g)(n)\\
  &= g(n) - (\id_N \circ g)(n)\\
  &= g(n) - g(n) \\
  &= 0
  .\]
  - The second term is clearly in $\im f$.
- Claim: the sum is direct.
  - Suppose $n\in \ker(g) \intersect \im(f)$, so $g(n) = 0$ and $n=f(m)$ for some $m\in M$.
  Then
  \[
  0 = g(n) = g(f(m)) = (g\circ f)(m)
  = \id_M(m) = m
  ,\]
  so $m=0$ and since $f$ is a morphism in \(R\dash\)modules, $n\da f(m) = 0$.
:::


