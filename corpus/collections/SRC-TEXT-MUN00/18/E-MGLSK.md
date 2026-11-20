---
schema: qual/card@1
id: E-MGLSK
kind: problem
title: Right-continuous functions and the lower limit topology
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 7, printed pp. 111-112, with Theorem
    18.1 and the lower limit topology of §13; both parts are stored as printed, including
    that (b) asks only for a conjecture.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.7, PDF p. 12, for (a) the half-open interval
    [a, a+delta) as the neighbourhood in R_l, and for the two answers of (b): only the
    constant maps R -> R_l are continuous, and f: R_l -> R_l is continuous exactly when it
    is continuous and non-decreasing from the right. The two lemmas behind the first answer
    - that half-open intervals are closed in R_l, and that R has no clopen sets but the
    empty set and R - are proved on the card from Whitman's printed pp. 182-183, whose
    longer proof of (b) they are. (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked every claim against Munkres §18 Exercise 7,
    printed pp. 111-112: (a) the half-open interval [a,a+delta) as the R_l-neighbourhood,
    with Theorem 18.1(4); the two lemmas that half-open intervals are clopen in R_l and that
    R has no clopen subsets but the empty set and R; constancy of a continuous R -> R_l
    through the clopen set [f(0),f(x)); and both implications of the characterisation of the
    continuous maps R_l -> R_l. positron0802, Exercise 18.7, PDF p. 12, for (a) and both
    answers of (b); Whitman, printed pp. 182-183, for the two lemmas. The printed statement
    needed no repair.
---

::: {.exercise}

(a) Suppose that $f: \RR \to \RR$ is "continuous from the right," that is,

$$
\lim_{x \to a^+} f(x) = f(a)
$$

for each $a \in \RR$.
Show that $f$ is continuous when considered as a function from $\RR_\ell$ to $\RR$.

(b) Can you conjecture what functions $f: \RR \to \RR$ are continuous when considered as maps from $\RR$ to $\RR_\ell$?
As maps from $\RR_\ell$ to $\RR_\ell$?
We shall return to this question in Chapter 3.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.7, PDF p. 12** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); part (a) and both answers of (b) are theirs. Whitman, proves (a) in the same way and proves the two answers of (b) at greater length, supplying the two lemmas used below.

Call $f:\RR\to\RR$ **continuous from the right** when $\lim_{x\to a^{+}}f(x)=f(a)$ for every $a$, that is, when for every $a$ and every $\varepsilon>0$ there is $\delta>0$ such that $0<x-a<\delta$ implies $\abs{f(x)-f(a)}<\varepsilon$; and **non-decreasing from the right** when for every $x$ and every $\varepsilon>0$ there is $\delta>0$ such that $x\le y<x+\delta$ implies $f(x)\le f(y)<f(x)+\varepsilon$.

::: pf

