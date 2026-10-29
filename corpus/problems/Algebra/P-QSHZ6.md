---
schema: qual/card@1
id: P-QSHZ6
kind: problem
title: Prime elements of $\ZZ[i]$
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Prime Ideals
  - Number Theory
relations: []
review: draft
---

::: {.problem}
Classify the prime elements of the Gaussian integers $\ZZ[i]$, up to multiplication by units.
:::

::: {.solution}
Write $N(a+bi)\coloneqq a^2+b^2$; it is multiplicative, and $N(\alpha)=1$ exactly when $\alpha$ is a unit, so the units are $\pm1,\pm i$. The ring $\ZZ[i]$ is Euclidean for $N$, so its prime elements are its irreducible elements.

::: pf

::: {.pf-step #prime-norm}
If $N(\pi)$ is a rational prime, then $\pi$ is a Gaussian prime.

::: pf-proof
If $\pi=\alpha\beta$, then $N(\alpha)N(\beta)$ is prime, so one of $N(\alpha),N(\beta)$ is $1$ and that factor is a unit.
:::

:::

::: {.pf-step #inert}
A rational prime $p\equiv3\pmod4$ is a Gaussian prime.

::: pf-proof
A nontrivial factorization $p=\alpha\beta$ gives $N(\alpha)N(\beta)=p^2$ with both norms greater than $1$, so $N(\alpha)=a^2+b^2=p$. A sum of two squares is $0$, $1$, or $2$ modulo $4$, never $3$.
:::

:::

::: {.pf-step #split}
A rational prime $p\not\equiv3\pmod4$ is not a Gaussian prime.

::: pf-proof
$2=-i(1+i)^2$. For $p\equiv1\pmod4$, Fermat's two-squares theorem gives $p=a^2+b^2=(a+bi)(a-bi)$ with $N(a\pm bi)=p>1$.
:::

:::

::: {.pf-step #exhaust}
Every Gaussian prime $\pi$ is a unit multiple of a Gaussian integer of rational prime norm or of a rational prime $p\equiv3\pmod4$.

::: pf-proof
The rational integer $N(\pi)=\pi\bar\pi>1$ factors into rational primes, so the prime $\pi$ divides some rational prime $p$. Then $N(\pi)$ divides $N(p)=p^2$, so $N(\pi)\in\{p,p^2\}$. If $N(\pi)=p^2$, then $p=\pi u$ with $N(u)=1$, so $\pi$ is associate to $p$, and $p\equiv3\pmod4$ by step [](#split){.pf-ref}.
:::

:::

::: pf-qed
By steps [](#prime-norm){.pf-ref}, [](#inert){.pf-ref} and [](#exhaust){.pf-ref}, up to units the Gaussian primes are exactly $1+i$; the elements $a\pm bi$ with $a^2+b^2=p$ for each rational prime $p\equiv1\pmod4$; and the rational primes $p\equiv3\pmod4$. Equivalently, a nonunit $a+bi$ is prime if and only if either $a^2+b^2$ is a rational prime, or one of $a,b$ is $0$ and the absolute value of the other is a rational prime congruent to $3$ modulo $4$.
:::

:::
:::
