---
schema: qual/card@1
id: P-UCLARA18F-01
kind: problem
title: $L^1$ convergence from almost everywhere convergence with weighted $L^1$ and $L^2$ bounds
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Convergence of Integrals
  - Small Tails
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $\{f_n\}$ be a sequence of real-valued Lebesgue measurable functions on $\RR$, and let $f$ be another such function. Assume that

1. $f_n\to f$ Lebesgue almost everywhere;
2. $\displaystyle \int_{\RR}\abs{x}\,\abs{f_n(x)}\,dx\le100$ for all $n$;
3. $\displaystyle \int_{\RR}\abs{f_n(x)}^2\,dx\le100$ for all $n$.

Prove that $f_n\in L^1$ for all $n$, that $f\in L^1$, and that
$$
\norm{f_n-f}_{L^1}\to0.
$$
Also show that neither assumption 2 nor assumption 3 can be omitted while making these deductions.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every $f_n$ lies in $L^1(\RR)$, and
$$
\norm{f_n}_{L^1}\le 10\sqrt2+100
\qquad(n\ge1).
$$


::: pf-proof

Split the integral into $\abs{x}\le1$ and $\abs{x}>1$. By Cauchy--Schwarz and assumption 3,
$$
\int_{\abs{x}\le1}\abs{f_n(x)}\,dx
\le \sqrt2\left(\int_{\abs{x}\le1}\abs{f_n(x)}^2\,dx\right)^{1/2}
\le10\sqrt2.
$$
On $\abs{x}>1$, assumption 2 gives
$$
\int_{\abs{x}>1}\abs{f_n(x)}\,dx
\le\int_{\abs{x}>1}\abs{x}\,\abs{f_n(x)}\,dx
\le100.
$$
Adding the two estimates proves the claim.

:::

:::

::: {.pf-step #s1-2}

The limit $f$ satisfies
$$
\boxed{f\in L^1(\RR)},
\qquad
\int_{\RR}\abs{f}^2\,dx\le100,
\qquad
\int_{\RR}\abs{x}\,\abs{f(x)}\,dx\le100.
$$


::: pf-proof

By assumption 1, the nonnegative functions $\abs{f_n}$, $\abs{f_n}^2$, and $\abs{x}\,\abs{f_n}$ converge almost everywhere to $\abs{f}$, $\abs{f}^2$, and $\abs{x}\,\abs{f}$, respectively. Applying [[T-LDJNS|Fatou's lemma]] and using step [](#s1-1){.pf-ref} and assumptions 2--3 gives
$$
\int\abs{f}\le\liminf_n\int\abs{f_n}\le10\sqrt2+100,
$$
$$
\int\abs{f}^2\le\liminf_n\int\abs{f_n}^2\le100,
\qquad
\int\abs{x}\,\abs{f}\le\liminf_n\int\abs{x}\,\abs{f_n}\le100.
$$

:::

:::

::: {.pf-step #s1-3}

For every $R>0$ and every $n$,
$$
\int_{\abs{x}>R}\abs{f_n-f}\,dx\le\frac{200}{R}.
$$


::: pf-proof

By assumption 2 and step [](#s1-2){.pf-ref},
$$
\begin{aligned}
\int_{\abs{x}>R}\abs{f_n-f}\,dx
&\le\int_{\abs{x}>R}\abs{f_n}\,dx+\int_{\abs{x}>R}\abs{f}\,dx\\
&\le\frac1R\int \abs{x}\,\abs{f_n(x)}\,dx
 +\frac1R\int \abs{x}\,\abs{f(x)}\,dx\\
&\le\frac{200}{R}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Fix $R>0$. For every $\delta>0$ there is a measurable set $E\subseteq[-R,R]$ with $m(E)<\delta$ such that $f_n\to f$ uniformly on $[-R,R]\setminus E$, and for every $n$,
$$
\int_E\abs{f_n-f}\,dx\le20\sqrt\delta.
$$


::: pf-proof

By [[FT-OGS76|Egorov's theorem]], such an $E$ may be chosen because $[-R,R]$ has finite measure and $f_n\to f$ almost everywhere there. By Cauchy--Schwarz, assumption 3, and step [](#s1-2){.pf-ref},
$$
\begin{aligned}
\int_E\abs{f_n-f}\,dx
&\le m(E)^{1/2}\norm{f_n-f}_{L^2}\\
&\le\sqrt\delta\bigl(\norm{f_n}_{L^2}+\norm{f}_{L^2}\bigr)\\
&\le20\sqrt\delta.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{\norm{f_n-f}_{L^1}\longrightarrow0}.
$$


::: pf-proof

Let $\varepsilon>0$. Choose $R$ so large that $200/R<\varepsilon/3$, and then choose $\delta>0$ so small that $20\sqrt\delta<\varepsilon/3$. Take $E$ from step [](#s1-4){.pf-ref}. Uniform convergence on $[-R,R]\setminus E$ gives an $N$ such that, for $n\ge N$,
$$
\sup_{[-R,R]\setminus E}\abs{f_n-f}<\frac{\varepsilon}{6R}.
$$
Hence, by steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref},
$$
\begin{aligned}
\norm{f_n-f}_{L^1}
&\le \int_{\abs{x}>R}\abs{f_n-f}
 +\int_E\abs{f_n-f}
 +\int_{[-R,R]\setminus E}\abs{f_n-f}\\
&<\frac\varepsilon3+\frac\varepsilon3
 +(2R)\frac{\varepsilon}{6R}
=\varepsilon.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

Assumption 2 cannot be omitted.


::: pf-proof

Set
$$
f_n(x)=f(x)=\frac{1}{1+\abs{x}}
\qquad(n\ge1).
$$
Then $f_n\to f$ everywhere and
$$
\int_{\RR}\abs{f_n(x)}^2\,dx
=2\int_0^\infty\frac{dx}{(1+x)^2}=2\le100,
$$
so assumptions 1 and 3 hold. However,
$$
\int_{\RR}\abs{f_n(x)}\,dx
=2\int_0^\infty\frac{dx}{1+x}=\infty.
$$
Thus even the conclusion $f_n\in L^1$ can fail without assumption 2.

:::

:::

::: {.pf-step #s1-7}

Assumption 3 cannot be omitted.


::: pf-proof

Define, for every $n$,
$$
f_n(x)=f(x)=
\begin{cases}
\abs{x}^{-1},&0<\abs{x}<1,\\
0,&\text{otherwise}.
\end{cases}
$$
Then $f_n\to f$ everywhere and
$$
\int_{\RR}\abs{x}\,\abs{f_n(x)}\,dx
=\int_{-1}^1 1\,dx=2\le100,
$$
so assumptions 1 and 2 hold. But
$$
\int_{\RR}\abs{f_n(x)}\,dx
=2\int_0^1\frac{dx}{x}=\infty.
$$
Thus even the conclusion $f_n\in L^1$ can fail without assumption 3.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} establish all asserted conclusions, while steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref} show that each of assumptions 2 and 3 is indispensable.

:::

:::

:::
