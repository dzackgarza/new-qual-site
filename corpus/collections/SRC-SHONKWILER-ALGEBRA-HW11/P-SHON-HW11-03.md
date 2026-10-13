---
schema: qual/card@1
id: P-SHON-HW11-03
kind: problem
title: Prime-degree extensions and Galois subfields of the normal closure
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 3 of the retained Algebra HW 11 solution packet.
---

::: {.problem}
Let $p$ be prime and let $K\subset L$ be a separable extension of degree $p$ which is not Galois.
Let $\widetilde L$ be the Galois closure of $L/K$.
Show that $\widetilde L$ contains no subfield $M$ which is Galois over $K$ of degree $p$.
:::

::: {.solution}
Let
\[
K\subset L,
\qquad
[L:K]=p,
\]
and let
\[
\widetilde L
\]
be the Galois closure of \(L/K\).

<1>1. Since \(L/K\) is finite separable of degree \(p\), there exists
\[
\alpha\in L
\]
such that
\[
\boxed{L=K(\alpha)}.
\]

::: {.proof}
Apply the primitive element theorem.
:::

<1>2. Let
\[
f(x)\in K[x]
\]
be the minimal polynomial of \(\alpha\). Then
\[
\boxed{\deg f=p}.
\]

::: {.proof}
For a simple algebraic extension,
\[
[K(\alpha):K]=\deg m_\alpha.
\]
Use \([L:K]=p\).
:::

<1>3. The polynomial \(f\) is separable.

::: {.proof}
The extension \(L/K\) is separable, so the minimal polynomial of every element of \(L\), in particular \(\alpha\), is separable.
:::

<1>4. The Galois closure \(\widetilde L\) is the splitting field of \(f\) over \(K\).

::: {.proof}
Since \(L=K(\alpha)\), the normal closure of \(L/K\) is obtained by adjoining all \(K\)-conjugates of \(\alpha\), equivalently all roots of \(f\).
:::

<1>5. The action of
\[
G=\operatorname{Gal}(\widetilde L/K)
\]
on the \(p\) roots of \(f\) gives an injective homomorphism
\[
\boxed{G\hookrightarrow S_p}.
\]

::: {.proof}
Every \(K\)-automorphism of \(\widetilde L\) permutes the roots of \(f\). The action is faithful because \(\widetilde L\) is generated over \(K\) by those roots.
:::

<1>6. Therefore
\[
\boxed{
[\widetilde L:K]=|G|\mid p!}.
\]

::: {.proof}
Since \(\widetilde L/K\) is finite Galois,
\[
[\widetilde L:K]=|G|.
\]
By step <1>5, \(G\) is a subgroup of \(S_p\), so Lagrange's theorem gives
\[
|G|\mid|S_p|=p!.
\]
:::

Assume, toward a contradiction, that there exists a field
\[
K\subset M\subset\widetilde L
\]
such that \(M/K\) is Galois and
\[
[M:K]=p.
\]

<1>7. The compositum
\[
LM
\]
is contained in \(\widetilde L\).

::: {.proof}
Both \(L\) and \(M\) are subfields of \(\widetilde L\), so the smallest field containing both is also a subfield of \(\widetilde L\).
:::

<1>8. The extension
\[
LM/L
\]
is Galois.

::: {.proof}
The extension \(M/K\) is finite Galois. Base change from \(K\) to \(L\) preserves separability and normality of the resulting compositum extension:
\[
LM/L
\]
is finite separable, and every \(L\)-embedding of \(LM\) fixes \(L\) and sends \(M\) to itself because \(M/K\) is normal. Hence \(LM/L\) is Galois.
:::

<1>9. One has
\[
\boxed{
[LM:L]
=
[M:L\cap M]}.
\]

::: {.proof}
This is the standard degree formula for a compositum when \(M/K\) is finite:
\[
[LM:L]=[M:L\cap M].
\]
:::

<1>10. Since
\[
[M:K]=p
\]
is prime,
\[
\boxed{
[LM:L]\in\{1,p\}}.
\]

::: {.proof}
The intermediate field
\[
K\subseteq L\cap M\subseteq M
\]
has degree over \(K\) dividing the prime degree \([M:K]=p\). Hence
\[
[L\cap M:K]
\]
is \(1\) or \(p\), and step <1>9 gives the two possibilities for \([LM:L]\).
:::

<1>11. The case
\[
[LM:L]=1
\]
is impossible.

::: {.proof}
If
\[
LM=L,
\]
then
\[
M\subseteq L.
\]
But
\[
[M:K]=[L:K]=p,
\]
so the tower law forces
\[
M=L.
\]
This contradicts the hypotheses that \(M/K\) is Galois while \(L/K\) is not.
:::

<1>12. Therefore
\[
\boxed{
[LM:L]=p}.
\]

::: {.proof}
Step <1>10 gives only the two possibilities, and step <1>11 excludes \(1\).
:::

<1>13. Hence
\[
\boxed{
L\cap M=K}.
\]

::: {.proof}
By step <1>9,
\[
p=[LM:L]=[M:L\cap M].
\]
Since
\[
[M:K]=p,
\]
the tower law
\[
[M:K]
=
[M:L\cap M]\,[L\cap M:K]
\]
gives
\[
[L\cap M:K]=1.
\]
:::

<1>14. Therefore
\[
\boxed{
[LM:K]=p^2}.
\]

::: {.proof}
Use the tower
\[
K\subset L\subset LM:
\]
\[
[LM:K]
=
[LM:L][L:K]
=
p\cdot p
=
p^2.
\]
:::

<1>15. Since
\[
LM\subseteq\widetilde L,
\]
one has
\[
\boxed{
p^2\mid[\widetilde L:K]}.
\]

::: {.proof}
By the tower law,
\[
[\widetilde L:K]
=
[\widetilde L:LM]\,[LM:K].
\]
Apply step <1>14.
:::

<1>16. Combining steps <1>6 and <1>15,
\[
\boxed{
p^2\mid p!}.
\]

::: {.proof}
Step <1>15 gives
\[
p^2\mid[\widetilde L:K],
\]
and step <1>6 gives
\[
[\widetilde L:K]\mid p!.
\]
Divisibility is transitive.
:::

<1>17. But
\[
\boxed{
v_p(p!)=1}.
\]

::: {.proof}
Among the factors
\[
1,2,\dots,p,
\]
the only multiple of the prime \(p\) is \(p\) itself, and it contributes exactly one factor of \(p\).
:::

<1>18. Hence
\[
p^2\nmid p!,
\]
contradicting step <1>16.

::: {.proof}
Step <1>17 says the exponent of \(p\) in the prime factorization of \(p!\) is exactly \(1\), whereas divisibility by \(p^2\) would require exponent at least \(2\).
:::

<1>19. Therefore no such field \(M\) exists.

::: {.proof}
The assumption of its existence led to the contradiction in step <1>18.
:::

<1>20. Thus
\[
\boxed{
\widetilde L
\text{ contains no subfield }M
\text{ with }
M/K\text{ Galois and }[M:K]=p.}
\]

::: {.proof}
This is step <1>19.
:::

<1>21. Q.E.D.

::: {.proof}
Step <1>20 is the required conclusion.
:::
:::
