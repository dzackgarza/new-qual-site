---
schema: qual/card@1
id: P-AGH2310FIBRES
kind: problem
title: Fibres of a morphism as schemes over the residue field
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibre Products
  - Fibres
  - Residue Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.10 statement; the nonzero closed-fibre claim requires char(k) != 2.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
a. If $f: X \to Y$ is a morphism and $y \in Y$ a point, show that $\operatorname{sp}(X_y)$ is homeomorphic to $\inverseof{f}(y)$ with the induced topology.

b. Let $X = \Spec k[s,t]/(s - t^2)$, let $Y = \Spec k[s]$, and let $f: X \to Y$ be the morphism defined by sending $s \mapsto s$.
   Assume $k$ algebraically closed.

   - If $y \in Y$ is the point $a \in k$ with $a \neq 0$, show that the fibre $X_y$ consists of two points, with residue field $k$.

   - If $y \in Y$ corresponds to $0 \in k$, show that the fibre $X_y$ is a nonreduced one-point scheme.

   - If $\eta$ is the generic point of $Y$, show that $X_\eta$ is a one-point scheme whose residue field is an extension of degree two of the residue field of $\eta$.
:::

::: {.solution}
<1>1. It is enough to identify the topology of a fibre affine-locally on $X$ and $Y$.
::: {.proof}
Choose an affine neighborhood
\[
V=\Spec B\subseteq Y
\]
of $y$, corresponding to a prime $\mathfrak p\subseteq B$, and cover $f^{-1}(V)$ by affine opens
\[
U=\Spec A.
\]
The fibre restricted to $U$ is
\[
U_y
=
U\times_V\Spec\kappa(y)
\cong
\Spec\bigl(A\otimes_B\kappa(\mathfrak p)\bigr).
\]
These affine pieces cover $X_y$, so it suffices to compare each $|U_y|$ with $U\cap f^{-1}(y)$.
:::

<1>2. There is a canonical ring isomorphism
\[
A\otimes_B\kappa(\mathfrak p)
\cong
S^{-1}(A/\mathfrak p A),
\qquad
S=B\setminus\mathfrak p.
\]
::: {.proof}
Since
\[
\kappa(\mathfrak p)
=
\operatorname{Frac}(B/\mathfrak p)
=
S^{-1}(B/\mathfrak p),
\]
tensoring first with $B/\mathfrak p$ and then localizing gives
\[
A\otimes_B\kappa(\mathfrak p)
\cong
S^{-1}(A\otimes_B B/\mathfrak p)
\cong
S^{-1}(A/\mathfrak p A).
\]
:::

<1>3. The points of $U_y$ correspond bijectively to the primes
\[
\mathfrak q\in\Spec A
\]
such that
\[
\mathfrak q\cap B=\mathfrak p.
\]
::: {.proof}
By <1>2, primes of the fibre ring correspond to primes $\mathfrak q\subseteq A$ which contain $\mathfrak pA$ and are disjoint from the image of $S$.

The first condition gives
\[
\mathfrak p\subseteq\mathfrak q\cap B,
\]
while disjointness from $B\setminus\mathfrak p$ gives the reverse inclusion.  Thus
\[
\mathfrak q\cap B=\mathfrak p.
\]
These are exactly the points of $U$ mapping to $y$.
:::

<1>4. The bijection in <1>3 is a homeomorphism from $|U_y|$ onto $U\cap f^{-1}(y)$ with the induced topology.
::: {.proof}
Let $R=S^{-1}(A/\mathfrak pA)$ be the fibre ring.  Any closed subset of $\Spec R$ is $V_R(J)$ for an ideal $J\subseteq R$.
Let $I\subseteq A$ be the inverse image in $A$ of the contraction of $J$ to $A/\mathfrak pA$.  Under the prime correspondence of <1>3,
\[
V_R(J)
\]
corresponds exactly to
\[
V_A(I)\cap f^{-1}(y)\cap U.
\]
Thus closed subsets on the fibre side are precisely intersections with closed subsets of $U$, which is the induced topology.
:::

<1>5. Therefore
\[
\boxed{|X_y|\xrightarrow{\sim}f^{-1}(y)}
\]
is a homeomorphism onto the set-theoretic fibre with its subspace topology.
::: {.proof}
The affine homeomorphisms from <1>4 are compatible on overlaps because they all arise from the projection $X_y\to X$.  They glue to the claimed global homeomorphism.
:::

<1>6. In part (b), the coordinate ring of $X$ is canonically isomorphic to $k[t]$, with the structural map
\[
k[s]\longrightarrow k[t],
\qquad
s\longmapsto t^2.
\]
::: {.proof}
The quotient relation $s-t^2=0$ eliminates $s$:
\[
k[s,t]/(s-t^2)\cong k[t].
\]
Under this isomorphism, the inclusion of the base coordinate ring is exactly $s\mapsto t^2$.
:::

