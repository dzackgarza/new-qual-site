---
schema: qual/card@1
id: P-RAF05A
kind: problem
title: "Three applications of major theorems: monotone convergence, Stone-Weierstrass, Baire category"
classification:
  areas:
  - real-analysis
  topics:
  - Monotone Convergence
  - Stone-Weierstrass
  - Baire Category
  - L1 Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Fall 2005 real-analysis qualifying exam. The source prints h_j with domain [a,b], but h_j is evaluated at y in [c,d]; the card corrects that domain to [c,d].
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Prove the following.
Each follows in a straightforward way by applying theorems.
Be sure to name each theorem when you use it.

(a) Let $\{f_j\}$ be a sequence of real-valued functions in $L^1(\mu)$ such that $f_1 \geq f_2 \geq \cdots \geq 0$.
Then $\lim_j \int f_j \, d\mu = \int \lim_j f_j \, d\mu$.

(b) Let $f : [a, b] \times [c, d] \to \mathbb{R}$ be continuous.
Then for all $\varepsilon > 0$ there exists $N > 0$, continuous functions $g_j : [a, b] \to \mathbb{R}$, and continuous functions $h_j : [c, d] \to \mathbb{R}$ such that $\left|f(x, y) - \sum_{j=1}^N g_j(x) h_j(y)\right| < \varepsilon$ for all $(x, y) \in [a, b] \times [c, d]$.

(c) Let $C([0, 1], \mathbb{R})$ be the space of all real-valued functions on $[0, 1]$ with the uniform norm topology.
Suppose that $C([0, 1], \mathbb{R}) = \bigcup_j F_j$ where each $F_j$ is closed.
Then there exists $\varepsilon > 0$, $j_0 \in \mathbb{N}$, and $f_0 \in F_{j_0}$ such that $\sup_{x \in [0,1]} |f(x) - f_0(x)| < \varepsilon \implies f \in F_{j_0}$.
:::

::: solution
<1>1. Prove part (a) by monotone convergence.
::: proof
Since
\[
f_1\ge f_2\ge\cdots\ge0,
\]
the functions
\[
g_j:=f_1-f_j
\]
satisfy
\[
0\le g_1\le g_2\le\cdots
\]
and
\[
g_j\uparrow f_1-f,
\qquad
f:=\lim_{j\to\infty}f_j.
\]
By the Monotone Convergence Theorem,
\[
\int g_j\,d\mu\longrightarrow\int(f_1-f)\,d\mu.
\]
Because $f_1\in L^1(\mu)$,
\[
\int f_j\,d\mu
=\int f_1\,d\mu-\int g_j\,d\mu
\longrightarrow
\int f_1\,d\mu-\int(f_1-f)\,d\mu
=\int f\,d\mu.
\]
Thus
\[
\boxed{\lim_j\int f_j\,d\mu=\int\lim_j f_j\,d\mu.}
\]
:::

<1>2. Prove part (b) by Stone--Weierstrass.
::: proof
Let
\[
K=[a,b]\times[c,d]
\]
and let $\mathcal A$ be the set of finite sums
\[
\sum_{j=1}^N g_j(x)h_j(y),
\qquad
g_j\in C([a,b]),\quad h_j\in C([c,d]).
\]
Then $\mathcal A$ is a subalgebra of $C(K)$ and contains the constants. It also separates points: if
\[
(x_1,y_1)\ne(x_2,y_2),
\]
then either $x_1\ne x_2$, in which case the function $(x,y)\mapsto x$ separates them, or $y_1\ne y_2$, in which case $(x,y)\mapsto y$ does.

By the real Stone--Weierstrass theorem, $\mathcal A$ is uniformly dense in $C(K)$. Hence for every $\varepsilon>0$ there exists
\[
\sum_{j=1}^N g_j(x)h_j(y)\in\mathcal A
\]
such that
\[
\sup_{(x,y)\in K}
\left|f(x,y)-\sum_{j=1}^N g_j(x)h_j(y)\right|<\varepsilon.
\]
This is the required approximation.
:::

<1>3. Prove part (c) by Baire category.
::: proof
The normed space $C([0,1],\mathbb R)$ with the uniform norm is Banach. By hypothesis,
\[
C([0,1],\mathbb R)=\bigcup_{j=1}^\infty F_j
\]
with every $F_j$ closed. The Baire Category Theorem therefore implies that at least one $F_{j_0}$ has nonempty interior.

Hence there exist $f_0\in F_{j_0}$ and $\varepsilon>0$ such that the open ball
\[
B_\infty(f_0,\varepsilon)
=\left\{f:\sup_{x\in[0,1]}|f(x)-f_0(x)|<\varepsilon\right\}
\]
is contained in $F_{j_0}$. Therefore
\[
\sup_{x\in[0,1]}|f(x)-f_0(x)|<\varepsilon
\quad\Longrightarrow\quad
f\in F_{j_0},
\]
as required.
:::
:::
