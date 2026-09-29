---
schema: qual/card@1
id: P-BKF20-1B
kind: problem
title: Impossible orderings of four real polynomials
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 lowest-term argument. After
    subtracting a, continuity forces the other three polynomials to vanish at
    zero; their orders and signs force i>j>k and then contradict b<d on the
    negative side.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the normalization, the missing continuity-at-zero step, positivity
    of the leading coefficients, the order inequalities, parity constraints,
    and the final asymptotic contradiction.
---

::: {.problem}
Prove that there do not exist real polynomials $a,b,c,d$ such that
\[
a(x)<b(x)<c(x)<d(x)\quad(0<x<1)
\]
and
\[
b(x)<d(x)<a(x)<c(x)\quad(-1<x<0).
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Subtracting $a$ from all four polynomials, it is enough to rule
out polynomials $B,C,D$ satisfying
$$
0<B(x)<C(x)<D(x)
$$
for $0<x<1$ and
$$
B(x)<D(x)<0<C(x)
$$
for $-1<x<0$.

::: pf-proof

Set
$$
B=b-a,
\qquad
C=c-a,
\qquad
D=d-a.
$$
Subtracting the same real number $a(x)$ from every entry in each
ordering preserves all strict inequalities and replaces $a$ by the
zero polynomial.

:::

:::

::: {.pf-step #s2}

The three normalized polynomials satisfy
$$
B(0)=C(0)=D(0)=0.
$$

::: pf-proof

Letting $x\to0^+$ in
$$
0<B(x)<C(x)<D(x)
$$
and using continuity gives
$$
0\le B(0)\le C(0)\le D(0).
$$
Letting $x\to0^-$ in
$$
B(x)<D(x)<0<C(x)
$$
gives
$$
B(0)\le D(0)\le0\le C(0).
$$
Thus
$$
0\le B(0)\le D(0)\le0,
$$
so $B(0)=D(0)=0$. The first chain then forces $C(0)=0$ as well.

:::

:::

::: {.pf-step #s3}

Write the lowest nonzero terms as
$$
B(x)=\beta x^i+O(x^{i+1}),
\qquad
C(x)=\gamma x^j+O(x^{j+1}),
\qquad
D(x)=\delta x^k+O(x^{k+1}),
$$
where
$$
\beta,\gamma,\delta>0.
$$

::: pf-proof

The strict inequalities in step [](#s1){.pf-ref} show that none of $B,C,D$ is the
zero polynomial. Step [](#s2){.pf-ref} shows that each has positive vanishing
order at $0$, so the displayed lowest terms exist.

For sufficiently small positive $x$, all three polynomials are positive
by step [](#s1){.pf-ref}. Since $x^i,x^j,x^k$ are then positive, their first
nonzero coefficients must satisfy
$$
\beta>0,\qquad\gamma>0,\qquad\delta>0.
$$

:::

:::

::: {.pf-step #s4}

The positive-side ordering implies
$$
i\ge j\ge k.
$$

::: pf-proof

If $i<j$, then as $x\to0^+$,
$$
\frac{B(x)}{C(x)}
\sim
\frac{\beta}{\gamma}x^{i-j}
\longrightarrow
\infty,
$$
contradicting $0<B(x)<C(x)$. Hence $i\ge j$.

Likewise, if $j<k$, then
$$
\frac{C(x)}{D(x)}
\longrightarrow
\infty
$$
as $x\to0^+$, contradicting $C(x)<D(x)$. Thus $j\ge k$.

:::

:::

::: {.pf-step #s5}

The negative-side signs imply that $i$ and $k$ are odd while
$j$ is even.

::: pf-proof

For sufficiently small negative $x$, step [](#s1){.pf-ref} gives
$$
B(x)<0,\qquad D(x)<0,\qquad C(x)>0.
$$
The leading coefficients in step [](#s3){.pf-ref} are all positive. Therefore the
sign of each polynomial near $0$ on the negative side is the sign of
$x$ raised to its vanishing order. Hence $i$ and $k$ must be odd and
$j$ must be even.

:::

:::

::: {.pf-step #s6}

Consequently,
$$
i>j>k.
$$

::: pf-proof

By step [](#s4){.pf-ref},
$$
i\ge j\ge k.
$$
By step [](#s5){.pf-ref}, $i$ and $j$ have opposite parity, so they cannot be
equal; hence $i>j$. Similarly $j$ and $k$ have opposite parity, so
$j>k$.

:::

:::

::: {.pf-step #s7}

For all sufficiently small negative $x$,
$$
B(x)>D(x),
$$
contradicting the required ordering.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s6){.pf-ref},
$$
\frac{B(x)}{D(x)}
\sim
\frac{\beta}{\delta}x^{i-k}.
$$
The integer $i-k$ is positive and even, so as $x\to0^-$,
$$
\frac{B(x)}{D(x)}
\longrightarrow0^+.
$$
Thus for all sufficiently small negative $x$,
$$
0<\frac{B(x)}{D(x)}<1.
$$
Step [](#s1){.pf-ref} also gives $D(x)<0$. Multiplying the last inequality by the
negative number $D(x)$ reverses the order and yields
$$
B(x)>D(x).
$$
This contradicts the required inequality $B(x)<D(x)$.

:::

:::

::: {.pf-step #s8}

Therefore no such four polynomials exist.

::: pf-proof

If the original polynomials existed, step [](#s1){.pf-ref} would produce normalized
polynomials $B,C,D$, but step [](#s7){.pf-ref} shows those cannot exist.

:::

:::

::: pf-qed

Step [](#s8){.pf-ref} is the required conclusion.

:::

:::

:::
