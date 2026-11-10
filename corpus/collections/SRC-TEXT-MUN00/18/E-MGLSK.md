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
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.7, PDF p. 12** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); part (a) and both answers of part (b) are theirs. Whitman, printed pp. 182--183, proves (a) in the same way and proves the two answers of (b) at greater length, with the two lemmas quoted below.

(a) Let $f:\RR\to\RR$ be continuous from the right in the sense that $\lim_{x\to a^{+}}f(x)=f(a)$ for every $a$: for every $a$ and every $\varepsilon>0$ there is $\delta>0$ such that $0<x-a<\delta$ implies $\abs{f(x)-f(a)}<\varepsilon$.

Let $a\in\RR$ and let $V$ be a neighbourhood of $f(a)$ in $\RR$. Choose $\varepsilon>0$ with $(f(a)-\varepsilon,f(a)+\varepsilon)\subset V$, and then $\delta>0$ as above. The set $U=[a,a+\delta)$ is a basis element of $\RR_{\ell}$, hence a neighbourhood of $a$ in $\RR_{\ell}$. For $x\in U$: if $x=a$ then $f(x)=f(a)\in V$; if $x>a$ then $0<x-a<\delta$, so $\abs{f(x)-f(a)}<\varepsilon$ and again $f(x)\in V$. Hence $f(U)\subset V$, and by Theorem 18.1(4) the map $f:\RR_{\ell}\to\RR$ is continuous at $a$; as $a$ was arbitrary, it is continuous.

(b) The two conjectures, both proved below, are: the only continuous maps $\RR\to\RR_{\ell}$ are the constant ones; and a map $f:\RR_{\ell}\to\RR_{\ell}$ is continuous exactly when it is continuous from the right and non-decreasing from the right, that is, for every $x$ and every $\varepsilon>0$ there is $\delta>0$ such that $x\le y<x+\delta$ implies $f(x)\le f(y)<f(x)+\varepsilon$.

*Continuity of $\RR\to\RR_{\ell}$ forces constancy.* Two lemmas. First, every basis element $[a,b)$ of $\RR_{\ell}$ is closed there: its complement is $(-\infty,a)\cup[b,\infty)$, and this is open because
$$
(-\infty,a)=\bigcup_{n\in\ZZ_{+}}[a-n-1,a-n),\qquad [b,\infty)=\bigcup_{n\in\ZZ_{+}}[b+n,b+n+1).
$$
Second, the only subsets of $\RR$ that are both open and closed in the usual topology are $\varnothing$ and $\RR$: if $U$ is nonempty, clopen and not all of $\RR$, take $x\in U$, $y\notin U$, assume $x<y$ and let $A=\{z>x\mid z\notin U\}$ with $a=\inf A$; if $a\in U$ then no interval around $a$ lies in $U$, since it would contain points of $A$; if $a\notin U$ then no interval around $a$ lies in the open set $\RR-U$, since it would contain points of $U$ below $a$; either way a contradiction, and the case $y<x$ is symmetric.

Now let $f:\RR\to\RR_{\ell}$ be continuous and suppose $f(x)\ne f(0)$ for some $x$; say $f(0)<f(x)$. The basis element $B=[f(0),f(x))$ of $\RR_{\ell}$ is open and closed, contains $f(0)$ and not $f(x)$. By continuity $f^{-1}(B)$ is open, and it is closed because $B$ is closed and $f$ is continuous into $\RR_{\ell}$; it contains $0$ and not $x$. This contradicts the second lemma. So $f(x)=f(0)$ for every $x$ and $f$ is constant; constant maps are continuous.

*Characterisation of the continuous maps $\RR_{\ell}\to\RR_{\ell}$.* If $f$ is continuous from the right and non-decreasing from the right, let $x\in\RR$ and let $V$ be a neighbourhood of $f(x)$; choose a basis element $[c,d)$ with $f(x)\in[c,d)\subset V$ and put $\varepsilon=d-f(x)>0$. Take $\delta>0$ as in the condition and $U=[x,x+\delta)$, a neighbourhood of $x$ in $\RR_{\ell}$. For $y\in U$ we have $f(x)\le f(y)<f(x)+\varepsilon=d$ and $f(y)\ge f(x)\ge c$, so $f(y)\in[c,d)\subset V$. So $f$ is continuous at $x$.

Conversely, suppose the condition fails at some $x$ for some $\varepsilon>0$: for every $\delta>0$ there is $y$ with $x\le y<x+\delta$ and either $f(y)<f(x)$ or $\abs{f(y)-f(x)}\ge\varepsilon$. The set $V=[f(x),f(x)+\varepsilon)$ is a basis element of $\RR_{\ell}$ containing $f(x)$. Let $U$ be any neighbourhood of $x$ in $\RR_{\ell}$ and choose a basis element $[a,b)\subset U$ with $x\in[a,b)$; then $\delta=b-x>0$, so there is $y\in[x,b)\subset U$ with $f(y)\notin V$ as above. Hence $f(U)\not\subset V$ for every neighbourhood $U$ of $x$, and $f$ is not continuous at $x$.
:::
