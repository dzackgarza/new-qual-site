---
schema: qual/card@1
id: E-FVXIT
kind: exercise
title: "Suppose $f: \\DD\\to \\HH$ is analytic and satisfies $f(0) = 2$. Find a sharp upper\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-lemma
  - conformal-maps
  - fractional-linear-transformations
relations: []
review: draft
---
:::{.problem title="?"}
Suppose $f: \DD\to \HH$ is analytic and satisfies $f(0) = 2$.
Find a sharp upper bound for $\abs{f'(0)}$, and prove it is sharp by example.
:::

:::{.concept}
Some useful facts about the Cayley map:

- $C(z) \da {z-i\over z+i}$ maps $\HH\to \DD$ sending $i\to 0$.
- $C\inv(z) \da -i {z+1\over z-1}$ maps $\DD\to\HH$ sending $0\to i$.
- $C'(z) = {2i\over (z+i)^2}$ and $C'(i) = -{1\over 2}i$.
- $(C\inv)'(z) = {2i\over (z-1)^2}$ and $C'(0) = 2i$.
- A mistake that's useful to know: $\psi_w'(z) = {1-\abs{w}^2 \over (1-\bar{w}z )^2}$ and $\psi_w'(w) \to \infty$.

:::

:::{.solution}
Define $g:\HH\to \HH$ by $g(z) = {1\over 2}iz$, so $g(2) = i$.
Then set $F \da C\circ g \circ f: \DD\to \DD$ where $C(z) \da {z-i\over z+i}$ is the Cayley map.Since $F(0) = C(g(f(0))) = C(g(2)) = C(i) = 0$, Schwarz applies to $F$ and $\abs{F'(z)}\leq 1$ for $z\in \DD$.
By the chain rule,
\[
F'(z) = f'( (g\circ C) (z))\cdot g'(C(z)) \cdot C'(z)
.\]
Setting $g(C(z)) = 0$ yields $z=C\inv(g\inv(0)) = C\inv(0) = i$.
\[
F'(i) &= f'(0) \cdot g'(0) \cdot C'(i) \\
\implies \abs{f'(0)} 
&\leq \abs{F'(i) \over g'(0) C'(i)} \\
&\leq {1\over \abs{g'(0)} \cdot \abs{C'(i)} } \\
&= {1\over \abs{i\over 2} \cdot \abs{-{i\over 2} } } \\
&= 4
.\]

By Schwarz, if $\abs{F'(z)} = 1$ for any $z\in \DD$, we'll have $F(z) = \lambda z$ for some $\abs{ \lambda} = 1$.
Unwinding this:
\[
F(z) &= \lambda z \implies (C\circ g\circ f)(z) = \lambda z \\
\implies f(z) &= g\inv(C\inv(\lambda z)) = g\inv\qty{-i {\lambda z + 1 \over \lambda z - 1}} \\
\implies f(z) &= -2 {\lambda z + 1\over \lambda z - 1}
.\]
Moreover $f'(z) = -2\qty{-2\lambda \over (\lambda z - 1)^2}$, so
\[
\abs{f'(0)} = 4\abs{\lambda} = 4
.\]







:::
