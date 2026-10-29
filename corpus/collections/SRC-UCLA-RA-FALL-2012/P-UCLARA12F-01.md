---
schema: qual/card@1
id: P-UCLARA12F-01
kind: problem
title: Almost-everywhere convergence plus an Lp bound implies weak convergence
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $1<p<\infty$ and let $(f_n)$ be a sequence of functions $f_n:\RR^3\to\RR$ such that
\[
\limsup_{n\to\infty}\|f_n\|_{L^p}<\infty.
\]
Show that if $f_n$ converges almost everywhere, then $f_n$ converges weakly in $L^p$.
:::

::: {.solution}

Let
$$
f(x)\coloneqq\lim_{n\to\infty}f_n(x)
$$
at points where the limit exists, and define $f$ arbitrarily on the null exceptional set. Let $q=p/(p-1)$.

::: pf

::: pf-step

After discarding finitely many terms, there is a constant $M<\infty$ such that
$$
\|f_n\|_{L^p}\le M
$$
for every remaining $n$.


::: pf-proof

The hypothesis
$$
\limsup_{n\to\infty}\|f_n\|_{L^p}<\infty
$$
implies that the norms are uniformly bounded for all sufficiently large $n$. Removing finitely many initial terms does not affect weak convergence of the sequence.

:::

:::

::: {.pf-step #s1-2}

The pointwise limit $f$ belongs to $L^p(\RR^3)$ and
$$
\|f\|_{L^p}\le M.
$$


::: pf-proof

By Fatou's lemma,
$$
\int_{\RR^3}|f|^p
\le
\liminf_{n\to\infty}
\int_{\RR^3}|f_n|^p
\le M^p.
$$

:::

:::

::: {.pf-step #s1-3}

Fix $g\in L^q(\RR^3)$. The family
$$
\{f_ng:n\ge1\}
$$
is uniformly integrable.


::: pf-proof

Let $E\subseteq\RR^3$ be measurable. Hölder's inequality gives
$$
\int_E|f_ng|
\le
\|f_n\|_{L^p(E)}
\|g\|_{L^q(E)}
\le
M\left(\int_E|g|^q\right)^{1/q}.
$$
Since $|g|^q\in L^1$, the absolute continuity of the Lebesgue integral implies that the right-hand side can be made uniformly small in $n$ by requiring $|E|$ to be sufficiently small. Hence the family is uniformly integrable.

:::

:::

::: {.pf-step #s1-4}

The family $\{f_ng:n\ge1\}$ is tight in $L^1(\RR^3)$.


::: pf-proof

Given $\varepsilon>0$, choose $R>0$ so large that
$$
\left(\int_{\RR^3\setminus B(0,R)}|g|^q\right)^{1/q}
<\frac{\varepsilon}{M+1}.
$$
Then Hölder's inequality gives, uniformly in $n$,
$$
\int_{\RR^3\setminus B(0,R)}|f_ng|
\le
M
\left(\int_{\RR^3\setminus B(0,R)}|g|^q\right)^{1/q}
<\varepsilon.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
\int_{\RR^3} f_n(x)g(x)\,dx
\longrightarrow
\int_{\RR^3} f(x)g(x)\,dx.
$$


::: pf-proof

Since $f_n\to f$ almost everywhere,
$$
f_ng\to fg
$$
almost everywhere. Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} give uniform integrability and tightness of the sequence $(f_ng)$. By the Vitali convergence theorem on $\RR^3$,
$$
\|f_ng-fg\|_{L^1}\to0.
$$
Therefore the integrals converge. The function $fg$ is integrable by Hölder's inequality and step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

The sequence $(f_n)$ converges weakly to $f$ in $L^p(\RR^3)$.


::: pf-proof

Because $1<p<\infty$, the dual of $L^p(\RR^3)$ is $L^q(\RR^3)$. Step [](#s1-5){.pf-ref} proves convergence of the pairing
$$
\langle f_n,g\rangle
=\int f_ng
$$
to $\langle f,g\rangle$ for every $g\in L^q$. This is exactly weak convergence in $L^p$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
