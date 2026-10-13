---
schema: qual/card@1
id: P-UTCT-1-23
kind: problem
title: Homotopy classes of plane fields on the lens space $L(p,q)$
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Exercise 1.23 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the construction of Gamma_tau, Corollary 1.21 and Example 1.22, on which the exercise depends, from pp. 5-6 of Gompf Contact Topology.pdf.
---

::: {.problem}
Let $M$ be a closed, oriented $3$-manifold with a trivialization $\tau$ of $TM$, so that oriented plane fields on $M$ up to homotopy correspond to $[M, S^2]$ and hence to framed cobordism classes of framed links in $M$.
Let $\Gamma_\tau$ be the map taking an oriented plane field $\xi$ to the class in $H_1(M)$ of the corresponding framed link; it is onto, and the Euler class satisfies $\operatorname{PD}(e(\xi)) = 2\Gamma_\tau(\xi)$.
Consequently an oriented plane bundle $\xi$ on $M$ is realized as a plane field if and only if $e(\xi) = 2x$ for some $x \in H_1(M)$.

Example: consider $M = \mathbb{RP}^3$.
We know $H_1(\mathbb{RP}^3) = \mathbb{Z}/2\mathbb{Z}$.
Note that only $0 \in H_1$ can be represented as $2x$, so every plane field in $\mathbb{RP}^3$ is trivial as a plane bundle.
For fixed choice of $\tau$, however, we get two values of $\Gamma_\tau$ and therefore there are at least two different plane fields that are not homotopic.

Analyze the lens space $L(p,q)$ in the same way.
(Hint: $H_1(L(p,q)) = \mathbb{Z}/p\mathbb{Z}$.)
:::

::: {.solution}
Let
\[
M=L(p,q).
\]
By the hint,
\[
H_1(M;\mathbb Z)\cong\mathbb Z/p.
\]
By Poincaré duality for the closed oriented \(3\)-manifold \(M\),
\[
H^2(M;\mathbb Z)\cong H_1(M;\mathbb Z)\cong\mathbb Z/p.
\]

<1>1. For a fixed trivialization \(\tau\) of \(TM\), the invariant
\[
\Gamma_\tau
\]
is a surjection
\[
\boxed{
\Gamma_\tau:
\{\text{oriented plane fields on }M\}/\simeq
\twoheadrightarrow
\mathbb Z/p}.
\]

::: {.proof}
This is the surjectivity statement preceding the exercise, applied to
\[
H_1(M)\cong\mathbb Z/p.
\]
:::

<1>2. Consequently, for fixed \(\tau\), there are at least \(p\) distinct
homotopy classes of oriented plane fields on \(M\).

::: {.proof}
Plane fields with different values of \(\Gamma_\tau\) cannot be homotopic,
since \(\Gamma_\tau\) is a homotopy invariant. Step <1>1 shows that all
\(p\) elements of \(\mathbb Z/p\) occur.
:::

<1>3. For every oriented plane field \(\xi\),
\[
\boxed{
\operatorname{PD}(e(\xi))
=
2\Gamma_\tau(\xi)}
\]
in
\[
H_1(M)\cong\mathbb Z/p.
\]

::: {.proof}
This is the identity established immediately before Corollary 1.21 in the
source notes.
:::

<1>4. Therefore an oriented \(2\)-plane bundle over \(M\) with Euler class
\(e\in H^2(M)\) is realizable as a plane field exactly when
\[
\boxed{
\operatorname{PD}(e)\in2(\mathbb Z/p)}.
\]

::: {.proof}
Corollary 1.21 says that an oriented plane bundle is realized as a plane
field if and only if
\[
e=2x
\]
under the Poincaré-duality identification with \(H_1(M)\).
:::

## The case \(p\) odd

<1>5. If \(p\) is odd, multiplication by \(2\),
\[
d_2:\mathbb Z/p\to\mathbb Z/p,
\qquad
x\longmapsto2x,
\]
is an isomorphism.

::: {.proof}
Since
\[
\gcd(2,p)=1,
\]
the class of \(2\) is invertible modulo \(p\).
:::

<1>6. Hence, if \(p\) is odd,
\[
\boxed{
2(\mathbb Z/p)=\mathbb Z/p}.
\]

::: {.proof}
This is surjectivity of the isomorphism in step <1>5.
:::

<1>7. Therefore every oriented \(2\)-plane bundle over \(L(p,q)\) is
realizable as a plane field when \(p\) is odd.

::: {.proof}
Oriented real rank-\(2\) bundles are classified by their Euler class in
\[
H^2(M;\mathbb Z)\cong\mathbb Z/p.
\]
By step <1>6, every Euler class is divisible by \(2\), so step <1>4 applies
to every bundle class.
:::

