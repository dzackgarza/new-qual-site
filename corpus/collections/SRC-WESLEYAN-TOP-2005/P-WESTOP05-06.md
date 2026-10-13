---
schema: qual/card@1
id: P-WESTOP05-06
kind: problem
title: Define the fundamental group and sketch the proof that it is a group
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Given a pointed space $(X,x_0)$, define the fundamental group
\[
\pi_1(X,x_0)
\]
and sketch the proof that the resulting set of homotopy classes is in fact a group.
:::

::: {.solution}
Let
\[
I=[0,1].
\]

<1>1. A based loop at \(x_0\) is a continuous map
\[
\gamma:I\to X
\]
such that
\[
\boxed{
\gamma(0)=\gamma(1)=x_0}.
\]

::: {.proof}
This is the standard definition of a loop based at \(x_0\).
:::

<1>2. Two based loops \(\gamma_0,\gamma_1\) are equivalent if there is a
homotopy
\[
H:I\times I\to X
\]
such that
\[
H(s,0)=\gamma_0(s),
\qquad
H(s,1)=\gamma_1(s),
\]
and
\[
\boxed{
H(0,t)=H(1,t)=x_0}
\]
for every \(t\in I\).

::: {.proof}
This is homotopy relative to the endpoints.
:::

<1>3. The fundamental group is the set
\[
\boxed{
\pi_1(X,x_0)
=
\{\text{based loops at }x_0\}
/\simeq_{\partial I}}.
\]

::: {.proof}
The equivalence relation is based homotopy from step <1>2.
:::

<1>4. For based loops \(\alpha,\beta\), define their concatenation
\[
\alpha*\beta:I\to X
\]
by
\[
\boxed{
(\alpha*\beta)(s)
=
\begin{cases}
\alpha(2s),&0\le s\le1/2,\\[3pt]
\beta(2s-1),&1/2\le s\le1.
\end{cases}}
\]

::: {.proof}
At \(s=1/2\), both formulas equal
\[
\alpha(1)=x_0=\beta(0),
\]
so the pasting lemma gives continuity. The endpoints are \(x_0\), so it is a
based loop.
:::

<1>5. Define multiplication on homotopy classes by
\[
\boxed{
[\alpha]\,[\beta]
=
[\alpha*\beta]}.
\]

::: {.proof}
Well-definedness is proved in step <1>6.
:::

<1>6. The multiplication in step <1>5 is well defined.

::: {.proof}
Suppose
\[
\alpha\simeq_{\partial I}\alpha'
\]
through \(H_\alpha\), and
\[
\beta\simeq_{\partial I}\beta'
\]
through \(H_\beta\).

Define
\[
H(s,t)
=
\begin{cases}
H_\alpha(2s,t),&0\le s\le1/2,\\[3pt]
H_\beta(2s-1,t),&1/2\le s\le1.
\end{cases}
\]
The two formulas agree at \(s=1/2\) because both homotopies fix the
basepoint. Thus \(H\) is a based homotopy
\[
\alpha*\beta
\simeq_{\partial I}
\alpha'*\beta'.
\]
Hence the class depends only on \([\alpha]\) and \([\beta]\).
:::

<1>7. Let
\[
c(s)=x_0
\]
be the constant loop.

::: {.proof}
This is a based loop.
:::

<1>8. For every loop \(\alpha\),
\[
\boxed{
[c][\alpha]=[\alpha]}.
\]

::: {.proof}
The loop \(c*\alpha\) stays at \(x_0\) on the first half of the interval and
then traverses \(\alpha\) on the second half.

It differs from \(\alpha\) only by a monotone reparametrization that inserts
a constant initial segment. Any two nondecreasing continuous
reparametrizations
\[
\rho_0,\rho_1:I\to I
\]
with
\[
\rho_j(0)=0,\qquad \rho_j(1)=1
\]
are homotopic through
\[
\rho_t=(1-t)\rho_0+t\rho_1.
\]
Thus
\[
H(s,t)=\alpha(\rho_t(s))
\]
gives a based homotopy from \(c*\alpha\) to \(\alpha\).
:::

