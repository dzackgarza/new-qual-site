---
schema: qual/card@1
id: P-AGXVARFIBERDIM
kind: problem
title: Dimension of the fibers of a dominant morphism of affine varieties
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fiber Dimension
  - Dominant Morphisms
  - Generic Behavior
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Proposition 4.8 in the recorded Zaidenberg source together with the
    notes' standing conventions: the base field is algebraically closed of
    characteristic zero and an affine variety is irreducible. The source
    states the fibre-dimension proposition without a proof.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked the lower bound against the local dimension inequality and the
    affine height-dimension formula, and checked generic equality by generic
    flatness and going-down. Cross-checked the resulting argument against the
    more general Hartshorne II.3.22 solution P-AGH2322FIBREDIM.
---

::: {.problem}
Let $f:X\to Y$ be a dominant morphism of affine varieties.
Show that for any $y\in f(X)$, any irreducible component of the fiber $f^{-1}(y)$ is an affine variety of dimension $d\geq \dim X-\dim Y$.
Show that equality holds on a Zariski-dense open subset of $Y$.
:::

::: {.solution}
Let $k$ be the algebraically closed ground field of the source, and write
$$
A=\mco(Y),
\qquad
B=\mco(X),
\qquad
m=\dim Y,
\qquad
n=\dim X,
\qquad
e=n-m.
$$
Because $X$ and $Y$ are affine varieties in the source's convention, $A$ and
$B$ are finitely generated integral $k$-algebras. Dominance of $f$ says that
the comorphism
$$
A\hookrightarrow B
$$
is injective.

<1>1. Let $y\in f(X)$, let $\mathfrak p\subseteq A$ be the maximal ideal
of $y$, and let $Z$ be an irreducible component of $f^{-1}(y)$. Then there is
a prime $\mathfrak q\subseteq B$, minimal over $\mathfrak pB$, such that
$$
Z=V(\mathfrak q)=\Spec(B/\mathfrak q),
$$
so $Z$ is an affine variety.

::: {.proof}
Since $k$ is algebraically closed,
$$
\kappa(y)=k.
$$
Hence the fibre is
$$
f^{-1}(y)
=
\Spec(B\tensor_A k)
=
\Spec(B/\mathfrak pB).
$$
Its irreducible components correspond to the primes of $B$ minimal over
$\mathfrak pB$. Thus $Z=V(\mathfrak q)$ for such a prime
$\mathfrak q$, and
$$
Z\cong\Spec(B/\mathfrak q).
$$
Because $\mathfrak q$ is prime, $B/\mathfrak q$ is a finitely generated
integral $k$-algebra. Therefore $Z$ is an affine variety.

Moreover,
$$
\mathfrak p
\subseteq
\mathfrak q\cap A.
$$
The contraction $\mathfrak q\cap A$ is proper and $\mathfrak p$ is
maximal, so
$$
\mathfrak q\cap A=\mathfrak p.
$$
:::

<1>2. For the prime $\mathfrak q$ of step <1>1,
$$
\height\mathfrak q\leq m.
$$

::: {.proof}
Localize the injective map $A\to B$ at
$\mathfrak p$ and $\mathfrak q$:
$$
A_{\mathfrak p}\longrightarrow B_{\mathfrak q}.
$$
Since $\mathfrak q$ is minimal over $\mathfrak pB$, the quotient
$$
B_{\mathfrak q}/\mathfrak pB_{\mathfrak q}
$$
has Krull dimension $0$.

The standard local dimension inequality for a homomorphism of Noetherian
local rings gives
$$
\dim B_{\mathfrak q}
\leq
\dim A_{\mathfrak p}
+
\dim\bigl(B_{\mathfrak q}/\mathfrak pB_{\mathfrak q}\bigr)
=
\dim A_{\mathfrak p}.
$$
This is the same inequality used in
[[P-AGH2322FIBREDIM|the fibre-dimension calculation for Hartshorne II.3.22]].

The point $y$ is closed, so the affine dimension theorem
[[P-AGH2320DIMENSION|gives]]
$$
\dim A_{\mathfrak p}=\dim A=m.
$$
Finally,
$$
\dim B_{\mathfrak q}=\height\mathfrak q,
$$
which proves the claim.
:::

<1>3. Every irreducible component $Z$ of every nonempty fibre satisfies
$$
\boxed{
\dim Z\geq\dim X-\dim Y.
}
$$

::: {.proof}
For the prime $\mathfrak q$ of step <1>1, the affine dimension formula
[[P-AGH2320DIMENSION|gives]]
$$
\dim(B/\mathfrak q)+\height\mathfrak q
=
\dim B
=
n.
$$
By step <1>2,
$$
\height\mathfrak q\leq m.
$$
Therefore
$$
\dim Z
=
n-\height\mathfrak q
\geq
n-m
=
e.
$$
:::

<1>4. There is a nonempty Zariski-open subset
$$
V\subseteq Y
$$
such that
$$
V\subseteq f(X)
$$
and
$$
f^{-1}(V)\longrightarrow V
$$
is flat.

::: {.proof}
Generic flatness gives a nonempty open subset
$$
V_0\subseteq Y
$$
over which $f$ is flat; this is the characteristic-free companion statement
recorded with [[T-MORGEN|generic smoothness]].

Since $f$ is a dominant finite-type morphism, Chevalley's theorem
[[P-AGH2319CHEVALLEY|shows]] that $f(X)$ is constructible. Dominance says
that $f(X)$ is dense in the irreducible variety $Y$. A dense constructible
subset of an irreducible Noetherian space contains a nonempty open subset.
Hence there is a nonempty open
$$
V_1\subseteq Y
$$
with
$$
V_1\subseteq f(X).
$$
Set
$$
V=V_0\cap V_1.
$$
The intersection is nonempty and open because $Y$ is irreducible. It has both
required properties.
:::

<1>5. If $y\in V$ and $Z$ is any irreducible component of $f^{-1}(y)$,
then
$$
\boxed{
\dim Z=e=\dim X-\dim Y.
}
$$

::: {.proof}
Let $\mathfrak p\subseteq A$ and $\mathfrak q\subseteq B$ be as in
step <1>1. Since $y\in V$, the local map
$$
A_{\mathfrak p}\longrightarrow B_{\mathfrak q}
$$
is flat. Flat ring maps satisfy going-down.

Because $y$ is a closed point of the $m$-dimensional affine variety $Y$,
$$
\height\mathfrak p=m.
$$
Going-down lifts a chain of primes of length $m$ ending at
$\mathfrak p$ to a chain of primes of $B_{\mathfrak q}$ ending at
$\mathfrak q$. Hence
$$
\height\mathfrak q\geq m.
$$
Step <1>2 gives the reverse inequality, so
$$
\height\mathfrak q=m.
$$
Using the affine dimension formula exactly as in step <1>3 now gives
$$
\dim Z
=
n-\height\mathfrak q
=
n-m
=
e.
$$
:::

<1>6. The equality locus contains a Zariski-dense open subset of $Y$.

::: {.proof}
The set $V$ from step <1>4 is a nonempty open subset of the irreducible
variety $Y$, so it is Zariski dense. Step <1>5 shows that for every
$y\in V$, every irreducible component of the fibre has dimension
$$
\dim X-\dim Y.
$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 proves that every fibre component is affine, step <1>3 proves the
dimension lower bound for every $y\in f(X)$, and steps <1>4--<1>6 prove
generic equality on a Zariski-dense open subset of $Y$.
:::
:::
