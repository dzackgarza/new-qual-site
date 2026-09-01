---
schema: qual/card@1
id: P-YHXGO
kind: problem
title: Multiplicative linear functionals on $A(\mathbb{D})$ are point evaluations
classification:
  areas:
  - real-analysis
  topics:
  - Holomorphic Functions
  - Functional Analysis
relations: []
review: draft
---

::: {.problem}
Let $A(\mathbb{D})$ be the $\mathbb{C}$-vector space of all holomorphic functions on $\mathbb{D}$ and suppose that $L:A(\mathbb{D})\to\mathbb{C}$ is a multiplicative linear functional.
If $L$ is not identically zero, show that there is a $z_0\in\mathbb{D}$ so that $L(f)=f(z_0)$ for all $f\in A(\mathbb{D})$.
:::

::: {.solution}
Note that if this were true, then we would have to have $L(z)=z_0$.
So define $z_0:=L(z)$ and we want to show that $L(f)=f(z_0)$ for any $f\in A(\mathbb{D})$.
Since we are assuming that $L$ is not identically zero, let $f$ be such that $L(f)\ne0$.
Then because $L$ is multiplicative we can write $L(f)=L(f\cdot1)=L(f)L(1)$, so $L(1)=1$.
This, combined with the linear and multiplicative hypotheses again, imply that $L(P)=P(z_0)$ for any polynomial $P$.
Now let $f$ be any element of $A(\mathbb{D})$.
We can write $f(z)-f(z_0)=(z-z_0)g(z)$ for some other $g\in A(\mathbb{D})$.
Therefore we have $$L(f)-f(z_0) = L((z-z_0)g(z)) = (L(z)-z_0)L(g) = 0,$$ which establishes the desired result.
The only thing left to check is that we actually have $z_0\in\mathbb{D}$.
If not, then $1/(z-z_0)$ would be in $A(\mathbb{D})$, and so we would have $$L(1/(z-z_0)) = 1/L(z-z_0) = 1/(z_0-z_0),$$ [solution cut off at end of source page — remainder not available]
:::
