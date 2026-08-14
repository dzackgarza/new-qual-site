---
schema: qual/card@1
id: P-HAGJY
kind: problem
title: "By part 1, $(\\hom_{R\\dash\\text{mod}}(A, A), +)$ is an abelian group, \u2026"
classification:
  areas:
  - algebra
  topics:
  - modules
  - rings
  - homomorphisms
relations: []
review: draft
---

By part 1, $(\hom_{R\dash\text{mod}}(A, A), +)$ is an abelian group, We just need to check that $(\hom_R(A, A), \circ)$ is a monoid, i.e.:

- Associativity: $f \circ (g\circ h) = (f\circ g) \circ h$

- Identity: $\id \circ f = f$

- Closure: $f\circ g \in \hom_{R\dash\text{mod}}(A, A)$

Associativity: We have
\[
\begin{align*}
f\circ (g\circ h) \actson x &\definedas (f \circ (g \circ h))(x) \\
&= f((g\circ h)(x)) \\
&= f(g(h(x))) \\
&= (f\circ g)(h(x)) \\
&= ((f\circ g) \circ h)(x)\\
&\definedas (f \circ g) \circ h \actson x
.\end{align*}
\]

Identity: Take $\id_A: A \to A$ given by $\id_A(x) = x$, then
\[
\begin{align*}
f\circ \id_A \actson x = f(\id_A(x)) = f(x) = \id_A(f(x)) = \id_A \circ f \actson x
.\end{align*}
\]

Closure: If $f: A\to A$ and $g: A\to A$ are homomorphisms, then $f\circ g: A \to A$ as a set map, and is an $R\dash$module homomorphism because
\[
\begin{align*}
f\circ g \actson (r+s)(x+y) &= f(g((r+s)(x+y)))\\
&= f((r+s)(g(x) + g(y))) \\
&= (r+s)(f(g(x)) + f(g(y))) \\
&= (f \actson (r+s)(x+y)) \circ (g \actson (r+s)(x+y))
.\end{align*}
\]
