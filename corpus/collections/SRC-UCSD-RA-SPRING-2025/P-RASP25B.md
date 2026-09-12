---
schema: qual/card@1
id: P-RASP25B
kind: problem
title: "Atomless probability measure is inner regular on diameter"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Spring 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $\mathcal{B}_{\mathbb{R}^n}$ be the Borel $\sigma$-algebra on $\mathbb{R}^n$ and let $\mu : \mathcal{B}_{\mathbb{R}^n} \to [0, \infty]$ be a measure such that

(1) $\mu(\mathbb{R}^n) = 1$,

(2) $\mu(\{x\}) = 0$ for every $x \in \mathbb{R}^n$.

Prove that for every $\epsilon > 0$ there is $\delta > 0$ such that
$$
\operatorname{diam}(E) = \sup\{|x - y| : x, y \in E\} < \delta \implies \mu(E) < \epsilon.
$$

Hint: Start with $E \subset \overline{B_K(0)}$.
:::

::: solution
Suppose the conclusion were false. Then there would exist
\[
\varepsilon_0>0
\]
such that for every $j\ge1$ one could find a Borel set $E_j\subset\mathbb R^n$ with
\[
\operatorname{diam}(E_j)<\frac1j
\qquad\text{and}\qquad
\mu(E_j)\ge\varepsilon_0.
\]

<1>1. Reduce to sets inside a fixed compact ball.
::: proof
Since
\[
\overline{B_K(0)}\uparrow\mathbb R^n
\]
as $K\to\infty$ and $\mu(\mathbb R^n)=1$, continuity from below gives
\[
\mu(\overline{B_K(0)})\longrightarrow1.
\]
Choose $K$ so large that
\[
\mu(\mathbb R^n\setminus\overline{B_K(0)})<\frac{\varepsilon_0}{2}.
\]
Set
\[
F_j:=E_j\cap\overline{B_K(0)}.
\]
Then
\[
\mu(F_j)
\ge \mu(E_j)-\mu(\mathbb R^n\setminus\overline{B_K(0)})
\ge\frac{\varepsilon_0}{2},
\]
and
\[
\operatorname{diam}(F_j)<\frac1j.
\]
In particular each $F_j$ is nonempty.
:::

<1>2. Extract a limiting point.
::: proof
Choose $x_j\in F_j$. Since all $x_j$ lie in the compact ball $\overline{B_K(0)}$, a subsequence, still denoted $(x_j)$, converges to some
\[
x\in\overline{B_K(0)}.
\]
Fix $r>0$. For all sufficiently large $j$,
\[
|x_j-x|<\frac r2
\qquad\text{and}\qquad
\operatorname{diam}(F_j)<\frac r2.
\]
If $y\in F_j$, then
\[
|y-x|
\le |y-x_j|+|x_j-x|
<r.
\]
Thus
\[
F_j\subset B_r(x)
\]
for all sufficiently large $j$. Hence
\[
\mu(B_r(x))\ge\mu(F_j)\ge\frac{\varepsilon_0}{2}.
\]
:::

<1>3. Obtain the contradiction with atomlessness.
::: proof
Applying Step 2 with $r=1/m$ gives
\[
\mu(B_{1/m}(x))\ge\frac{\varepsilon_0}{2}
\qquad\text{for every }m.
\]
The balls decrease to the singleton $\{x\}$, and the measure is finite. Therefore continuity from above yields
\[
\mu(\{x\})
=\lim_{m\to\infty}\mu(B_{1/m}(x))
\ge\frac{\varepsilon_0}{2}>0,
\]
contradicting hypothesis (2).

Hence for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
\operatorname{diam}(E)<\delta
\quad\Longrightarrow\quad
\boxed{\mu(E)<\varepsilon}.
\]
:::
:::
