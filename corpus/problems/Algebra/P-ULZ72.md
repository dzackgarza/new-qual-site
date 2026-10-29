---
schema: qual/card@1
id: P-ULZ72
kind: problem
title: Elements $g$ for which $\chi(g)$ is real for every character $\chi$
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Conjugacy
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and $g\in G$. Suppose $\chi(g)\in\RR$ for every complex irreducible character $\chi$ of $G$. What can be said about $g$?
:::

::: {.solution}

::: pf

::: {.pf-step #conj}

For every complex character $\chi$ of $G$, $\chi(g^{-1})=\overline{\chi(g)}$.

::: pf-proof

A representation $\rho$ of a finite group may be chosen unitary, so the eigenvalues of $\rho(g)$ lie on the unit circle and the trace of $\rho(g^{-1})$ is the complex conjugate of the trace of $\rho(g)$.

:::

:::

::: {.pf-step #forward}

If $\chi(g)\in\RR$ for every irreducible $\chi$, then $g$ is conjugate to $g^{-1}$.

::: pf-proof

By step [](#conj){.pf-ref} and the hypothesis, $\chi(g^{-1})=\chi(g)$ for every irreducible $\chi$. The irreducible characters form a basis of the space of complex class functions on $G$, so two elements on which all irreducible characters take the same values lie in the same conjugacy class. Hence $g^{-1}\sim g$.

:::

:::

::: {.pf-step #converse}

If $g$ is conjugate to $g^{-1}$, then $\chi(g)\in\RR$ for every character $\chi$.

::: pf-proof

A character is a class function, so step [](#conj){.pf-ref} gives $\chi(g)=\chi(g^{-1})=\overline{\chi(g)}$.

:::

:::

::: pf-qed

Steps [](#forward){.pf-ref} and [](#converse){.pf-ref} give
$$\boxed{\chi(g)\in\RR\text{ for every irreducible }\chi\iff g\text{ is conjugate to }g^{-1}.}$$

:::

:::

:::
