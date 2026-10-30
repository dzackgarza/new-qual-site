---
schema: qual/card@1
id: P-ALGFINAL11-03
kind: problem
title: Irreducible but nonprime elements in Z[sqrt(-5)]
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Prove that in $\ZZ[\sqrt{-5}]$, $7$ is irreducible but not prime.

(b) Is $\ZZ[\sqrt{-5}]$ a Principal Ideal Domain? (Justify your answer.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
The norm $N(a+b\sqrt{-5})=a^2+5b^2$ is multiplicative, and the units of $\ZZ[\sqrt{-5}]$ are the elements of norm $1$, namely $\pm1$.

::: pf-proof
$N(xy)=xy\overline{xy}=x\bar x\,y\bar y=N(x)N(y)$. If $xy=1$, then $N(x)N(y)=1$ in $\ZZ_{>0}$, so $N(x)=1$. Conversely $a^2+5b^2=1$ forces $b=0$ and $a=\pm1$.
:::

:::

::: {.pf-step #s2}
(a) $7$ is irreducible.

::: pf-proof
Suppose $7=xy$ with $x,y$ not units. Then $N(x)N(y)=N(7)=49$ and $N(x),N(y)>1$ by step [](#s1){.pf-ref}, so $N(x)=7$. But $a^2+5b^2=7$ has no integer solution: $b=0$ gives $a^2=7$, $\abs{b}=1$ gives $a^2=2$, and $\abs{b}\ge2$ gives $a^2+5b^2\ge20$.
:::

:::

::: {.pf-step #s3}
(a) $7$ is not prime.

::: pf-proof
$(3+\sqrt{-5})(3-\sqrt{-5})=14$ is divisible by $7$. If $7\mid 3\pm\sqrt{-5}$, then $(3\pm\sqrt{-5})/7=3/7\pm\tfrac17\sqrt{-5}$ would lie in $\ZZ[\sqrt{-5}]$, which it does not. So $7$ divides a product without dividing either factor.
:::

:::

::: {.pf-step #s4}
(b) $\ZZ[\sqrt{-5}]$ is not a principal ideal domain.

::: pf-proof
A principal ideal domain is a unique factorization domain, and in a unique factorization domain every irreducible element is prime. Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give an irreducible element that is not prime.
:::

:::

::: pf-qed
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove (a), and step [](#s4){.pf-ref} answers (b).
:::

:::

:::
