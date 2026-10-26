---
schema: qual/card@1
id: P-KSRING17-094
kind: problem
title: Irreducible elements of a principal ideal domain are prime
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 94 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let π be an irreducible element of a principal ideal domain R. Prove that π is a prime element (that is, π | ab implies ${ \pi } \mid a \ \mathrm { o r } \ \pi \mid b )$
:::

::: pf

::: pf-step

The ideal $(\pi)$ is proper.


::: pf-proof

If $(\pi)=R$, then $1=r\pi$ for some $r\in R$, so $\pi$ is a unit, contradicting irreducibility. Thus $(\pi)\subsetneq R$.

:::

:::

::: pf-step

Let $(\pi)\subseteq I\subseteq R$. Since $R$ is a PID, write $I=(d)$.


::: pf-proof

Every ideal of a principal ideal domain is principal.

:::

:::

::: pf-step

The containment $(\pi)\subseteq(d)$ implies $\pi=dr$ for some $r\in R$.


::: pf-proof

Since $\pi\in(\pi)\subseteq(d)$, the element $\pi$ is a multiple of $d$.

:::

:::

::: pf-step

Either $I=R$ or $I=(\pi)$.


::: pf-proof

From $\pi=dr$ and irreducibility of $\pi$, either $d$ is a unit or $r$ is a unit. If $d$ is a unit, then $I=(d)=R$. If $r$ is a unit, then $d$ is associate to $\pi$, so $I=(d)=(\pi)$.

:::

:::

::: pf-step

Therefore $(\pi)$ is maximal, hence prime.


::: pf-proof

Step <1>1 gives properness and step <1>4 gives maximality. Every maximal ideal in a commutative ring with identity is prime.

:::

:::

::: pf-step

If $\pi\mid ab$, then $\pi\mid a$ or $\pi\mid b$.


::: pf-proof

The divisibility $\pi\mid ab$ means $ab\in(\pi)$. Since $(\pi)$ is prime by step <1>5, either $a\in(\pi)$ or $b\in(\pi)$, equivalently $\pi\mid a$ or $\pi\mid b$.

:::

:::

::: pf-step

Therefore
$$
\boxed{\pi\text{ is a prime element of }R.}
$$


::: pf-proof

Step <1>6 is the defining prime-element divisibility condition.

:::

:::

::: pf-qed

Step <1>7 is the required conclusion.

:::

:::
