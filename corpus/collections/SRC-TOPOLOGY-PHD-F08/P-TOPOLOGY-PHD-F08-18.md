---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-18
kind: problem
title: $n$-sheeted coverings of $S^1$ and subgroup index
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part Two, question 6 of the Topology Ph.D. Qualifying Exam
    dated January 17, 2009 in assets/attachments/F08phdtop.pdf. The PDF really
    states that no finite n-sheeted covering of S^1 exists; this conclusion is
    false.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Exhibited p_n(z)=z^n for every n>=1, verified directly that it is an
    n-sheeted covering, and computed its induced subgroup as nZ in Z. Its index
    is n, exactly matching the quoted covering-space theorem.
---

::: {.problem}
It is known that if $p:\widetilde X\to X$ is a covering space and $x_0\in X$ then the cardinality of $p^{-1}(x_0)$ is the index of $p_*\pi_1(\widetilde X,y_0)$ in $\pi_1(X,x_0)$ where $p(y_0)=x_0$.
Use this fact to deduce that there is no $n$-sheeted covering of the circle $S^1$ for any finite $n$.
:::

::: {.solution}
The requested conclusion is false.

<1>1. For every integer $n\ge1$, the map
\[
p_n:S^1\to S^1,
\qquad
p_n(z)=z^n,
\]
is an $n$-sheeted covering map.
::: {.proof}
Fix
\[
w=e^{i\theta_0}\in S^1.
\]
Choose $0<\varepsilon<\pi$ and let
\[
U=\{e^{i\theta}:|\theta-\theta_0|<\varepsilon\},
\]
where the interval is understood through the chosen local argument around $w$.
For $k=0,\ldots,n-1$, define
\[
U_k
=
\left\{
e^{i\phi}:
\left|\phi-\frac{\theta_0+2\pi k}{n}\right|<\frac{\varepsilon}{n}
\right\}.
\]
These are pairwise disjoint open arcs, and
\[
p_n^{-1}(U)=U_0\sqcup\cdots\sqcup U_{n-1}.
\]
On each $U_k$, the map $p_n$ is a homeomorphism onto $U$, with inverse
\[
e^{i\theta}
\longmapsto
e^{i(\theta+2\pi k)/n}
\]
using the same local argument on $U$.
Thus $U$ is evenly covered and has exactly $n$ sheets.
Since $w$ was arbitrary, $p_n$ is an $n$-sheeted covering.
:::

<1>2. Under the standard identification
\[
\pi_1(S^1,1)\cong\mathbb Z,
\]
the induced homomorphism is
\[
(p_n)_*:\mathbb Z\to\mathbb Z,
\qquad
m\longmapsto nm.
\]
::: {.proof}
A generator of $\pi_1(S^1,1)$ is represented by
\[
\alpha(t)=e^{2\pi i t}.
\]
Its image under $p_n$ is
\[
(p_n\circ\alpha)(t)
=e^{2\pi i n t},
\]
which winds $n$ times around the circle and therefore represents $n\in\mathbb Z$.
Since $(p_n)_*$ is a group homomorphism, it sends $m$ to $nm$.
:::

<1>3. Hence
\[
(p_n)_*\pi_1(S^1,1)=n\mathbb Z
\]
and
\[
[\mathbb Z:n\mathbb Z]=n.
\]
::: {.proof}
The image statement follows immediately from <1>2.
The quotient
\[
\mathbb Z/n\mathbb Z
\]
has exactly $n$ elements, so the subgroup $n\mathbb Z$ has index $n$ in $\mathbb Z$.
:::

<1>4. The quoted covering-space fact is therefore consistent with these covers and contradicts the requested conclusion.
::: {.proof}
By <1>1, every fiber of $p_n$ has cardinality $n$.
By <1>3, the induced subgroup has index $n$.
Thus the equality quoted in the problem reads
\[
|p_n^{-1}(1)|
=n
=[\pi_1(S^1):(p_n)_*\pi_1(S^1)].
\]
So the theorem does not rule out finite-sheeted coverings of $S^1$; the maps $p_n(z)=z^n$ provide one for every finite $n\ge1$.
:::
:::
