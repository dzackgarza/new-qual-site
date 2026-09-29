---
schema: qual/card@1
id: P-BERK96S-11
kind: problem
title: If $\varphi$ and $\varphi'$ both have limits at $\infty$, then $\varphi'\to0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained PDF page confirms the limits phi(x)->a and phi'(x)->b as x->infinity; the extraction dropped the arrows.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified the mean-value-theorem identity and that the intermediate points
    tend to infinity, so the two limits force b=0.
---

::: {.problem}
Let $\varphi\in C^1(\mathbb R)$ and suppose
\[
\varphi(x)\to a,
\qquad
\varphi'(x)\to b
\qquad(x\to\infty).
\]
Prove or give a counterexample: must $b=0$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $x\in\RR$, there is a point
$$
\xi_x\in(x,x+1)
$$
such that
$$
\varphi(x+1)-\varphi(x)=\varphi'(\xi_x).
$$

::: pf-proof

Apply the mean value theorem to $\varphi$ on the interval $[x,x+1]$.

:::

:::

::: {.pf-step #s2}

One has
$$
b=0.
$$

::: pf-proof

As $x\to\infty$,
$$
\varphi(x+1)-\varphi(x)\longrightarrow a-a=0.
$$
Also $\xi_x>x$, so
$$
\xi_x\longrightarrow\infty.
$$
The hypothesis $\varphi'(y)\to b$ as $y\to\infty$ therefore gives
$$
\varphi'(\xi_x)\longrightarrow b.
$$
Taking limits in the identity from step [](#s1){.pf-ref} yields $0=b$.

:::

:::

::: {.pf-step #s3}

Thus the answer is
$$
\boxed{\text{yes: }b=0}.
$$

::: pf-proof

This is exactly step [](#s2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} answers the question.

:::

:::

:::
