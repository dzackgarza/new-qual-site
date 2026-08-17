---
schema: qual/card@1
id: P-45CLI
kind: problem
title: "Let $G$ be a finite group and $\\pi: G\\to \\sym(G)$ the Cayley representation. Prove\u2026"
classification:
  areas:
  - algebra
  topics:
  - permutations
  - group-actions
  - cosets-and-lagrange
relations: []
review: draft
solved: true
---
Let $G$ be a finite group and $\pi: G\to \sym(G)$ the Cayley representation.

> (Recall that this means that for an element $x\in G$, $\pi(x)$ acts by left translation on $G$.)

Prove that $\pi(x)$ is an odd permutation $\iff$ the order $\abs{\pi(x)}$ of $\pi(x)$ is even and $\abs{G} / \abs{\pi(x)}$ is odd.

:::{.warnings}
(DZG): This seems like an unusually hard group theory problem.
My guess is this year's qual class spent more time than usual on the proof of Cayley's theorem.
:::

:::{.concept}
\envlist

- $\Sym(G) \da \Aut_\Set(G, G)$ is the group of set morphisms from $G$ to itself, i.e. permutations of elements of $G$.
- More standard terminology: this is related to the **left regular representation** where $g\mapsto \phi_g$ where $\phi_g(x) = gx$, regarded instead as a permutation representation.
  - This action is transitive!
- Cayley's theorem: every $G$ is isomorphic to a subgroup of a permutation group.
  In particular, take \( \ts{ \phi_g \st G\in G } \) with function composition as a subgroup of $\Aut_\Set(G)$.
:::

:::{.solution}
\envlist

> (DZG): Warning!! I haven't checked this solution very carefully, and this is kind of a delicate parity argument.
  Most of the key ideas are borrowed [from here](https://math.stackexchange.com/questions/3028603/show-that-phig-is-an-even-permutation).

- Write $k \da o(\pi_g)$, then since $\pi$ is injective, $k = o(g)$ in $G$.
- Since $\pi_g$ as a cycle is obtained from the action of $g$, we can pick an element $x_0$ in $G$, take the orbit under the action, and obtain a cycle of length $k$ since the order of $g$ is $k$.
  Then continue by taking any $x_1$ not in the first orbit and taking *its* orbit.
  Continuing this way exhausts all group elements and yields a decomposition into disjoint cycles:
\[
\pi_g = 
(x_0, gx_0, g^2 x_0, \cdots, g^{k-1} x_0)
(x_1, gx_1, g^2 x_1, \cdots, g^{k-1} x_1)
\cdots
(x_m, gx_m, g^2 x_m, \cdots, g^{k-1} x_m)
.\]
- So there are $m$ orbits all of length exactly $k$.
  Proceed by casework.
- A cycle of length $k$ has sign $(-1)^{k-1}$, so $\sgn(\pi_g) = (-1)^{m(k-1)}$.
- If $k$ is odd:
  - Then $k-1$ is even, each of the $m$ cycles is an even permutation, and $\sgn(\pi_g) = +1$.
  - So $\pi_g \in \ker\sgn$ is an even permutation, whatever $m$ is.
- If $k$ is even:
  - Then $k-1$ is odd, each of the $m$ cycles is an odd permutation, and $\sgn(\pi_g) = (-1)^m$.
  - So $\pi_g$ is even iff $m$ is even, and odd iff $m$ is odd.
- The claim is that the number of orbit representatives $m$ is equal to $[G:H] = \# G/H$ for $H = \gens{ g }$. 
  - Proof: define a map
  \[
  \ts{ \text{Orbit representatives } x_i } &\to H\backslash G \\
  x &\mapsto Hx
  .\]

  The orbits are the RIGHT cosets $Hx = \ts{ g^\ell x }$, since $g$ acts by left translation.
  - This is injective and surjective because
  \[
  Hx = Hy &\iff xy\inv \in H = \gens{ g } \\
  &\iff xy\inv = g^\ell \\
  &\iff x=g^\ell y \\
  &\iff y\in \OO_x
  ,\]
  so $y$ and $x$ are in the same orbit and have the same orbit representative.

- We now have
\[
\pi_g \text{ is an even permutation } \iff
\begin{cases}
k \text{ is odd} &
\\
\text{ or } & \\
k \text{ is even and } m \text{ is even}
 & .
\end{cases}
\]
- Everything was an iff, so flip the evens to odds:
\[
\pi_g \text{ is an odd permutation } \iff k \text{ is even and } m \text{ is odd}
.\]
- Then just recall that $k\da o(\pi_g)$ and 
\[
m= [G: \gens{ g }] = \# G / \# \gens{ g }= \# G / o(g) = \# G/ o(\pi_g)
.\]




:::


