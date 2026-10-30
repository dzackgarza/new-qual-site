---
schema: qual/card@1
id: P-TIE-S15-19
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 19.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source assumes only that f is analytic in the unit disk D with f(0) = 0, so the iterates need not be defined. The statement now assumes f maps D into D.
---

::: {.problem}
Assume $f(z)$ is analytic in $\DD: \abs{z} < 1$, maps $\DD$ into $\DD$, satisfies $f(0) = 0$, and is not a rotation (i.e. $f(z) \neq e^{i\theta} z$). Show that $\sum^{\infty} f^{n}(z)$ converges uniformly to an analytic function on compact subsets of $\DD$, where $f^{n+1}(z) = f(f^{n}(z))$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function
$$
g(z)\coloneqq
\begin{cases}
f(z)/z,&z\ne0,\\
f'(0),&z=0
\end{cases}
$$
is holomorphic on $\DD$ and satisfies $\abs{g(z)}<1$ for every $z\in\DD$.


::: pf-proof

Since $f(0)=0$, the quotient $f(z)/z$ has a removable singularity at $0$, with extended value $f'(0)$. Schwarz's lemma gives $\abs{f(z)}\le\abs{z}$, hence $\abs{g(z)}\le1$. If equality held at a nonzero point, or if $\abs{f'(0)}=1$, the equality case of Schwarz's lemma would imply $f(z)=e^{i\theta}z$ for some real $\theta$, contrary to the hypothesis. Thus $\abs{g(z)}<1$ everywhere.

:::

:::

::: {.pf-step #s1-2}

For every $0<r<1$, there exists $q_r<1$ such that
$$
\abs{f(z)}\le q_r\abs{z}
$$
whenever $\abs{z}\le r$.


::: pf-proof

Set
$$
q_r\coloneqq\max_{\abs{z}\le r}\abs{g(z)}.
$$
The maximum exists by compactness, and step [](#s1-1){.pf-ref} gives $q_r<1$. Since $f(z)=zg(z)$, the estimate follows.

:::

:::

::: {.pf-step #s1-3}

If $\abs{z}\le r<1$, then for every $n\ge1$,
$$
\abs{f^n(z)}\le q_r^n\abs{z}\le rq_r^n.
$$


::: pf-proof

Schwarz's lemma gives $\abs{f(w)}\le\abs{w}$, so all iterates of $z$ remain in $\abs{w}\le r$. Step [](#s1-2){.pf-ref} therefore applies at every stage:
$$
\abs{f^{k+1}(z)}\le q_r\abs{f^k(z)}.
$$
Induction yields the stated bound.

:::

:::

::: {.pf-step #s1-4}

The series $\sum_{n=1}^{\infty}f^n(z)$ converges uniformly on every compact subset of $\DD$.


::: pf-proof

On $\abs{z}\le r<1$, step [](#s1-3){.pf-ref} gives
$$
\abs{f^n(z)}\le rq_r^n.
$$
The right-hand side is the general term of a convergent geometric series, so the Weierstrass $M$-test gives uniform convergence on that closed disk. Every compact subset of $\DD$ lies in such a disk.

:::

:::

::: {.pf-step #s1-5}

The sum
$$
\boxed{F(z)\coloneqq\sum_{n=1}^{\infty}f^n(z)}
$$
is holomorphic on $\DD$.


::: pf-proof

Each iterate $f^n$ is holomorphic on $\DD$, and step [](#s1-4){.pf-ref} gives locally uniform convergence. The Weierstrass theorem therefore implies that $F$ is holomorphic.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves compact-uniform convergence, and step [](#s1-5){.pf-ref} proves analyticity of the limit.

:::

:::

:::
