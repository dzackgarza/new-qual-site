---
schema: qual/card@1
id: P-WESRA10-II3
kind: problem
title: 'Positive-measure nowhere-dense set and unavoidable discontinuities'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
(a) Give an example of a closed set $A\subset\RR^2$ of positive Lebesgue measure containing no nonempty open set.

(b) If $A$ is such a set and $f:\RR^2\to\RR$ satisfies $f=\chi_A$ almost everywhere, prove that there is a set $B$ of positive measure such that $f$ is discontinuous at every point of $B$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let $C\subset[0,1]$ be a fat Cantor set: $C$ is closed, has empty
interior, and has positive one-dimensional Lebesgue measure.
Set
$$
A=C\times[0,1].
$$
Then $A$ is closed, has positive two-dimensional Lebesgue measure, and
contains no nonempty open set.


::: pf-proof

Since both factors are closed, $A$ is closed in $\RR^2$. By the product
measure formula,
$$
m_2(A)=m_1(C)\,m_1([0,1])=m_1(C)>0.
$$
If $A$ contained a nonempty open ball, its projection to the first coordinate
would contain a nonempty open interval lying in $C$, contradicting that
$C$ has empty interior. Hence $A$ contains no nonempty open set.

:::

:::

::: {.pf-step #s1-2}

Let
$$
N=\{x\in\RR^2:f(x)\ne\chi_A(x)\}.
$$
Then $m_2(N)=0$, and
$$
B=A\setminus N
$$
has positive measure.


::: pf-proof

The hypothesis $f=\chi_A$ almost everywhere means exactly that $N$ is null.
Since $m_2(A)>0$,
$$
m_2(B)=m_2(A\setminus N)=m_2(A)>0.
$$
For every $x\in B$ one has
$$
f(x)=\chi_A(x)=1.
$$

:::

:::

::: {.pf-step #s1-3}

Every point of $A$ is a boundary point of $A$.


::: pf-proof

The set $A$ is closed and has empty interior by step [](#s1-1){.pf-ref}. Therefore
$$
\partial A
=A\setminus\operatorname{int}(A)
=A.
$$

:::

:::

::: {.pf-step #s1-4}

For every $x\in B$ and every $r>0$, there is
$$
y\in B_r(x)\setminus A
$$
such that $f(y)=0$.


::: pf-proof

Fix $x\in B\subseteq A$. By step [](#s1-3){.pf-ref}, every ball $B_r(x)$ meets
$\RR^2\setminus A$. Since $A$ is closed, $\RR^2\setminus A$ is
open, so
$$
B_r(x)\cap(\RR^2\setminus A)
$$
is a nonempty open set and therefore has positive Lebesgue measure. The set
$N$ is null by step [](#s1-2){.pf-ref}, so this open set cannot be contained in $N$.
Choose
$$
y\in
B_r(x)\cap(\RR^2\setminus A)\setminus N.
$$
Then
$$
f(y)=\chi_A(y)=0.
$$

:::

:::

::: {.pf-step #s1-5}

The function $f$ is discontinuous at every point of $B$.


::: pf-proof

Fix $x\in B$. By step [](#s1-2){.pf-ref},
$$
f(x)=1.
$$
By step [](#s1-4){.pf-ref}, every neighborhood of $x$ contains a point $y$ with
$f(y)=0$. Hence there are points arbitrarily close to $x$ at which the
function value differs from $f(x)$ by $1$. Therefore $f$ is not continuous
at $x$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} solves part (a). Steps [](#s1-2){.pf-ref} through [](#s1-5){.pf-ref} produce a set
$B$ of positive measure on which every point is a discontinuity of $f$, which
proves part (b).

:::

:::

:::
