---
schema: qual/card@1
id: P-WESCA16-8
kind: problem
title: 'A triple zero forces at least three nearby preimages'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $f$ be holomorphic with
\[
f(0)=f'(0)=f''(0)=0.
\]
Prove that there is $\varepsilon>0$ such that for every $w\in B_\varepsilon(0)$, the equation
\[
f(z)=w
\]
has at least three zeros counted with multiplicity.
:::

::: {.solution}
<1>1. The statement as printed is false.

::: {.proof}
Take
\[
f(z)\equiv0.
\]
Then
\[
f(0)=f'(0)=f''(0)=0,
\]
but for every nonzero $w$ the equation
\[
f(z)=w
\]
has no solutions. Hence no positive $\varepsilon$ can satisfy the printed
conclusion for this $f$.
:::

<1>2. Assume in addition that $f\not\equiv0$ on the connected component of
its domain containing $0$. Then $0$ is a zero of finite order $m\ge3$.

::: {.proof}
Since $f$ is holomorphic and not identically zero, its Taylor series at $0$
has a first nonzero coefficient. Thus there is an integer $m\ge1$ and a
holomorphic function $g$ near $0$ such that
\[
f(z)=z^m g(z),
\qquad
g(0)\ne0.
\]
The hypotheses
\[
f(0)=f'(0)=f''(0)=0
\]
force the coefficients of $z^0,z^1,z^2$ in the Taylor series to vanish, so
the first possible nonzero coefficient occurs in degree at least $3$.
Therefore $m\ge3$.
:::

<1>3. There is $r>0$ such that $f$ has no zeros on
\[
0<|z|\le r.
\]

::: {.proof}
By step <1>2,
\[
f(z)=z^m g(z)
\]
with $g(0)\ne0$. By continuity of $g$, after shrinking to a sufficiently
small disk one has $g(z)\ne0$. Hence the only zero of $f$ in that disk is
the zero at $0$, of multiplicity $m$. Choose $r>0$ so that the closed disk
$\overline{B_r(0)}$ lies in this neighborhood.
:::

<1>4. Define
\[
\varepsilon=\min_{|z|=r}|f(z)|.
\]
Then $\varepsilon>0$.

::: {.proof}
By step <1>3, $f$ has no zeros on the compact circle $|z|=r$. The continuous
function $|f|$ therefore has a positive minimum on that circle.
:::

<1>5. If $|w|<\varepsilon$, then $f(z)-w$ has exactly $m$ zeros in
$B_r(0)$, counted with multiplicity.

::: {.proof}
On $|z|=r$, step <1>4 gives
\[
|w|<\varepsilon\le |f(z)|.
\]
Thus
\[
|(f(z)-w)-f(z)|=|w|<|f(z)|
\]
on the boundary circle. Rouché's theorem implies that $f-w$ and $f$ have
the same number of zeros in $B_r(0)$, counted with multiplicity. By step
<1>3, $f$ has exactly the single zero $0$ there, with multiplicity $m$.
Hence $f-w$ has exactly $m$ zeros in $B_r(0)$, counted with multiplicity.
:::

<1>6. Under the additional hypothesis $f\not\equiv0$, there is
$\varepsilon>0$ such that every $|w|<\varepsilon$ has at least three
preimages under $f$, counted with multiplicity.

::: {.proof}
By step <1>2, $m\ge3$. Step <1>5 gives exactly $m$ zeros of
\[
f(z)-w
\]
in $B_r(0)$ for every $|w|<\varepsilon$. Therefore there are at least three
zeros counted with multiplicity.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 refutes the literal source statement, and step <1>6 proves the
corrected statement obtained by excluding the identically-zero function.
:::
:::
