---
schema: qual/card@1
id: P-RVL3K
kind: problem
title: $L^p$ norms tend to $L^\infty$, the converse of dominated convergence, translation
  continuity, and $L^p$ inclusions
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The first part printed f in L^p(X) and the norm of L^p(X) for a set named E; it now reads L^p(E).
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source printed the sequence inclusions as l^2(Z) ⊂ l^1(Z) ⊂ l^∞(Z), which is false, and asked for translation continuity for all p with no integrability hypothesis; the statement now reads l^1(Z) ⊂ l^2(Z) ⊂ l^∞(Z) and assumes f in L^p for finite p.'
---

::: {.problem}

(a) Show that if $E\subseteq \RR^n$ is measurable with $\mu(E) < \infty$ and $f\in L^p(E)$ then
$$
\norm{f}_{L^p(E)} \converges{p\to\infty}\to \norm{f}_\infty.
$$

(b) Is it true that the converse to the DCT holds?
I.e. if $\int f_n \to \int f$, is there a $g\in L^p$ such that $f_n < g$ a.e. for every $n$?

(c) Prove continuity in $L^p$: If $f$ is uniformly continuous, then
$$
\norm{\tau_h f - f}_p \converges{h\to 0}\to 0
$$
for $p = \infty$, and for every $1 \le p < \infty$ with $f \in L^p$.

(d) Prove the following inclusions of $L^p$ spaces for $m(X) < \infty$:
$$
\begin{aligned}
L^\infty(X) &\subset L^2(X) \subset L^1(X), \\
\ell^1(\ZZ) &\subset \ell^2(\ZZ) \subset \ell^\infty(\ZZ).
\end{aligned}
$$

:::

::: {.solution}

::: pf

::: pf-step

If $0 < \mu(E) < \infty$ and $f$ is measurable on $E$, then $\norm{f}_p \to \norm{f}_\infty$ as $p \to \infty$.

::: pf-proof

$\norm{f}_p \le \norm{f}_\infty\,\mu(E)^{1/p}$, so $\limsup_p \norm{f}_p \le \norm{f}_\infty$. If $0 < M < \norm{f}_\infty$, then $\mu\theset{|f| > M} > 0$ and $\norm{f}_p \ge M\,\mu\theset{|f|>M}^{1/p} \to M$, so $\liminf_p \norm{f}_p \ge M$. See [[E-TVBUC]].

:::

:::

::: pf-step

The converse of the dominated convergence theorem fails.

::: pf-proof

On $[0,1]$, $f_n = n\chi_{[1/(n+1),\,1/n)}$ satisfies $f_n \to 0$ pointwise and $\int f_n = \frac{1}{n+1} \to 0$. Any $g$ with $f_n \le g$ a.e. for all $n$ has $g \ge \sup_n f_n$, and $\int (\sup_n f_n)^p = \sum_n \frac{n^{p-1}}{n+1} = \infty$ for $1 \le p < \infty$. See [[E-PUNDP]].

:::

:::

::: pf-step

If $f\colon \RR^n \to \CC$ is uniformly continuous, then $\norm{\tau_h f - f}_\infty \to 0$, and if moreover $f \in L^p$ with $1 \le p < \infty$, then $\norm{\tau_h f - f}_p \to 0$.

::: pf-proof

Let $\tau_h f(x) = f(x - h)$ and $\omega(r) = \sup\theset{|f(x) - f(y)| : |x - y| \le r}$, which tends to $0$ with $r$. Then $\norm{\tau_h f - f}_\infty \le \omega(|h|)$. For $p < \infty$ and $\eps > 0$, choose $R$ with $\int_{|x| > R}|f|^p < \eps$; for $|h| \le 1$, the integral of $|\tau_h f - f|^p$ over $|x| > R + 1$ is less than $2^p\eps$, and over $|x| \le R + 1$ it is at most $\omega(|h|)^p\, m(B(0, R+1))$. See [[E-KO5PK]].

:::

:::

::: pf-step

If $\mu(X) < \infty$, then $L^\infty(X) \subseteq L^2(X) \subseteq L^1(X)$; for counting measure on $\ZZ$, $\ell^1(\ZZ) \subseteq \ell^2(\ZZ) \subseteq \ell^\infty(\ZZ)$.

::: pf-proof

The Cauchy--Schwarz inequality gives $\norm{f}_1 \le \mu(X)^{1/2}\norm{f}_2$, and $\norm{f}_2 \le \mu(X)^{1/2}\norm{f}_\infty$. For sequences, $|a_n| \le \norm{a}_{\ell^2}$ for each $n$, and $\sum|a_n|^2 \le \left(\sup_n|a_n|\right)\sum_n|a_n| \le \norm{a}_{\ell^1}^2$. The sequence $a_n = 1/n$ for $n \ge 1$, $a_n = 0$ otherwise, lies in $\ell^2 \setminus \ell^1$. See [[E-SDQ4U]].

:::

:::

:::

:::

