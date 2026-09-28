---
schema: qual/card@1
id: P-S07LM
kind: problem
title: One-sided $\varepsilon$-$\delta$ limit, and $\lim_{x\to 0^+} 1/\ln x = 0$
classification:
  areas:
  - prelim
  topics:
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
a) Give the $\varepsilon$-$\delta$ definition of the one-sided limit $\lim_{x \to a^+} f(x) = L$.

b) Using the definition and basic properties of $\ln(x)$, show that $\lim_{x \to 0^+} 1/\ln(x) = 0$.
:::


::: {.solution}
<1>1. The statement
\[
\lim_{x\to a^+}f(x)=L
\]
means: for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
0<x-a<\delta\implies |f(x)-L|<\varepsilon.
\]
:::

<1>2. Let $\varepsilon>0$ and set
\[
\delta=e^{-1/\varepsilon}.
\]
Then $0<\delta<1$.

<1>3. If $0<x<\delta$, then
\[
\ln x<-\frac1\varepsilon<0.
\]
::: {.proof}
The logarithm is strictly increasing on $(0,\infty)$. Hence
\[
0<x<e^{-1/\varepsilon}
\implies
\ln x<\ln(e^{-1/\varepsilon})=-\frac1\varepsilon.
\]
:::

<1>4. Therefore, if $0<x<\delta$,
\[
\left|\frac1{\ln x}-0\right|<\varepsilon.
\]
::: {.proof}
By <1>3, $\ln x<0$ and $|\ln x|>1/\varepsilon$. Thus
\[
\left|\frac1{\ln x}\right|
=\frac1{|\ln x|}
<\varepsilon.
\]
:::

<1>5. Hence
\[
\boxed{\lim_{x\to0^+}\frac1{\ln x}=0.}
\]
::: {.proof}
The estimate in <1>4 holds for every $x$ satisfying $0<x-0<\delta$, so it is exactly the right-hand $\varepsilon$-$\delta$ condition from <1>1.
:::