<1>8. For \(p\) odd, the Euler class determines the value of
\(\Gamma_\tau\).

::: {.proof}
From step <1>3,
\[
2\Gamma_\tau(\xi)
=
\operatorname{PD}(e(\xi)).
\]
Since multiplication by \(2\) is injective by step <1>5, the right-hand side
determines the unique value of \(\Gamma_\tau(\xi)\).
:::

<1>9. Thus, for \(p\) odd, the \(p\) values of \(\Gamma_\tau\) obtained in
step <1>1 give \(p\) plane fields whose underlying plane bundles have \(p\)
different Euler classes.

::: {.proof}
Step <1>8 says distinct \(\Gamma_\tau\)-values have distinct doubles, hence
distinct Euler classes. There are \(p\) values by step <1>1.
:::

## The case \(p\) even

Assume
\[
p=2r.
\]

<1>10. The kernel of multiplication by \(2\) on \(\mathbb Z/p\) is
\[
\boxed{
\ker d_2
=
\{0,r\}}.
\]

::: {.proof}
The congruence
\[
2x\equiv0\pmod{2r}
\]
is equivalent to
\[
x\equiv0\pmod r.
\]
Modulo \(2r\), the two such classes are \(0\) and \(r\).
:::

<1>11. The image of multiplication by \(2\) is
\[
\boxed{
2(\mathbb Z/p)
=
\{0,2,4,\dots,2r-2\}}
\]
and has order
\[
\boxed{r=p/2}.
\]

::: {.proof}
The image consists of the even residue classes modulo \(2r\). By the
first-isomorphism theorem,
\[
|\operatorname{im}d_2|
=
\frac{|\mathbb Z/p|}{|\ker d_2|}
=
\frac{p}{2}
=
r.
\]
:::

<1>12. Therefore, when \(p\) is even, exactly
\[
\boxed{p/2}
\]
Euler classes occur among plane fields.

::: {.proof}
By step <1>4, the realizable Euler classes are exactly the image of
multiplication by \(2\). Step <1>11 gives its cardinality.
:::

<1>13. Each realizable Euler class has exactly two possible
\(\Gamma_\tau\)-values.

::: {.proof}
If
\[
2x=2y
\]
in \(\mathbb Z/p\), then
\[
x-y\in\ker d_2
=
\{0,p/2\}
\]
by step <1>10. Thus the two solutions differ by \(p/2\), and there are
exactly two of them.
:::

<1>14. Hence, when \(p\) is even, there are pairs of nonhomotopic plane
fields having isomorphic underlying oriented plane bundles.

::: {.proof}
Let \(x\in\mathbb Z/p\). By surjectivity of \(\Gamma_\tau\), choose plane
fields
\[
\xi,\xi'
\]
with
\[
\Gamma_\tau(\xi)=x,
\qquad
\Gamma_\tau(\xi')=x+p/2.
\]
They are not homotopic because their \(\Gamma_\tau\)-values differ. But
step <1>3 and
\[
2(x+p/2)
=
2x+p
=
2x
\]
in \(\mathbb Z/p\) show that
\[
e(\xi)=e(\xi').
\]
Oriented \(2\)-plane bundles are classified by Euler class, so the underlying
plane bundles are isomorphic.
:::

<1>15. For \(p=2\), this recovers the \(\mathbb{RP}^3\) example:
every plane field has trivial Euler class, but \(\Gamma_\tau\) takes two
values.

::: {.proof}
When
\[
p=2,
\]
the image of doubling is
\[
\{0\},
\]
while
\[
H_1\cong\mathbb Z/2
\]
has two elements. This is exactly Example 1.22.
:::

<1>16. Summarizing:
\[
\boxed{
\begin{array}{c|c|c}
& \text{realizable Euler classes} &
\text{\(\Gamma_\tau\)-values over each Euler class}\\
\hline
p\text{ odd} & p & 1\\
p\text{ even} & p/2 & 2.
\end{array}}
\]

::: {.proof}
For odd \(p\), use steps <1>5--<1>9. For even \(p\), use steps
<1>10--<1>14.
:::

<1>17. In either parity, for fixed \(\tau\) there are at least \(p\)
pairwise nonhomotopic plane fields on \(L(p,q)\).

::: {.proof}
This is step <1>2. The parity analysis describes how those \(p\) distinct
\(\Gamma_\tau\)-values project to Euler classes.
:::

<1>18. Q.E.D.

::: {.proof}
Steps <1>7--<1>9 analyze the odd case, and steps <1>12--<1>15 analyze the
even case, including the \(\mathbb{RP}^3\) specialization.
:::
:::
