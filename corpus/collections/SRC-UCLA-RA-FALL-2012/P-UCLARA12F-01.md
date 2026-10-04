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
Let $1<p<\infty$ and let $(f_n)$ be a sequence of functions $f_n:\mathbb R^3\to\mathbb R$ such that
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

<1>1. After discarding finitely many terms, there is a constant $M<\infty$ such that
$$
\|f_n\|_{L^p}\le M
$$
for every remaining $n$.

::: {.proof}
The hypothesis
$$
\limsup_{n\to\infty}\|f_n\|_{L^p}<\infty
$$
implies that the norms are uniformly bounded for all sufficiently large $n$. Removing finitely many initial terms does not affect weak convergence of the sequence.
:::

<1>2. The pointwise limit $f$ belongs to $L^p(\RR^3)$ and
$$
\|f\|_{L^p}\le M.
$$

::: {.proof}
By Fatou's lemma,
$$
\int_{\RR^3}|f|^p
\le
\liminf_{n\to\infty}
\int_{\RR^3}|f_n|^p
\le M^p.
$$
:::

<1>3. Fix $g\in L^q(\RR^3)$. The family
$$
\{f_ng:n\ge1\}
$$
is uniformly integrable.

::: {.proof}
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

<1>4. The family $\{f_ng:n\ge1\}$ is tight in $L^1(\RR^3)$.

::: {.proof}
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

<1>5. One has
$$
\int_{\RR^3} f_n(x)g(x)\,dx
\longrightarrow
\int_{\RR^3} f(x)g(x)\,dx.
$$

::: {.proof}
Since $f_n\to f$ almost everywhere,
$$
f_ng\to fg
$$
almost everywhere. Steps <1>3 and <1>4 give uniform integrability and tightness of the sequence $(f_ng)$. By the Vitali convergence theorem on $\RR^3$,
$$
\|f_ng-fg\|_{L^1}\to0.
$$
Therefore the integrals converge. The function $fg$ is integrable by Hölder's inequality and step <1>2.
:::

<1>6. The sequence $(f_n)$ converges weakly to $f$ in $L^p(\RR^3)$.

::: {.proof}
Because $1<p<\infty$, the dual of $L^p(\RR^3)$ is $L^q(\RR^3)$. Step <1>5 proves convergence of the pairing
$$
\langle f_n,g\rangle
=\int f_ng
$$
to $\langle f,g\rangle$ for every $g\in L^q$. This is exactly weak convergence in $L^p$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
