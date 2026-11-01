---
schema: qual/card@1
id: E-SS7.EX-9
kind: problem
title: Zeta estimates on the line of real part one
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta Function
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 7, §3, exercise 9, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, parts (a)--(c); nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    All three. (a) and (b) come from the Euler--Maclaurin form of $\zeta$ with the cut-off
    $N=\lfloor\abs{t}\rfloor$: the sum is bounded by $\sum_{n\le N}n^{-1}$ and by
    $\sum_{n\le N}n^{-1}\log n$, which are $O(\log\abs{t})$ and $O((\log\abs{t})^2)$. (c) is the
    $3$-$4$-$1$ inequality with $\abs{\zeta(\sigma+2it)}\le A\log\abs{t}$ from (a), the mean value
    theorem with (b), and the choice $\sigma-1\asymp(\log\abs{t})^{-9}$, which yields the exponent
    $7$. Nothing is left in outline.
---

::: {.exercise}
Refine the estimates in Proposition 2.7 of Chapter 6 and Proposition 1.6 to show that, for $\abs{t}\geq2$,

(a) $\abs{\zeta(1+it)}\leq A\log\abs{t}$;

(b) $\abs{\zeta'(1+it)}\leq A(\log\abs{t})^2$;

(c) $1/\abs{\zeta(1+it)}\leq A(\log\abs{t})^a$, with $a=7$.
:::

::: {.solution}

Throughout $s=\sigma+it$ with $\abs{t}\ge2$, and $N=\lfloor\abs{t}\rfloor\ge1$.

::: pf

::: {.pf-step #s1}

Euler--Maclaurin form: for $\sigma>0$,
$$
\zeta(s)=\sum_{n\le N}\frac{1}{n^{s}}+\frac{N^{1-s}}{s-1}-s\int_N^{\infty}\frac{\{x\}}{x^{s+1}}\,dx,
\qquad
\zeta'(s)=-\sum_{n\le N}\frac{\log n}{n^{s}}-\frac{N^{1-s}\log N}{s-1}+\frac{N^{1-s}}{(s-1)^2}+R(s),
$$
where $R(s)$ collects the differentiated tail, and $\abs{R(s)}=O\bigl((\log N)/N\bigr)$.

::: pf-proof

Euler--Maclaurin summation (Chapter 6) gives the first display, with $\{x\}=x-\lfloor x\rfloor\in[0,1)$ bounding the integral by $\abs{s}\int_N^\infty x^{-\sigma-1}dx=\abs{s}N^{-\sigma}/\sigma$.

For the derivative, differentiate the identity $\zeta(s)=\sum_{n\le N}n^{-s}+N^{1-s}/(s-1)-s\int_N^\infty\{x\}x^{-s-1}dx$ term by term, which is legitimate because the last integral converges locally uniformly in $s$ for $\sigma\ge\delta>0$ together with its $s$-derivative. The derivative of the integral is
$$
-\int_N^\infty\frac{\{x\}}{x^{s+1}}\,dx+s\int_N^\infty\frac{\{x\}\log x}{x^{s+1}}\,dx,
$$
whose modulus is at most $N^{-\sigma}/\sigma+\abs{s}\int_N^\infty(\log x)x^{-\sigma-1}dx=O\bigl((\log N)/N\bigr)$ for $\sigma$ bounded near $1$.

:::

:::

::: {.pf-step #s2}

Part (a): $\abs{\zeta(1+it)}\le A\log\abs{t}$.

::: pf-proof

Put $\sigma=1$ in step [](#s1){.pf-ref}. Then $\abs{n^{-s}}=n^{-1}$ for each $n$, so
$$
\Bigl|\sum_{n\le N}\frac{1}{n^{s}}\Bigr|\le\sum_{n\le N}\frac1n\le1+\log N\le1+\log\abs{t},
$$
and $\abs{N^{1-s}/(s-1)}=\abs{N^{-it}}/\abs{it}=1/\abs{t}\le1$, while the integral is at most $\abs{s}N^{-1}\le(1+\abs{t})/\abs{t}\le2$. Hence $\abs{\zeta(1+it)}\le\log\abs{t}+O(1)\le A\log\abs{t}$ for $\abs{t}\ge2$.

:::

:::

::: {.pf-step #s3}

Part (b): $\abs{\zeta'(1+it)}\le A(\log\abs{t})^2$.

::: pf-proof

With $\sigma=1$, the first term of $\zeta'$ in step [](#s1){.pf-ref} is bounded by
$$
\sum_{n\le N}\frac{\log n}{n}\le1+\int_1^{N}\frac{\log x}{x}\,dx\le1+\tfrac12(\log N)^2\le\tfrac12(\log\abs{t})^2+1 .
$$
The terms $\dfrac{N^{1-s}\log N}{s-1}$ and $\dfrac{N^{1-s}}{(s-1)^2}$ are bounded by $(\log N)/\abs{t}\le1$ and $1/\abs{t}^2\le1$, and the remainder is $O((\log N)/N)\le O(\log\abs{t})$. Hence $\abs{\zeta'(1+it)}\le\frac12(\log\abs{t})^2+O(\log\abs{t})\le A(\log\abs{t})^2$.

:::

:::

::: {.pf-step #s4}

Part (c): $\abs{\zeta(1+it)}^{-1}\le A(\log\abs{t})^{7}$.

::: pf-proof

First, $\abs{\zeta(\sigma+2it)}\le A'\log\abs{t}$ for $1\le\sigma\le2$: at $\sigma$ close to $1$ it follows from step [](#s2){.pf-ref} applied to the imaginary part $2t$ together with the mean value theorem and step [](#s3){.pf-ref}, and for $\sigma\ge1$ the series bound $\abs{\zeta(\sigma+2it)}\le\zeta(\sigma)\le1+1/(\sigma-1)$ is finite; we only use the region $\sigma\le1+\delta$ with $\delta\le1$, so a single bound $A'\log\abs{t}$ holds there after enlarging $A'$.

By Lemma 1.4 of Chapter 7 (the inequality $3+4\cos\theta+\cos2\theta\ge0$) applied termwise to the Dirichlet series, for $\sigma>1$,
$$
\abs{\zeta(\sigma)}^{3}\,\abs{\zeta(\sigma+it)}^{4}\,\abs{\zeta(\sigma+2it)}\ge1 .
$$
Since $\abs{\zeta(\sigma)}\le\zeta(\sigma)\le1+1/(\sigma-1)\le2/(\sigma-1)$ for $\sigma\in(1,2]$, substitution gives, with $\delta=\sigma-1$,
$$
\abs{\zeta(\sigma+it)}^{4}\ge\frac{1}{\abs{\zeta(\sigma)}^{3}\abs{\zeta(\sigma+2it)}}\ge\frac{\delta^{3}}{8A'\log\abs{t}},
\qquad\text{so}\qquad
\abs{\zeta(\sigma+it)}\ge c\,\frac{\delta^{3/4}}{(\log\abs{t})^{1/4}} .
$$
Also, by the mean value theorem applied on the horizontal segment from $1+it$ to $\sigma+it$ and step [](#s3){.pf-ref},
$$
\abs{\zeta(\sigma+it)-\zeta(1+it)}\le\delta\sup_{1\le u\le\sigma}\abs{\zeta'(u+it)}\le C\delta\,(\log\abs{t})^{2},
$$
where the supremum is estimated as in steps [](#s2){.pf-ref} and [](#s3){.pf-ref} uniformly for $u\in[1,1+\delta]$. Therefore
$$
\abs{\zeta(1+it)}\ge c\,\frac{\delta^{3/4}}{(\log\abs{t})^{1/4}}-C\delta(\log\abs{t})^{2}.
$$
Choose $\delta=c_0(\log\abs{t})^{-9}$ with $c_0=(c/(2C))^{4}$, so that the two terms are equal: $c\delta^{3/4}(\log\abs{t})^{-1/4}=2C\delta(\log\abs{t})^{2}$. Then
$$
\abs{\zeta(1+it)}\ge C\delta(\log\abs{t})^{2}=Cc_0(\log\abs{t})^{-7},
$$
that is $\abs{\zeta(1+it)}^{-1}\le A(\log\abs{t})^{7}$ with $A=(Cc_0)^{-1}$. All this is for $\abs{t}$ large; for $2\le\abs{t}\le T_0$ the function $1/\abs{\zeta(1+it)}$ is continuous and finite, so enlarging $A$ covers those $t$ as well.

:::

:::

:::

:::
