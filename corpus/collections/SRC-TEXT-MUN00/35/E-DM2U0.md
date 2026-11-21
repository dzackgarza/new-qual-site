---
schema: qual/card@1
id: E-DM2U0
kind: problem
title: The three-way split in the Tietze theorem proof
classification:
  areas:
  - topology
  topics:
  - Normal Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: dbFin, "Section 35: Problem 2 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-35-the-tietze-extension-theorem/problem-2-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-35-the-tietze-extension-theorem/problem-2-solution.txt), checked
    against Munkres, Topology (2000), Section 35 Exercise 2, printed p. 223, and Step 1 of the proof
    of Theorem 35.1. Its estimate is the card's: the approximating function g satisfies
    |f - g| <= r max{2a, 1-a} = rb, and the iteration converges exactly when b < 1, which for
    0 < a < 1 is equivalent to 0 < a < 1/2. What was corrected: the source leaves the convergence
    conditions as the broken displays "we need to ensure that sum_{k>=0} r a b^k ... or b. This
    means 0 < b < 1 ... or b", so the value of b is never stated as a condition; the card states
    q = max{1-a, 2a} < 1 and reads off the interval. The source's remark that a = 1/3 minimizes b is
    kept in spirit: at a = 1/3, b = 2/3.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the Urysohn step on the two outer preimages,
    the error bound max((1-a)r, 2ar) case by case, the equivalence of q < 1 with a < 1/2,
    and the convergence of the geometric series of corrections. The argument is the card's
    own; no retained set is cited. Two corrections to the earlier prose: the estimate 'a <=
    1-q' used to bound the sum holds only for a <= 1/3, so the sum is clamped to [-r,r] by
    composing with the retraction of R, which fixes the values on A; and the case analysis
    of the error bound is stated for the two outer pieces separately. Munkres §35 Step 1,
    printed pp. 220-221.
---

::: {.exercise}

In the proof of the Tietze theorem, how essential was the clever decision in Step 1 to divide the interval $[-r, r]$ into three equal pieces?
Suppose instead that one divides this interval into the three intervals

$$
I_1 = [-r, -ar], \quad I_2 = [-ar, ar], \quad I_3 = [ar, r],
$$

for some $a$ with $0 < a < 1$.
For what values of $a$ other than $a = 1/3$ (if any) does the proof go through?
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against the proof of the Tietze theorem, Munkres §35 Step 1, in which the interval $[-r,r]$ is cut into the three equal pieces $a=1/3$.

::: pf

::: {.pf-step #construction}
Let $A$ be closed in the normal space $X$ and $f:A\to[-r,r]$ continuous, with $0<a<1$. Put
$$
D_{1}=f^{-1}\big([-r,-ar]\big),\qquad D_{2}=f^{-1}\big([ar,r]\big),
$$
two disjoint closed subsets of $A$, hence of $X$. Urysohn's lemma gives a continuous $g:X\to[-ar,ar]$ with $g=-ar$ on $D_{1}$ and $g=ar$ on $D_{2}$.

::: pf-proof
$D_{1}$ and $D_{2}$ are disjoint, since $0<a$ gives $-ar<ar$ and no point of $[-r,r]$ lies in both intervals. They are closed in $A$, because $f$ is continuous and the two intervals are closed in $\RR$; and $A$ is closed in $X$, so they are closed in $X$. By Urysohn's lemma (§33) applied to the disjoint closed sets $D_{1}$, $D_{2}$ there is a continuous $h:X\to[0,1]$ with $h=0$ on $D_{1}$ and $h=1$ on $D_{2}$, and $g=ar(2h-1)$ then has the stated properties, since $0<a$ and $r>0$.
:::

:::

::: {.pf-step #error}
$\abs{f(x)-g(x)}\le qr$ for all $x\in A$, where $q=\max\{1-a,\,2a\}$.

::: pf-proof
Let $x\in A$. If $x\in D_{1}$ then $f(x)\in[-r,-ar]$ and $g(x)=-ar$, so $f(x)-g(x)=f(x)+ar\in\big[-(1-a)r,\,0\big]$ and the error is at most $(1-a)r$. If $x\in D_{2}$ then $g(x)=ar$ and $f(x)\in[ar,r]$, so $f(x)-g(x)\in\big[0,(1-a)r\big]$ and again the error is at most $(1-a)r$. If $x\in A-(D_{1}\cup D_{2})$ then $f(x)\in(-ar,ar)$ and $g(x)\in[-ar,ar]$, so the error is less than $2ar$. In every case the error is at most $\max\{(1-a)r,\,2ar\}=qr$.
:::

:::

::: {.pf-step #contraction}
$q<1$ if and only if $0<a<\tfrac12$.

::: pf-proof
Since $0<a<1$ one has $0<1-a<1$, so $q<1$ fails exactly when $2a\ge1$, that is exactly when $a\ge\tfrac12$.
:::

:::

::: {.pf-step #iteration}
If $0<a<\tfrac12$ the iterative construction converges, and its limit extends $f$.

::: pf-proof
Write $r_{0}=r$ and $f_{0}=f$, and having defined $f_{n}$ with $\abs{f_{n}}\le r_{n}$ on $A$, apply step [](#construction){.pf-ref} to obtain $g_{n}$ with $\abs{g_{n}}\le ar_{n}$ and $\abs{f_{n}-g_{n}}\le qr_{n}$ on $A$; put $f_{n+1}=f_{n}-g_{n}$ and $r_{n+1}=qr_{n}$. Then $r_{n}=q^{n}r$ and the partial sums $\sum_{n}g_{n}$ converge uniformly on $X$, since $\abs{g_{n}}\le arq^{n}$ and $\sum q^{n}$ converges for $q<1$; let $G$ be their sum. On $A$ the identity $f=\sum_{n=0}^{N}g_{n}+f_{N+1}$ holds, and $\abs{f_{N+1}}\le r_{N+1}=q^{N+1}r\to0$, so $G=f$ on $A$. Finally replace $G$ by its composite $G'$ with the map $t\mapsto\max\{-r,\min\{r,t\}\}$ of $\RR$ onto $[-r,r]$, which is continuous and is the identity on $[-r,r]$; then $G':X\to[-r,r]$ is continuous and $G'=G=f$ on $A$.
:::

:::

::: {.pf-step}
The proof goes through exactly for $0<a<\tfrac12$.

::: pf-proof
Step [](#iteration){.pf-ref} gives the proof for those $a$, by steps [](#error){.pf-ref} and [](#contraction){.pf-ref}. For $a\ge\tfrac12$ the error factor of step [](#error){.pf-ref} satisfies $q\ge1$, so the successive errors $q^{n}r$ do not tend to $0$ and the iterative argument of this proof does not force convergence.
:::

:::

:::
:::