::: {.pf-step #part-a}
(a) If $f$ is continuous from the right, then $f:\RR_{\ell}\to\RR$ is continuous.

:::: pf-proof

::: {.pf-step #a-neighbourhood}
At each $a$, for every neighbourhood $V$ of $f(a)$ in $\RR$ there is a neighbourhood $U$ of $a$ in $\RR_{\ell}$ with $f(U)\subset V$.

::: pf-proof
Since $V$ is a neighbourhood of $f(a)$ and the intervals form a basis for $\RR$, there is $\varepsilon>0$ with $(f(a)-\varepsilon,f(a)+\varepsilon)\subset V$. Right continuity gives $\delta>0$ with $\abs{f(x)-f(a)}<\varepsilon$ for $0<x-a<\delta$. Let $U=[a,a+\delta)$, a basis element of $\RR_{\ell}$ and hence a neighbourhood of $a$ in $\RR_{\ell}$. For $x\in U$: if $x=a$ then $f(x)=f(a)\in V$; if $x>a$ then $0<x-a<\delta$, so $\abs{f(x)-f(a)}<\varepsilon$ and $f(x)\in V$. In either case $f(x)\in V$, so $f(U)\subset V$.
:::

:::

::: {.pf-step}
(a) holds.

::: pf-proof
By Theorem 18.1(4), $f:\RR_{\ell}\to\RR$ is continuous at $a$ exactly when for every neighbourhood $V$ of $f(a)$ some neighbourhood $U$ of $a$ satisfies $f(U)\subset V$; step [](#a-neighbourhood){.pf-ref} provides such a $U$ at every $a$, so $f$ is continuous.
:::

:::

:::

:::

::: {.pf-step #clopen-half-open}
Every half-open interval $[a,b)$ is both open and closed in $\RR_{\ell}$.

::: pf-proof
$[a,b)$ is a basis element of $\RR_{\ell}$, hence open. Its complement is $(-\infty,a)\cup[b,\infty)$, and both parts are unions of basis elements:
$$
(-\infty,a)=\bigcup_{n\in\ZZ_{+}}[a-n-1,a-n),\qquad [b,\infty)=\bigcup_{n\in\ZZ_{+}}[b+n,b+n+1).
$$
So the complement is open and $[a,b)$ is closed.
:::

:::

::: {.pf-step #clopen-R}
The only subsets of $\RR$ that are both open and closed in the usual topology are $\varnothing$ and $\RR$.

::: pf-proof
Let $U$ be clopen, nonempty and not all of $\RR$. Choose $x\in U$ and $y\notin U$; by passing to the complement if necessary, and relabelling, assume $x<y$. The set $A=\{z\mid z>x\text{ and }z\notin U\}$ is nonempty, as $y\in A$, and is bounded below by $x$, so $a=\inf A$ exists. If $a\in U$ then, $U$ being open, some $\varepsilon>0$ has $(a-\varepsilon,a+\varepsilon)\subset U$; but $\inf A=a$ gives $z\in A$ with $a\le z<a+\varepsilon$, and such a $z$ lies in $U$, contradicting $z\notin U$. If $a\notin U$ then, $\RR-U$ being open, some $\varepsilon>0$ has $(a-\varepsilon,a+\varepsilon)\subset\RR-U$; since $x\in U$ we have $x\ne a$, so $x<a$, and choosing $z$ with $\max\{x,a-\varepsilon\}<z<a$ gives $z>x$ with $z\notin U$, that is $z\in A$ with $z<a=\inf A$, a contradiction. Both cases are impossible, so no such $U$ exists.
:::

:::

::: {.pf-step #constant}
The only continuous maps $\RR\to\RR_{\ell}$ are the constant ones.

:::: pf-proof

::: {.pf-step #constant-forced}
If $f:\RR\to\RR_{\ell}$ is continuous and $f(x)\ne f(0)$ for some $x$, then a contradiction follows.

::: pf-proof
Assume $f(0)<f(x)$, the other case being symmetric. Put $B=[f(0),f(x))$, a set that contains $f(0)$ and not $f(x)$ and is both open and closed in $\RR_{\ell}$ by step [](#clopen-half-open){.pf-ref}. Then $f^{-1}(B)$ is open in $\RR$, because $B$ is open in $\RR_{\ell}$ and $f$ is continuous, and $f^{-1}(B)$ is closed in $\RR$, because $B$ is closed in $\RR_{\ell}$ and the preimage of a closed set under a continuous map is closed. It contains $0$ and not $x$, so it is a nonempty proper subset of $\RR$ that is both open and closed, which step [](#clopen-R){.pf-ref} excludes.
:::

:::

::: {.pf-step #constant-continuous}
Every constant map $\RR\to\RR_{\ell}$ is continuous, so the continuous maps $\RR\to\RR_{\ell}$ are exactly the constant ones.

::: pf-proof
A constant map is continuous as a map into any space (Theorem 18.2), and step [](#constant-forced){.pf-ref} shows that no nonconstant map $\RR\to\RR_{\ell}$ is continuous.
:::

:::

:::

:::

::: {.pf-step #ell-ell}
A map $f:\RR_{\ell}\to\RR_{\ell}$ is continuous if and only if it is continuous from the right and non-decreasing from the right.

:::: pf-proof

::: {.pf-step #ell-ell-easy}
If $f$ is continuous from the right and non-decreasing from the right, then $f:\RR_{\ell}\to\RR_{\ell}$ is continuous.

::: pf-proof
Let $x\in\RR$ and let $V$ be a neighbourhood of $f(x)$ in $\RR_{\ell}$; choose a basis element $[c,d)$ of $\RR_{\ell}$ with $f(x)\in[c,d)\subset V$, and put $\varepsilon=d-f(x)>0$. Let $\delta>0$ be as in the definition of non-decreasing from the right at $x$, and let $U=[x,x+\delta)$, a neighbourhood of $x$ in $\RR_{\ell}$. For $y\in U$ the condition gives $f(x)\le f(y)<f(x)+\varepsilon=d$, while $c\le f(x)$; hence $f(y)\in[c,d)\subset V$. So $f(U)\subset V$ and $f$ is continuous at $x$ by Theorem 18.1(4).
:::

:::

::: {.pf-step #ell-ell-hard}
If $f:\RR_{\ell}\to\RR_{\ell}$ is continuous, then $f$ is continuous from the right and non-decreasing from the right.

::: pf-proof
Suppose not: at some $x$ and for some $\varepsilon>0$, every $\delta>0$ admits $y$ with $x\le y<x+\delta$ and either $f(y)<f(x)$ or $f(y)\ge f(x)+\varepsilon$. Put $V=[f(x),f(x)+\varepsilon)$, a basis element of $\RR_{\ell}$ containing $f(x)$, hence a neighbourhood of $f(x)$. Let $U$ be any neighbourhood of $x$ in $\RR_{\ell}$ and choose a basis element $[a,b)$ with $x\in[a,b)\subset U$; then $\delta=b-x>0$, so there is $y$ with $x\le y<x+\delta=b$, that is $y\in[a,b)\subset U$, and $f(y)\notin V$. Hence no neighbourhood $U$ of $x$ satisfies $f(U)\subset V$, and $f$ is not continuous at $x$, contrary to hypothesis.
:::

:::

::: {.pf-step}
The characterisation holds.

::: pf-proof
Steps [](#ell-ell-easy){.pf-ref} and [](#ell-ell-hard){.pf-ref} are the two implications.
:::

:::

:::

:::

::: {.pf-step}
Both parts hold: right continuity gives continuity $\RR_{\ell}\to\RR$, and the two conjectures of (b) are that the continuous maps $\RR\to\RR_{\ell}$ are the constant ones and that the continuous maps $\RR_{\ell}\to\RR_{\ell}$ are the maps continuous and non-decreasing from the right.

::: pf-proof
Step [](#part-a){.pf-ref} answers (a); step [](#constant-continuous){.pf-ref} and step [](#ell-ell){.pf-ref} answer the two questions of (b), which ask only for a conjecture in each case.
:::

:::

:::
:::
