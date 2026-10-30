---
schema: qual/card@1
id: P-BKS07-2B
kind: problem
title: Iterates $a_{n+1}=\cos a_n$ converge to the unique solution of $\cos x=x$
classification:
  areas: [prelim]
  topics:
  - Real Analysis
relations: []
review: draft
---

::: {.problem}
Given any real number $a_{0}$, define $a_{1}, a_{2}, \ldots$ by the rule $a_{n+1} = \cos a_{n}$ for all $n \geq 0$. Prove that the sequence $(a_{n})$ converges, and that the limit is the unique solution of the equation $\cos x = x$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The equation $\cos x=x$ has exactly one solution $a$, and $\frac12<a<1$.

::: pf-proof

Let $g(x)=\cos x-x$. Then $g(1)<0$, and $g(\frac12)>0$ because $\cos\frac12>\cos\frac\pi3=\frac12$. By the intermediate value theorem, $g$ has a zero in $(\frac12,1)$. A solution lies in $[-1,1]$, and none lies in $[-1,0)$, where $x<0<\cos x$. On $[0,1]$, $g'(x)=-\sin x-1<0$, so $g$ has only one zero there.

:::

:::

::: {.pf-step #s2}

On $I=[a-\frac12,a+\frac12]$, $\abs{\sin x}\le c=\sin(a+\frac12)<1$, and $\cos$ maps $I$ into $I$.

::: pf-proof

By step [](#s1){.pf-ref}, $I\subseteq(0,\frac32)\subseteq(0,\frac\pi2)$, where $\sin$ is positive and increasing. For $x\in I$, the mean value theorem gives $\abs{\cos x-a}=\abs{\cos x-\cos a}\le c\abs{x-a}\le\frac12$.

:::

:::

::: {.pf-step #s3}

$a_2\in I$.

::: pf-proof

$a_1=\cos a_0\in[-1,1]$, so $a_2=\cos a_1\in[\cos1,1]$. Since $\cos1>\cos\frac\pi3=\frac12$, and $a-\frac12<\frac12$ and $a+\frac12>1$, this interval lies in $I$.

:::

:::

::: pf-qed

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, induction gives $a_n\in I$ and $\abs{a_{n+1}-a}\le c\abs{a_n-a}$ for $n\ge2$. So $\abs{a_n-a}\le c^{n-2}\abs{a_2-a}\to0$, and $a_n\to a$, the unique solution of $\cos x=x$ by step [](#s1){.pf-ref}.

:::

:::

:::