<1>7. For a closed point $y=(s-a)$ of $Y$, the fibre is
\[
\boxed{
X_y
\cong
\Spec k[t]/(t^2-a).}
\]
::: {.proof}
Since $k$ is algebraically closed,
\[
\kappa(y)=k.
\]
Hence
\[
X_y
\cong
\Spec\bigl(k[t]\otimes_{k[s]}k[s]/(s-a)\bigr)
\cong
\Spec k[t]/(t^2-a).
\]
:::

<1>8. Assume $a\ne0$ and $\operatorname{char}k\ne2$.  Then $X_y$ consists of two reduced points, each with residue field $k$.
::: {.proof}
Choose $r\in k$ with $r^2=a$.  Since $a\ne0$, we have $r\ne0$, and since $2\ne0$ in $k$,
\[
r\ne-r.
\]
Thus
\[
t^2-a=(t-r)(t+r)
\]
has two distinct linear factors.  The Chinese remainder theorem gives
\[
k[t]/(t^2-a)
\cong
k[t]/(t-r)\times k[t]/(t+r)
\cong
k\times k.
\]
Therefore the fibre is the disjoint union of two reduced $k$-points.
:::

<1>9. If $a=0$, then the fibre is a nonreduced one-point scheme.
::: {.proof}
By <1>7,
\[
X_0=\Spec k[t]/(t^2).
\]
The quotient has the unique prime ideal $(t)$, so the spectrum has one point.  The class of $t$ is nonzero and nilpotent, so the scheme is not reduced.
:::

<1>10. If $a\ne0$ and $\operatorname{char}k=2$, then the fibre is likewise a nonreduced one-point scheme.
::: {.proof}
Choose $r\in k$ with $r^2=a$.  In characteristic $2$,
\[
t^2-a=t^2-r^2=(t-r)^2.
\]
Hence
\[
X_y\cong\Spec k[t]/(t-r)^2,
\]
which has one point and a nonzero nilpotent.  This is the correction recorded in the erratum.
:::

<1>11. Let $\eta$ be the generic point of $Y$.  Then
\[
\kappa(\eta)=k(s)
\]
and
\[
X_\eta
\cong
\Spec\bigl(k(s)[t]/(t^2-s)\bigr).
\]
::: {.proof}
The generic point corresponds to the zero prime of $k[s]$, whose residue field is its fraction field $k(s)$.  Base change along
\[
k[s]\hookrightarrow k(s)
\]
gives
\[
k[t]\otimes_{k[s]}k(s)
\cong
k(s)[t]/(t^2-s).
\]
:::

<1>12. The polynomial
\[
t^2-s\in k(s)[t]
\]
is irreducible in every characteristic.
::: {.proof}
A quadratic polynomial of the form $t^2-s$ is reducible over the field $k(s)$ exactly when $s$ is a square in $k(s)$.

But the discrete valuation $v_s$ on $k(s)$ associated to the prime $(s)$ satisfies
\[
v_s(s)=1.
\]
Every square has even $v_s$-valuation.  Therefore $s$ is not a square in $k(s)$, so $t^2-s$ is irreducible.
:::

<1>13. The generic fibre is a one-point scheme whose residue field has degree two over $k(s)$:
\[
\boxed{
X_\eta
=
\Spec k(s)(\sqrt{s}),
\qquad
[\kappa(X_\eta):k(s)]=2.}
\]
::: {.proof}
By <1>12, the quotient
\[
k(s)[t]/(t^2-s)
\]
is a field and has vector-space dimension $2$ over $k(s)$.
The spectrum of a field is one point.

If $\operatorname{char}k\ne2$, the extension is separable.  If $\operatorname{char}k=2$, it is purely inseparable.  Its degree is $2$ in either case.
:::

<1>14. Q.E.D.
::: {.proof}
Steps <1>1--<1>5 prove part (a).  Steps <1>6--<1>9 prove the source's intended characteristic-$\ne2$ closed-fibre statements, <1>10 records the characteristic-$2$ correction, and <1>11--<1>13 prove the generic-fibre statement.
:::
:::

::: {.remark title="Erratum"}
The first bullet in part (b) needs the hypothesis $\operatorname{char}k\ne2$.
If $\operatorname{char}k=2$ and $a\ne0$, then for the unique $r\in k$ with $r^2=a$,
\[
t^2-a=(t-r)^2,
\]
so the fibre is a nonreduced one-point scheme rather than two points.
The fibre over $0$ and the generic degree-two fibre statements are valid in every characteristic.
:::
