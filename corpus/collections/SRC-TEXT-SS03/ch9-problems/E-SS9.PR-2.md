---
schema: qual/card@1
id: E-SS9.PR-2
kind: problem
title: Sine series for the Weierstrass elliptic function
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 9, §4, problem 2, together
    with problem 1(b) of the same section, read from
    `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the print. No
    correction to the printed statement is claimed: with $S_2$ as in problem 1(b) and
    $F$ as defined in §1.2 (the same `n then m` order) one gets exactly
    $\wp=S_2-F=\pi^2\sum_m\sin^{-2}(\pi(z+m\tau))-F(\tau)$.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    The single input is the classical expansion $\sum_{n\in\ZZ}(w+n)^{-2}=\pi^2\sin^{-2}(\pi w)$,
    obtained from the book's cotangent formula (Chapter 5, formula (4)) by differentiation. Summing
    it over $m$ reproduces the iterated sum $S_2$ of problem 1(b) minus the excluded term $1/z^2$;
    combining with the definition of $\wp$ and with $F$ in the same order gives the identity. The
    constant $c=-F(\tau)$ is confirmed by the absence of a constant term in $\wp$. Nothing is left
    in outline.
---

::: {.exercise}
Show that
$$
\wp(z)=c+\pi^2\sum_{m=-\infty}^{\infty}
\frac{1}{\sin^2(\pi(z+m\tau))}
$$
for an appropriate constant $c$. In fact, by part (b) of the previous problem, $c=-F(\tau)$, where $F$ is the forbidden Eisenstein series.
:::

::: {.solution}

Let $\Lambda=\{n+m\tau:n,m\in\ZZ\}$, which is a lattice for $\tau\in\HH$, and let
$$
\wp(z)=\frac1{z^2}+\sum_{\omega\in\Lambda\setminus\{0\}}\Bigl(\frac1{(z+\omega)^2}-\frac1{\omega^2}\Bigr)
$$
be the Weierstrass function.

::: pf

::: {.pf-step #s1}

For $w\notin\ZZ$,
$$
\sum_{n\in\ZZ}\frac{1}{(w+n)^2}=\frac{\pi^2}{\sin^2(\pi w)} .
$$

::: pf-proof

The cotangent expansion of Chapter 5, formula (4), is
$$
\pi\cot(\pi w)=\frac1w+\sum_{n\ge1}\frac{2w}{w^2-n^2},
$$
the series converging uniformly on compact subsets of $\CC\setminus\ZZ$. Both sides are holomorphic there, so termwise differentiation gives
$$
-\frac{\pi^2}{\sin^2(\pi w)}=-\frac1{w^2}-\sum_{n\ge1}\frac{2(w^2+n^2)}{(w^2-n^2)^2}=-\sum_{n\in\ZZ}\frac{1}{(w+n)^2},
$$
since $\frac{d}{dw}\frac{2w}{w^2-n^2}=\frac2{w^2-n^2}-\frac{4w^2}{(w^2-n^2)^2}=-\frac{2(w^2+n^2)}{(w^2-n^2)^2}$ and $\frac{2(w^2+n^2)}{(w^2-n^2)^2}=\frac{1}{(w-n)^2}+\frac{1}{(w+n)^2}$. Multiplying by $-1$ gives the identity.

:::

:::

::: {.pf-step #s2}

For fixed $z\notin\Lambda$ and every $m\in\ZZ$, applying step [](#s1){.pf-ref} to $w=z+m\tau\notin\ZZ$ gives
$$
\sum_{n\in\ZZ}\frac{1}{(z+n+m\tau)^2}=\frac{\pi^2}{\sin^2(\pi(z+m\tau))}.
$$

::: pf-proof

$z+m\tau\notin\ZZ$ follows from $z\notin\Lambda$: if $z+m\tau=k\in\ZZ$ then $z=k-m\tau\in\Lambda$. So step [](#s1){.pf-ref} applies verbatim.

:::

:::

::: {.pf-step #s3}

For $z\notin\Lambda$ the series $\displaystyle\pi^2\sum_{m\in\ZZ}\frac{1}{\sin^2(\pi(z+m\tau))}$ converges, locally uniformly away from $\Lambda$, and equals $S_2(z)+\dfrac{1}{z^2}$, where $S_2$ is the iterated sum of problem 1(b), namely $\sum_m\bigl(\sum_n\bigr)$ over $(n,m)\ne(0,0)$.

::: pf-proof

The double sum of problem 1(b) is the iterated sum over all pairs $(n,m)\ne(0,0)$, that is, the sum over $m$ of the full inner sums $\sum_{n\in\ZZ}$ minus the single excluded term, which is the pair $(n,m)=(0,0)$ and contributes $1/z^2$. Hence
$$
S_2(z)=\sum_{m\in\ZZ}\Bigl(\sum_{n\in\ZZ}\frac{1}{(z+n+m\tau)^2}\Bigr)-\frac{1}{z^2}=\pi^2\sum_{m\in\ZZ}\frac{1}{\sin^2(\pi(z+m\tau))}-\frac1{z^2}
$$
by step [](#s2){.pf-ref}.

For convergence: $\abs{\sin(\pi(z+m\tau))}=e^{\pi\abs{m}\operatorname{Im}\tau}\abs{\sin(\pi(z+m\tau))e^{-\pi i m\tau}\operatorname{sgn}m}$ and $\abs{\sin(\pi w)}\ge\frac12e^{\abs{\operatorname{Im}w}\pi}$ for $\abs{\operatorname{Im}w}\ge1$. With $w=z+m\tau$ and $\operatorname{Im}w=\operatorname{Im}z+m\operatorname{Im}\tau$, this grows linearly in $\abs m$, so each term is $O(e^{-2\pi\abs m\operatorname{Im}\tau})$, uniformly for $z$ in a compact set; the series converges locally uniformly.

:::

:::

::: {.pf-step #s4}

$\wp(z)=\pi^2\displaystyle\sum_{m\in\ZZ}\frac{1}{\sin^2(\pi(z+m\tau))}-F(\tau)$, where $F$ is the forbidden Eisenstein series summed in the same order.

::: pf-proof

By definition of $\wp$,
$$
\wp(z)=\frac1{z^2}+\sum_{\omega\in\Lambda\setminus\{0\}}\Bigl(\frac1{(z+\omega)^2}-\frac1{\omega^2}\Bigr)
=\frac1{z^2}+\sum_{\omega\ne0}\frac1{(z+\omega)^2}-\sum_{\omega\ne0}\frac1{\omega^2},
$$
the two series on the right being taken in the same order. The first is $\sum_{(n,m)\ne(0,0)}(z+n+m\tau)^{-2}=S_2(z)$ in the iterated order of problem 1(b), and the second is $F(\tau)$ by the definition of $F$ in §1.2. Hence
$$
\wp(z)=\frac1{z^2}+S_2(z)-F(\tau).
$$
Substituting step [](#s3){.pf-ref}, $S_2(z)=\pi^2\sum_m\sin^{-2}(\pi(z+m\tau))-1/z^2$, the two terms $1/z^2$ cancel and
$$
\wp(z)=\pi^2\sum_{m\in\ZZ}\frac{1}{\sin^2(\pi(z+m\tau))}-F(\tau),
$$
which is the stated identity with $c=-F(\tau)$.

Consistency of the constant: $\wp$ has no constant term in its Laurent expansion at $0$, since $\wp(z)-1/z^2\to0$ as $z\to0$; and the right side has the constant term $\pi^2/3+\pi^2\sum_{m\ne0}\sin^{-2}(\pi m\tau)-F(\tau)$ coming from $\pi^2\sin^{-2}(\pi z)=1/z^2+\pi^2/3+O(z^2)$ and the finitely-behaved terms with $m\ne0$. So $c=-F(\tau)$ is exactly the value that makes the constant terms agree.

:::

:::

:::

:::
