---
schema: qual/card@1
id: E-SS7.EX-12
kind: problem
title: Asymptotic size of the nth prime
classification:
  areas:
  - complex-analysis
  topics:
  - Prime Number Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 7, §3, exercise 12, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, both parts; nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved as directed: (a) by taking logarithms of $\pi(x)\sim x/\log x$; (b) by subtracting
    $\log\log x=o(\log x)$ and then evaluating at $x=p_n$, where $\pi(p_n)=n$. The prime number
    theorem itself is cited, not reproved. Nothing is left in outline.
---

::: {.exercise}
Let $p_n$ be the $n$th prime. Prove from the prime number theorem that $p_n\sim n\log n$ as $n\to\infty$.

(a) Show that $\pi(x)\sim x/\log x$ implies
$$
\log\pi(x)+\log\log x\sim\log x.
$$

(b) Deduce that $\log\pi(x)\sim\log x$, then set $x=p_n$ to conclude the proof.
:::

::: {.solution}

Let $\pi$ be the prime counting function and $p_n$ the $n$-th prime, so that $\pi(p_n)=n$.

::: pf

::: {.pf-step #s1}

Part (a): $\pi(x)\sim x/\log x$ implies $\log\pi(x)+\log\log x\sim\log x$.

::: pf-proof

Since $\log$ is continuous at $1$ and $\pi(x)\big/\bigl(x/\log x\bigr)\to1$,
$$
\log\pi(x)=\log\frac{x}{\log x}+o(1)=\log x-\log\log x+o(1).
$$
Adding $\log\log x$ gives $\log\pi(x)+\log\log x=\log x+o(1)$, and dividing by $\log x$ shows the ratio tends to $1$.

:::

:::

::: {.pf-step #s2}

Part (b): $\log\pi(x)\sim\log x$.

::: pf-proof

From step [](#s1){.pf-ref}, $\log\pi(x)=\log x-\log\log x+o(1)$, and $\log\log x=o(\log x)$. Hence
$$
\frac{\log\pi(x)}{\log x}=1-\frac{\log\log x}{\log x}+o\Bigl(\frac{1}{\log x}\Bigr)\longrightarrow1 .
$$

:::

:::

::: {.pf-step #s3}

Conclusion: $p_n\sim n\log n$.

::: pf-proof

Apply the prime number theorem at $x=p_n$, where $\pi(p_n)=n$:
$$
n=\pi(p_n)\sim\frac{p_n}{\log p_n},
\qquad\text{so}\qquad
p_n\sim n\log p_n .
$$
Apply step [](#s2){.pf-ref} at $x=p_n$: $\log p_n=\log\pi(p_n)\,(1+o(1))=\log n\,(1+o(1))$. Therefore
$$
\frac{p_n}{n\log n}=\frac{p_n}{n\log p_n}\cdot\frac{\log p_n}{\log n}\longrightarrow1\cdot1=1,
$$
that is, $p_n\sim n\log n$.

:::

:::

:::

:::
