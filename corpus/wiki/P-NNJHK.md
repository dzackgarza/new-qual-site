---
schema: qual/card@1
id: P-NNJHK
kind: problem
title: $\hom_R(A, B)$ under pointwise addition is an abelian group
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homomorphisms
  - Abelian Groups
relations: []
review: draft
solved: false
---

::: problem
We want to show that if $A, B$ are $R\dash$modules then $X = (\hom_{R\dash\text{mod}}(A, B), +)$ is an abelian group.
Let $f, g, h \in X$, we then need to show the following:

a. Closure: $f + g \in X$
b. Associativity: $f + (g + h) = (f + g) + h$
c. Identity: the zero map $\vector 0 \in X$
d. Inverses: $-f \in X$
e. Commutativity: $f + g = g + f$

The group operation is pointwise addition, so the identity is the zero map and the inverse of $f$ is $-f$, not $\id$ and $f\inv$.

Closure: 
This follows from the definition, because $(f + g) \actson x \definedas f(x) + g(x)$ pointwise, which is well-defined homomorphism $A \to B$.

Associativity:
We have 
\[
\begin{align*}
f + (g + h) \actson x &\definedas f(x) + (g + h)(x) \\
&\definedas f(x) + (g(x) + h(x)) \\
&= (f(x) + g(x)) + h(x) \\
&= (f+g) + h \actson x
.\end{align*}
\]

Identity: 
We can define $\vector 0: A \to B$ by $\vector 0(x) = 0 \in B$. 
Then 
$$(f + \vector 0)\actson x = f(x) + 0 = f(x) = 0 + f(x) = (\vector 0 + f) \actson x.$$

Inverses:
Given $f\in X$, we can define $-f: A \to B$ by $(-f)(x) \definedas -\left( f(x) \right)$, which is again a module morphism.
Then
\[
\begin{align*}
(f + (-f)) \actson x &= f(x) + (-f)(x) = f(x) - f(x) = 0 = \vector 0 \actson x \\
((-f) + f) \actson x &= (-f)(x) + f(x) = -f(x) + f(x) = 0 = \vector 0 \actson x
.\end{align*}
\]

Commutativity:
Since $B$ is a module, by definition $(B, +)$ is an abelian group. Thus

\[
\begin{align*}
(f + g) \actson x &= f(x) + g(x) = g(x) + f(x) = (g+f)\actson x
.\end{align*}
\]
:::
