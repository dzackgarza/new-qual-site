---
schema: qual/card@1
id: P-NNJHK
kind: problem
title: "We want to show that if $A, B$ are $R\\dash$modules then $X = (\\hom_{R\\\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
We want to show that if $A, B$ are $R\dash$modules then $X = (\hom_{R\dash\text{mod}}(A, B), +$ is an abelian group.
Let $f, g, h \in X$, we then need to show the following:

a. Closure: $f + g \in X$
b. Associativity: $f + (g + h) = (f + g) + h$
c. Identity: $\id \in X$
d. Inverses: $f\inv \in X$
e. Commutativity: $f + g = g + f$

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
Given $f\in X$, we can define $-f: A \to B$ as $-f(x) = -x$.
Then
\[
\begin{align*}
(f + -f) \actson x = f(x) + -f(x) &= f(x) - f(x) = x - x = 0 = \vector 0 \actson x \\
(-f + f) \actson x = -f(x) + f(x) &= -f(x) + f(x) = -x + x = 0 = \vector 0 \actson x
.\end{align*}
\]

Commutativity:
Since $B$ is a module, by definition $(B, +)$ is an abelian group. Thus

\[
\begin{align*}
(f + g) \actson x &= f(x) + g(x) = g(x) + f(x) = (g+f)\actson x
.\end{align*}
\]
## Part 2

By part 1, $(\hom_{R\dash\text{mod}}(A, A), +)$ is an abelian group, We just need to check that $(\hom_R(A, A), \circ)$ is a monoid, i.e.:

- Associativity: $f \circ (g\circ h) = (f\circ g) \circ h$
- Identity: $\id \circ f = f$
- Closure: $f\circ g \in \hom_{R\dash\text{mod}}(A, A)$


Associativity: 
We have 
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

Identity: 
Take $\id_A: A \to A$ given by $\id_A(x) = x$, then
\[
\begin{align*}
f\circ \id_A \actson x = f(\id_A(x)) = f(x) = \id_A(f(x)) = \id_A \circ f \actson x
.\end{align*}
\]

Closure:
If $f: A\to A$ and $g: A\to A$ are homomorphisms, then $f\circ g: A \to A$ as a set map, and is an $R\dash$module homomorphism because
\[
\begin{align*}
f\circ g \actson (r+s)(x+y) &= f(g((r+s)(x+y)))\\
&= f((r+s)(g(x) + g(y))) \\
&= (r+s)(f(g(x)) + f(g(y))) \\
&= (f \actson (r+s)(x+y)) \circ (g \actson (r+s)(x+y))
.\end{align*}
\]
## Part 3

For arbitrary $x, y \in A$, we need to check the following:

a. $f\actson (x+y) = f\actson x + f \actson y$
b. $(f+g)\actson x = f \actson x + g \actson x$
c. $f\circ g \actson x = f \actson (g \actson x)$
d. $\id_a \actson x = x$


For (a):
\[
\begin{align*}
f \actson (x + y) &\definedas f(x + y) \\
&= f(x) + f(y)\quad\quad\text{since $f$ is a homomorphism} \\
&= f\actson x + f \actson y \\
.\end{align*}
\]

For (b):
\[
\begin{align*}
(f+g)\actson x &= (f+g)(x) \\
&= f(x) + g(x) \\
&= f \actson x + g \actson x
.\end{align*}
\]

For (c):
\[
\begin{align*}
f\circ g \actson x &= (f\circ g)(x)  \\
&= f(g(x)) \\
&= f \actson g(x) \\
&= f \actson (g \actson x)
.\end{align*}
\]

For (d):
\[
\begin{align*}
\id_A \actson x &= \id_A(x) = x
.\end{align*}
\]

