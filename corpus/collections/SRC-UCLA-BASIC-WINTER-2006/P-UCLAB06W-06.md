---
schema: qual/card@1
id: P-UCLAB06W-06
kind: problem
title: Intermediate values of a continuous function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the official UCLA Basic Qual Winter 2006 PDF.
---

::: {.problem}
Let $-\infty<a<b<\infty$.
Prove that a continuous function $f:[a,b]\to\RR$ attains all values in $[f(a),f(b)]$.
:::

::: {.solution}

Let $c$ be any real number lying between $f(a)$ and $f(b)$. If $c=f(a)$ or $c=f(b)$ there is nothing to prove, so assume $c$ lies strictly between the endpoint values. After exchanging $a$ and $b$ in the argument if necessary, assume
$$
f(a)<c<f(b).
$$

::: pf

::: {.pf-step #s1-1}

The set
$$
E=\{x\in[a,b]:f(x)\le c\}
$$
is nonempty and bounded above.


::: pf-proof

Since $f(a)<c$, one has $a\in E$, so $E$ is nonempty. Also $E\subseteq[a,b]$, so $b$ is an upper bound.

:::

:::

::: pf-step

Let
$$
s=\sup E.
$$
Then $s\in[a,b]$.


::: pf-proof

By step [](#s1-1){.pf-ref}, the least-upper-bound property of $\RR$ gives a real number $s=\sup E$. Since every point of $E$ lies in $[a,b]$ and $a\in E$, one has $a\le s\le b$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
f(s)\le c.
$$


::: pf-proof

By the definition of supremum, for every $n\ge1$ there exists $x_n\in E$ such that
$$
s-\frac1n<x_n\le s.
$$
Hence $x_n\to s$. Since $x_n\in E$,
$$
f(x_n)\le c
$$
for every $n$. Continuity of $f$ at $s$ gives
$$
f(s)=\lim_{n\to\infty}f(x_n)\le c.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
f(s)\ge c.
$$


::: pf-proof

Suppose instead that $f(s)<c$. By continuity at $s$, there exists $\delta>0$ such that
$$
\abs{x-s}<\delta
\quad\Longrightarrow\quad
f(x)<c.
$$
Because $f(b)>c$ and $f$ is continuous at $b$, there exists $\eta>0$ such that $f(x)>c$ whenever $x\in[b-\eta,b]$. Thus $E\cap[b-\eta,b]=\varnothing$, so $s\le b-\eta<b$. Choose
$$
x\in(s,\min\{s+\delta,b\}).
$$
Then $f(x)<c$, so $x\in E$, contradicting that $s$ is an upper bound for $E$.

:::

:::

::: {.pf-step #s1-5}

Therefore there exists $s\in[a,b]$ such that
$$
f(s)=c.
$$


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} give both inequalities $f(s)\le c$ and $f(s)\ge c$.

:::

:::

::: pf-qed

The value $c$ was arbitrary between $f(a)$ and $f(b)$. Step [](#s1-5){.pf-ref} therefore shows that $f$ attains every intermediate value. If $f(b)<f(a)$, the same argument applies after reversing the endpoint roles.

:::

:::

:::
