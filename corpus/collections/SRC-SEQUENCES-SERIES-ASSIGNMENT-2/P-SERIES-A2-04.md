---
schema: qual/card@1
id: P-SERIES-A2-04
kind: problem
title: Subsequence criteria for convergence of a sequence
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Let $\{a_n\}$ be a bounded sequence with the property that every convergent subsequence converges to the same limit $a$. Show that the entire sequence converges to $a$.

(b) Now assume that $\{a_n\}$ has the property that every subsequence has a further subsequence that converges to the same limit $a$. Show that the entire sequence converges to $a$.
:::

::: {.solution}
## Part (a)

Assume \((a_n)\) is bounded and every convergent subsequence converges to
the same limit \(a\).

<1>1. Suppose, toward a contradiction, that
\[
a_n\not\to a.
\]

::: {.proof}
This is the negation of the desired conclusion.
:::

<1>2. Then there exists
\[
\varepsilon>0
\]
such that for every \(N\), there is some \(n\ge N\) with
\[
\boxed{|a_n-a|\ge\varepsilon}.
\]

::: {.proof}
This is the negation of the \(\varepsilon\)-\(N\) definition of convergence
to \(a\).
:::

<1>3. Therefore one can choose a subsequence
\[
(a_{n_k})
\]
such that
\[
\boxed{
|a_{n_k}-a|\ge\varepsilon}
\]
for every \(k\).

::: {.proof}
Choose \(n_1\) using step <1>2 with \(N=1\). After choosing \(n_k\), apply
step <1>2 with \(N=n_k+1\) to choose \(n_{k+1}>n_k\) satisfying the same
inequality.
:::

<1>4. The subsequence \((a_{n_k})\) is bounded.

::: {.proof}
Every subsequence of a bounded sequence is bounded.
:::

<1>5. By Bolzano--Weierstrass, \((a_{n_k})\) has a convergent
subsubsequence
\[
a_{n_{k_j}}\to b
\]
for some \(b\in\mathbb R\).

::: {.proof}
Bolzano--Weierstrass states that every bounded real sequence has a convergent
subsequence.
:::

<1>6. By the hypothesis of part (a),
\[
\boxed{b=a}.
\]

::: {.proof}
The sequence \((a_{n_{k_j}})\) is a convergent subsequence of the original
sequence, and every such subsequence is assumed to converge to \(a\).
:::

<1>7. On the other hand,
\[
\boxed{|b-a|\ge\varepsilon}.
\]

::: {.proof}
Every term of the convergent subsubsequence satisfies
\[
|a_{n_{k_j}}-a|\ge\varepsilon
\]
by step <1>3. Passing to the limit and using continuity of
\(x\mapsto|x-a|\) gives
\[
|b-a|\ge\varepsilon.
\]
:::

<1>8. Steps <1>6 and <1>7 contradict one another.

::: {.proof}
If \(b=a\), then
\[
|b-a|=0,
\]
but step <1>7 gives
\[
|b-a|\ge\varepsilon>0.
\]
:::

<1>9. Therefore
\[
\boxed{a_n\to a}.
\]

::: {.proof}
The assumption of nonconvergence in step <1>1 led to a contradiction.
:::

## Part (b)

Assume now that every subsequence of \((a_n)\) has a further subsequence
converging to \(a\).

<1>10. Suppose, toward a contradiction, that
\[
a_n\not\to a.
\]

::: {.proof}
Again this is the negation of the desired conclusion.
:::

<1>11. Then there are
\[
\varepsilon>0
\]
and a subsequence \((a_{n_k})\) such that
\[
\boxed{
|a_{n_k}-a|\ge\varepsilon}
\]
for every \(k\).

::: {.proof}
Repeat the construction in steps <1>2--<1>3.
:::

<1>12. By the hypothesis of part (b), the subsequence \((a_{n_k})\) has a
further subsequence
\[
a_{n_{k_j}}\to a.
\]

::: {.proof}
The stated property applies to every subsequence, including the one chosen in
step <1>11.
:::

<1>13. Since
\[
a_{n_{k_j}}\to a,
\]
there exists \(J\) such that for all \(j\ge J\),
\[
|a_{n_{k_j}}-a|<\varepsilon.
\]

::: {.proof}
Apply the definition of convergence with the same positive
\(\varepsilon\) from step <1>11.
:::

<1>14. This contradicts
\[
|a_{n_{k_j}}-a|\ge\varepsilon
\]
from step <1>11.

::: {.proof}
The further subsequence is still a subsequence of \((a_{n_k})\), so every
one of its terms satisfies the lower bound from step <1>11.
:::

<1>15. Therefore
\[
\boxed{a_n\to a}.
\]

::: {.proof}
The nonconvergence assumption in step <1>10 leads to the contradiction in
step <1>14.
:::

<1>16. Q.E.D.

::: {.proof}
Step <1>9 proves part (a), and step <1>15 proves part (b).
:::
:::
