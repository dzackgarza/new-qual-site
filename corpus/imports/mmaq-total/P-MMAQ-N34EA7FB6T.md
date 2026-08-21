---
schema: qual/card@1
id: P-MMAQ-N34EA7FB6T
kind: problem
title: Inverse images of primes are prime, the nilradical is contained in every prime,
  and $\mathrm{Spec}(R/N)\to\mathrm{Spec}(R)$ is bijective
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Commutative Algebra
  - Ideals
relations: []
review: draft
solved: false
---

::: problem
Let $R$ and $S$ be commutative rings, and $f:R\rightarrow S$ a ring homomorphism.

- Show that if $I$ is a prime ideal of $S$, then `\begin{align*} f\inv(I)=\{r\in R:f(r)\in I\} \end{align*}`{=tex}

  is a prime ideal of $R$.

- Let $N$ be the set of nilpotent elements of $R$: `\begin{align*} N=\{r\in R:r^m=0\text{ for some }m\geq 1\}. .\end{align*}`{=tex}

  $N$ is called the `\textit{nilradical}`{=tex} of $R$.
  Prove that it is an ideal which is contained in every prime ideal.

- Part (a) lets us define a function `\begin{align*} f^*:\{\text{prime ideals of }S\} &\rightarrow \{\text{prime ideals of }R\}. I &\mapsto f\inv(I). .\end{align*}`{=tex}

  Let $N$ be the nilradical of $R$.
  Show that if $S=R/N$ and $f:R\rightarrow R/N$ is the quotient map, then $f^*$ is a bijection
:::
