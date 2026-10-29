---
schema: qual/card@1
id: P-UCLARA16S-03
kind: problem
title: Monotonicity under translations by $1/n$ implies monotonicity under all translations
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f\in L^1_{\mathrm{loc}}(\RR)$ be real valued and assume that for each integer $n>0$,
$$
f\!\left(x+\frac1n\right)\ge f(x)
$$
for almost all $x\in\RR$. Show that for each real number $a\ge0$,
$$
f(x+a)\ge f(x)
$$
for almost all $x\in\RR$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every nonnegative rational number $q$,
$$
f(x+q)\ge f(x)
$$
for almost every $x\in\RR$.


::: pf-proof

Write
$$
q=\frac{m}{n}
$$
with integers $m\ge0$ and $n\ge1$. Let $N_n$ be a null set outside of which
$$
f\!\left(x+\frac1n\right)\ge f(x).
$$
For $m>0$, define
$$
E_{m,n}
\coloneqq
\bigcup_{j=0}^{m-1}
\left(N_n-\frac{j}{n}\right).
$$
This is a finite union of translates of null sets, hence is null. If $x\notin E_{m,n}$, then the hypothesis may be applied successively at
$$
x,\quad
x+\frac1n,\quad
\dots,\quad
x+\frac{m-1}{n},
$$
which gives
$$
f\!\left(x+\frac{m}{n}\right)
\ge
f\!\left(x+\frac{m-1}{n}\right)
\ge
\cdots
\ge
f(x).
$$
The case $m=0$ is equality.

:::

:::

::: {.pf-step #s1-2}

If $a\ge0$ and $(q_k)$ is a sequence of nonnegative rationals with $q_k\to a$, then for every compact interval $K\subset\RR$,
$$
f(\cdot+q_k)
\longrightarrow
f(\cdot+a)
\quad\text{in }L^1(K).
$$


::: pf-proof

Choose a compact interval $J$ containing
$$
K+a
\quad\text{and}\quad
K+q_k
$$
for all sufficiently large $k$. Set
$$
F=f\,\mathbf 1_J.
$$
Then $F\in L^1(\RR)$. Continuity of translations in $L^1(\RR)$ gives
$$
\|F(\cdot+q_k-a)-F\|_{L^1(\RR)}
\longrightarrow0.
$$
Indeed, given $\eta>0$, choose $\varphi\in C_c(\RR)$ with
$$
\|F-\varphi\|_1<\eta.
$$
Translations are isometries of $L^1$, while uniform continuity and compact support of $\varphi$ give
$$
\|\varphi(\cdot+h)-\varphi\|_1\longrightarrow0
\qquad
(h\to0).
$$
Therefore
$$
\|F(\cdot+h)-F\|_1
\le
2\eta
+
\|\varphi(\cdot+h)-\varphi\|_1,
$$
and then $h\to0$ followed by $\eta\downarrow0$ proves the asserted translation continuity.

After translating variables, this implies
$$
\|f(\cdot+q_k)-f(\cdot+a)\|_{L^1(K)}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-3}

Fix $a\ge0$. For every compact interval $K\subset\RR$,
$$
f(x+a)-f(x)\ge0
$$
for almost every $x\in K$.


::: pf-proof

Choose nonnegative rationals $q_k\to a$ and define
$$
h_k(x)
\coloneqq
f(x+q_k)-f(x),
\qquad
h(x)
\coloneqq
f(x+a)-f(x).
$$
By step [](#s1-1){.pf-ref},
$$
h_k\ge0
$$
almost everywhere. By step [](#s1-2){.pf-ref},
$$
h_k\longrightarrow h
\quad\text{in }L^1(K).
$$
Let
$$
h_-(x)
\coloneqq
\max\{-h(x),0\}.
$$
Where $h(x)<0$, the inequality $h_k(x)\ge0$ gives
$$
h_-(x)
=
-h(x)
\le
|h(x)-h_k(x)|.
$$
Thus
$$
\|h_-\|_{L^1(K)}
\le
\|h-h_k\|_{L^1(K)}
\longrightarrow0.
$$
Hence $h_-=0$ almost everywhere on $K$, which is equivalent to $h\ge0$ almost everywhere there.

:::

:::

::: {.pf-step #s1-4}

For every real number $a\ge0$,
$$
\boxed{
f(x+a)\ge f(x)
\quad\text{for almost every }x\in\RR
}.
$$


::: pf-proof

Apply step [](#s1-3){.pf-ref} to the compact intervals
$$
[-N,N],
\qquad
N=1,2,\dots.
$$
The exceptional set in each interval is null, and the countable union of these exceptional sets is null. Since the intervals exhaust $\RR$, the stated inequality holds almost everywhere on $\RR$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