<1>9. Likewise,
\[
\boxed{
[\alpha][c]=[\alpha]}.
\]

::: {.proof}
The same reparametrization argument removes the constant terminal segment of
\(\alpha*c\).
:::

<1>10. Thus
\[
\boxed{[c]}
\]
is the identity element.

::: {.proof}
Combine steps <1>8--<1>9.
:::

<1>11. Define the reverse loop
\[
\boxed{
\overline\alpha(s)=\alpha(1-s)}.
\]

::: {.proof}
It begins and ends at \(x_0\), so it is a based loop.
:::

<1>12. One has
\[
\boxed{
[\alpha][\overline\alpha]=[c]}.
\]

::: {.proof}
The concatenation \(\alpha*\overline\alpha\) traverses \(\alpha\) and then
retraces it.

Define
\[
H(s,t)
=
\begin{cases}
\alpha\!\left(2s(1-t)\right),
&0\le s\le1/2,\\[4pt]
\alpha\!\left(2(1-s)(1-t)\right),
&1/2\le s\le1.
\end{cases}
\]
At \(t=0\), this is \(\alpha*\overline\alpha\). At \(t=1\), it is the
constant loop at \(\alpha(0)=x_0\). The two pieces agree at \(s=1/2\), and
the endpoints remain \(x_0\). Hence this is a based nullhomotopy.
:::

<1>13. Likewise,
\[
\boxed{
[\overline\alpha][\alpha]=[c]}.
\]

::: {.proof}
Apply step <1>12 to the loop \(\overline\alpha\), whose reverse is
\(\alpha\).
:::

<1>14. Thus
\[
\boxed{
[\alpha]^{-1}
=
[\overline\alpha]}.
\]

::: {.proof}
Steps <1>12--<1>13 show that \([\overline\alpha]\) is a two-sided inverse.
:::

<1>15. For based loops \(\alpha,\beta,\gamma\), the loops
\[
(\alpha*\beta)*\gamma
\]
and
\[
\alpha*(\beta*\gamma)
\]
traverse the same three paths in the same order, but at different speeds.

::: {.proof}
The first loop allocates one quarter of the interval to \(\alpha\), one
quarter to \(\beta\), and one half to \(\gamma\). The second allocates one
half to \(\alpha\), one quarter to \(\beta\), and one quarter to \(\gamma\).
:::

<1>16. These two loops are based-homotopic.

::: {.proof}
Let
\[
p_0,p_1:I\to[0,3]
\]
be the piecewise-linear nondecreasing parametrizations that encode the
traversal schedules of
\[
(\alpha*\beta)*\gamma
\]
and
\[
\alpha*(\beta*\gamma),
\]
respectively, where the intervals
\[
[0,1],\quad[1,2],\quad[2,3]
\]
correspond to \(\alpha,\beta,\gamma\).

The convex interpolation
\[
p_t=(1-t)p_0+tp_1
\]
is still nondecreasing and fixes the endpoints. Composing the common
three-stage path with \(p_t\) gives a based homotopy between the two
concatenations.
:::

<1>17. Therefore multiplication is associative:
\[
\boxed{
([\alpha][\beta])[\gamma]
=
[\alpha]([\beta][\gamma])}.
\]

::: {.proof}
By step <1>16,
\[
[(\alpha*\beta)*\gamma]
=
[\alpha*(\beta*\gamma)].
\]
:::

<1>18. Consequently,
\[
\boxed{
\pi_1(X,x_0)
}
\]
is a group under concatenation.

::: {.proof}
Closure and well-definedness are steps <1>4--<1>6, the identity is step
<1>10, inverses are step <1>14, and associativity is step <1>17.
:::

<1>19. Q.E.D.

::: {.proof}
Step <1>18 proves that the homotopy classes of based loops form the
fundamental group.
:::
:::
