---
schema: qual/card@1
id: P-AGH2321DVRLINE
kind: problem
title: Dimension theory fails for the affine line over a discrete valuation ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension Theory
  - Discrete Valuation Rings
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.21 statement and the dimension formulas contrasted in II.3.20.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $R$ be a discrete valuation ring containing its residue field $k$.
Let $X = \Spec R[t]$ be the affine line over $\Spec R$.
Show that statements (a), (d), and (e) of Hartshorne II.3.20 are false for $X$.
:::

::: {.solution}
Let
\[
\pi\in R
\]
be a uniformizer and let
\[
K=\operatorname{Frac}(R).
\]

<1>1. The scheme
\[
X=\Spec R[t]
\]
has dimension $2$.
::: {.proof}
The DVR $R$ is a noetherian ring of dimension $1$.  For a noetherian ring,
\[
\dim R[t]=\dim R+1=2.
\]
Concretely, the chain
\[
(0)\subsetneq(\pi)\subsetneq(\pi,t)
\]
already shows that the dimension is at least $2$.
:::

<1>2. The ideal
\[
\mathfrak m=(\pi t-1)\subseteq R[t]
\]
is maximal.
::: {.proof}
In the quotient, the relation
\[
\pi t=1
\]
makes $\pi$ invertible.  Hence
\[
R[t]/(\pi t-1)
\cong
R[\pi^{-1}]
=K,
\]
which is a field.  Therefore $\mathfrak m$ is maximal and the corresponding point
\[
P\in X
\]
is closed.
:::

<1>3. The maximal ideal $\mathfrak m=(\pi t-1)$ has height $1$.
::: {.proof}
The ring $R[t]$ is a noetherian domain and $\pi t-1$ is a nonzero nonunit.  Since the principal ideal it generates is prime by <1>2, Krull's principal ideal theorem gives
\[
\operatorname{ht}(\mathfrak m)\le1.
\]
Because
\[
(0)\subsetneq\mathfrak m,
\]
its height is at least $1$.  Hence
\[
\operatorname{ht}(\mathfrak m)=1.
\]
:::

<1>4. Hartshorne II.3.20(a) fails for $X$.
::: {.proof}
At the closed point $P$ from <1>2,
\[
\mathcal O_{X,P}=R[t]_{\mathfrak m}.
\]
Therefore
\[
\dim\mathcal O_{X,P}
=
\operatorname{ht}(\mathfrak m)
=1
\]
by <1>3, whereas
\[
\dim X=2
\]
by <1>1.  Thus the equality asserted in II.3.20(a) is false here.
:::

<1>5. Hartshorne II.3.20(d) also fails for $X$.
::: {.proof}
Take the closed subset
\[
Y=\{P\}=V(\mathfrak m).
\]
Since $Y$ is a single point,
\[
\dim Y=0.
\]
Its codimension in the integral affine scheme $X$ is the height of $\mathfrak m$:
\[
\codim(Y,X)=1.
\]
Thus
\[
\dim Y+\codim(Y,X)=0+1=1\ne2=\dim X.
\]
:::

<1>6. The nonempty open subset
\[
D(\pi)\subseteq X
\]
has dimension $1$.
::: {.proof}
Localizing at $\pi$ gives
\[
D(\pi)
\cong
\Spec R[t]_\pi
\cong
\Spec K[t].
\]
The polynomial ring in one variable over the field $K$ has dimension $1$.
:::

<1>7. Hartshorne II.3.20(e) fails for $X$.
::: {.proof}
The open $D(\pi)$ is nonempty, but by <1>6
\[
\dim D(\pi)=1,
\]
while by <1>1
\[
\dim X=2.
\]
Thus a nonempty open subset need not have the same dimension once the base is no longer a field.
:::

<1>8. Q.E.D.
::: {.proof}
Step <1>4 disproves II.3.20(a), <1>5 disproves II.3.20(d), and <1>7 disproves II.3.20(e).
:::
:::
