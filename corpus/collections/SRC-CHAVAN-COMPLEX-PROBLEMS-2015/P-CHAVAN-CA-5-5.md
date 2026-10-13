---
schema: qual/card@1
id: P-CHAVAN-CA-5-5
kind: problem
title: The boundary of the image of a relatively compact domain lies in the image of its boundary
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $D\subseteq\mathbb C$ be a domain and let $B\subseteq D$ be open and bounded with
\[
\overline B\subseteq D.
\]
If $f$ is holomorphic on $D$, prove that
\[
\partial(f(B))\subseteq f(\partial B).
\]
Show also that the conclusion can fail when $B$ is unbounded.
:::

::: {.solution}
<1>1. If $B=\varnothing$, then
$$
\partial(f(B))\subseteq f(\partial B).
$$

::: {.proof}
In this case $f(B)=\varnothing$, so its boundary is empty.
:::

<1>2. If $B\neq\varnothing$ and $f$ is constant, then
$$
\partial(f(B))\subseteq f(\partial B).
$$

::: {.proof}
Write $f\equiv c$. Since $B$ is a nonempty bounded open subset of the connected
space $\CC$, its boundary is nonempty. Hence
$$
\partial(f(B))=\partial\{c\}=\{c\}=f(\partial B).
$$
:::

<1>3. Suppose that $B\neq\varnothing$ and $f$ is nonconstant. Then $f(B)$ is
open.

::: {.proof}
Since $D$ is a domain and $f$ is a nonconstant holomorphic function on $D$, the
open mapping theorem says that $f:D\to\CC$ is open. Since $B$ is open in $D$,
$f(B)$ is open in $\CC$.
:::

<1>4. Under the hypotheses of step <1>3, every
$w\in\partial(f(B))$ belongs to $f(\partial B)$.

::: {.proof}
Fix $w\in\partial(f(B))$. Since $w\in\overline{f(B)}$, choose a sequence
$z_n\in B$ such that
$$
f(z_n)\longrightarrow w.
$$
The set $\overline B$ is compact because $B$ is bounded. Passing to a
subsequence, assume $z_n\to z$ for some $z\in\overline B$. Since
$\overline B\subseteq D$ and $f$ is continuous on $D$,
$$
w=\lim_{n\to\infty}f(z_n)=f(z).
$$
If $z\in B$, then $w=f(z)\in f(B)$. This is impossible because step <1>3 shows
that $f(B)$ is open, hence disjoint from its boundary. Therefore
$z\in\overline B\setminus B=\partial B$, and so $w=f(z)\in f(\partial B)$.
:::

<1>5. For bounded $B$,
$$
\partial(f(B))\subseteq f(\partial B).
$$

::: {.proof}
The empty case is step <1>1, the constant case is step <1>2, and the remaining
case is step <1>4.
:::

<1>6. The inclusion can fail for unbounded $B$.

::: {.proof}
Take
$$
D=\CC\setminus\{-1\},
\qquad
B=\{z\in\CC:\operatorname{Re}z>0\},
\qquad
f(z)=\frac{1}{z+1}.
$$
Then $D$ is a domain, $B$ is open and unbounded,
$\overline B\subseteq D$, and $f$ is holomorphic on $D$.

For $w\neq0$, the equation $w=f(z)$ is equivalent to
$z=1/w-1$. Hence
$$
z\in B
\iff
\operatorname{Re}\frac1w>1
\iff
\operatorname{Re}w>\abs{w}^2
\iff
\abs{w-\tfrac12}<\frac12.
$$
Therefore
$$
f(B)=\left\{w\in\CC:\abs{w-\tfrac12}<\frac12\right\},
$$
so $0\in\partial(f(B))$. On the other hand,
$\partial B=i\RR$, and
$$
f(it)=\frac{1}{1+it}\neq0
\qquad(t\in\RR).
$$
Thus $0\notin f(\partial B)$, proving that the inclusion fails.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 proves the bounded case, and step <1>6 gives the requested unbounded
counterexample.
:::
:::
