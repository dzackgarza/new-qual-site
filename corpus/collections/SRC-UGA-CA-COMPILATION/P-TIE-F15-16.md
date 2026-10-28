---
schema: qual/card@1
id: P-TIE-F15-16
kind: problem
title: Convergence of the iterates $\sum f^n$ of a non-rotation self-map of the disk fixing $0$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 16.
---

::: {.problem}
Assume $f ( z )$ is analytic in D and $f ( 0 ) = 0$ and is not a rotation $( { \mathrm { i . e . ~ } } f ( z ) \neq e ^ { i \theta } z )$ . Show that $\sum _ { n = 1 } ^ { \infty } f ^ { n } ( z )$ converges uniformly to an analytic function on compact subsets of D, where $f ^ { n + 1 } ( z ) = f ( f ^ { n } ( z ) )$
:::

::: {.solution}

The iterates in the statement require the intended hypothesis
$$
f:\DD\to\DD.
$$
For $n\ge1$, write $f^n$ for the $n$-fold iterate.

::: pf

::: {.pf-step #s1-1}

The function
$$
g(z)
\coloneqq
\begin{cases}
f(z)/z,&z\ne0,\\
f'(0),&z=0
\end{cases}
$$
is holomorphic on $\DD$ and satisfies
$$
\abs{g(z)}<1
$$
for every $z\in\DD$.


::: pf-proof

Because $f(0)=0$, the quotient $f(z)/z$ has a removable singularity at $0$, whose extension has value $f'(0)$. Hence $g$ is holomorphic.

Schwarz's lemma gives
$$
\abs{f(z)}\le\abs{z}
$$
for $z\in\DD$, so $\abs{g(z)}\le1$. If equality held at some point of $\DD$, then either $\abs{f'(0)}=1$ or $\abs{f(z)}=\abs{z}$ at a nonzero point. The equality case of Schwarz's lemma would then give
$$
f(z)=e^{i\theta}z
$$
for some real $\theta$, contrary to the hypothesis. Therefore $\abs{g(z)}<1$ everywhere.

:::

:::

::: {.pf-step #s1-2}

For every $0<r<1$, there exists $q_r<1$ such that
$$
\abs{f(z)}\le q_r\abs{z}
$$
whenever $\abs{z}\le r$.


::: pf-proof

The closed disk $\abs{z}\le r$ is compact, and $\abs{g(z)}<1$ there by step [](#s1-1){.pf-ref}. Hence
$$
q_r
\coloneqq
\max_{\abs{z}\le r}\abs{g(z)}
$$
exists and satisfies $q_r<1$. Since $f(z)=zg(z)$, the asserted inequality follows.

:::

:::

::: {.pf-step #s1-3}

If $\abs{z}\le r<1$, then for every $n\ge1$,
$$
\abs{f^n(z)}
\le
q_r^n\abs{z}
\le
r q_r^n.
$$


::: pf-proof

Schwarz's lemma gives
$$
\abs{f(w)}\le\abs{w}
$$
for every $w\in\DD$. Thus if $\abs{z}\le r$, every iterate $f^k(z)$ also lies in the closed disk $\abs{w}\le r$. Step [](#s1-2){.pf-ref} can therefore be applied at every stage:
$$
\abs{f^{k+1}(z)}
\le
q_r\abs{f^k(z)}.
$$
Induction on $n$ yields
$$
\abs{f^n(z)}
\le
q_r^n\abs{z}.
$$

:::

:::

::: {.pf-step #s1-4}

The series
$$
\sum_{n=1}^{\infty}f^n(z)
$$
converges uniformly on every closed disk $\abs{z}\le r<1$.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\abs{f^n(z)}
\le
r q_r^n
$$
uniformly for $\abs{z}\le r$. Since
$$
\sum_{n=1}^{\infty}r q_r^n
$$
is a convergent geometric series, the Weierstrass $M$-test gives uniform convergence on the closed disk.

:::

:::

::: {.pf-step #s1-5}

The series converges uniformly on every compact subset of $\DD$.


::: pf-proof

Let $K\subset\DD$ be compact. Then
$$
r\coloneqq\max_{z\in K}\abs{z}<1,
$$
so $K\subset\{z:\abs{z}\le r\}$. Step [](#s1-4){.pf-ref} gives uniform convergence on that closed disk, hence on $K$.

:::

:::

::: {.pf-step #s1-6}

The sum
$$
\boxed{
F(z)\coloneqq\sum_{n=1}^{\infty}f^n(z)
}
$$
is analytic on $\DD$.


::: pf-proof

Each iterate $f^n$ is holomorphic on $\DD$. By step [](#s1-5){.pf-ref}, the series of holomorphic functions converges locally uniformly on $\DD$. The Weierstrass theorem therefore implies that its sum $F$ is holomorphic.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the required compact-uniform convergence, and step [](#s1-6){.pf-ref} proves that the limit is analytic.

:::

:::

:::
