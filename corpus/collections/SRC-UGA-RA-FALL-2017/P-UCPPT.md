---
schema: qual/card@1
id: P-UCPPT
kind: problem
title: $m^*(E)=0$ iff $m^*(f(E))=0$ for $f(x)=x^2$ on $[0,\infty)$, and $E\mapsto
  f(E)$ bijects Lebesgue sets of $\RR^+$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UGA August 2017 real-analysis qualifying exam; repaired the false claim that sqrt is Lipschitz at 0 and the false compact-plus-null representation of arbitrary measurable sets.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $f(x) = x^2$ and $E \subset [0, \infty) \definedas \RR^+$.

1. Show that
\[
m^*(E) = 0 \iff m^*(f(E)) = 0.
\]

2. Deduce that the map

\[
\phi: \mathcal{L}(\RR^+) &\to \mathcal{L}(\RR^+) \\
E &\mapsto f(E)
\]
  is a bijection from the class of Lebesgue measurable sets of $[0, \infty)$ to itself.
:::

::: solution
<1>1. Show that null sets are preserved by $x\mapsto x^2$.
::: proof
For every $M>0$, the map
\[
f(x)=x^2
\]
is Lipschitz on $[0,M]$, since $|f'(x)|=2x\le2M$ there. Hence if $A\subset[0,M]$ has outer measure zero, then $f(A)$ has outer measure zero.

Now let $E\subset[0,\infty)$ with $m^*(E)=0$ and put
\[
E_k=E\cap[k,k+1].
\]
Then each $E_k$ is null and $f(E_k)$ is null, so
\[
f(E)=\bigcup_{k=0}^\infty f(E_k)
\]
is null. Thus
\[
m^*(E)=0\Longrightarrow m^*(f(E))=0.
\]
:::

<1>2. Show that null sets are preserved by the inverse map $y\mapsto\sqrt y$.
::: proof
Fix $M>0$. The function
\[
g(y)=\sqrt y
\]
is absolutely continuous on $[0,M]$, because
\[
g(y)=\int_0^y \frac{dt}{2\sqrt t}
\]
and $(2\sqrt t)^{-1}\in L^1(0,M)$. Every absolutely continuous function has Luzin's property $(N)$, so it maps Lebesgue-null sets to null sets.

If $A\subset[0,\infty)$ is null, decompose
\[
A=\bigcup_{k=0}^\infty A_k,
\qquad A_k=A\cap[k,k+1].
\]
Each $A_k$ is null and bounded, hence $g(A_k)$ is null. Therefore
\[
g(A)=\bigcup_{k=0}^\infty g(A_k)
\]
is null.

Applying this to $A=f(E)$ gives
\[
m^*(f(E))=0\Longrightarrow m^*(E)=m^*(g(f(E)))=0.
\]
Thus
\[
\boxed{m^*(E)=0\iff m^*(f(E))=0.}
\]
:::

<1>3. Show that $f$ sends Lebesgue measurable sets to Lebesgue measurable sets.
::: proof
On $[0,\infty)$, $f(x)=x^2$ is a homeomorphism with inverse $g(y)=\sqrt y$. Hence $f$ and $g$ send Borel sets to Borel sets.

Let $E$ be Lebesgue measurable. There is a Borel set $B$ such that
\[
m(E\triangle B)=0.
\]
Since $f$ is injective,
\[
f(E)\triangle f(B)=f(E\triangle B).
\]
By part 1, $f(E\triangle B)$ is null, while $f(B)$ is Borel. Therefore $f(E)$ is Lebesgue measurable.
:::

<1>4. Conclude bijectivity on the Lebesgue sigma-algebra.
::: proof
The same argument applied to the inverse homeomorphism $g(y)=\sqrt y$ shows that $g$ also sends Lebesgue measurable sets to Lebesgue measurable sets. Since $f$ and $g$ are inverse bijections of $[0,\infty)$,
\[
E\longmapsto f(E)
\]
is a bijection from the Lebesgue measurable subsets of $[0,\infty)$ onto themselves.
:::
:::
