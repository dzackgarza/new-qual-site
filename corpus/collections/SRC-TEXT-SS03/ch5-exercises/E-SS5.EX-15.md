---
schema: qual/card@1
id: E-SS5.EX-15
kind: problem
title: Meromorphic functions as quotients of entire functions
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Weierstrass Products
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 5, §3, exercise 15, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise (both sentences) and nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Both assertions proved. The only input is Weierstrass's product theorem, Chapter 5, Theorem 4.1,
    whose statement allows repetitions in the sequence and so prescribes multiplicities. The first
    part divides $f$ by an entire function with zeros exactly at the poles of $f$; the second takes
    $A/B$ for entire $A$, $B$ with zero sets $\{a_n\}$ and $\{b_n\}$. The finite and empty cases of
    the two sequences are noted separately. Nothing is left in outline.
---

::: {.exercise}
Prove that every meromorphic function on $\CC$ is the quotient of two entire functions. Also, if $\{a_n\}$ and $\{b_n\}$ are two disjoint sequences with no finite limit points, prove that there exists a meromorphic function on $\CC$ that vanishes exactly at the $a_n$ and has poles exactly at the $b_n$.
:::

::: {.solution}

The single input is Weierstrass's product theorem (Chapter 5, Theorem 4.1): for any sequence $\{c_n\}$ in $\CC$ with $\abs{c_n}\to\infty$ there is an entire function vanishing at every $c_n$ and nowhere else, repetitions in the sequence giving the multiplicities of the zeros.

::: pf

::: {.pf-step #s1}

Let $f$ be meromorphic on $\CC$ and not identically zero. Then its poles form a set with no accumulation point in $\CC$; enumerating them with multiplicities as $b_1,b_2,\dots$ and the multiplicity of $b_n$ as $m_n$, one has $\abs{b_n}\to\infty$.

::: pf-proof

Let $P$ be the pole set. Each pole is isolated by definition, and $P$ has no accumulation point in $\CC$: if $w_j\in P$ converged to $w\in\CC$, then $f$ would have poles in every punctured neighbourhood of $w$, contradicting that $f$ is holomorphic on a punctured neighbourhood of $w$ (its Laurent expansion about $w$ has an isolated singularity there, so its principal part is finite). Hence $P$ is a closed discrete subset of $\CC$; if it were infinite, its points could be enumerated with $\abs{b_n}\to\infty$, and if it is finite the same holds after arbitrarily extending the list.

:::

:::

::: {.pf-step #s2}

There is an entire $h$, not identically zero, whose zeros are exactly the poles of $f$ with the same multiplicities; then $h\,f$ is entire and
$$
f=\frac{hf}{h}
$$
is a quotient of two entire functions.

::: pf-proof

Apply Theorem 4.1 to the sequence in which $b_n$ is repeated $m_n$ times; it gives an entire $h$ whose zero set is exactly $\{b_n\}$ with multiplicity $m_n$ at $b_n$, and $h\not\equiv0$.

At a pole $b$ of $f$ of order $m$, the Laurent expansion gives $f(z)=(z-b)^{-m}u(z)$ with $u$ holomorphic and non-zero near $b$, while $h(z)=(z-b)^{m}v(z)$ with $v$ holomorphic and non-zero near $b$; hence $(hf)(z)=u(z)v(z)$ near $b$, which is holomorphic there. At every other point both $h$ and $f$ are holomorphic. So $hf$ is entire, and $f=(hf)/h$ wherever $h\ne0$, hence on a dense open set, hence as meromorphic functions.

:::

:::

::: {.pf-step #s3}

Let $\{a_n\}$ and $\{b_n\}$ be disjoint sequences with no accumulation point in $\CC$. Then there is a meromorphic function on $\CC$ vanishing exactly at the $a_n$ and with poles exactly at the $b_n$.

::: pf-proof

If both sequences are infinite, then $\abs{a_n}\to\infty$ and $\abs{b_n}\to\infty$ because neither has an accumulation point in $\CC$; Theorem 4.1 applied to each gives entire $A$ and $B$ with zero sets exactly $\{a_n\}$ and $\{b_n\}$ respectively. Set $f=A/B$, a quotient of entire functions and therefore meromorphic on $\CC$.

Its poles are the zeros of $B$ at which $A$ does not vanish, that is exactly the points $b_n$, because $A(b_n)\ne0$ for every $n$: the zero set of $A$ is $\{a_n\}$ and the two sequences are disjoint. Its zeros are the zeros of $A$ at which $B$ does not vanish, that is exactly the points $a_n$, because $B(a_n)\ne0$ for every $n$ for the same reason. Hence $f$ vanishes exactly at the $a_n$ and has poles exactly at the $b_n$.

If one of the sequences is finite, replace the corresponding entire function by the finite product $\prod(z-c)$ over that finite set (and by $1$ if the set is empty); if both are finite, $f$ is a rational function. The computation of the zero and pole sets is the same, and the argument above never uses more than that each of $A$, $B$ is entire with the prescribed zero set.

:::

:::

:::

:::
