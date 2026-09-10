---
schema: qual/card@1
id: E-XIHWT
kind: problem
title: Distance to a set in a metric space
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $X$ be a metric space with metric $d$; let $A \subset X$ be nonempty.

(a) Show that $d(x, A) = 0$ if and only if $x \in \overline{A}$.

(b) Show that if $A$ is compact, $d(x, A) = d(x, a)$ for some $a \in A$.

(c) Define the $\epsilon$-neighborhood of $A$ in $X$ to be the set

$$
U(A, \epsilon) = \ts{x \mid d(x, A) < \epsilon}.
$$

Show that $U(A, \epsilon)$ equals the union of the open balls $B_d(a, \epsilon)$ for $a \in A$.

(d) Assume that $A$ is compact; let $U$ be an open set containing $A$.
Show that some $\epsilon$-neighborhood of $A$ is contained in $U$.

(e) Show the result in (d) need not hold if $A$ is closed but not compact.
:::

::: {.solution}
Let
\[
d(x,A)=\inf\{d(x,a):a\in A\}.
\]

(a) If \(x\in\overline A\), every \(\varepsilon>0\) ball about \(x\) meets \(A\), so some \(a\in A\) satisfies \(d(x,a)<\varepsilon\). Hence \(d(x,A)=0\). Conversely, if \(d(x,A)=0\), then for every \(\varepsilon>0\) there is \(a\in A\) with \(d(x,a)<\varepsilon\), so every neighborhood of \(x\) meets \(A\). Thus \(x\in\overline A\).

(b) The function \(a\mapsto d(x,a)\) is continuous on compact \(A\), so it attains a minimum at some \(a_0\in A\). Therefore
\[
d(x,A)=d(x,a_0).
\]

(c) We have
\[
x\in U(A,\varepsilon)
\iff d(x,A)<\varepsilon
\iff \exists a\in A:\ d(x,a)<\varepsilon
\iff x\in\bigcup_{a\in A}B(a,\varepsilon).
\]
Hence
\[
U(A,\varepsilon)=\bigcup_{a\in A}B(a,\varepsilon).
\]

(d) If \(U=X\), any \(\varepsilon>0\) works. Otherwise let \(F=X\setminus U\), which is a nonempty closed set disjoint from \(A\). Since \(A\) is compact, the continuous function
\[
a\mapsto d(a,F)
\]
attains a positive minimum \(\delta>0\) on \(A\). Then \(U(A,\delta)\subset U\): if \(x\notin U\), then \(x\in F\), so \(d(x,A)\ge\delta\).

(e) Take \(X=\mathbb R^2\),
\[
A=\{(x,0):x\in\mathbb R\},
\]
which is closed but not compact, and
\[
U=\{(x,y):|y|<1/(1+|x|)\}.
\]
Then \(U\) is open and contains \(A\), but no \(\varepsilon\)-neighborhood of \(A\) lies in \(U\), since for sufficiently large \(|x|\) the vertical width \(1/(1+|x|)\) is smaller than \(\varepsilon\).
:::
