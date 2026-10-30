---
schema: qual/card@1
id: P-UCLARA15F-03
kind: problem
title: Locally integrable functions bounded by the $L^p$ quasinorm with $0<p<1$ vanish
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 3 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $f \in L^1_{\mathrm{loc}}(\RR^d)$ be such that for some $0 < p < 1$, we have
$$
\abs{ \int f(x) g(x)\,dx } \leq \left( \int \abs{g(x)}^p\,dx \right)^{\frac{1}{p}},
$$
for all $g \in C_0(\RR^d)$. Show that $f(x) = 0$ a.e. Here $C_0(\RR^d)$ is the space of continuous functions with compact support on $\RR^d$.
:::

::: {.solution}

Fix
$$
0<p<1.
$$

## A compact-set estimate

Let
$$
K\subset\RR^d
$$
be compact.

::: pf

::: {.pf-step #s1-1}

Choose a bounded open set $U$ with
$$
K\subset U
$$
such that both
$$
\boxed{
\int_{U\setminus K}\abs{f(x)}\,dx<\varepsilon}
$$
and
$$
\boxed{
\setmeasure{U\setminus K}<\varepsilon}.
$$


::: pf-proof

Since $f\in L^1_{\mathrm{loc}}$, it is integrable on some bounded neighborhood of $K$, and its integral is absolutely continuous with respect to Lebesgue measure there. By outer regularity of Lebesgue measure, choose bounded open $U\supset K$ with $\setmeasure{U\setminus K}$ as small as desired; then absolute continuity of the integral makes $\int_{U\setminus K}\abs{f}$ small as well.

:::

:::

::: pf-step

By Urysohn's lemma on $\RR^d$, choose
$$
g\in C_c(\RR^d)
$$
such that
$$
0\le g\le1,
\qquad
g=1\text{ on }K,
\qquad
\operatorname{supp}g\subset U.
$$


::: pf-proof

Euclidean space is normal, and $K$ is closed while $U$ is open with $K\subset U$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\abs{
\int_{\RR^d}f(x)g(x)\,dx
-
\int_K f(x)\,dx
}
<
\varepsilon.
$$


::: pf-proof

Since $g=1$ on $K$ and $g=0$ outside $U$,
$$
\begin{aligned}
\abs{
\int fg-\int_K f
}
&=
\abs{
\int_{U\setminus K}
f(x)g(x)\,dx
}\\
&\le
\int_{U\setminus K}\abs{f(x)}\,dx
<
\varepsilon
\end{aligned}
$$
by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

By the hypothesis,
$$
\abs{
\int fg
}
\le
\left(
\int \abs{g}^p
\right)^{1/p}.
$$


::: pf-proof

This is the assumed inequality applied to the test function $g\in C_c(\RR^d)$.

:::

:::

::: {.pf-step #s1-5}

Since
$$
0\le g\le1
$$
and
$$
\operatorname{supp}g\subset U,
$$
$$
\boxed{
\int \abs{g}^p\le \setmeasure{U}}.
$$


::: pf-proof

On $U$,
$$
\abs{g}^p\le1,
$$
and outside $U$, $g=0$.

:::

:::

::: pf-step

Therefore
$$
\abs{
\int_K f
}
\le
\varepsilon+\setmeasure{U}^{1/p}.
$$


::: pf-proof

Use the triangle inequality with steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Since
$$
\setmeasure{U}
\le
\setmeasure{K}+\varepsilon,
$$
$$
\abs{
\int_K f
}
\le
\varepsilon+(\setmeasure{K}+\varepsilon)^{1/p}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\setmeasure{U}=\setmeasure{K}+\setmeasure{U\setminus K}
<
\setmeasure{K}+\varepsilon.
$$

:::

:::

::: {.pf-step #s1-8}

Letting $\varepsilon\downarrow0$,
$$
\boxed{
\abs{
\int_K f(x)\,dx
}
\le
\setmeasure{K}^{1/p}}.
$$


::: pf-proof

The bound in step [](#s1-7){.pf-ref} holds for every positive $\varepsilon$, and the right-hand side converges to $\setmeasure{K}^{1/p}$.

:::

:::

::: pf-step

Partition $Q$ into
$$
N^d
$$
closed subcubes
$$
Q_1,\dots,Q_{N^d}
$$
of side length
$$
s/N.
$$


::: pf-proof

Divide each coordinate interval into $N$ equal pieces and take Cartesian products.

:::

:::

::: {.pf-step #s1-10}

Since the overlaps of distinct subcubes lie in boundaries of measure zero,
$$
\int_Q f
=
\sum_{j=1}^{N^d}
\int_{Q_j}f.
$$


::: pf-proof

The interiors are disjoint and cover $Q$ up to the union of finitely many lower-dimensional faces, which has Lebesgue measure zero.

:::

:::

::: pf-step

Hence
$$
\abs{
\int_Q f
}
\le
\sum_{j=1}^{N^d}
\abs{
\int_{Q_j}f
}.
$$


::: pf-proof

Apply the triangle inequality to step [](#s1-10){.pf-ref}.

:::

:::

::: pf-step

By step [](#s1-8){.pf-ref},
$$
\abs{
\int_{Q_j}f
}
\le
\setmeasure{Q_j}^{1/p}
=
\left(
\frac{s^d}{N^d}
\right)^{1/p}.
$$


::: pf-proof

Each $Q_j$ is compact, and its volume is
$$
(s/N)^d.
$$

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
\boxed{
\abs{
\int_Q f
}
\le
s^{d/p}
N^{d-d/p}}.
$$


::: pf-proof

There are $N^d$ subcubes, so
$$
N^d
\left(
\frac{s^d}{N^d}
\right)^{1/p}
=
s^{d/p}
N^{d(1-1/p)}.
$$

:::

:::

::: {.pf-step #s1-14}

Since $0<p<1$,
$$
\boxed{
d-d/p<0}.
$$


::: pf-proof

Because
$$
1/p>1,
$$
one has
$$
1-1/p<0.
$$
Multiply by $d>0$.

:::

:::

::: {.pf-step #s1-15}

Letting $N\to\infty$ in step [](#s1-13){.pf-ref} gives
$$
\boxed{
\int_Q f(x)\,dx=0}
$$
for every closed cube $Q$.


::: pf-proof

By step [](#s1-14){.pf-ref},
$$
N^{d-d/p}\to0.
$$
The left-hand side is independent of $N$, so its absolute value is bounded by quantities tending to zero.

:::

:::

::: {.pf-step #s1-16}

Since
$$
f\in L^1_{\mathrm{loc}}(\RR^d),
$$
the Lebesgue differentiation theorem gives, for almost every $x$,
$$
\boxed{
f(x)
=
\lim_{r\downarrow0}
\frac1{\setmeasure{Q_r(x)}}
\int_{Q_r(x)}f(y)\,dy},
$$
where $Q_r(x)$ is any family of cubes centered at $x$ with side length tending to zero.


::: pf-proof

This is the Lebesgue differentiation theorem for locally integrable functions, with cubes as the differentiation basis.

:::

:::

::: {.pf-step #s1-17}

Every integral in step [](#s1-16){.pf-ref} is zero.


::: pf-proof

Each $Q_r(x)$ is a closed cube, so step [](#s1-15){.pf-ref} applies.

:::

:::

::: {.pf-step #s1-18}

Therefore
$$
\boxed{
f(x)=0}
$$
for almost every $x\in\RR^d$.


::: pf-proof

At every Lebesgue differentiation point of $f$, steps [](#s1-16){.pf-ref} through [](#s1-17){.pf-ref} give
$$
f(x)=\lim_{r\downarrow0}0=0.
$$
Such points form a full-measure set.

:::

:::

::: pf-qed

Step [](#s1-18){.pf-ref} is the required conclusion.

:::

:::

:::
