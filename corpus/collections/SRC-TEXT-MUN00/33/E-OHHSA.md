---
schema: qual/card@1
id: E-OHHSA
kind: problem
title: A regular space that is not completely regular
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
---

::: {.exercise}

Define a set $X$ as follows.
For each even integer $m$, let $L_m$ denote the line segment $m \times [-1, 0]$ in the plane.
For each odd integer $n$ and each integer $k \geq 2$, let $C_{n,k}$ denote the union of the line segments $(n + 1 - 1/k) \times [-1, 0]$ and $(n - 1 + 1/k) \times [-1, 0]$ and the semicircle

$$
\ts{x \times y \mid (x - n)^2 + y^2 = (1 - 1/k)^2 \text{ and } y \geq 0}
$$

in the plane.
Let $p_{n,k}$ denote the topmost point $n \times (1 - 1/k)$ of this semicircle.
Let $X$ be the union of all the sets $L_m$ and $C_{n,k}$, along with two extra points $a$ and $b$.
Topologize $X$ by taking sets of the following four types as basis elements:

(i) The intersection of $X$ with a horizontal open line segment that contains none of the points $p_{n,k}$.

(ii) A set formed from one of the sets $C_{n,k}$ by deleting finitely many points.

(iii) For each even integer $m$, the union of $\ts{a}$ and the set of points $x \times y$ of $X$ for which $x < m$.

(iv) For each even integer $m$, the union of $\ts{b}$ and the set of points $x \times y$ of $X$ for which $x > m$.

(a) Sketch $X$; show that these sets form a basis for a topology on $X$.

(b) Let $f$ be a continuous real-valued function on $X$.
Show that for any $c$, the set $f^{-1}(c)$ is a $G_\delta$ set in $X$.
(This is true for any space $X$.)
Conclude that the set $S_{n,k}$ consisting of those points $p$ of $C_{n,k}$ for which $f(p) \neq f(p_{n,k})$ is countable.
Choose $d \in [-1, 0]$ so that the line $y = d$ intersects none of the sets $S_{n,k}$.
Show that for $n$ odd,

$$
f((n - 1) \times d) = \lim_{k \to \infty} f(p_{n,k}) = f((n + 1) \times d).
$$

Conclude that $f(a) = f(b)$.

(c) Show that $X$ is regular but not completely regular.
:::

::: {.solution}
(a) The four families cover \(X\): ordinary points of the line segments and semicircles have type-(i) neighborhoods, each top point \(p_{n,k}\) has type-(ii) neighborhoods, and \(a,b\) have type-(iii) and type-(iv) neighborhoods.

We verify the basis-intersection condition. At \(a\), type-(iii) neighborhoods are nested after decreasing the even cutoff; similarly type-(iv) neighborhoods at \(b\). At a top point \(p_{n,k}\), intersecting any two basis neighborhoods containing it can be refined by deleting the union of the two finite exceptional sets from \(C_{n,k}\). At any other point of \(X\), a sufficiently short horizontal open segment avoids all finitely many excluded points and all top points involved, and lies inside the intersection. Intersections involving a type-(iii) or type-(iv) set and an ordinary or type-(ii) neighborhood are handled by shortening the latter within the relevant half-plane. Hence the stated sets form a basis.

(b) For any continuous \(f:X\to\mathbb R\) and \(c\in\mathbb R\),
\[
f^{-1}(c)=\bigcap_{r=1}^\infty f^{-1}((c-1/r,c+1/r)),
\]
so every level set is a \(G_\delta\).

Fix odd \(n\) and \(k\ge2\), and put \(c=f(p_{n,k})\). Since \(f^{-1}(c)\) is a \(G_\delta\) containing \(p_{n,k}\), write it as \(\bigcap_r U_r\) with each \(U_r\) open and containing \(p_{n,k}\). For each \(r\), choose a type-(ii) neighborhood
\[
C_{n,k}\setminus F_r\subset U_r
\]
with \(F_r\) finite. Therefore
\[
S_{n,k}=\{p\in C_{n,k}:f(p)\ne f(p_{n,k})\}
\subset\bigcup_{r=1}^\infty F_r,
\]
so \(S_{n,k}\) is countable.

There are only countably many pairs \((n,k)\), so the set of \(y\)-coordinates of all points in all \(S_{n,k}\) is countable. Choose
\[
d\in[-1,0]
\]
outside this countable set. Then for every odd \(n\) and every \(k\ge2\), the two points
\[
q^-_{n,k}=(n-1+1/k,d),\qquad q^+_{n,k}=(n+1-1/k,d)
\]
lie in \(C_{n,k}\setminus S_{n,k}\). Hence
\[
f(q^-_{n,k})=f(p_{n,k})=f(q^+_{n,k}).
\]
As \(k\to\infty\), the points \(q^-_{n,k}\) converge to \((n-1,d)\) and \(q^+_{n,k}\) converge to \((n+1,d)\): this is immediate from the type-(i) horizontal neighborhoods. Continuity gives
\[
f((n-1,d))=\lim_{k\to\infty}f(p_{n,k})=f((n+1,d)).
\]
Thus the values of \(f\) at all points \((m,d)\) with even \(m\) are equal to one common constant \(c_0\). As \(m\to-\infty\) through even integers, \((m,d)\to a\) by the type-(iii) neighborhood definition; as \(m\to+\infty\), \((m,d)\to b\). Hence
\[
f(a)=c_0=f(b).
\]

(c) We prove regularity by shrinking basis neighborhoods.

- For a type-(i) horizontal segment \(B\) containing \(x\), choose a shorter horizontal segment \(B'\ni x\) whose horizontal closure is still contained in \(B\) and avoids all top points. Then \(\overline{B'}\subset B\).
- If \(x=p_{n,k}\) and \(B=C_{n,k}\setminus F\) is type (ii), then \(p_{n,k}\notin F\). Every point of \(F\) is an ordinary point of \(C_{n,k}\) and is isolated in \(C_{n,k}\) by a sufficiently short horizontal type-(i) neighborhood. Hence \(F\) is open in the subspace \(C_{n,k}\), while \(C_{n,k}\) is closed in \(X\). Therefore \(B=C_{n,k}\setminus F\) is closed in \(X\), so it already has closure contained in itself.
- For a type-(iii) neighborhood
\[
B_m=\{a\}\cup\{(x,y)\in X:x<m\},
\]
choose an even \(m'<m\). Then the closure of \(B_{m'}\) can add only points with first coordinate \(m'\), all of which still lie in \(B_m\). Hence \(\overline{B_{m'}}\subset B_m\). The type-(iv) case at \(b\) is symmetric.

Thus every point and basis neighborhood admit a smaller neighborhood with closure inside the given one, so \(X\) is regular.

It is not completely regular. The points \(a\ne b\) are closed, but part (b) shows that every continuous real-valued function on \(X\) satisfies \(f(a)=f(b)\). Complete regularity would provide a continuous \(f:X\to[0,1]\) separating \(a\) from the closed set \(\{b\}\), impossible. Hence \(X\) is regular but not completely regular.
:::
