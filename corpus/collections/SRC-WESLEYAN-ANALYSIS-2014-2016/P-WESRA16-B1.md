---
schema: qual/card@1
id: P-WESRA16-B1
kind: problem
title: 'A summable exceptional-set criterion for almost uniform convergence'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group B, problem B1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $(X,\mathcal M,\mu)$ be a measure space, let $f_n:X\to\RR$ be measurable, and define
$$
M_n=\{x:\abs{f_n(x)}\ge2^{-n}\}.
$$

(a) Define what it means that $f_n\to0$ almost uniformly.

(b) Prove that if $\mu(M_n)\le2^{-n}$ for every $n$, then $f_n\to0$ almost uniformly.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The statement $f_n\to0$ almost uniformly means that for every $\varepsilon>0$ there exists a measurable set $E\subseteq X$ such that
$$
\mu(E)<\varepsilon
$$
and $f_n\to0$ uniformly on $X\setminus E$.


::: pf-proof

This is the definition of almost uniform convergence to zero. Equivalently, for every $\varepsilon>0$ there is such an $E$ for which
$$
\sup_{x\in X\setminus E}\abs{f_n(x)}\longrightarrow0.
$$
This answers part (a).

:::

:::

::: {.pf-step #s1-2}

For $N\ge0$, define
$$
E_N=\bigcup_{n=N}^\infty M_n.
$$
Then
$$
\mu(E_N)\le2^{1-N}.
$$


::: pf-proof

By countable subadditivity and the assumed estimate on $M_n$,
$$
\mu(E_N)
\leq\sum_{n=N}^\infty\mu(M_n)
\leq\sum_{n=N}^\infty2^{-n}
=2^{1-N}.
$$

:::

:::

::: {.pf-step #s1-3}

For every $N$ and every $n\ge N$,
$$
\sup_{x\in X\setminus E_N}\abs{f_n(x)}\leq2^{-n}.
$$


::: pf-proof

If $x\in X\setminus E_N$ and $n\ge N$, then $x\notin M_n$. By the definition of $M_n$,
$$
\abs{f_n(x)}<2^{-n}.
$$
Taking the supremum over $X\setminus E_N$ gives the asserted bound.

:::

:::

::: {.pf-step #s1-4}

If $\mu(M_n)\le2^{-n}$ for every $n$, then
$$
\boxed{f_n\to0\text{ almost uniformly}.}
$$


::: pf-proof

Let $\varepsilon>0$. Choose $N$ so large that
$$
2^{1-N}<\varepsilon.
$$
By step [](#s1-2){.pf-ref}, $\mu(E_N)<\varepsilon$. By step [](#s1-3){.pf-ref},
$$
\sup_{x\in X\setminus E_N}\abs{f_n(x)}
\leq2^{-n}\longrightarrow0
$$
for $n\ge N$. Hence $f_n\to0$ uniformly on $X\setminus E_N$, and therefore almost uniformly by step [](#s1-1){.pf-ref}. This proves part (b).

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition, and step [](#s1-4){.pf-ref} proves the criterion.

:::

:::

:::
