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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source did not exclude f identically zero, for which f(z)=w has no solution when w is nonzero; the statement now assumes f is holomorphic on a domain containing 0 and not identically zero.
---

::: {.problem}
Let $f$ be holomorphic on a domain containing $0$, not identically zero, with
$$
f(0)=f'(0)=f''(0)=0.
$$
Prove that there is $\varepsilon>0$ such that for every $w\in B_\varepsilon(0)$, the equation
$$
f(z)=w
$$
has at least three zeros counted with multiplicity.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The point $0$ is a zero of finite order $m\ge3$.


::: pf-proof

Since $f$ is holomorphic and not identically zero, its Taylor series at $0$
has a first nonzero coefficient. Thus there is an integer $m\ge1$ and a
holomorphic function $g$ near $0$ such that
$$
f(z)=z^m g(z),
\qquad
g(0)\ne0.
$$
The hypotheses
$$
f(0)=f'(0)=f''(0)=0
$$
force the coefficients of $z^0,z^1,z^2$ in the Taylor series to vanish, so
the first possible nonzero coefficient occurs in degree at least $3$.
Therefore $m\ge3$.

:::

:::

::: {.pf-step #s1-2}

There is $r>0$ such that $f$ has no zeros on
$$
0<\abs{z}\le r.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
f(z)=z^m g(z)
$$
with $g(0)\ne0$. By continuity of $g$, after shrinking to a sufficiently
small disk one has $g(z)\ne0$. Hence the only zero of $f$ in that disk is
the zero at $0$, of multiplicity $m$. Choose $r>0$ so that the closed disk
$\overline{B_r(0)}$ lies in this neighborhood.

:::

:::

::: {.pf-step #s1-3}

Define
$$
\varepsilon=\min_{\abs{z}=r}\abs{f(z)}.
$$
Then $\varepsilon>0$.


::: pf-proof

By step [](#s1-2){.pf-ref}, $f$ has no zeros on the compact circle $\abs{z}=r$. The continuous
function $\abs{f}$ therefore has a positive minimum on that circle.

:::

:::

::: {.pf-step #s1-4}

If $\abs{w}<\varepsilon$, then $f(z)-w$ has exactly $m$ zeros in
$B_r(0)$, counted with multiplicity.


::: pf-proof

On $\abs{z}=r$, step [](#s1-3){.pf-ref} gives
$$
\abs{w}<\varepsilon\le \abs{f(z)}.
$$
Thus
$$
\abs{(f(z)-w)-f(z)}=\abs{w}<\abs{f(z)}
$$
on the boundary circle. Rouché's theorem implies that $f-w$ and $f$ have
the same number of zeros in $B_r(0)$, counted with multiplicity. By step
[](#s1-2){.pf-ref}, $f$ has exactly the single zero $0$ there, with multiplicity $m$.
Hence $f-w$ has exactly $m$ zeros in $B_r(0)$, counted with multiplicity.

:::

:::

::: {.pf-step #s1-5}

There is
$\varepsilon>0$ such that every $\abs{w}<\varepsilon$ has at least three
preimages under $f$, counted with multiplicity.


::: pf-proof

By step [](#s1-1){.pf-ref}, $m\ge3$. Step [](#s1-4){.pf-ref} gives exactly $m$ zeros of
$$
f(z)-w
$$
in $B_r(0)$ for every $\abs{w}<\varepsilon$. Therefore there are at least three
zeros counted with multiplicity.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the assertion.

:::

:::

:::
