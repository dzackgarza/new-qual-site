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
  - L¹
  - Limits
  - Convergence of Integrals
  - Counterexamples
  - Uniform Continuity
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

::: {.pf-step #a}

(a) If $\mu(E)<\infty$ and $f$ is measurable on $E$, then $\lim_{p\to\infty}\norm{f}_{L^p(E)}=\norm{f}_{L^\infty(E)}$.

::: pf-proof

Write $\norm{f}_p=\norm{f}_{L^p(E)}$ and $\norm{f}_\infty=\norm{f}_{L^\infty(E)}$.
If $\mu(E)=0$, then $\norm{f}_p=0=\norm{f}_\infty$ for all $p$, so assume $0<\mu(E)<\infty$.

::: {.pf-step #a-upper}

$\limsup_{p\to\infty}\norm{f}_p\le\norm{f}_\infty$.

::: pf-proof

There is nothing to prove if $\norm{f}_\infty=\infty$.
Otherwise $\abs{f}\le\norm{f}_\infty$ almost everywhere on $E$, so
$$
\norm{f}_p=\left(\int_E\abs{f}^p\,d\mu\right)^{1/p}\le\norm{f}_\infty\,\mu(E)^{1/p},
$$
and $\mu(E)^{1/p}\to1$ as $p\to\infty$.

:::

:::

::: {.pf-step #a-level}

If $0<M<\norm{f}_\infty$, then $\liminf_{p\to\infty}\norm{f}_p\ge M$.

::: pf-proof

The set $A_M=\theset{x\in E\st\abs{f(x)}>M}$ has $\mu(A_M)>0$ by the definition of the essential supremum, and $\mu(A_M)\le\mu(E)<\infty$.
Restricting the integral to $A_M$ gives
$$
\norm{f}_p\ge\left(\int_{A_M}\abs{f}^p\,d\mu\right)^{1/p}\ge M\,\mu(A_M)^{1/p},
$$
and $\mu(A_M)^{1/p}\to1$ as $p\to\infty$.

:::

:::

::: {.pf-step #a-lower}

$\liminf_{p\to\infty}\norm{f}_p\ge\norm{f}_\infty$.

::: pf-proof

If $\norm{f}_\infty=0$, the inequality is trivial.
Otherwise step [](#a-level){.pf-ref} applies to every $M$ with $0<M<\norm{f}_\infty$, and the supremum of these $M$ is $\norm{f}_\infty$, finite or infinite.

:::

:::

::: pf-qed

Steps [](#a-upper){.pf-ref} and [](#a-lower){.pf-ref} give $\norm{f}_\infty\le\liminf_p\norm{f}_p\le\limsup_p\norm{f}_p\le\norm{f}_\infty$.

:::

:::

:::

::: pf-step

(b) No. Let $f\equiv0$ and $f_n=n\chi_{[1/(n+1),1/n)}$ on $\RR$ for $n\ge1$. Then $f_n\to f$ pointwise and $\int f_n\to\int f$, but no $g\in L^p$ with $1\le p<\infty$ satisfies $f_n\le g$ a.e. for every $n$.

::: pf-proof

::: pf-step

$f_n\ge0$ and $f_n\to0$ pointwise.

::: pf-proof

For $x\le0$ or $x\ge1$, $f_n(x)=0$ for all $n$. For $0<x<1$, $f_n(x)=0$ once $1/n<x$.

:::

:::

::: pf-step

$\int f_n=n\left(\frac1n-\frac1{n+1}\right)=\frac1{n+1}\to0=\int f$.

::: pf-proof

This is the integral of a constant over an interval of length $\frac1n-\frac1{n+1}$.

:::

:::

::: pf-step

No $g\in L^p$ with $1\le p<\infty$ satisfies $f_n\le g$ a.e. for every $n$.

::: pf-proof

The intervals $[1/(n+1),1/n)$ are pairwise disjoint and $f_n$ is supported on its own interval, so $\sup_nf_n=n$ on $[1/(n+1),1/n)$.
Such a $g$ satisfies $g\ge\sup_nf_n\ge0$ a.e., so
$$
\int g^p\ge\int\left(\sup_nf_n\right)^p=\sum_{n\ge1}n^p\cdot\frac1{n(n+1)}\ge\frac12\sum_{n\ge1}n^{p-2}=\infty.
$$

:::

:::

:::

:::

::: pf-step

(c) If $f\colon\RR^n\to\CC$ is uniformly continuous, then $\norm{\tau_hf-f}_\infty\to0$ as $h\to0$, and if moreover $f\in L^p$ with $1\le p<\infty$, then $\norm{\tau_hf-f}_p\to0$.

::: pf-proof

Let $\tau_hf(x)\coloneqq f(x-h)$ and $\omega(r)\coloneqq\sup\theset{\abs{f(x)-f(y)}:\abs{x-y}\le r}$. Uniform continuity says $\omega(r)\to0$ as $r\to0$.

::: {.pf-step #c-sup}

$\norm{\tau_hf-f}_\infty\le\omega(\abs h)\to0$.

::: pf-proof

$\abs{f(x-h)-f(x)}\le\omega(\abs h)$ for every $x$.

:::

:::

::: pf-step

For $1\le p<\infty$, $\norm{\tau_hf-f}_p\to0$.

::: pf-proof

Fix $\eps>0$ and choose $R$ with $\int_{\abs x>R}\abs f^p<\eps$. Let $\abs h\le1$ and $B=\theset{\abs x\le R+1}$. Off $B$, $\abs{x-h}>R$, so by $\abs{a-b}^p\le2^{p-1}(\abs a^p+\abs b^p)$,
$$
\int_{\RR^n\setminus B}\abs{f(x-h)-f(x)}^p\,dx\le2^{p-1}\left(\int_{\abs y>R}\abs{f(y)}^p\,dy+\int_{\abs x>R}\abs{f(x)}^p\,dx\right)<2^p\eps.
$$
On $B$, step [](#c-sup){.pf-ref} gives $\int_B\abs{f(x-h)-f(x)}^p\,dx\le\omega(\abs h)^p\,m(B)$, which is less than $\eps$ for $\abs h$ small. So $\norm{\tau_hf-f}_p^p<(2^p+1)\eps$ for $\abs h$ small.

:::

:::

:::

:::

::: pf-step

(d) If $m(X)<\infty$, then $L^\infty(X)\subseteq L^2(X)\subseteq L^1(X)$; for counting measure on $\ZZ$, $\ell^1(\ZZ)\subseteq\ell^2(\ZZ)\subseteq\ell^\infty(\ZZ)$. All four inclusions can be strict.

::: pf-proof

::: {.pf-step #d-1}

$\norm{f}_1\le m(X)^{1/2}\norm{f}_2$ for $f\in L^2(X)$.

::: pf-proof

By the Cauchy--Schwarz inequality, $\int\abs f=\int\abs f\cdot1\le\norm{f}_2\norm{1}_2=\norm{f}_2\,m(X)^{1/2}$.

:::

:::

::: {.pf-step #d-2}

$\norm{f}_2\le m(X)^{1/2}\norm{f}_\infty$ for $f\in L^\infty(X)$.

::: pf-proof

$\int\abs f^2\le\norm{f}_\infty^2\,m(X)$.

:::

:::

::: {.pf-step #d-3}

If $\sum_n\abs{a_n}<\infty$, then $\sum_n\abs{a_n}^2<\infty$; if $\sum_n\abs{a_n}^2<\infty$, then $\abs{a_n}\le\norm{a}_2$ for every $n$.

::: pf-proof

The terms of a convergent series tend to $0$, so $\abs{a_n}\le1$ for all but finitely many $n$, and for those $n$, $\abs{a_n}^2\le\abs{a_n}$. For the second claim, $\abs{a_n}^2\le\sum_k\abs{a_k}^2$.

:::

:::

::: {.pf-step #d-4}

The inclusions are strict in general.

::: pf-proof

On $[0,1]$ with Lebesgue measure, $x^{-1/2}\in L^1\setminus L^2$, since $\int_0^1x^{-1/2}\,dx=2$ and $\int_0^1x^{-1}\,dx=\infty$; and $\log x\in L^2\setminus L^\infty$, since $\int_0^1(\log x)^2\,dx=2$ and $\log x$ is unbounded near $0$.
On $\ZZ$, with $a_0=0$, the sequence $a_n=1/\abs n$ lies in $\ell^2\setminus\ell^1$ and $a_n=1/\sqrt{\abs n}$ lies in $\ell^\infty\setminus\ell^2$.

:::

:::

::: pf-qed

Steps [](#d-1){.pf-ref} and [](#d-2){.pf-ref} give the first chain, step [](#d-3){.pf-ref} the second, and step [](#d-4){.pf-ref} strictness.

:::

:::

:::

:::

:::

::: {.remark title="Variations"}
Part (a) is also posed for every measurable $f\colon E\to\CC$, with no hypothesis $f\in L^p(E)$. The proof of (a) uses no such hypothesis, so it applies unchanged.

Part (b) is also posed with the extra hypothesis $f_n\to f$ a.e. The counterexample satisfies it.
:::
