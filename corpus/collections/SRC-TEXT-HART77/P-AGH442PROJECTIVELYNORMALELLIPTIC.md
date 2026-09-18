---
schema: qual/card@1
id: P-AGH442PROJECTIVELYNORMALELLIPTIC
kind: problem
title: An elliptic curve embedded by $\abs{D}$ with $\deg D \geq 3$ is projectively normal
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Embeddings
  - Linear Systems
  - Very Ample Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.2 and its Mumford note. The proof below does not invoke
    the general degree-2g+1 theorem: it uses genus-one Riemann--Roch and the
    base-point-free pencil trick to prove the quadratic multiplication map and
    then every higher multiplication map directly.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
If $D$ is any divisor of degree $\geq 3$ on the elliptic curve $X$, and if we embed $X$ in $\PP^n$ by the complete linear system $\abs{D}$, show that the image of $X$ in $\PP^n$ is projectively normal.

Note.
It is true more generally that if $D$ is a divisor of degree $\geq 2g+1$ on a curve of genus $g$, then the embedding of $X$ by $\abs{D}$ is projectively normal (Mumford, p. 55).
:::

::: {.solution}
Put
$$
L=\mco_X(D),
\qquad
d=\deg L\ge3.
$$

<1>1. Every line bundle $A$ on $X$ of degree at least $2$ is globally
generated, and it contains a two-dimensional base-point-free space of
sections.

::: {.proof}
For any point $Q\in X$, Serre duality and $K_X\sim0$ give
$$
H^1(X,A(-Q))
\cong
H^0(X,A^{-1}(Q))^*.
$$
Since
$$
\deg A^{-1}(Q)=1-\deg A<0,
$$
the group on the right vanishes.  The exact sequence
$$
0\longrightarrow A(-Q)
\longrightarrow A
\longrightarrow A|_Q
\longrightarrow0
$$
therefore shows that
$$
H^0(X,A)\longrightarrow A|_Q
$$
is surjective for every $Q$.  Thus $A$ is globally generated.

Choose a nonzero section $s_0$.  Its zero divisor has finitely many points.
For each such point, the sections vanishing there form a proper hyperplane
of $H^0(X,A)$.  Since $k$ is infinite, choose $s_1$ outside the finite union
of these hyperplanes.  Then $s_0$ and $s_1$ have no common zero, so
$$
V=\langle s_0,s_1\rangle
$$
is a base-point-free pencil.
:::

<1>2. The quadratic multiplication map
$$
\operatorname{Sym}^2H^0(X,L)
\longrightarrow
H^0(X,L^2)
$$
is surjective.

::: {.proof}
Fix a point $P\in X$ and set
$$
A=L(-P).
$$
Since $\deg A=d-1\ge2$, step <1>1 supplies a base-point-free pencil
$$
V\subseteq H^0(X,A).
$$
The base-point-free pencil sequence is
$$
0\longrightarrow A^{-1}
\longrightarrow V\otimes\mco_X
\longrightarrow A
\longrightarrow0.
$$
Tensoring by $L$ gives
$$
0\longrightarrow\mco_X(P)
\longrightarrow V\otimes L
\longrightarrow L^2(-P)
\longrightarrow0,
$$
because $L\otimes A^{-1}\cong\mco_X(P)$.  The line bundle
$\mco_X(P)$ has positive degree, hence
$$
H^1(X,\mco_X(P))=0.
$$
Taking global sections therefore gives a surjection
$$
V\otimes H^0(X,L)
\twoheadrightarrow
H^0(X,L^2(-P)).
$$
Since $H^0(X,A)\subseteq H^0(X,L)$, the image of the full quadratic
multiplication map contains $H^0(X,L^2(-P))$.

By step <1>1, $L$ is globally generated.  Choose
$$
s\in H^0(X,L)
$$
with $s(P)\ne0$.  Then $s^2$ does not vanish at $P$, so
$$
s^2\notin H^0(X,L^2(-P)).
$$
The latter space has codimension one in $H^0(X,L^2)$, because
$H^1(X,L^2(-P))=0$.  Thus the quadratic multiplication image contains a
codimension-one subspace and an element outside it.  It is all of
$H^0(X,L^2)$.
:::

<1>3. For every $n\ge2$, multiplication gives a surjection
$$
H^0(X,L)\otimes H^0(X,L^n)
\twoheadrightarrow
H^0(X,L^{n+1}).
$$

::: {.proof}
By step <1>1 choose a base-point-free pencil
$$
W\subseteq H^0(X,L).
$$
Its pencil sequence
$$
0\longrightarrow L^{-1}
\longrightarrow W\otimes\mco_X
\longrightarrow L
\longrightarrow0
$$
becomes, after tensoring by $L^n$,
$$
0\longrightarrow L^{n-1}
\longrightarrow W\otimes L^n
\longrightarrow L^{n+1}
\longrightarrow0.
$$
For $n\ge2$ the line bundle $L^{n-1}$ has positive degree, so
$$
H^1(X,L^{n-1})=0.
$$
Hence
$$
W\otimes H^0(X,L^n)
\twoheadrightarrow
H^0(X,L^{n+1}).
$$
The same is therefore true with $H^0(X,L)$ in place of $W$.
:::

<1>4. For every $m\ge1$, the natural map
$$
\operatorname{Sym}^mH^0(X,L)
\longrightarrow
H^0(X,L^m)
$$
is surjective.

::: {.proof}
The assertion is tautological for $m=1$ and is step <1>2 for $m=2$.
Assume it for some $m\ge2$.  Compose its tensor product with $H^0(X,L)$
with the multiplication map of step <1>3:
$$
H^0(X,L)\otimes\operatorname{Sym}^mH^0(X,L)
\twoheadrightarrow
H^0(X,L)\otimes H^0(X,L^m)
\twoheadrightarrow
H^0(X,L^{m+1}).
$$
This composition is multiplication and therefore factors through
$$
\operatorname{Sym}^{m+1}H^0(X,L).
$$
Hence the latter maps surjectively to $H^0(X,L^{m+1})$.  Induction proves
the assertion for all $m$.
:::

<1>5. The embedding defined by $\abs{D}$ is projectively normal.

::: {.proof}
For the complete linear-series embedding
$$
X\hookrightarrow\PP(H^0(X,L)^*),
$$
the restriction map on degree-$m$ homogeneous forms is precisely
$$
\operatorname{Sym}^mH^0(X,L)
\longrightarrow
H^0(X,L^m).
$$
Step <1>4 proves that it is surjective for every $m\ge1$.  For $m=0$, the
restriction map is
$$
k\longrightarrow H^0(X,\mco_X),
$$
which is an isomorphism because $X$ is an integral projective curve over the
algebraically closed field $k$.  Since $X$ is nonsingular and hence normal,
the criterion of [[P-AGH2514PROJNORM|Exercise II.5.14(d)]] now gives
$$
\boxed{X\subseteq\PP^n\text{ is projectively normal}.}
$$
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>2--<1>4 prove normal generation of $L=\mco_X(D)$, and step <1>5
identifies this with projective normality of the complete-linear-series
embedding.
:::
:::
