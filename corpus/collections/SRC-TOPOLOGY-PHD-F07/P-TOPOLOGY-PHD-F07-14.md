---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-14
kind: problem
title: Path homotopy and simple connectedness
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part Two, question 2 of the Topology Ph.D. Qualifying Exam
    in assets/attachments/F07phdtop.pdf. The source's converse in part (ii)
    omits path-connectedness; under the standard definition of simply connected
    the literal statement is false.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Proved the path-homotopy criterion using concatenation, cancellation, and
    constant-path identities. For part (ii), proved the forward direction,
    exhibited a two-point discrete counterexample to the literal converse, and
    proved the intended converse after adding path-connectedness.
---

::: {.problem}
(i) Let $X$ be a topological space.
Let $f,g:I\to X$ be two paths from $p$ to $q$.
Show that $f\sim g$, that is, $f$ is homotopic to $g$ if and only if $f\mathbin{\cdot}g^{-1}\sim c_p$ where $g^{-1}$ is the inverse path to $g$, $c_p$ denotes the constant path based at $p$ and the “$\mathbin{\cdot}$” denotes the product of (compatible) paths.

(ii) Show that $X$ is simply connected if and only if any two paths in $X$ with the same initial and terminal points are path homotopic.
:::

::: {.solution}
Throughout, $\simeq_p$ denotes path homotopy relative to the endpoints.

<1>1. Path homotopy is compatible with concatenation, and for every path $\alpha$ from $a$ to $b$ one has
\[
\alpha\mathbin{\cdot}c_b\simeq_p\alpha,
\qquad
c_a\mathbin{\cdot}\alpha\simeq_p\alpha,
\qquad
\alpha\mathbin{\cdot}\alpha^{-1}\simeq_p c_a,
\qquad
\alpha^{-1}\mathbin{\cdot}\alpha\simeq_p c_b,
\]
and concatenation is associative up to path homotopy.
::: {.proof}
If $H$ is a path homotopy from $\alpha_0$ to $\alpha_1$ and $K$ is a path homotopy from $\beta_0$ to $\beta_1$, with the terminal point of each $\alpha_i$ equal to the initial point of each $\beta_i$, then
\[
L(s,t)=
\begin{cases}
H(2s,t),&0\le s\le \frac12,\\
K(2s-1,t),&\frac12\le s\le1
\end{cases}
\]
is a path homotopy
\[
\alpha_0\mathbin{\cdot}\beta_0
\simeq_p
\alpha_1\mathbin{\cdot}\beta_1.
\]
Continuity follows from the pasting lemma because the two formulas agree at $s=1/2$.

For cancellation, the loop $\alpha\mathbin{\cdot}\alpha^{-1}$ contracts through
\[
C(s,t)=
\begin{cases}
\alpha\bigl(2s(1-t)\bigr),&0\le s\le\frac12,\\
\alpha\bigl(2(1-s)(1-t)\bigr),&\frac12\le s\le1.
\end{cases}
\]
At $t=0$ this is $\alpha\mathbin{\cdot}\alpha^{-1}$; at $t=1$ it is constantly $a$; and both endpoints remain $a$ for all $t$.
Applying the same construction to $\alpha^{-1}$ gives
\[
\alpha^{-1}\mathbin{\cdot}\alpha\simeq_p c_b.
\]

The constant-path identities and associativity follow from endpoint-preserving reparametrization.
Indeed, if $r_0,r_1:I\to I$ are continuous nondecreasing maps with
\[
r_0(0)=r_1(0)=0,
\qquad
r_0(1)=r_1(1)=1,
\]
then for any path $\gamma$ the formula
\[
R(s,t)=\gamma\bigl((1-t)r_0(s)+t r_1(s)\bigr)
\]
is a path homotopy between $\gamma\circ r_0$ and $\gamma\circ r_1$.
The paths $\alpha\mathbin{\cdot}c_b$ and $c_a\mathbin{\cdot}\alpha$ are reparametrizations of $\alpha$, while the two parenthesizations of a triple concatenation are reparametrizations of the same path obtained by traversing the three factors successively.
:::

