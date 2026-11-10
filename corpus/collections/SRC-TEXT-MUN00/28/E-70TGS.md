---
schema: qual/card@1
id: E-70TGS
kind: problem
title: Shrinking maps and contractions on compact metric spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §28 Exercise 7, printed p. 181, with Theorem
    26.9, Theorem 27.4 and Theorem 28.2; the four parts and the two hints are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 28.7, PDF pp. 20-21. (b) the intersection of the
    iterated images is a single fixed point, by the extreme value theorem on the diameter;
    (c) x - x^2/2 on [0,1] is shrinking but not a contraction; (d) (x + sqrt(x^2+1))/2 on R
    is shrinking with no fixed point, its difference quotient being 1/2 plus a term of
    modulus below 1/2. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $(X, d)$ be a nonempty metric space.
If $f$ satisfies the condition

$$
d(f(x), f(y)) < d(x, y)
$$

for all $x, y \in X$ with $x \neq y$, then $f$ is called a shrinking map.
If there is a number $\alpha < 1$ such that

$$
d(f(x), f(y)) \leq \alpha d(x, y)
$$

for all $x, y \in X$, then $f$ is called a contraction.
A fixed point of $f$ is a point $x$ such that $f(x) = x$.

(a) If $f$ is a contraction and $X$ is compact, show $f$ has a unique fixed point.
[Hint: Define $f^1 = f$ and $f^{n+1} = f \circ f^n$. Consider the intersection $A$ of the sets $A_n = f^n(X)$.]

(b) Show more generally that if $f$ is a shrinking map and $X$ is compact, then $f$ has a unique fixed point.
[Hint: Let $A$ be as before. Given $x \in A$, choose $x_n$ so that $x = f^{n+1}(x_n)$. If $a$ is the limit of some subsequence of the sequence $y_n = f^n(x_n)$, show that $a \in A$ and $f(a) = x$. Conclude that $A = f(A)$, so that $\operatorname{diam} A = 0$.]

(c) Let $X = [0, 1]$.
Show that $f(x) = x - x^2/2$ maps $X$ into $X$ and is a shrinking map that is not a contraction.
[Hint: Use the mean-value theorem of calculus.]

(d) The result in (a) holds if $X$ is a complete metric space, such as $\RR$; see the exercises of §43. The result in (b) does not: show that the map $f: \RR \to \RR$ given by $f(x) = [x + (x^2 + 1)^{1/2}]/2$ is a shrinking map that is not a contraction and has no fixed point.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 28.7, PDF pp. 20--21** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); parts (b), (c) and (d) are theirs.

(b) *A shrinking map of a compact metric space has a unique fixed point.* Let $f:X\to X$ satisfy $d(f(x),f(y))<d(x,y)$ for $x\ne y$, and put $A_{n}=f^{n}(X)$, $A=\bigcap_{n}A_{n}$. Each $A_{n}$ is compact, hence closed, and $A_{n+1}\subset A_{n}$, so $A\ne\varnothing$ (Theorem 26.9).

$f(A)\subset A$: if $y=f(x)$ with $x\in A$, then $x\in A_{n}$ gives $y\in A_{n+1}\subset A_{n}$ for every $n$, so $y\in A$. $A\subset f(A)$: if $x\in A$, choose $x_{n}$ with $f^{n+1}(x_{n})=x$ and put $y_{n}=f^{n}(x_{n})\in A$; by sequential compactness a subsequence $y_{n_{k}}\to a\in A$, and $f(y_{n})=x$ for all $n$, so continuity gives $f(a)=x$.

$A$ is a single point: otherwise the continuous function $(x,y)\mapsto d(x,y)$ attains a maximum at some $x_{0}\ne y_{0}$ in $A$ (Theorem 27.4), and writing $x_{0}=f(a)$, $y_{0}=f(b)$ with $a,b\in A$ gives $d(x_{0},y_{0})=d(f(a),f(b))<d(a,b)\le d(x_{0},y_{0})$, a contradiction. So $A=\{p\}$ with $f(p)=p$, and a second fixed point $q\ne p$ would give $d(p,q)=d(f(p),f(q))<d(p,q)$.

(c) On $X=[0,1]$, $f(x)=x-x^{2}/2$ satisfies $\abs{f(x)-f(y)}=\abs{x-y}\abs{1-(x+y)/2}<\abs{x-y}$ for $x\ne y$, so it is shrinking; but $\abs{f(x)-f(0)}/\abs{x-0}=1-x/2\to1$ as $x\to0$, so no $\alpha<1$ works: $f$ is not a contraction. (Its fixed point is $0$.)

(d) On $X=\RR$ let $f(x)=\big(x+(x^{2}+1)^{1/2}\big)/2$. For $x\ne y$,
$$
\frac{f(x)-f(y)}{x-y}=\frac12+\frac{x+y}{2\big((x^{2}+1)^{1/2}+(y^{2}+1)^{1/2}\big)},
$$
because $(x^{2}+1)^{1/2}-(y^{2}+1)^{1/2}=(x^{2}-y^{2})/\big((x^{2}+1)^{1/2}+(y^{2}+1)^{1/2}\big)$. Since $\abs{x}<(x^{2}+1)^{1/2}$ and $\abs{y}<(y^{2}+1)^{1/2}$,
$$
\abs{x+y}\le\abs{x}+\abs{y}<(x^{2}+1)^{1/2}+(y^{2}+1)^{1/2},
$$
so the second term has absolute value $<\tfrac12$ and the ratio is $<1$ in absolute value: $f$ is shrinking. It is not a contraction, since the ratio tends to $1$ as $x,y\to+\infty$ with $x\ne y$. And $f$ has no fixed point: $f(x)=x$ forces $(x^{2}+1)^{1/2}=x$, whose square reads $x^{2}+1=x^{2}$.
:::
