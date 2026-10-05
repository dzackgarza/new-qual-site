---
schema: qual/card@1
id: P-WESTOP06-B8
kind: problem
title: Lebesgue numbers and unique path lifting for covering spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. State the Lebesgue Number Lemma.
2. Let $p:E\to B$ be a covering map and let $p(e_0)=b_0$. Prove that every path
   \[
   f:[0,1]\to B,
   \qquad f(0)=b_0,
   \]
   has a unique lift $\widetilde f:[0,1]\to E$ beginning at $e_0$.
:::

::: {.solution}
<1>1. The Lebesgue Number Lemma states: if \(K\) is a compact metric space and \(\mathcal U\) is an open cover of \(K\), then there is a number \(\delta>0\) such that every subset of \(K\) of diameter less than \(\delta\) is contained in some member of \(\mathcal U\).

::: {.proof}
This is the statement of the lemma. Such a \(\delta\) is called a Lebesgue number for the cover.
:::

<1>2. The path \(f([0,1])\) admits a finite subdivision
\[
0=t_0<t_1<\cdots<t_n=1
\]
such that for each \(i\), the set
\[
f([t_{i-1},t_i])
\]
is contained in an evenly covered open set \(U_i\subseteq B\).

::: {.proof}
For every \(t\in[0,1]\), choose an evenly covered open neighborhood \(U_t\) of \(f(t)\). Then
\[
\{f^{-1}(U_t):t\in[0,1]\}
\]
is an open cover of the compact metric space \([0,1]\). By step <1>1, it has a Lebesgue number \(\delta>0\). Choose a subdivision whose mesh is less than \(\delta\). Each closed subinterval \([t_{i-1},t_i]\) has diameter less than \(\delta\), so it is contained in some \(f^{-1}(U_t)\). Rename that evenly covered neighborhood \(U_i\). Then
\[
f([t_{i-1},t_i])\subseteq U_i.
\]
:::

<1>3. Suppose a lift \(\widetilde f\) has been constructed on \([0,t_{i-1}]\), ending at \(e_{i-1}\in E\). There is a unique lift of
\[
f|_{[t_{i-1},t_i]}
\]
that begins at \(e_{i-1}\).

::: {.proof}
By step <1>2, the image of this subpath lies in an evenly covered set \(U_i\). Thus
\[
p^{-1}(U_i)=\coprod_{\lambda\in\Lambda_i}V_{i,\lambda},
\]
where each restriction
\[
p|_{V_{i,\lambda}}:V_{i,\lambda}\to U_i
\]
is a homeomorphism.

Because
\[
p(e_{i-1})=f(t_{i-1})\in U_i,
\]
the point \(e_{i-1}\) lies in a unique sheet \(V_i\). Define
\[
\widetilde f(t)
=
\bigl(p|_{V_i}\bigr)^{-1}(f(t)),
\qquad
t\in[t_{i-1},t_i].
\]
This is continuous, lifts \(f\), and takes the value \(e_{i-1}\) at \(t_{i-1}\).

For uniqueness, any lift of this subpath beginning at \(e_{i-1}\) must remain in the same sheet \(V_i\): its image is connected, it lies in the disjoint union of the sheets over \(U_i\), and it contains \(e_{i-1}\in V_i\). On \(V_i\), the equation \(p\circ\widetilde f=f\) forces
\[
\widetilde f=(p|_{V_i})^{-1}\circ f.
\]
:::

<1>4. There exists a lift
\[
\widetilde f:[0,1]\to E
\]
with
\[
\widetilde f(0)=e_0.
\]

::: {.proof}
Start with \(e_0\) at \(t_0=0\). Apply step <1>3 to the first subinterval \([t_0,t_1]\). Its endpoint supplies the starting point for the second subinterval. Continue inductively through the finite subdivision from step <1>2.

On adjacent subintervals, the two formulas agree at their common endpoint by construction. Hence the pasting lemma gives a continuous map
\[
\widetilde f:[0,1]\to E.
\]
Each piece satisfies \(p\circ\widetilde f=f\), so the pasted map does also, and its initial value is \(e_0\).
:::

<1>5. The lift in step <1>4 is unique.

::: {.proof}
Let \(\widetilde f\) and \(\widehat f\) be two lifts of \(f\) with
\[
\widetilde f(0)=\widehat f(0)=e_0.
\]
On the first subinterval \([t_0,t_1]\), step <1>3 gives uniqueness for the prescribed initial point, so
\[
\widetilde f=\widehat f
\]
there. In particular, the two lifts have the same value at \(t_1\). Applying step <1>3 again on \([t_1,t_2]\) shows that they agree there as well. Induction over the finite subdivision proves
\[
\widetilde f=\widehat f
\]
on all of \([0,1]\).
:::

<1>6. Every path \(f:[0,1]\to B\) beginning at \(b_0\) has a unique lift beginning at \(e_0\).

::: {.proof}
Existence is step <1>4 and uniqueness is step <1>5. Therefore
\[
\boxed{\text{there is a unique }\widetilde f:[0,1]\to E
\text{ with }p\circ\widetilde f=f,\ \widetilde f(0)=e_0.}
\]
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 states the Lebesgue Number Lemma, and step <1>6 proves the path-lifting theorem.
:::
:::