<1>2. If $f\simeq_p g$, then
\[
f\mathbin{\cdot}g^{-1}\simeq_p c_p.
\]
::: {.proof}
By compatibility of path homotopy with concatenation from <1>1,
\[
f\mathbin{\cdot}g^{-1}
\simeq_p
g\mathbin{\cdot}g^{-1}.
\]
The cancellation identity in <1>1 gives
\[
g\mathbin{\cdot}g^{-1}\simeq_p c_p.
\]
By transitivity,
\[
f\mathbin{\cdot}g^{-1}\simeq_p c_p.
\]
:::

<1>3. If
\[
f\mathbin{\cdot}g^{-1}\simeq_p c_p,
\]
then $f\simeq_p g$.
::: {.proof}
Concatenate the assumed homotopy on the right with $g$.
By <1>1,
\[
(f\mathbin{\cdot}g^{-1})\mathbin{\cdot}g
\simeq_p
c_p\mathbin{\cdot}g.
\]
Using associativity, cancellation, and the constant-path identities from <1>1,
\[
\begin{aligned}
(f\mathbin{\cdot}g^{-1})\mathbin{\cdot}g
&\simeq_p f\mathbin{\cdot}(g^{-1}\mathbin{\cdot}g)\\
&\simeq_p f\mathbin{\cdot}c_q\\
&\simeq_p f,
\end{aligned}
\]
while
\[
c_p\mathbin{\cdot}g\simeq_p g.
\]
Hence $f\simeq_p g$.
This proves part (i).
:::

<1>4. Under the standard definition of simply connected, if $X$ is simply connected, then any two paths in $X$ with the same initial and terminal points are path homotopic.
::: {.proof}
Let $f,g:I\to X$ both run from $p$ to $q$.
Then
\[
f\mathbin{\cdot}g^{-1}
\]
is a loop based at $p$.
Since $X$ is simply connected, every based loop is path homotopic to the constant loop, so
\[
f\mathbin{\cdot}g^{-1}\simeq_p c_p.
\]
By <1>3,
\[
f\simeq_p g.
\]
:::

<1>5. The converse in part (ii) is false as literally stated if “simply connected” includes path-connectedness.
::: {.proof}
Let
\[
X=\{0,1\}
\]
with the discrete topology.
Every continuous map
\[
\alpha:I\to X
\]
is constant because $I$ is connected and the image of a connected space is connected, whereas the only connected subsets of a discrete space are singletons.
Consequently, whenever two paths in $X$ have the same initial and terminal points, they are the same constant path and hence are path homotopic.

However, $X$ is not path-connected: there is no path from $0$ to $1$.
Thus $X$ is not simply connected under the standard definition.
So the path-homotopy condition alone does not imply simple connectedness.
:::

<1>6. The intended converse becomes correct after adding the hypothesis that $X$ is path-connected.
::: {.proof}
Assume $X$ is path-connected and that any two paths with the same initial and terminal points are path homotopic.
Fix $p\in X$ and let
\[
\ell:I\to X
\]
be any loop based at $p$.
The loop $\ell$ and the constant loop $c_p$ have the same initial and terminal points, so by hypothesis
\[
\ell\simeq_p c_p.
\]
Hence every loop based at $p$ is null-homotopic, and therefore
\[
\pi_1(X,p)=0.
\]
Together with the assumed path-connectedness, this says that $X$ is simply connected.
:::

<1>7. Thus part (ii) is correct either with path-connectedness included as a hypothesis in the converse, or under the nonstandard convention that “simply connected” means only that every loop is null-homotopic componentwise.
::: {.proof}
The standard forward implication is <1>4, the literal converse fails by <1>5, and the corrected standard converse is <1>6. If one drops path-connectedness from the definition of simply connected, the proof in <1>6 applies within each path component without any additional global hypothesis.
:::
:::
