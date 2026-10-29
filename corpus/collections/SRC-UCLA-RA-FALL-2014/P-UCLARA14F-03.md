---
schema: qual/card@1
id: P-UCLARA14F-03
kind: problem
title: Bounded $L^2$ sequences converging to 0 almost everywhere converge weakly
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
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 3 on page 1 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $(f_n)$ be a bounded sequence in $L^2(\RR)$ and suppose that $f_n \to 0$ Lebesgue almost everywhere. Show that $f_n \to 0$ in the weak topology on $L^2(\RR)$.
:::

::: {.solution}

Let
$$
M=\sup_n\|f_n\|_2<\infty.
$$

::: pf

::: {.pf-step #s1-1}

To prove weak convergence to $0$, it suffices to show that for every
$g\in L^2(\RR)$,
$$
\int_{\RR} f_n(x)g(x)\,dx\longrightarrow0.
$$


::: pf-proof

By the Riesz representation theorem, every bounded linear functional on the
Hilbert space $L^2(\RR)$ has the form
$$
\Lambda_g(f)
=
\int_{\RR}f(x)g(x)\,dx
$$
for some $g\in L^2(\RR)$. Weak convergence is exactly convergence
against all such functionals.

:::

:::

::: {.pf-step #s1-2}

Fix $h\in L^\infty(\RR)$ with compact support. Then
$$
\int_{\RR}f_n h\longrightarrow0.
$$


::: pf-proof

Let
$$
E=\operatorname{supp}(h),
$$
so $m(E)<\infty$, and set
$$
H=\|h\|_\infty.
$$
If $H=0$, the assertion is immediate, so assume $H>0$.

Fix $\varepsilon>0$. Choose $\delta>0$ so that
$$
MH\sqrt{\delta}<\frac{\varepsilon}{2}.
$$
Since $f_n\to0$ almost everywhere on the finite-measure set $E$, Egoroff's
theorem gives a measurable set
$$
A\subseteq E,
\qquad
m(A)<\delta,
$$
such that $f_n\to0$ uniformly on $E\setminus A$.

For the exceptional set, Cauchy--Schwarz gives
$$
\begin{aligned}
\int_A|f_nh|
&\le
\|f_n\|_2\|h\chi_A\|_2\\
&\le
M H\sqrt{m(A)}
<
\frac{\varepsilon}{2}.
\end{aligned}
$$
On $E\setminus A$,
$$
\int_{E\setminus A}|f_nh|
\le
H\,m(E)\,
\sup_{E\setminus A}|f_n|.
$$
The supremum tends to $0$ by uniform convergence, so for all sufficiently
large $n$ this term is less than $\varepsilon/2$. Therefore
$$
\left|\int_{\RR}f_nh\right|
\le
\int_E|f_nh|
<\varepsilon
$$
for all sufficiently large $n$.

:::

:::

::: {.pf-step #s1-3}

The space of bounded compactly supported functions is dense in
$L^2(\RR)$.


::: pf-proof

For $g\in L^2(\RR)$, define
$$
h_k
=
g\,
\chi_{[-k,k]}
\chi_{\{|g|\le k\}}.
$$
Then $h_k$ is bounded by $k$ and supported in $[-k,k]$. Moreover,
$$
|g-h_k|^2
\longrightarrow0
$$
pointwise and is dominated by $|g|^2\in L^1$. By dominated convergence,
$$
\|g-h_k\|_2\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-4}

For every $g\in L^2(\RR)$,
$$
\int_{\RR}f_n g\longrightarrow0.
$$


::: pf-proof

Fix $\varepsilon>0$. If $M=0$, then every $f_n=0$ in $L^2$ and there is
nothing to prove. Assume $M>0$.

By step [](#s1-3){.pf-ref}, choose bounded compactly supported $h$ such that
$$
\|g-h\|_2
<
\frac{\varepsilon}{2M}.
$$
Then
$$
\begin{aligned}
\left|\int f_n g\right|
&\le
\left|\int f_n h\right|
+
\left|\int f_n(g-h)\right|\\
&\le
\left|\int f_n h\right|
+
\|f_n\|_2\|g-h\|_2\\
&<
\left|\int f_n h\right|
+
\frac{\varepsilon}{2}.
\end{aligned}
$$
By step [](#s1-2){.pf-ref}, the first term is less than $\varepsilon/2$ for all sufficiently
large $n$. Hence
$$
\left|\int f_n g\right|<\varepsilon
$$
eventually.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{f_n\rightharpoonup0\text{ in }L^2(\RR)}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} proves convergence against every bounded linear functional described
in step [](#s1-1){.pf-ref}, which is exactly weak convergence.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
