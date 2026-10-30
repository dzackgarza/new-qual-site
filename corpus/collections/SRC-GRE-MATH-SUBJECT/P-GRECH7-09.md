---
schema: qual/card@1
id: P-GRECH7-09
kind: problem
title: Coefficient of $(z-2)^{-1}$ in a Laurent series of $1/(z-5)$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 9 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
What is the coefficient of the $(z-2)^{-1}$ term in the Laurent series for $f(z)=\dfrac{1}{z-5}$ centered at $z=2$?

(A) $81$
(B) $27$
(C) $9$
(D) $3$
(E) $1$
:::

::: {.solution}

Put $w=z-2$, so that
$$
f(z)=\frac1{w-3}.
$$

::: pf

::: {.pf-step #s1-1}

On the disk $\abs{z-2}<3$, the Laurent series centered at $2$ is the Taylor series
$$
f(z)=-\sum_{n=0}^{\infty}\frac{(z-2)^n}{3^{n+1}},
$$
and its $(z-2)^{-1}$ coefficient is $0$.


::: pf-proof

If $\abs{w}<3$, then $\abs{w/3}<1$, so the geometric-series identity gives
$$
\frac1{w-3}
=-\frac13\frac1{1-w/3}
=-\frac13\sum_{n=0}^{\infty}\left(\frac w3\right)^n.
$$
Only nonnegative powers of $w=z-2$ occur, so the coefficient of $(z-2)^{-1}$ is $0$.

:::

:::

::: {.pf-step #s1-2}

On the exterior annulus $\abs{z-2}>3$, the Laurent series centered at $2$ is
$$
f(z)=\sum_{n=0}^{\infty}3^n(z-2)^{-n-1},
$$
whose $(z-2)^{-1}$ coefficient is
$$
\boxed{1}.
$$


::: pf-proof

If $\abs{w}>3$, then $\abs{3/w}<1$, and hence
$$
\frac1{w-3}
=\frac1w\frac1{1-3/w}
=\frac1w\sum_{n=0}^{\infty}\left(\frac3w\right)^n
=\sum_{n=0}^{\infty}3^nw^{-n-1}.
$$
The power $w^{-1}$ occurs exactly for $n=0$, with coefficient $1$.

:::

:::

::: {.pf-step #s1-3}

Therefore the question, as written without an annulus of convergence, does not determine a unique coefficient; under the exterior-Laurent interpretation represented by the answer choices, the answer is (E).


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give two distinct Laurent expansions centered at $2$, on the two maximal annuli separated by the singularity $z=5$, and their $(z-2)^{-1}$ coefficients are respectively $0$ and $1$. Thus the annulus is mathematically necessary. Choice (E) is the value from the exterior expansion in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} records both the mathematical ambiguity and the answer corresponding to the intended exterior expansion.

:::

:::

:::
