---
schema: qual/card@1
id: E-SS9.EX-1
kind: problem
title: A meromorphic function with two periods of real ratio
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Lattices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The collection's provenance is the publisher's catalogue record only, with no retained text and no retained solution set, so the statement is taken as the card prints it; the argument is the card's own. Checked: the Bezout combination giving $\omega_1/q$; the density step and the resulting periods tending to $0$; that poles would accumulate; and that the difference quotients along the periods force $f'\equiv0$.
---

::: {.exercise}
Suppose that a meromorphic function $f$ has two periods $\omega_1$ and $\omega_2$, with $\omega_2/\omega_1 \in \RR$.

(a) Suppose $\omega_2/\omega_1$ is rational, say equal to $p/q$, where $p$ and $q$ are relatively prime integers. Prove that as a result the periodicity assumption is equivalent to the assumption that $f$ is periodic with the simple period $\omega_0 = \frac{1}{q}\omega_1$. [Hint: Since $p$ and $q$ are relatively prime, there exist integers $m$ and $n$ such that $mq + np = 1$ (Corollary 1.3, Chapter 8, Book I).]

(b) If $\omega_2/\omega_1$ is irrational, then $f$ is constant. To prove this, use the fact that $\{m - n\tau\}$ is dense in $\RR$ whenever $\tau$ is irrational and $m, n$ range over the integers.
:::

::: {.solution}
No retained text and no retained solution set for this collection: its provenance is the publisher's catalogue record, so the statement is taken as the card prints it, and the argument is the card's own. Part (a) is the Bezout identity for $p,q$; part (b) uses the density of $\{m-n\tau\}$ and the isolatedness of poles.

::: pf

::: {.pf-step #a-forward}
(a) If $f$ has period $\omega_0=\omega_1/q$ then it has periods $\omega_1$ and $\omega_2$.

::: pf-proof
$\omega_1=q\omega_0$ and $\omega_2=(p/q)\omega_1=p\omega_0$ are integer multiples of the period $\omega_0$, and integer multiples of a period are periods.
:::
:::

::: {.pf-step #a-back}
(a) If $\omega_1,\omega_2$ are periods and $\tau=p/q$ with $(p,q)=1$, then $\omega_0=\omega_1/q$ is a period.

::: pf-proof
Choose integers $m,n$ with $mq+np=1$. Then $m\omega_1+n\omega_2=\left(m+\frac{np}{q}\right)\omega_1=\frac{mq+np}{q}\omega_1=\omega_0$, and an integer combination of periods is a period.
:::
:::

::: {.pf-step #dense}
(b) If $\tau$ is irrational, the group $G=\{m-n\tau\st m,n\in\ZZ\}$ is dense in $\RR$, so there are nonzero periods $h_j=(m_j-n_j\tau)\omega_1$ with $h_j\to0$.

::: pf-proof
The density of $\{m-n\tau\}$ for irrational $\tau$ is the standard fact quoted in the exercise; multiplying a dense subset of $\RR$ by the nonzero complex number $\omega_1$ gives a dense subset of the line $\RR\omega_1$, so periods of $f$ accumulate at $0$.
:::
:::

::: {.pf-step #entire}
(b) $f$ has no poles, hence is entire.

::: pf-proof
If $p$ were a pole, then translating by the period $h_j$ would make every $p+h_j$ a pole too, and the $p+h_j$ are distinct and accumulate at $p$, contradicting that the poles of a meromorphic function are isolated.
:::
:::

::: {.pf-step #constant}
(b) $f$ is constant.

::: pf-proof
For every $z$, each $h_j$ is a period, so $\frac{f(z+h_j)-f(z)}{h_j}=0$; letting $j\to\infty$, when $h_j\to0$, the difference quotients tend to $f'(z)$, so $f'(z)=0$. Hence $f'\equiv0$ on the connected set $\CC$ and $f$ is constant.
:::
:::

::: {.pf-step}
(a) For rational $\omega_2/\omega_1=p/q$ the periodicity by $\omega_1,\omega_2$ is equivalent to periodicity by $\omega_1/q$; (b) for irrational $\omega_2/\omega_1$ the function is constant.

::: pf-proof
Steps [](#a-forward){.pf-ref} and [](#a-back){.pf-ref} give (a); steps [](#dense){.pf-ref}, [](#entire){.pf-ref} and [](#constant){.pf-ref} give (b).
:::
:::

:::
:::
