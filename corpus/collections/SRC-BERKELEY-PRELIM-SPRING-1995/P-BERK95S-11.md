---
schema: qual/card@1
id: P-BERK95S-11
kind: problem
title: Extend an isometry of a finite subset fixing the origin to a linear map
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $S\subset\mathbb R^n$ be finite with $0\in S$. Suppose $\varphi:S\to S$ satisfies
\[
\varphi(0)=0
\]
and
\[
d(\varphi(s),\varphi(t))=d(s,t)
\]
for all $s,t\in S$, where $d$ is the Euclidean metric. Prove that there is a linear map
\[
F:\mathbb R^n\to\mathbb R^n
\]
whose restriction to $S$ is $\varphi$.
:::

::: {.solution}
Write $\langle\cdot,\cdot\rangle$ for the Euclidean inner product.

<1>1. For all $s,t\in S$,
$$
\langle\varphi(s),\varphi(t)\rangle
=
\langle s,t\rangle.
$$

::: {.proof}
Because $\varphi(0)=0$ and distances are preserved,
$$
\norm{\varphi(s)}
=d(\varphi(s),0)
=d(s,0)
=\norm{s}.
$$
Using
$$
2\langle u,v\rangle
=\norm u^2+\norm v^2-\norm{u-v}^2
$$
and the preservation of the distance between $s$ and $t$ gives the
claim.
:::

<1>2. Every linear relation among elements of $S$ is carried to the
same linear relation among their images.

::: {.proof}
Suppose
$$
\sum_{j=1}^r a_js_j=0,
\qquad
s_j\in S.
$$
By step <1>1,
$$
\begin{aligned}
\norm{\sum_{j=1}^r a_j\varphi(s_j)}^2
&=
\sum_{i,j=1}^r
a_i a_j
\langle\varphi(s_i),\varphi(s_j)\rangle\\
&=
\sum_{i,j=1}^r
a_i a_j
\langle s_i,s_j\rangle\\
&=
\norm{\sum_{j=1}^r a_js_j}^2
=0.
\end{aligned}
$$
Hence
$$
\sum_{j=1}^r a_j\varphi(s_j)=0.
$$
:::

<1>3. There is a well-defined linear map
$$
T:\operatorname{span}(S)\longrightarrow\RR^n
$$
such that $T(s)=\varphi(s)$ for every $s\in S$.

::: {.proof}
For
$$
v=\sum_{j=1}^r a_js_j
$$
define
$$
T(v)\coloneqq\sum_{j=1}^r a_j\varphi(s_j).
$$
Step <1>2 shows that two representations of $v$ give the same value,
so $T$ is well-defined. Its linearity is immediate from the
definition.
:::

<1>4. The map $T$ extends to a linear map
$$
F:\RR^n\longrightarrow\RR^n.
$$

::: {.proof}
Choose a complementary subspace
$$
\RR^n=\operatorname{span}(S)\oplus U.
$$
Define
$$
F(v+u)\coloneqq T(v)
\qquad
(v\in\operatorname{span}(S),\ u\in U).
$$
The direct-sum decomposition makes this well-defined and linear. By
step <1>3, for every $s\in S$,
$$
F(s)=T(s)=\varphi(s).
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 provides the required linear extension.
:::
:::
