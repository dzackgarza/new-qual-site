---
schema: qual/card@1
id: P-PRACT20-W6-10
kind: problem
title: Functions not tending to $0$ at infinity despite integrability or vanishing along integer translates
classification:
  areas:
  - prelim
  topics:
  - Improper Integrals
  - Uniform Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 5 of the retained solutions booklet GRE Prep: Miscellaneous
    Practice Problem Solutions by Christian Parkinson
    (assets/attachments/prelim-practice-week6-2020/page-5.png), which prints this
    problem together with a worked solution; the practice sheet itself is not
    retained and the collection's provenance list is empty, so the statement was
    compared with the card from that page: the printed problem asks for continuous f and g on [0, infinity) with (A) a convergent integral but f not tending to 0 and (B) g(t+n) tending to 0 for each fixed t while g does not tend to 0, plus the bonus that neither is possible under uniform continuity; the card states all of this
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The printed solution's construction is transcribed: triangular spikes of height 1 and area 1/(2n^2) at the integers, one function serving for both (A) and (B), with the bonus proved here by a uniform-continuity argument the retained page does not spell out.
---

::: {.problem}
Find continuous functions $f, g : [0, \infty) \to \RR$ such that

(A) $\int_{0}^{\infty} f(x)\, dx$ converges but $f(x) \not\to 0$ as $x \to \infty$,

(B) $\{g(t + n)\}_{n \in \NN}$ converges to zero as $n \to \infty$ for any fixed $t \geq 0$ but $g(x) \not\to 0$ as $x \to \infty$.

Bonus: show that neither of these is possible if we stipulate that $f, g$ are uniformly continuous.
:::

::: {.solution}

Build a single continuous function $f\colon[0,\infty)\to\RR$ carrying spikes
of height $1$ and total area summable, placed at the integers: for $n\ge1$ set
$$
f_n(x)=\begin{cases}2n^2(x-n),&n\le x<n+\tfrac{1}{2n^2},\\ 2n^2\big(n+\tfrac{1}{n^2}-x\big),&n+\tfrac{1}{2n^2}\le x<n+\tfrac{1}{n^2},\\ 0,&\text{otherwise},\end{cases}
\qquad f=\sum_{n\ge1}f_n .
$$

::: pf

::: {.pf-step #welldefined}

Each $f_n$ is continuous with support $[n,n+1/n^2]$ and integral
$\frac{1}{2n^2}$; the sum $f$ is continuous and $\int_0^\infty
f=\sum_n\frac{1}{2n^2}<\infty$.

::: pf-proof

$f_n$ is piecewise linear, vanishes at the endpoints of its support and equals
$1$ at the midpoint $n+\frac{1}{2n^2}$, so it is continuous; being a triangle
of base $\frac{1}{n^2}$ and height $1$, its integral is $\frac{1}{2n^2}$. The
supports are pairwise disjoint except at the endpoints, and near any point
only finitely many $f_n$ are nonzero (the supports escape to infinity), so the
series is a finite sum locally and $f$ is continuous. By monotone convergence
$\int f=\sum_n\int f_n=\sum_n\frac{1}{2n^2}=\frac{\pi^2}{12}<\infty$, so the
improper integral converges.

:::

:::

::: {.pf-step #partA}

(A) holds: $\int_0^\infty f$ converges while $f(x)\not\to0$.

::: pf-proof

The integral is finite by step [](#welldefined){.pf-ref}. But
$f\big(n+\frac{1}{2n^2}\big)=1$ for every $n$, and
$n+\frac{1}{2n^2}\to\infty$, so $f$ does not tend to $0$ at infinity.

:::

:::

::: {.pf-step #partB}

(B) holds for the same $f$: for each fixed $t\ge0$, $f(t+n)\to0$ as
$n\to\infty$.

::: pf-proof

If $t=0$ or $t=1$ then $t+n$ is an integer, where $f$ vanishes (the supports
are $[n,n+1/n^2]$, strictly to the right of $n$), so $f(t+n)=0$ for all $n$.
If $t\in(0,1)$ choose $N$ with $t>\frac{1}{N^2}$; for $n\ge N$ we have
$t+n>n+\frac{1}{n^2}$ when $n\ge N$, so $t+n$ lies beyond the support of $f_n$
and before that of $f_{n+1}$, where $f$ vanishes; hence $f(t+n)=0$ for all
$n\ge N$. So $(f(t+n))_n$ converges to $0$ for every fixed $t\ge0$, while
$f(x)\not\to0$ as $x\to\infty$ by step [](#partA){.pf-ref}.

:::

:::

::: {.pf-step #bonus}

Neither is possible if $f$ is uniformly continuous.

::: pf-proof

Suppose $f$ uniformly continuous and $\int_0^\infty f$ convergent with
$f(x_j)\ge\varepsilon$ along some $x_j\to\infty$. Uniform continuity gives
$\delta>0$ with $\abs{f(x)-f(y)}<\varepsilon/2$ for $\abs{x-y}<\delta$, so
$f>\varepsilon/2$ on each interval $[x_j-\delta,x_j+\delta]$; the intervals
are disjoint for large $j$, and on each the integral of $f$ is at least
$\frac{\varepsilon}{2}\cdot\delta$, so the partial integrals cannot be Cauchy
and the improper integral diverges — contradicting convergence. Hence
$f(x)\to0$. For (B), suppose $g$ uniformly continuous and
$g(x_j)\ge\varepsilon$ with $x_j\to\infty$; write $x_j=t_j+n_j$ with
$t_j\in[0,1)$ and $n_j\in\NN$, and pass to a subsequence with $t_j\to t$. Then
$n_j\to\infty$, so $g(t+n_j)\to0$, while $\abs{g(x_j)-g(t+n_j)}\to0$ by
uniform continuity and $\abs{x_j-(t+n_j)}=\abs{t_j-t}\to0$, a contradiction.
So uniform continuity rules out both examples.

:::

:::

:::


:::
