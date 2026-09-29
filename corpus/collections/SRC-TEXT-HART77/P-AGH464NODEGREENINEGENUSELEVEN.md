---
schema: qual/card@1
id: P-AGH464NODEGREENINEGENUSELEVEN
kind: problem
title: There is no curve of degree $9$ and genus $11$ in $\PP^3$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Embeddings
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.4, the retained Lomont and Egbert companion solutions,
    Clifford's theorem, and the repository's smooth-quadric and quadric-cone
    genus calculations. The source statement needs no correction. Both
    companion solutions use Clifford's bound as though it were strict; the
    equality case must be excluded. The proof below does this by observing
    that equality would make 2H a multiple of the hyperelliptic pencil, while
    2H is very ample because H is the hyperplane bundle of the given embedding.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
There is no curve of degree 9 and genus 11 in $\PP^3$.

Hint: Show that it would have to lie on a quadric surface, then use (6.4.1).
:::

::: {.solution}
Suppose for contradiction that
$$
X\subseteq\PP^3
$$
is a curve of degree $9$ and genus $11$.  Put
$$
H=\OO_X(1),
$$
and let $K$ be a canonical divisor on $X$.

::: pf

::: {.pf-step #s1}

The curve $X$ is contained in a quadric surface.

::: pf-proof

We have
$$
\deg(2H)=18,
\qquad
\deg K=2g-2=20.
$$
If $2H$ is nonspecial, Riemann--Roch gives
$$
h^0(X,2H)=18+1-11=8.
$$

Suppose instead that $2H$ is special.  By [[T-CRVCLIFF|Clifford's
theorem]],
$$
h^0(X,2H)\le\frac{18}{2}+1=10.
$$
Equality cannot occur.  Indeed, since $0<\deg(2H)<\deg K$, the equality
case of Clifford's theorem would imply that $X$ is hyperelliptic and
$$
2H\sim 9A,
$$
where $A$ is its unique $g^1_2$.  Let
$$
f:X\longrightarrow\PP^1
$$
be the degree-two morphism defined by $\abs{A}$.  Then
$$
\OO_X(2H)\cong f^*\OO_{\PP^1}(9).
$$
Under the assumed equality, both
$$
H^0(\PP^1,\OO_{\PP^1}(9))
\quad\text{and}\quad
H^0(X,2H)
$$
have dimension $10$, so pullback identifies them.  Hence the complete map
defined by $\abs{2H}$ factors through the degree-two map $f$ and cannot be
an embedding.

But $H$ is very ample because it is the hyperplane bundle of the given
embedding $X\subseteq\PP^3$.  Hence $2H$ is also very ample: the composition
of this embedding with the quadratic Veronese embedding is defined by a
linear subsystem of $\abs{2H}$ and is already a closed immersion.
This contradiction excludes equality.  Thus in the special case
$$
h^0(X,2H)\le9.
$$
In either case,
$$
h^0(X,2H)\le9.
$$

Now
$$
h^0(\PP^3,\OO_{\PP^3}(2))=10,
$$
so the restriction map
$$
H^0(\PP^3,\OO_{\PP^3}(2))
\longrightarrow
H^0(X,2H)
$$
has nonzero kernel.  A nonzero element of the kernel is a quadratic equation
vanishing on $X$.  Hence $X$ lies on a quadric surface $Q$.

:::

:::

::: {.pf-step #s2}

The quadric $Q$ cannot be a union of planes or a double plane.

::: pf-proof

First, $X$ is not contained in a plane.  If it were, then it would be a
nonsingular plane curve of degree $9$, and
[[P-AGH72ARITHGENUS|the plane-curve genus formula]] would give
$$
g(X)=\frac{(9-1)(9-2)}2=28,
$$
contrary to $g(X)=11$.

If $Q$ is a union of two planes, the irreducibility of $X$ forces $X$ to lie
in one of them.  If $Q$ is a double plane, its underlying reduced surface is
a plane containing $X$.  Both possibilities contradict the preceding
paragraph.

:::

:::

::: {.pf-step #s3}

The quadric $Q$ cannot be nonsingular.

::: pf-proof

If $Q$ is nonsingular, then
$$
Q\cong\PP^1\times\PP^1,
$$
and [[FE-CRVQUAD]] writes the divisor class of $X$ as $(a,b)$ with
$$
\deg X=a+b,
\qquad
g(X)=(a-1)(b-1).
$$
Thus
$$
a+b=9
$$
and
$$
(a-1)(b-1)=11.
$$
The second equation and $a+b=9$ give
$$
ab=19.
$$
Hence $a$ and $b$ would be roots of
$$
t^2-9t+19=0,
$$
whose discriminant is
$$
81-76=5,
$$
not a square in $\ZZ$.  No integers $a,b$ satisfy the required equations.
Therefore $Q$ is not nonsingular.

:::

:::

::: {.pf-step #s4}

The quadric $Q$ cannot be an irreducible quadric cone.

::: pf-proof

By step [](#s2){.pf-ref}, a singular containing quadric that remains is an irreducible
quadric cone.  The cone calculation in [[FE-CRVQUAD]] says that an integral
curve of odd degree
$$
d=2a+1
$$
on such a cone has arithmetic genus
$$
p_a=a(a-1).
$$
Here
$$
9=2\cdot4+1,
$$
so any integral degree-$9$ curve on the cone has
$$
p_a=4\cdot3=12.
$$
Since $X$ is nonsingular, its arithmetic and geometric genera agree, giving
$$
g(X)=12,
$$
contrary to $g(X)=11$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} forces $X$ onto a quadric.  Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} exhaust the possible
quadric surfaces and give a contradiction in every case.  Therefore no curve
of degree $9$ and genus $11$ exists in $\PP^3$.

:::

:::

:::
