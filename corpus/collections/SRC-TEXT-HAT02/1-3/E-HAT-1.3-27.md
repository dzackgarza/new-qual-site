---
schema: qual/card@1
id: E-HAT-1.3-27
kind: problem
title: "Two actions of the fundamental group on the fiber"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: >-
    Checked against Hatcher, Algebraic Topology, Section 1.3, revised Exercise 27.
    Corrected the local second example from a wedge of three circles to the source's torus $S^1\times S^1$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Identified the two fiber actions as right multiplication by the inverse and left multiplication, yielding equality exactly for elementary abelian 2-groups.
---

For a universal cover $p: \tilde{X} \to X$ there are two actions of $\pi_1(X, x_0)$ on the fiber $p^{-1}(x_0)$.
The first is the action defined on page 69 in which the element of $\pi_1(X, x_0)$ determined by a loop $\gamma$ sends $\tilde{\gamma}(1)$ to $\tilde{\gamma}(0)$ for each lift $\tilde{\gamma}$ of $\gamma$ to $\tilde{X}$, and the second is the action given by restricting deck transformations to the fiber (see Proposition 1.39). Show that these two actions are different when $X = S^1 \vee S^1$ and when $X = S^1 \times S^1$, and determine when the two actions are the same.
[This is a revised version of the original form of this exercise.]


::: {.solution}
Fix a point $\tilde x_0\in p^{-1}(x_0)$ and write
\[
G=\pi_1(X,x_0).
\]
Since $p$ is universal, every point of the fiber is the endpoint of a unique homotopy class of lifted based loops.
Thus identify
\[
p^{-1}(x_0)\cong G
\]
by sending $h\in G$ to the endpoint of the lift of a representative loop for $h$ starting at $\tilde x_0$.

<1>1. Under this identification, the usual endpoint monodromy for $g\in G$ is right multiplication by $g$:
\[
R_g(h)=hg.
\]
::: {.proof}
Start at the fiber point represented by $h$.
A path from $\tilde x_0$ to this point projects to a loop representing $h$.
Lifting a loop representing $g$ from this point concatenates the projected paths, so the endpoint is represented by
\[
hg.
\]
:::

<1>2. Hatcher's first action in the exercise is the inverse of endpoint monodromy, hence
\[
A_g(h)=hg^{-1}.
\]
::: {.proof}
The action on page 69 is defined so that the element represented by $g$ sends the endpoint of each lift of $g$ to its starting point.
This is precisely the inverse permutation of the endpoint-monodromy bijection $R_g$ from <1>1.
Therefore
\[
A_g=R_g^{-1}=R_{g^{-1}}.
\]
:::

<1>3. Under the same identification, the deck-transformation action is left multiplication:
\[
D_g(h)=gh.
\]
::: {.proof}
In the path-class model of the universal cover, a point is represented by a path $h$ beginning at $x_0$.
For a loop $g$ at $x_0$, define
\[
T_g([h])=[g h].
\]
This preserves endpoints in $X$, hence is a deck transformation.
It sends the basepoint class of the constant path to the fiber point represented by $g$, so under the standard identification
\[
G\cong\operatorname{Deck}(\widetilde X/X)
\]
it is the deck transformation corresponding to $g$.
Restricting to the fiber gives
\[
D_g(h)=gh.
\]
:::

<1>4. The two actions agree if and only if
\[
gh=hg^{-1}
\qquad\text{for all }g,h\in G.
\]
::: {.proof}
By <1>2 and <1>3, equality of the two actions means
\[
D_g(h)=A_g(h)
\]
for all $g,h$, which is exactly the displayed identity.
:::

<1>5. If the two actions agree, every element of $G$ has order at most $2$ and $G$ is abelian.
::: {.proof}
Set $h=e$ in <1>4.
Then
\[
g=g^{-1},
\]
so
\[
g^2=e
\]
for every $g\in G$.
Substituting $g^{-1}=g$ back into <1>4 gives
\[
gh=hg
\]
for all $g,h$.
Thus $G$ is abelian and every element is self-inverse.
:::

<1>6. Conversely, if $G$ is abelian and every element satisfies $g^2=e$, then the two actions agree.
::: {.proof}
For all $g,h$,
\[
A_g(h)=hg^{-1}=hg=gh=D_g(h).
\]
:::

<1>7. Therefore the two actions are the same exactly when
\[
\boxed{\pi_1(X,x_0)\text{ is an elementary abelian }2\text{-group}.}
\]
::: {.proof}
This is the equivalence of <1>5 and <1>6.
:::

<1>8. For
\[
X=S^1\vee S^1,
\]
the actions are different.
::: {.proof}
Here
\[
G\cong F(a,b),
\]
which is nonabelian and contains elements of infinite order.
Hence it does not satisfy the criterion in <1>7.
For example, at the identity fiber point,
\[
A_a(e)=a^{-1}\ne a=D_a(e).
\]
:::

<1>9. For
\[
X=S^1\times S^1,
\]
the actions are also different.
::: {.proof}
Here
\[
G\cong\mathbb Z^2.
\]
Although this group is abelian, its nonzero elements are not self-inverse.
For a standard generator $a$,
\[
A_a(e)=a^{-1}\ne a=D_a(e).
\]
Thus abelianness alone does not make the actions agree.
:::
:::
