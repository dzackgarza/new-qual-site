---
schema: qual/card@1
id: E-SS1.EX-3
kind: problem
title: The $n$ solutions of $z^n=\omega$
classification:
  areas:
    - complex-analysis
  topics: [Complex Numbers]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Structured the computation into numbered steps and supplied three facts it used in passing:
      that a complex number has a polar form and that for s > 0 it has a unique positive nth root;
      that e^{in theta} = e^{i phi} implies n theta = phi + 2 pi k for an integer k; and that the n
      listed arguments are pairwise incongruent modulo 2 pi, which is what makes the solutions
      distinct. No source text is retained for this exercise beyond the statement stored on the card.

---

::: {.exercise}
With $\omega = s e^{i\varphi}$, where $s \geq 0$ and $\varphi \in \RR$, solve the equation $z^n = \omega$ in $\CC$ where $n$ is a natural number. How many solutions are there?
:::

::: {.solution}

The computation is the card's own; the statement is the exercise stored on the card, and no source text or solution set is retained for it.

Write $\omega=se^{i\varphi}$ with $s\geq0$ and $\varphi\in\RR$, and let $n\geq1$.

::: pf

::: {.pf-step #polar}
Every $z\in\CC$ has the form $z=re^{i\theta}$ with $r=\abs{z}\geq0$, and $z=0$ exactly when $r=0$.

::: pf-proof
For $z\neq0$ the modulus $r=\abs{z}$ is positive and $z/r$ lies on the unit circle, so $z/r=e^{i\theta}$ for some real $\theta$; for $z=0$ take $r=0$ and any $\theta$.
:::

:::

::: {.pf-step #zero}
If $s=0$ then $z^{n}=0$ has the unique solution $z=0$.

::: pf-proof
$z^{n}=0$ implies $\abs{z}^{n}=0$, hence $\abs{z}=0$ and $z=0$; and $z=0$ satisfies the equation.
:::

:::

::: {.pf-step #modulus}
Let $s>0$ and $z=re^{i\theta}$. Then $z^{n}=\omega$ if and only if $r=s^{1/n}$ and $n\theta=\varphi+2\pi k$ for some $k\in\ZZ$.

::: pf-proof
De Moivre's formula gives $z^{n}=r^{n}e^{in\theta}$, so by step [](#polar){.pf-ref} the equation $z^{n}=se^{i\varphi}$ with both moduli positive forces $r^{n}=s$ and $e^{in\theta}=e^{i\varphi}$. The first has the unique positive solution $r=s^{1/n}$ because $t\mapsto t^{n}$ is strictly increasing on $[0,\infty)$. The second says the unit complex numbers $e^{i(n\theta-\varphi)}$ and $1$ coincide, which happens exactly when $n\theta-\varphi\in2\pi\ZZ$.
:::

:::

::: {.pf-step #list}
The solutions are $z_{k}=s^{1/n}\exp\!\bigl(i\frac{\varphi+2\pi k}{n}\bigr)$ for $k=0,1,\dots,n-1$, and each integer $k$ gives one of these.

::: pf-proof
By step [](#modulus){.pf-ref} a solution is determined by an integer $k=\frac{n\theta-\varphi}{2\pi}$, and conversely every integer $k$ gives a solution through that formula. Two integers $k,k'$ give the same complex number exactly when their arguments differ by a multiple of $2\pi$, that is when $(k-k')2\pi/n\in2\pi\ZZ$, i.e. $n\mid(k-k')$. Hence the residue classes of $k$ modulo $n$ index the solutions, and $k=0,\dots,n-1$ is a complete set of representatives.
:::

:::

::: {.pf-step #distinct}
The $n$ numbers $z_{0},\dots,z_{n-1}$ of step [](#list){.pf-ref} are distinct.

::: pf-proof
If $z_{k}=z_{\ell}$ with $0\leq k<\ell\leq n-1$, step [](#list){.pf-ref} gives $n\mid(\ell-k)$, while $0<\ell-k<n$, which is impossible.
:::

:::

::: {.pf-step}
$z^{n}=\omega$ has exactly one solution when $\omega=0$ and exactly $n$ solutions when $\omega\neq0$.

::: pf-proof
The first case is step [](#zero){.pf-ref}. In the second, steps [](#list){.pf-ref} and [](#distinct){.pf-ref} exhibit $n$ distinct solutions and show that every solution is among them.
:::

:::

:::

:::
