---
schema: qual/card@1
id: P-BERK96S-02
kind: problem
title: Lebesgue number for a ball cover of a compact subset of $\RR^n$
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
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Shrunk a chosen covering ball around each point to a half-margin
    neighborhood, extracted a finite subcover by compactness, and took the
    minimum inner radius; the triangle inequality gives uniform containment.
---

::: {.problem}
Let $K\subset\mathbb R^n$ be compact, and let $\{B_j\}_{j=1}^\infty$ be a sequence of open balls covering $K$. Prove that there is $\varepsilon>0$ such that every open $\varepsilon$-ball centered at a point of $K$ is contained in one of the balls $B_j$.
:::

::: {.solution}
For $x\in\RR^n$ and $r>0$, write
$$
B(x,r)\coloneqq\{y\in\RR^n:\norm{y-x}<r\}.
$$

<1>1. For every $x\in K$, there are an index $j(x)$ and a number
$r_x>0$ such that
$$
B(x,2r_x)\subseteq B_{j(x)}.
$$

::: {.proof}
Because the balls $B_j$ cover $K$, choose $j(x)$ with
$$
x\in B_{j(x)}.
$$
Write
$$
B_{j(x)}=B(c_x,R_x).
$$
Since $x$ lies in this open ball,
$$
d_x\coloneqq R_x-\norm{x-c_x}>0.
$$
Set
$$
r_x\coloneqq\frac{d_x}{2}.
$$
If $y\in B(x,2r_x)$, then by the triangle inequality,
$$
\norm{y-c_x}
\leq
\norm{y-x}+\norm{x-c_x}
<
2r_x+\norm{x-c_x}
=
R_x.
$$
Hence $y\in B_{j(x)}$.
:::

<1>2. There are points $x_1,\ldots,x_N\in K$ such that
$$
K\subseteq\bigcup_{i=1}^N B(x_i,r_{x_i}).
$$

::: {.proof}
The family
$$
\{B(x,r_x):x\in K\}
$$
is an open cover of $K$. Since $K$ is compact, it has a finite subcover.
:::

<1>3. Define
$$
\varepsilon\coloneqq
\min_{1\leq i\leq N}r_{x_i}.
$$
Then
$$
\varepsilon>0.
$$

::: {.proof}
Every $r_{x_i}$ is positive by step <1>1, and the minimum is taken over
finitely many such numbers.
:::

<1>4. For every $y\in K$, the ball $B(y,\varepsilon)$ is contained in
one of the original covering balls $B_j$.

::: {.proof}
By step <1>2, choose $i$ such that
$$
y\in B(x_i,r_{x_i}).
$$
If $z\in B(y,\varepsilon)$, then
$$
\begin{aligned}
\norm{z-x_i}
&\leq
\norm{z-y}+\norm{y-x_i}\\
&<
\varepsilon+r_{x_i}\\
&\leq
2r_{x_i},
\end{aligned}
$$
because $\varepsilon\leq r_{x_i}$ by step <1>3. Thus
$$
z\in B(x_i,2r_{x_i}),
$$
and step <1>1 gives
$$
z\in B_{j(x_i)}.
$$
Therefore
$$
B(y,\varepsilon)\subseteq B_{j(x_i)}.
$$
:::

<1>5. Hence there exists a uniform radius
$$
\boxed{\varepsilon>0}
$$
such that every $\varepsilon$-ball centered at a point of $K$ is
contained in one member of the given cover.

::: {.proof}
Step <1>3 provides a positive $\varepsilon$, and step <1>4 proves the
required containment for every center $y\in K$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is exactly the required conclusion.
:::
:::
